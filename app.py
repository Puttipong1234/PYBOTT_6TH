from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
from FlexMessage.QuestionMsg import *
from FlexMessage.ResultMsg import *

from BasicFunction.COVID_ANALYZER import analyze_covid_from_user
from firebase import firebase
from BasicFunction.Firebase_Connect import get , get_daily_tracking , post, post_daily_tracking , update_daily_tracking , update , delete
from config import Firebase_DB_url
# Firebase_DB_url = "https://pybott-6th.firebaseio.com/" # Your firebase Application
firebase = firebase.FirebaseApplication(Firebase_DB_url, None)
DB_COV_TRACKER = "COV_TRACKER"
DB_USER_SESSION = "USER_SESSION"
DB_USER_DATA = "USER_DATA"

from config import Channel_access_token , Channel_secret

app = Flask(__name__)

line_bot_api = LineBotApi(Channel_access_token)
handler = WebhookHandler(Channel_secret)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # INPUT AND PARSING DATA
    REPLY_TOKEN = event.reply_token 
    MESSAGE_FROM_USER = event.message.text
    UID = event.source.user_id
    
    # get user id
    profile = line_bot_api.get_profile(UID)
    DISPLAY_NAME = profile.display_name
    PROFILE_PIC = profile.picture_url
    
    #check user in system?
    user = get(uid=UID,firebase_app=firebase , database_name=DB_USER_DATA)
    if not user:
        # continue
        data = {"session" : "None"}
        post(uid=UID,data=data,firebase_app=firebase,database_name=DB_USER_SESSION)
        
        data = { "DISPLAY_NAME" : DISPLAY_NAME , "PROFILE_PIC" : PROFILE_PIC }
        post(uid=UID,data=data,firebase_app=firebase,database_name=DB_USER_DATA)
    
    
    user_session = get(uid=UID,firebase_app=firebase , database_name=DB_USER_SESSION)
    user_session = user_session["session"]
    if user_session == "None":
        if MESSAGE_FROM_USER == "เริ่มบันทึกอาการป่วย":
            daily_report = {
            "มีไข้" : "",
            "มีอาการไอ" : "",
            "มีอาการเจ็บคอ" : "",
            "น้ำมูกไหล" : "",
            "เหนื่อยหอบ" : "",
            "วันที่" : "",
            "score" : 0,
            "ข้อเสนอแนะ" : "",
            "อาการอื่นๆที่พบ": ""
            }
            
            # create user daily report
            post_daily_tracking(uid=UID , data=daily_report , firebase_app=firebase , database_name=DB_COV_TRACKER)
            # update session
            
            session_data = {"session" : "บันทึกอาการไข้"}
            update(uid=UID,new_data=session_data,firebase_app=firebase,database_name=DB_USER_SESSION)
            
            #Reponse กลับไปที่ห้องแชท
            Bubble = Base.get_or_new_from_json_dict(คำถามอาการไข้(),FlexSendMessage)
            line_bot_api.reply_message(REPLY_TOKEN,messages=Bubble)
            
    
    ### func อื่นๆ
    else:
        if  user_session == "บันทึกอาการไข้": # validate session
                # "3" != 3
            if MESSAGE_FROM_USER in ["1","2","3","4","5"]: # validate input
                data = {"มีไข้" : MESSAGE_FROM_USER}
                update_daily_tracking(uid=UID,new_data=data,firebase_app=firebase,database_name=DB_COV_TRACKER) # update
                
                session_data = {"session" : "บันทึกอาการไอ"}
                update(uid=UID,new_data=session_data,firebase_app=firebase,database_name=DB_USER_SESSION) # update
                
                #Reponse กลับไปที่ห้องแชท
                Bubble = Base.get_or_new_from_json_dict(คำถามอาการไอ,FlexSendMessage)
                line_bot_api.reply_message(REPLY_TOKEN,messages=Bubble)
                
            else :
                line_bot_api.reply_message(REPLY_TOKEN,TextSendMessage("กรุณาระบุเป็นตัวเลขเท่านั้นคะ (พิมพ์เลข 1-5)"))
        
        elif  user_session == "บันทึกอาการไอ":
            if MESSAGE_FROM_USER in ["1","2","3","4","5"]: # validate input
                data = {"มีอาการไอ" : MESSAGE_FROM_USER}
                update_daily_tracking(uid=UID,new_data=data,firebase_app=firebase,database_name=DB_COV_TRACKER) # update
                
                session_data = {"session" : "บันทึกอาการเจ็บคอ"}
                update(uid=UID,new_data=session_data,firebase_app=firebase,database_name=DB_USER_SESSION) # update
                
                #Reponse กลับไปที่ห้องแชท
                Bubble = Base.get_or_new_from_json_dict(คำถามอาการเจ็บคอ,FlexSendMessage)
                line_bot_api.reply_message(REPLY_TOKEN,Bubble)
            else :
                line_bot_api.reply_message(REPLY_TOKEN,TextSendMessage("กรุณาระบุเป็นตัวเลขเท่านั้นคะ (พิมพ์เลข 1-5)"))
        
        elif  user_session == "บันทึกอาการเจ็บคอ":
            if MESSAGE_FROM_USER in ["1","2","3","4","5"]: # validate input
                data = {"มีอาการเจ็บคอ" : MESSAGE_FROM_USER}
                update_daily_tracking(uid=UID,new_data=data,firebase_app=firebase,database_name=DB_COV_TRACKER) # update
                
                session_data = {"session" : "บันทึกอาการน้ำมูกไหล"}
                update(uid=UID,new_data=session_data,firebase_app=firebase,database_name=DB_USER_SESSION) # update
                
                #Reponse กลับไปที่ห้องแชท
                Bubble = Base.get_or_new_from_json_dict(คำถามอาการน้ำมูกไหล,FlexSendMessage)
                line_bot_api.reply_message(REPLY_TOKEN,Bubble)
            else :
                line_bot_api.reply_message(REPLY_TOKEN,TextSendMessage("กรุณาระบุเป็นตัวเลขเท่านั้นคะ (พิมพ์เลข 1-5)"))

        elif  user_session == "บันทึกอาการน้ำมูกไหล":
            if MESSAGE_FROM_USER in ["1","2","3","4","5"]: # validate input
                data = {"น้ำมูกไหล" : MESSAGE_FROM_USER}
                update_daily_tracking(uid=UID,new_data=data,firebase_app=firebase,database_name=DB_COV_TRACKER) # update
                
                session_data = {"session" : "บันทึกอาการเหนื่อยหอบ"}
                update(uid=UID,new_data=session_data,firebase_app=firebase,database_name=DB_USER_SESSION) # update
                
                #Reponse กลับไปที่ห้องแชท
                Bubble = Base.get_or_new_from_json_dict(คำถามอาการเหนื่อยหอบ,FlexSendMessage)
                line_bot_api.reply_message(REPLY_TOKEN,Bubble)
            else :
                line_bot_api.reply_message(REPLY_TOKEN,TextSendMessage("กรุณาระบุเป็นตัวเลขเท่านั้นคะ (พิมพ์เลข 1-5)"))

        elif  user_session == "บันทึกอาการเหนื่อยหอบ":
            if MESSAGE_FROM_USER in ["1","2","3","4","5"]: # validate input
                data = {"เหนื่อยหอบ" : MESSAGE_FROM_USER}
                
                update_daily_tracking(uid=UID,new_data=data,firebase_app=firebase,database_name=DB_COV_TRACKER) # update
                
                session_data = {"session" : "บันทึกอาการอื่นๆ"}
                update(uid=UID,new_data=session_data,firebase_app=firebase,database_name=DB_USER_SESSION) # update
                
                user_daily_data = get_daily_tracking(uid=UID,firebase_app=firebase,database_name=DB_COV_TRACKER)
                result = analyze_covid_from_user(UID,user_daily_data)
                
                post_daily_tracking(uid=UID,data=result,firebase_app=firebase,database_name=DB_COV_TRACKER)
                
                qbtn = QuickReplyButton(image_url="https://www.krungsri.com/bank/getmedia/1f37428a-a9e9-4860-9efd-90aeb886d3d5/krungsri-coronavirus-insurance-detail.jpg.aspx?resizemode=1",
                                        action=MessageAction(label="ไม่มีแล้วจร้า",text="ไม่มีแล้วจร้า"))
                
                qrep = QuickReply(items=[qbtn])
                
                line_bot_api.reply_message(REPLY_TOKEN,TextSendMessage("เรียบร้อยแล้วคะ🧡🧡 \n ท่านมีอาการอื่นๆเพิ่มเติมอีกไหมคะ \n 💪💪 บอกน้องหมอได้นะ",quick_reply=qrep)) # reponse
            
            else :
                line_bot_api.reply_message(REPLY_TOKEN,TextSendMessage("กรุณาระบุเป็นตัวเลขเท่านั้นคะ (พิมพ์เลข 1-5)"))

        elif  user_session == "บันทึกอาการอื่นๆ":
                data = {"อาการอื่นๆที่พบ" : MESSAGE_FROM_USER}
                
                update_daily_tracking(uid=UID,new_data=data,firebase_app=firebase,database_name=DB_COV_TRACKER) # update
                
                session_data = {"session" : "None"}
                update(uid=UID,new_data=session_data,firebase_app=firebase,database_name=DB_USER_SESSION) # update
                
                user_daily_data = get_daily_tracking(uid=UID,firebase_app=firebase,database_name=DB_COV_TRACKER)
                result = analyze_covid_from_user(UID,user_daily_data)
                
                post_daily_tracking(uid=UID,data=result,firebase_app=firebase,database_name=DB_COV_TRACKER)
                
                raw_Bubble = GenerateResultMsg(Profile_name=DISPLAY_NAME , UserId=UID , Dict_daily_data=result)
                Bubble = Base.get_or_new_from_json_dict(raw_Bubble,FlexSendMessage)
                line_bot_api.reply_message(REPLY_TOKEN,Bubble)


