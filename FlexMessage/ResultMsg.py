def GenerateResultMsg( Profile_name , UserId , Dict_daily_data):
    
    msg = {
  "type": "flex",
  "altText": "Flex Message",
  "contents": {
    "type": "carousel",
    "contents": [
      {
        "type": "bubble",
        "direction": "ltr",
        "header": {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "image",
              "url": "https://firebasestorage.googleapis.com/v0/b/pybott-6th.appspot.com/o/doctor%20(1).png?alt=media&token=74e146ed-e391-4cc6-95cf-6c58fc1032ca"
            },
            {
              "type": "text",
              "text": "Diagonos Result",
              "margin": "xl",
              "size": "lg",
              "align": "center",
              "weight": "bold",
              "color": "#FFFFFF"
            }
          ]
        },
        "body": {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "box",
              "layout": "vertical",
              "contents": [
                {
                  "type": "box",
                  "layout": "vertical",
                  "contents": [
                    {
                      "type": "text",
                      "text": "ข้อมูลผู้ป่วย",
                      "size": "xl",
                      "align": "center",
                      "weight": "bold",
                      "color": "#3F72AF"
                    },
                    {
                      "type": "text",
                      "text": "| ชื่อผู้เข้าตรวจ",
                      "margin": "md",
                      "weight": "bold",
                      "color": "#3F72AF"
                    },
                    {
                      "type": "text",
                      "text": "คุณ " + Profile_name,
                      "margin": "sm",
                      "align": "start",
                      "weight": "bold"
                    },
                    {
                      "type": "text",
                      "text": "| รหัสผู้ใช้งาน",
                      "margin": "xl",
                      "weight": "bold",
                      "color": "#3F72AF"
                    },
                    {
                      "type": "text",
                      "text": UserId,
                      "margin": "sm",
                      "size": "sm",
                      "align": "start",
                      "weight": "bold"
                    },
                    {
                      "type": "text",
                      "text": "| รายงานวันที่",
                      "margin": "xl",
                      "weight": "bold",
                      "color": "#3F72AF"
                    },
                    {
                      "type": "text",
                      "text": Dict_daily_data["วันที่"],
                      "margin": "sm",
                      "size": "sm",
                      "align": "start",
                      "weight": "bold"
                    }
                  ]
                }
              ]
            }
          ]
        },
        "footer": {
          "type": "box",
          "layout": "horizontal",
          "margin": "xl",
          "contents": [
            {
              "type": "box",
              "layout": "vertical",
              "margin": "xxl",
              "contents": [
                {
                  "type": "text",
                  "text": "ขอขอบพระคุณเป็นอย่างสูงที่ให้ความร่วมมือกับน้องหมอนะคะ",
                  "margin": "xl",
                  "align": "center",
                  "weight": "bold",
                  "color": "#FFFFFF",
                  "wrap": True
                }
              ]
            }
          ]
        },
        "styles": {
          "header": {
            "backgroundColor": "#3F72AF"
          },
          "footer": {
            "backgroundColor": "#3F72AF"
          }
        }
      },
      {
        "type": "bubble",
        "direction": "ltr",
        "header": {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "image",
              "url": "https://firebasestorage.googleapis.com/v0/b/pybott-6th.appspot.com/o/doctor%20(1).png?alt=media&token=74e146ed-e391-4cc6-95cf-6c58fc1032ca"
            },
            {
              "type": "text",
              "text": "Diagonos Result",
              "margin": "xl",
              "size": "lg",
              "align": "center",
              "weight": "bold",
              "color": "#FFFFFF"
            }
          ]
        },
        "body": {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "box",
              "layout": "vertical",
              "contents": [
                {
                  "type": "box",
                  "layout": "baseline",
                  "margin": "xxl",
                  "contents": [
                    {
                      "type": "text",
                      "text": "ข้อมูลอาการ",
                      "size": "xl",
                      "align": "center",
                      "weight": "bold",
                      "color": "#3F72AF"
                    }
                  ]
                },
                {
                  "type": "box",
                  "layout": "horizontal",
                  "margin": "sm",
                  "contents": [
                    {
                      "type": "box",
                      "layout": "vertical",
                      "flex": 7,
                      "contents": [
                        {
                          "type": "text",
                          "text": "อาการเฝ้าระวัง",
                          "size": "md",
                          "weight": "bold",
                          "color": "#3F72AF"
                        },
                        {
                          "type": "text",
                          "text": "มีไข้สูง",
                          "margin": "lg",
                          "align": "start",
                          "weight": "bold"
                        },
                        {
                          "type": "text",
                          "text": "ไอแห้ง",
                          "margin": "lg",
                          "align": "start",
                          "weight": "bold"
                        },
                        {
                          "type": "text",
                          "text": "เจ็บคอ",
                          "margin": "lg",
                          "align": "start",
                          "weight": "bold"
                        },
                        {
                          "type": "text",
                          "text": "เหนื่อยหอบ",
                          "margin": "lg",
                          "align": "start",
                          "weight": "bold"
                        },
                        {
                          "type": "text",
                          "text": "น้ำมูกไหล",
                          "margin": "lg",
                          "align": "start",
                          "weight": "bold"
                        }
                      ]
                    },
                    {
                      "type": "box",
                      "layout": "vertical",
                      "flex": 4,
                      "contents": [
                        {
                          "type": "text",
                          "text": "ระดับ(1-5)",
                          "size": "md",
                          "weight": "bold",
                          "color": "#3F72AF"
                        },
                        {
                          "type": "text",
                          "text": Dict_daily_data["มีไข้"],
                          "margin": "lg",
                          "align": "center",
                          "weight": "bold"
                        },
                        {
                          "type": "text",
                          "text": Dict_daily_data["มีอาการไอ"],
                          "margin": "lg",
                          "align": "center",
                          "weight": "bold"
                        },
                        {
                          "type": "text",
                          "text": Dict_daily_data["มีอาการเจ็บคอ"],
                          "margin": "lg",
                          "align": "center",
                          "weight": "bold"
                        },
                        {
                          "type": "text",
                          "text": Dict_daily_data["เหนื่อยหอบ"],
                          "margin": "lg",
                          "align": "center",
                          "weight": "bold"
                        },
                        {
                          "type": "text",
                          "text": Dict_daily_data["น้ำมูกไหล"],
                          "margin": "lg",
                          "align": "center",
                          "weight": "bold"
                        }
                      ]
                    }
                  ]
                },
                {
                  "type": "text",
                  "text": "อาการอื่นๆที่พบ",
                  "margin": "lg",
                  "weight": "bold",
                  "color": "#3F72AF"
                },
                {
                  "type": "text",
                  "text": Dict_daily_data["อาการอื่นๆที่พบ"],
                  "margin": "md",
                  "size": "sm",
                  "align": "end",
                  "color": "#707070"
                }
              ]
            }
          ]
        },
        "footer": {
          "type": "box",
          "layout": "horizontal",
          "margin": "xl",
          "contents": [
            {
              "type": "box",
              "layout": "vertical",
              "margin": "xxl",
              "contents": [
                {
                  "type": "text",
                  "text": "ขอขอบพระคุณเป็นอย่างสูงที่ให้ความร่วมมือกับน้องหมอนะคะ",
                  "margin": "xl",
                  "align": "center",
                  "weight": "bold",
                  "color": "#FFFFFF",
                  "wrap": True
                }
              ]
            }
          ]
        },
        "styles": {
          "header": {
            "backgroundColor": "#3F72AF"
          },
          "footer": {
            "backgroundColor": "#3F72AF"
          }
        }
      },
      {
        "type": "bubble",
        "direction": "ltr",
        "header": {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "image",
              "url": "https://firebasestorage.googleapis.com/v0/b/pybott-6th.appspot.com/o/doctor%20(1).png?alt=media&token=74e146ed-e391-4cc6-95cf-6c58fc1032ca"
            },
            {
              "type": "text",
              "text": "Diagonos Result",
              "margin": "xl",
              "size": "lg",
              "align": "center",
              "weight": "bold",
              "color": "#FFFFFF"
            }
          ]
        },
        "body": {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "box",
              "layout": "vertical",
              "contents": [
                {
                  "type": "box",
                  "layout": "baseline",
                  "margin": "xxl",
                  "contents": [
                    {
                      "type": "text",
                      "text": "ผลการตรวจ",
                      "size": "xl",
                      "align": "center",
                      "weight": "bold",
                      "color": "#3F72AF"
                    }
                  ]
                },
                {
                  "type": "box",
                  "layout": "baseline",
                  "margin": "sm",
                  "contents": [
                    {
                      "type": "text",
                      "text": Dict_daily_data["ข้อเสนอแนะ"],
                      "size": "sm",
                      "align": "center",
                      "color": "#505050",
                      "wrap": True
                    }
                  ]
                }
              ]
            }
          ]
        },
        "footer": {
          "type": "box",
          "layout": "horizontal",
          "margin": "xl",
          "contents": [
            {
              "type": "box",
              "layout": "vertical",
              "margin": "xxl",
              "contents": [
                {
                  "type": "text",
                  "text": "ขอขอบพระคุณเป็นอย่างสูงที่ให้ความร่วมมือกับน้องหมอนะคะ",
                  "margin": "xl",
                  "align": "center",
                  "weight": "bold",
                  "color": "#FFFFFF",
                  "wrap": True
                }
              ]
            }
          ]
        },
        "styles": {
          "header": {
            "backgroundColor": "#3F72AF"
          },
          "footer": {
            "backgroundColor": "#3F72AF"
          }
        }
      }
    ]
  }
}
    return msg