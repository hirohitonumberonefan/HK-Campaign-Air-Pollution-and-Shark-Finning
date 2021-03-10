import aiohttp
import os
import json
token = os.getenv('TOKEN')
waqi_response = ""
waqi_json = ""
async def get_data():
  async with aiohttp.ClientSession() as session:
    async with session.get(f'http://api.waqi.info/feed/hongkong/?token={token}') as json_data:
      waqi_response = await json_data.json()
      print(waqi_response)
      with open('waqi_response.json','w') as file:
        json.dump(waqi_response, file)
      with open('waqi_response.json','r') as file:
        waqi_json = json.load(file)
      with open('air_aqi.txt','w') as txtfile:
        txtfile.write(str(waqi_json['data']['aqi']))
  return(waqi_response)
