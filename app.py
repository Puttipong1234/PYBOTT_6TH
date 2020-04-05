from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
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
            "ข้อเสนอแนะ" : ""
            }
            
            # create user daily report
            post_daily_tracking(uid=UID , data=daily_report , firebase_app=firebase , database_name=DB_COV_TRACKER)
            # update session
            
            session_data = {"session" : "บันทึกอาการไข้"}
            update(uid=UID,new_data=session_data,firebase_app=firebase,database_name=DB_USER_SESSION)
            
            #Reponse กลับไปที่ห้องแชท
            line_bot_api.reply_message(REPLY_TOKEN,TextSendMessage("ท่านมีอาการไข้สูงหรือไม่คะ? กรุณาระบุระดับความรุนแรงของอาการ (พิมพ์เลข 1-5)"))
            
    
    ### func อื่นๆ
    else:
        if  user_session == "บันทึกอาการไข้": # validate session
                # "3" != 3
            if MESSAGE_FROM_USER in ["1","2","3","4","5"]: # validate input
                data = MESSAGE_FROM_USER
                update_daily_tracking(uid=UID,new_data=data,firebase_app=firebase,database_name=DB_COV_TRACKER,fields="มีไข้") # update
                
                session_data = {"session" : "บันทึกอาการไข้"}
                update(uid=UID,new_data=session_data,firebase_app=firebase,database_name=DB_USER_SESSION) # update
                
                line_bot_api.reply_message(REPLY_TOKEN,TextSendMessage("บันทึกอาการไข้เรียบร้อยแล้วคะ ต่อไปกรุณาระบุอาการไอด้วยคะ (พิมพ์เลข 1-5)")) # reponse
            else :
                line_bot_api.reply_message(REPLY_TOKEN,TextSendMessage("กรุณาระบุเป็นตัวเลขเท่านั้นคะ (พิมพ์เลข 1-5)"))
        
        elif  user_session == "บันทึกอาการไอ":
            if MESSAGE_FROM_USER in ["1","2","3","4","5"]: # validate input
                data = MESSAGE_FROM_USER
                update_daily_tracking(uid=UID,new_data=data,firebase_app=firebase,database_name=DB_COV_TRACKER,fields="มีอาการไอ") # update
                
                session_data = {"session" : "บันทึกอาการเจ็บคอ"}
                update(uid=UID,new_data=session_data,firebase_app=firebase,database_name=DB_USER_SESSION) # update
                
                line_bot_api.reply_message(REPLY_TOKEN,TextSendMessage("บันทึกอาการไอเรียบร้อยแล้วคะ ต่อไปกรุณาระบุอาการเจ็บคอด้วยคะ (พิมพ์เลข 1-5)")) # reponse
            else :
                line_bot_api.reply_message(REPLY_TOKEN,TextSendMessage("กรุณาระบุเป็นตัวเลขเท่านั้นคะ (พิมพ์เลข 1-5)"))
        
        elif  user_session == "บันทึกอาการเจ็บคอ":
            if MESSAGE_FROM_USER in ["1","2","3","4","5"]: # validate input
                data = MESSAGE_FROM_USER
                update_daily_tracking(uid=UID,new_data=data,firebase_app=firebase,database_name=DB_COV_TRACKER,fields="มีอาการเจ็บคอ") # update
                
                session_data = {"session" : "บันทึกอาการน้ำมูกไหล"}
                update(uid=UID,new_data=session_data,firebase_app=firebase,database_name=DB_USER_SESSION) # update
                
                line_bot_api.reply_message(REPLY_TOKEN,TextSendMessage("บันทึกอาการเจ็บคอเรียบร้อยแล้วคะ ต่อไปกรุณาระบุอาการน้ำมูกไหลด้วยคะ (พิมพ์เลข 1-5)")) # reponse
            else :
                line_bot_api.reply_message(REPLY_TOKEN,TextSendMessage("กรุณาระบุเป็นตัวเลขเท่านั้นคะ (พิมพ์เลข 1-5)"))

        elif  user_session == "บันทึกอาการน้ำมูกไหล":
            if MESSAGE_FROM_USER in ["1","2","3","4","5"]: # validate input
                data = MESSAGE_FROM_USER
                update_daily_tracking(uid=UID,new_data=data,firebase_app=firebase,database_name=DB_COV_TRACKER,fields="น้ำมูกไหล") # update
                
                session_data = {"session" : "บันทึกอาการเหนื่อยหอบ"}
                update(uid=UID,new_data=session_data,firebase_app=firebase,database_name=DB_USER_SESSION) # update
                
                line_bot_api.reply_message(REPLY_TOKEN,TextSendMessage("บันทึกอาการไข้เรียบร้อยแล้วคะ ต่อไปกรุณาระบุอาการไอด้วยคะ (พิมพ์เลข 1-5)")) # reponse
            else :
                line_bot_api.reply_message(REPLY_TOKEN,TextSendMessage("กรุณาระบุเป็นตัวเลขเท่านั้นคะ (พิมพ์เลข 1-5)"))

        elif  user_session == "บันทึกอาการเหนื่อยหอบ":
            if MESSAGE_FROM_USER in ["1","2","3","4","5"]: # validate input
                data = MESSAGE_FROM_USER
                
                update_daily_tracking(uid=UID,new_data=data,firebase_app=firebase,database_name=DB_COV_TRACKER,fields="เหนื่อยหอบ") # update
                
                session_data = {"session" : "None"}
                update(uid=UID,new_data=session_data,firebase_app=firebase,database_name=DB_USER_SESSION) # update
                
                user_daily_data = get_daily_tracking(uid=UID,firebase_app=firebase,database_name=DB_COV_TRACKER)
                result = analyze_covid_from_user(user_daily_data)
                
                post_daily_tracking(uid=UID,data=result,firebase_app=firebase,database_name=DB_COV_TRACKER)
                
                line_bot_api.reply_message(REPLY_TOKEN,TextSendMessage("บันทึกอาการเหนื่อยหอบเรียบร้อยแล้วคะ นี้เป็นผลการตรวจจากการให้ข้อมูลของ่ทานนะคะ \n"+ str(result))) # reponse
            
            else :
                line_bot_api.reply_message(REPLY_TOKEN,TextSendMessage("กรุณาระบุเป็นตัวเลขเท่านั้นคะ (พิมพ์เลข 1-5)"))

    

    
    
    
    


if __name__ == "__main__":
    app.run(port=80,debug=True)