from datetime import date
from datetime import datetime

def analyze_covid_from_user(username,dict_report):
    
    today = date.today()
    now = datetime.now().strftime("%H:%M:%S")
    
    _input_current_date = str(today) + str(now) # วันที่ + เวลา ณ ตอนนั้น

    print("สรุปจากผลการตรวจสอบอาการเบื้องต้น พบว่า")
    score = 0

    if dict_report["มีไข้"] == "y":
        score += 20
        
    if dict_report["มีอาการไอ"] == "y":
        score += 20
        
    if dict_report["น้ำมูกไหล"] == "y":
        score += 20

    if dict_report["มีอาการเจ็บคอ"] == "y":
        score += 20

    if dict_report["เหนื่อยหอบ"] == "y":
        score += 20
    
    dict_report["score"] = score
    dict_report["วันที่"] = str(today)

    print("คุณ" + username)
    if 60 <= score < 100:
        dict_report["ข้อเสนอแนะ"] = "ควรกักตัวอยู่ที่บ้านนะคะ"
        print("ควรกักตัวอยู่ที่บ้านนะคะ")

    elif score == 100:
        print("ควรไปพบแพทย์เดี๋ยวนี้เลยคะ")
        dict_report["ข้อเสนอแนะ"] = "ควรไปพบแพทย์เดี๋ยวนี้เลยคะ"

    else :
        print("ไม่มีอาการสุ่มเสี่ยงต่อเชื่อไวรัส COVID-19")
        dict_report["ข้อเสนอแนะ"] = "ไม่มีอาการสุ่มเสี่ยงต่อเชื่อไวรัส"

    print("ข้อมูลการตรวจเฝ้าระวังวันที่ " + str(today))
    
    return dict_report