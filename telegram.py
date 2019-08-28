"""
python으로 telegram message 보내기
"""

import requests

token = '956871410:AAHQaQ447UboyBT-fKDTXKYcYeQl9lHgX8I'
base_url = 'https://api.telegram.org'

# (1) getUpdates를 통해 chat_id를 가져옴
url = f'{base_url}/bot{token}/getUpdates'
res = requests.get(url)
res_dict = res.json()

chat_id = res_dict['result'][0]['message']['chat']['id']

# (2) url을 조합하여 requests로 요청보내기
text = '자동화'
url = f'{base_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
requests.get(url)