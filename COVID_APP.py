from BasicFunction.COVID_ANALYZER import analyze_covid_from_user
from firebase import firebase
from BasicFunction.Firebase_Connect import get , post , update , delete
from config import Firebase_DB_url
# Firebase_DB_url = "https://pybott-6th.firebaseio.com/" # Your firebase Application
firebase = firebase.FirebaseApplication(Firebase_DB_url, None)
DB_NAME = "COVID-19-Tracker"

while not input("Press x to Exit!") == "x":
    print("ยินดีต้องรับเข้าสู่บริการตรวจคัดกรองไวรัส COVID-19 \n คุณควรจะกักตัวหรือไม่")
    _input_name = input("กรุณากรอกชื่อของท่าน :   ")
    print("สวัสดีคุณ : " + _input_name)
    _input_has_fever = input("คุณ" + _input_name+" มีไข้สูงมากกว่า 37.5 องศา หรือไม่? (y/n) :   ")
    _input_has_cought = input("คุณ" + _input_name+" มีอาการไอหรือไม่ (y/n) :   ")
    _input_has_เจ็บคอ = input("คุณ" + _input_name+" มีอาการเจ็บคอหรือไม่ (y/n) :   ")
    _input_has_น้ำมูกไหล = input("คุณ" + _input_name+" มีอาการน้ำมูกไหลหรือไม่ (y/n) :   ")
    _input_has_เหนื่อยหอบ = input("คุณ" + _input_name+" มีอาการายใจเหนื่อยหอบ หายใจลำบากไหลหรือไม่ (y/n) :   ")

    ข้อมูลวันที่1 = {
        "มีไข้" : _input_has_fever,
        "มีอาการไอ" : _input_has_cought,
        "มีอาการเจ็บคอ" : _input_has_เจ็บคอ,
        "น้ำมูกไหล" : _input_has_น้ำมูกไหล,
        "เหนื่อยหอบ" : _input_has_เหนื่อยหอบ,
        "วันที่" : "",
        "score" : 0,
        "ข้อเสนอแนะ" : ""
    }

    result = analyze_covid_from_user(username=_input_name,dict_report=ข้อมูลวันที่1)
    print(result)

    post(uid=_input_name, data=result, firebase_app=firebase, database_name=DB_NAME) # post ไปที่ firebase


print("You are Exited!")
