import aiohttp
import os
import json
import datetime
from datetime import datetime
import pytz
token = os.getenv('TOKEN')
waqi_response = ""
waqi_json = ""
async def get_data():
  async with aiohttp.ClientSession() as session:
    async with session.get(f'http://api.waqi.info/feed/hongkong/?token={token}') as json_data:
      waqi_response = await json_data.json()
      hk_timezone = pytz.timezone('Asia/Hong_Kong')
      hk_time = datetime.now(hk_timezone)
      hk_time_format = hk_time.astimezone(hk_timezone).strftime('%H:%M:%S')
      print(waqi_response)
      with open('waqi_response.json','w') as file:
        json.dump(waqi_response, file)
      with open('waqi_response.json','r') as file:
        waqi_json = json.loads(file.read())
      with open('air_aqi.txt','w') as txtfile:
        #I rather be storing this in a text file than parsing it with Javascript
        txtfile.write(str(waqi_json['data']['aqi']))
      with open('air_aqi.txt','a') as txtfile:
        #Could've written all in one go but eh
        txtfile.write(",")
        forecast_pm25 = waqi_json['data']['forecast']['daily']['pm25'][2]
        forecast_o3 = waqi_json['data']['forecast']['daily']['o3'][2]
        txtfile.write(str(forecast_pm25['avg']))
        txtfile.write(",")
        txtfile.write(str(forecast_pm25['max']))
        txtfile.write(",")
        txtfile.write(str(forecast_pm25['min']))
        txtfile.write(",")
        txtfile.write(str(forecast_o3['avg']))
        txtfile.write(",")
        txtfile.write(str(forecast_o3['max']))
        txtfile.write(",")
        txtfile.write(str(forecast_o3['min']))
        txtfile.write(",")
        txtfile.write(hk_time_format)
  return(waqi_response)