import requests
from requests.auth import HTTPBasicAuth, HTTPDigestAuth
from bs4 import BeautifulSoup

domain = 'https://sbermarket.ru'
url = f'{domain}/user/shipments/H26279238074'

headers = {
    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    # 'Accept-Encoding': 'gzip, deflate',
    # 'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'Cache-Control': 'max-age=0',
    # 'Connection': 'keep-alive',
    # 'Cookie': 'PHPSESSID=6d22f1d5b66fa1539e3ee2df8b15c77d; InstantCMS[geodata]=a%3A7%3A%7Bs%3A7%3A%22inetnum%22%3Bs%3A27%3A%2246.158.0.0+-+46.159.255.255%22%3Bs%3A7%3A%22country%22%3Bs%3A2%3A%22RU%22%3Bs%3A4%3A%22city%22%3Bs%3A18%3A%22%D0%9A%D1%80%D0%B0%D1%81%D0%BD%D0%BE%D0%B4%D0%B0%D1%80%22%3Bs%3A6%3A%22region%22%3Bs%3A35%3A%22%D0%9A%D1%80%D0%B0%D1%81%D0%BD%D0%BE%D0%B4%D0%B0%D1%80%D1%81%D0%BA%D0%B8%D0%B9+%D0%BA%D1%80%D0%B0%D0%B9%22%3Bs%3A8%3A%22district%22%3Bs%3A44%3A%22%D0%AE%D0%B6%D0%BD%D1%8B%D0%B9+%D1%84%D0%B5%D0%B4%D0%B5%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9+%D0%BE%D0%BA%D1%80%D1%83%D0%B3%22%3Bs%3A3%3A%22lat%22%3Bs%3A9%3A%2245.042149%22%3Bs%3A3%3A%22lng%22%3Bs%3A9%3A%2238.980640%22%3B%7D; InstantCMS[logdate]=1577386070; InstantCMS[userid]=00cb7b95006f9aa9c861d9fc32fba967',
    # 'dnt': '1',
    # 'Host': 'dedmorozural.ru',
    # 'Upgrade-Insecure-Requests': '1',
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
    'authority': 'sbermarket.ru',
    'method': 'GET',
    'path': '/user/shipments/H26279238074',
    'scheme': 'https',
    'accept': 'text / html, application / xhtml + xml, application / xml; q = 0.9, image / avif, image / webp, image / apng, * / *;q = 0.8, application / signed - exchange; v = b3; q = 0.9',
    'accept - encoding': 'gzip, deflate, br',
    'accept - language': 'ru - RU, ru;    q = 0.9, en - US;    q = 0.8, en;    q = 0.7',
    'cache - control': 'max - age = 0',
    'cookie' : '_sa=SA1.d9d4de1d-91ce-4b22-be86-19b7a830a2c2.1657889911; adtech_uid=a2cf1430-cd7b-4b22-8cdb-900a1d208276%3Asbermarket.ru; _ym_uid=1657889913267271337; _ym_d=1657889913; __exponea_etc__=ae206062-ff7e-45ee-8cdd-072e5e5606b2; external_analytics_anonymous_id=39789a70-f832-436b-b2a6-3c323dd73a3e; city_info=%7B%22slug%22%3A%22rostov-na-donu%22%2C%22name%22%3A%22%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83%22%2C%22lat%22%3A47.2361%2C%22lon%22%3A39.7189%7D; _pk_ref.6.3ec0=%5B%22inh_b2c_yd_ua_web-desk_brand_ru-all_sea%7Cinhouse_search_ua-goal_desktop_brand_pure_city%22%2C%22sbermarket%22%2C1671300484%2C%22%22%5D; _pk_id.6.3ec0=be409fa2165b9fbd.1671300484.; iap.uid=541e7f5e2d8d4dbd80bf5f6a9c1bf1dd; top100_id=t1.7588506.1201145471.1671300484417; identified_address=true; remember_user_token=BAhbCFsGaQNY6rhJIhlLQnMyZExnb1JRbUdMVFN3Q1ZRTQY6BkVGSSIWMTY3MTMwMDY5MS40NDUyMDIGOwBG--6d04018006d937689c54a7c485fd04b0542aec4b; identified_user=true; resemble_b2b_tag=true; cookies_consented=yes; _pk_ses.6.3ec0=1; sessionId=16713232244418263264; ngenix_jscv_cd881f1695eb=cookie_signature=J0YRbXzJd2SAyG5UlO7ELs9CWHM%3D&cookie_expires=1671328279; ssrMedia={%22windowWidth%22:1096%2C%22primaryInput%22:%22touch%22}; _808db7ba1248=%5B%7B%22source%22%3A%22acs5.sbrf.ru%22%2C%22medium%22%3A%22referral%22%2C%22cookie_changed_at%22%3A1671306073%7D%2C%7B%22source%22%3A%22sbermarket.ru%22%2C%22medium%22%3A%22referral%22%2C%22cookie_changed_at%22%3A1671326577%7D%2C%7B%22source%22%3A%22%28direct%29%22%2C%22medium%22%3A%22%28none%29%22%2C%22cookie_changed_at%22%3A1671326579%7D%5D; last_visit=1671315780016%3A%3A1671326580016; _Instamart_session=MVBvc2lVNkdrdVREV0VhM29hZ3BGSm5Xd1RCN3FaYUxnbjc5Y25UOGtQdWtzN0I4bnNwckhoM25QakFMelplc242anE1UDlqVnFCZ2VzclNYVHg4aDZBSmdqTENpVGo2eUFGdlZlWlVjZFRrbTY2MFZxUkUwaHB2RC83VGhWb0xvUWxtN1NXd3NYRlBtTTJtNHhBSDhxYXJCeEdOY1V0WlVRaWN4S2w5VVNINHVtWnV3aVVENmMxU1UrSEVsM0x1cmZ1ZkhnbVRlUDMxQ3JRRWQ5V2o0WHlXRy96NmJsZmRtTHdRdlFwVUs1aFBVbTFjQVVFb2N5dDA5MjdnWmxuVUdHL0RaZGpFQXNXQllFamdKVXJRRll4dHZpTkNDaDNQZFVJSFJuMEFVL2ZEU1Q5ZXQrOXF6bHRpdG5zTkZmWDFKeDRJcmpyNXJaazVNREtHdzQyQlE0UWl0K0gyWUdHczB2Y3lLQVJUcUNIazVndmRLcjNyUXUzNVEzb2I2OGZCME00V3kweENpRFcrOVBlMUM2MlBVY0lHS3NlMFllbUpMUEdZaFlTL09wSlMwaDRDNnFsTGJSRmNVK255SEdibVFPQ0Q3UTk3VjZIMGtuZUlEQmdwS21wcFYvMFZZSXE1TFhsU1Vyd3VsZ0hZWHZiOUt6WkZuaXZ6UlhnTHhFcGVxeFAvUnZ6OThZak1EbFNMSURnRUZBcjVMR3E1WFpja3o5S0xhdHgwK2JSUnpXN3BNK3VpZDJhTUxmOXVMQVE0RS9kU3ZzRS9HejFOdnFPd1prRVo5ODY4MTQyNEhjQkdJZ1Rvc0FUU2N4bz0tLXJMb0QwTzBNOVIzU2xQMFZUMHBPVFE9PQ%3D%3D--ba5c018f8b1cbdc2f1ccb1408b5d39fe48cef124; t3_sid_7588506=s1.676064963.1671300484424.1671326591080.1.652',
    'referer': 'https://sbermarket.ru/user/shipments',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'
}
# response = requests.get(url, auth=HTTPDigestAuth('DanteOnline', 'dywtbofywed'))

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')

# span = soup.find('span', class_='register')
# print(span)

span = soup.find('span', class_='i-flocktory')
print(span)