@handler.add(FollowEvent)
def handler_Follow(event):
    UID = event.source.user_id
    REPLY_TOKEN = event.reply_token
    line_bot_api.link_rich_menu_to_user(user_id=UID , rich_menu_id="richmenu-58d183f8dde81277a8f1d554c1ebacfb")

    #ส่งรูปภาพ
    image_message = ImageSendMessage(
    original_content_url='https://www.krungsri.com/bank/getmedia/1f37428a-a9e9-4860-9efd-90aeb886d3d5/krungsri-coronavirus-insurance-detail.jpg.aspx?resizemode=1',
    preview_image_url='https://www.krungsri.com/bank/getmedia/1f37428a-a9e9-4860-9efd-90aeb886d3d5/krungsri-coronavirus-insurance-detail.jpg.aspx?resizemode=1'
)
    
    qbtn1 = QuickReplyButton(image_url="https://www.krungsri.com/bank/getmedia/1f37428a-a9e9-4860-9efd-90aeb886d3d5/krungsri-coronavirus-insurance-detail.jpg.aspx?resizemode=1",
                            action=MessageAction(label="เริ่มบันทึกอาการป่วย",text="เริ่มบันทึกอาการป่วย"))
    
    qbtn2 = QuickReplyButton(image_url="https://www.krungsri.com/bank/getmedia/1f37428a-a9e9-4860-9efd-90aeb886d3d5/krungsri-coronavirus-insurance-detail.jpg.aspx?resizemode=1",
                            action=MessageAction(label="วันนี้เป็นไงบ้าง",text="วันนี้เป็นไงบ้าง"))
    
    qrep = QuickReply(items=[qbtn1,qbtn2])
    text_message = TextSendMessage(text="ยินดีต้อนรับเข้าสู่ บันทึกของผู้กักตัว" ,quick_reply=qrep)
    
    line_bot_api.reply_message(REPLY_TOKEN,messages=[image_message,text_message])


if __name__ == "__main__":
    app.run(port=80,debug=True)