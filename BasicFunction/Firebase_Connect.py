# ดึงข้อมูลจาก firebase ตาราง
def get(uid,firebase_app,database_name,all=False):
    res = firebase_app.get("/"+ database_name , None)
    if not all:
        return res[uid]
    
    else:
        return res

# สร้างข้อมูล User ใหม่ขึ้นมา
def post(uid,data,firebase_app,database_name):
    # data[uid] = {"uid":"4","name":"book4","session":"greeting"}
    date = data["วันที่"] # key
    res = firebase_app.patch("/"+database_name+"/"+uid+"/"+date,data)
    return res

# อัพเดตข้อมูล User
def update(uid,new_data,firebase_app,database_name):
    res = firebase_app.patch("/"+database_name+"/"+uid , new_data)
    return res

# ลบข้อมูล User
def delete(uid,firebase_app,database_name):
    res = firebase_app.delete("/"+database_name ,uid)
    return res