import requests
from colorama import Fore
from os import system, name
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
clear()
print(Fore.GREEN + """
██╗░░██╗██╗░░██╗░█████╗░░░░░░░░██╗░░░░░░░██╗███████╗██████╗░
██║░░██║██║░░██║██╔══██╗░░░░░░░██║░░██╗░░██║██╔════╝██╔══██╗
███████║███████║██║░░╚═╝█████╗░╚██╗████╗██╔╝█████╗░░██████╦╝
██╔══██║██╔══██║██║░░██╗╚════╝░░████╔═████║░██╔══╝░░██╔══██╗
██║░░██║██║░░██║╚█████╔╝░░░░░░░░╚██╔╝░╚██╔╝░███████╗██████╦╝
╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░░░░░░░░░░╚═╝░░░╚═╝░░╚══════╝╚═════╝░

Created By : MR.HACKER
""")
hacktarget = input(Fore.CYAN + "[TARGET] : ")
hacktarget = hacktarget.replace("http://","")
hacktarget = hacktarget.replace("https://","")
hacktarget = hacktarget.replace("www.","")
hacktarget = "http://"+str(hacktarget)
testurl = requests.get(hacktarget)
if testurl.status_code == 200 :
	headers = ['Server', 'Date', 'Via', 'X-Powered-By', 'X-Country-Code','X-Frame-Options', 'Host', 'X-XSS-Protection', 'Cache-Control', 'Pragma', 'Content-Type', 'Content-Encoding', 'Accept-Encoding', 'X-UA-Compatible', 'IE', 'Date', 'Set-Cooki', 'Dnn_IsMobile', 'HttpOnly', 'Referer', 'Expires', 'User-Agent', 'Content-Length', 'X-Content-Type-Options', 'Content-Type', 'Connection', 'Authorization', 'Accept', 'A-IM', 'Accept-Charset', 'Accept-Datetime', 'Accept-Language', 'Expect', 'Origin', 'Forwarded', 'From', 'If-Match', 'If-Modified-Since', 'If-None-Match', 'If-Range', 'If-Unmodified-Since', 'Max-Forwards', 'Proxy-Authorization', 'Range', 'TE', 'Upgrade', 'Warning','Non-Standard-Headers' , 'Dnt', 'X-Requested-With', 'X-CSRF-Token']
	for header in headers:
		try:
			result = testurl.headers[header]
			print(Fore.GREEN + '%s: %s' % (header, result))
		except :
			print(Fore.RED  + '%s: Not found' % header)
else :
	hacktarget = "https://"+str(hacktarget)
	testurl = requests.get(hacktarget)
	if testurl.status_code == 200 :
		headers = ['Server', 'Date', 'Via', 'X-Powered-By', 'X-Country-Code','X-Frame-Options', 'Host', 'X-XSS-Protection', 'Cache-Control', 'Pragma', 'Content-Type', 'Content-Encoding', 'Accept-Encoding', 'X-UA-Compatible', 'IE', 'Date', 'Set-Cooki', 'Dnn_IsMobile', 'HttpOnly', 'Referer', 'Expires', 'User-Agent', 'Content-Length', 'X-Content-Type-Options', 'Content-Type', 'Connection', 'Authorization', 'Accept', 'A-IM', 'Accept-Charset', 'Accept-Datetime', 'Accept-Language', 'Expect', 'Origin', 'Forwarded', 'From', 'If-Match', 'If-Modified-Since', 'If-None-Match', 'If-Range', 'If-Unmodified-Since', 'Max-Forwards', 'Proxy-Authorization', 'Range', 'TE', 'Upgrade', 'Warning','Non-Standard-Headers' , 'Dnt', 'X-Requested-With', 'X-CSRF-Token']
		for header in headers:
			try:
				result = testurl.headers[header]
				print(Fore.GREEN + '%s: %s' % (header, result))
			except :
	    			print(Fore.RED  + '%s: Not found' % header)
	else :
		print(Fore.RED + "[-] " + Fore.WHITE + "PLEASE TRY AGAIN...")
exitfromapp = input(Fore.GREEN + "[+] " + "Press ENTER To Exit " )
if exitfromapp == "" :
	system("exit")
else :
	system("exit")
