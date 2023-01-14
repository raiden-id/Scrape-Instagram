import requests, json

c = {'Cookie':'ig_did=2B5DA078-C84F-493B-B7EF-CBC3A6E592D0;ig_nrcb=1;mid=Yz_asQABAAEG57JFqdJwkLAuRrva;datr=Q_w_Yw71iH-OSDNW4sj9T8Es;fbm_124024574287414=base_domain=.instagram.com;dpr=2.75;fbsr_124024574287414=jQUHsBD_L2HCbvBPsuqykomlE05sicvRi4DirQzoCmc.eyJ1c2VyX2lkIjoiMTAwMDM2MDY1NzQzODAwIiwiY29kZSI6IkFRQnBJc2xJU0hYaEdhN3J0dU5XX25wRnp4SVRHdDFpRlJwTG5uV1h4UlQ0WFVpS1NUYjRHbFZnb0RTalZCdENKbGs2b3pNZmFRSzNlQ2JNTnRkaEZBLUpYdWo1Y2FtczR1N3NrQXYtc1FaTzAwblFZLVNoTTdEM19rc08yei1hV2FFcE0tYWxkZ3V5bndHMnh6b1VmX1FNUXlIbVBVelE3aWhzOWROM041R0JVUzlFbU9OZFlXRlZhVnVaNnZ0S1NUWkFrbTloREJiaVpkZXgzeUZreU4zMGJTajQwbDBRdGxPSGJsQkF3c054SzRDSW5PSncyT1JLTlJhSW1sTTBTczlvcXQwX2I0VkZwVGdwY0dMcUlSaXdia1pYNldMTzFqYUlVZ2FrYzJTdFNmQjhraktDTVJORDBLTjFqZHM2SFp1bW9oQmhOaTFwZDNKR1RSUjAxTTVoIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUlqV3l5RFkyeVpDV0tveVRrUWQ4YWMxQ2lQTWs3NVBwYmVscHVpTVpDcXVQMVFZZWJBVjdLSzZzNmtKSHplb1pCbkI1SjIwbTd3TUlSWUZhbHA0aVpBZXlmNzFBdUpuN3Q0bFJPYnY2VXRnR1RaQUF6a3h5VDJHOVpDc2lFcm1JYjhmakRXQURLNjZjYmxxeXlaQTRrWkJlNGpHaUxtUjZITGlyQzlxWkFVcEIiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTY3MjE4NDIwMX0;csrftoken=ueblwG6ynmEko5GJ0fgWR6Em6LXYBw7E;ds_user_id=13286955926;sessionid=13286955926%3APGerdL3cKuauI3%3A21%3AAYedOV2vlgzv9NDCsXCsWeu8s_A1EO8lnyUZT_V-vg;shbid="11125\05413286955926\0541703720207:01f7099cbf9720cd7f4a92d9940e698281dc0fe1648d800dd9052eace0a4cc5d10b26b8b";shbts="1672184207\05413286955926\0541703720207:01f75041b1e8d088dc41d6472ad75b32669eb74d6b4308c4a9acc5d7e8e751f7057a5c63";rur="PRN\05413286955926\0541703720228:01f7e31038d4878b90549bbd2e0062429f8ec0fab053b2ead9ee45df5422b88473b0a6b7"'}

def query(name):
	url = f"https://i.instagram.com/api/v1/web/search/topsearch/?context=blended&query={name}&rank_token=0.2571702827593578&include_reel=true"
	ses = requests.Session()
	r = ses.get(url,cookies=c,headers={"user-agent":'Mozilla/5.0 (iPhone; CPU iPhone OS 15_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 213.1.0.22.117 (iPhone13,2; iOS 15_0_2; en_US; en-US; scale=3.00; 1170x2532; 332048479'})
	x = json.loads(r.text)
	for a in x["users"]:
		print(a["user"]["username"]+"-"+a["user"]["full_name"])
	for i in x["hashtags"]:
		hastag = (i["hashtag"]["name"] + "-" + i["hashtag"]["search_result_subtitle"]) 
		print("TAG : "+hastag) 

query("angga")
	