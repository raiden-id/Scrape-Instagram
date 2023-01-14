# writen by Muhamad Huda
import requests,re,json,time,datetime


cv  =    {"01":"Januari","02":"Febuari","03":"Maret","04":"April","05":"Mei","06":"Juni","07":"Juli","08":"Agustus","09":"September","10":"Oktober","11":"November","12":"Desember"}
def description(user,coki):
	ses = requests.Session()
	url = (f'https://i.instagram.com/api/v1/users/web_profile_info/?username={user}')
	acc = (f'https://www.instagram.com/accounts/access_tool/?__a=1')
	hea = {
	'Host': 'i.instagram.com',
	'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
	'x-ig-app-id': '1217981644879628',
	'x-ig-www-claim': 'hmac.AR1-tfMt5o_UDCMM3xmiKmHH4jofwWDY8rnyParpnlCtMJMf',
	'sec-ch-ua-mobile': '?1',
	'user-agent': 'Mozilla/5.0 (Linux; Android 11; RMX2180) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Mobile Safari/537.36',
	'viewport-width': '501',
	'accept': '*/*',
	'x-asbd-id': '198387',
	'x-csrftoken': 'missing',
	'sec-ch-ua-platform': '"Android"',
	'sec-fetch-site': 'same-site',
	'sec-fetch-mode': 'cors',
	'sec-fetch-dest': 'empty',
	'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
	}
	r   = ses.get(url,headers=hea).json()['data']['user']
	try:   q   = requests.get(acc,cookies={'Cookie':coki}).json()
	except:q   = requests.get(acc).json()

	try:   stamp 		= q["date_joined"]["data"]["timestamp"]
	except:stamp		= '1556951916'
	created		= tahun_pembuatan(stamp)
	ttl		= get_ttl(stamp)

	nama    	= r['full_name']
	follower	= r['edge_followed_by']['count']
	following	= r['edge_follow']['count']
	posted		= r['edge_owner_to_timeline_media']['count']
	all 	        = nama , follower , following , posted, created , ttl

	return all

def tahun_pembuatan(time):
	timestamp = datetime.datetime.fromtimestamp(time)
	bulan = cv[str(timestamp.strftime('%m'))]
	return timestamp.strftime(f'%d {bulan} %Y %H:%M')

def get_ttl(time):
	timestamp = datetime.datetime.fromtimestamp(time)
	bulan = cv[str(timestamp.strftime('%m'))]
	return timestamp.strftime(f'%d {bulan} %Y')


