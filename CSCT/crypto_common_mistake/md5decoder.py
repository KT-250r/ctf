#~ MD5 Decoder
#~ Coder : Cavid Rustamli
#~ Instagram : @rust4mlee

import os,requests,sys

if os.name == "nt":
	os.system("cls")
else:
	os.system("clear")
	
print("""
               _ _____     _                    _           
              | |  ___|   | |                  | |          
 _ __ ___   __| |___ \  __| | ___  ___ ___   __| | ___ _ __ 
| '_ ` _ \ / _` |   \ \/ _` |/ _ \/ __/ _ \ / _` |/ _ \ '__|
| | | | | | (_| /\__/ / (_| |  __/ (_| (_) | (_| |  __/ |   
|_| |_| |_|\__,_\____/ \__,_|\___|\___\___/ \__,_|\___|_|   
                                                            
    by Cavid Rustamli ~ @rust4mlee                                                        
""")
md5dir = input("[*] MD5 list --> ")
try:
	print("[!] Please wait...")
	md5list = open(md5dir,"r").read().splitlines()
	for md5 in md5list:
		try:
			r = requests.get("http://www.nitrxgen.net/md5db/" + md5)
			if r.headers['Content-Length'] == "0":
				print("[-] MD5 not cracked   =====>   | " + md5 + " |")
				with open("md5_results.txt","a") as f:
					f.write("Not cracked   ===>   | " + md5 + " | " + "\n")
			else:
				print("[+] MD5 cracked !!!   =====>   | " + md5 + " | " + r.text)
				with open("md5_results.txt","a") as f:
					f.write("Cracked !!!  ===>   | " + md5 + " | " + r.text + "\n")
		except:
			pass
except:
	print("[-] MD5 list not found!")
	sys.exit()