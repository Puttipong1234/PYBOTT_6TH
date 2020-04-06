import requests

def get_case_location_data(Province):
    res = requests.get(url="https://covid19.th-stat.com/api/open/cases/sum")
    res = res.json()
    return res["Province"][Province]

res = get_case_location_data(Province="Bangkok")

def get_location_reccommend_data(Province):
    res = requests.get(url="https://covid19.th-stat.com/api/open/area")
    res = res.json()
    print(res["Data"])
    data = []
    for each in res["Data"]:
        if each["Province"] == Province:
            data.append(each)

    return data
    

# res = get_case_location_data(Province="Bangkok")
res = get_location_reccommend_data(Province="สงขลา")
print(res)