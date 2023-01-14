import requests
import json
from time import sleep
from urllib.parse import quote
max_id = '100'
ca = 'ig_did=03EE6EAE-8885-47C0-8AA3-5638B7CB6E91; ig_nrcb=1; mid=YukyZAABAAEAYHvvfMtNt_OkDdWR; dpr=2.75; datr=os6sY1-stUnzaJQF7HWKTiia; csrftoken=iXbre5vD5TXXKKp75VvHiWgSyabIZXVR; ds_user_id=13286955926; sessionid=13286955926%3A8MsJ2RA5Weiw7L%3A5%3AAYcXV0NbPr8P3Ggmm9vfijYiztw5Og3PPyaeyAY2dw; shbid="11125\05413286955926\0541703834527:01f7e6da64fa2a3eb348a6c4cc1d093a265d5b4a2666910cd6fa4f0a7ccb61842ee696e0"; shbts="1672298527\05413286955926\0541703834527:01f77d7d4d312acdcb07361b1dfe79d016bc08d70ac33218cf05fc70292ca85d44a5c6b7"; rur="VLL\05413286955926\0541703847330:01f717843b6c10ceaa6f6af22e204256493697dca94a027f2e4a82406b452d8c769c3452"'
c = {'Cookie':ca}


session = requests.Session()

#session.cookies.set(ca)
base_url = "https://www.instagram.com/graphql/query/?query_hash=174a5243287c5f3a7de741089750ab3b&variables="
variables = {
        "tag_name": "cats",
        "first": "10",
        "after": None
}


result = session.get(base_url + quote(json.dumps(variables)),cookies=c)
posts = json.loads(result.content)["data"]["hashtag"]["edge_hashtag_to_media"]
for post in posts['edges']:
	a = post["node"]
print(a)
