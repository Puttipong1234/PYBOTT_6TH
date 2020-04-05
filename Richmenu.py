richdata = {
  "size": {
    "width": 2500,
    "height": 1686
  },
  "selected": True,
  "name": "แถบช่วยเหลือ",
  "chatBarText": "แถบช่วยเหลือ",
  "areas": [
    {
      "bounds": {
        "x": 0,
        "y": 0,
        "width": 1670,
        "height": 849
      },
      "action": {
        "type": "message",
        "text": "4"
      }
    },
    {
      "bounds": {
        "x": 9,
        "y": 855,
        "width": 821,
        "height": 812
      },
      "action": {
        "type": "message",
        "text": "1"
      }
    },
    {
      "bounds": {
        "x": 849,
        "y": 855,
        "width": 802,
        "height": 802
      },
      "action": {
        "type": "message",
        "text": "2"
      }
    },
    {
      "bounds": {
        "x": 1679,
        "y": 855,
        "width": 802,
        "height": 809
      },
      "action": {
        "type": "message",
        "text": "3"
      }
    },
    {
      "bounds": {
        "x": 1679,
        "y": 0,
        "width": 802,
        "height": 840
      },
      "action": {
        "type": "message",
        "text": "เข้าสู่เมนู CSV Search"
      }
    }
  ]
}


from config import Channel_secret #
channel_access_token = Channel_secret
Image_File_Path = "Material\\richmenu.png"
import json

import requests



def RegisRich(Rich_json,channel_access_token):

    url = 'https://api.line.me/v2/bot/richmenu'

    Rich_json = json.dumps(Rich_json)

    Authorization = 'Bearer {}'.format(channel_access_token)


    headers = {'Content-Type': 'application/json; charset=UTF-8',
    'Authorization': Authorization}

    response = requests.post(url,headers = headers , data = Rich_json)

    print(str(response.json()['richMenuId']))

    return str(response.json()['richMenuId'])

def CreateRichMenu(ImageFilePath,Rich_json,channel_access_token):


    richId = RegisRich(Rich_json = Rich_json,channel_access_token = channel_access_token)

    url = ' https://api.line.me/v2/bot/richmenu/{}/content'.format(richId)

    Authorization = 'Bearer {}'.format(channel_access_token)

    headers = {'Content-Type': 'image/jpeg',
    'Authorization': Authorization}

    img = open(ImageFilePath,'rb').read()

    response = requests.post(url,headers = headers , data = img)

    print(response.json())


CreateRichMenu(ImageFilePath=Image_File_Path,Rich_json=richdata,channel_access_token=channel_access_token)