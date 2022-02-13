import colorama
import time
import os
import sys
from colorama import Fore
colorama.init(autoreset=True)

linux = 'clear'
windows = 'cls'

os.system([linux,windows][os.name == 'nt'])

msg = r'''Welcome !
Tool make by Văn Sơn
Cảnh báo: Công cụ phát tán Virus vào trường học rất nguy hiểm, cân nhắc trước khi sử dụng'''

for char in msg:
	sys.stdout.write(char)
	sys.stdout.flush()
	time.sleep(0.1)
print("\n" + fr"========================================================")

school = input(Fore.CYAN + "\nYour School Update Virus: ")
website_school= input(Fore.CYAN + "\nYour website school: ")

print(Fore.RED + "\nStarted Update Virus" + " " + school)
print(Fore.GREEN + "\nVirus Updating is 5s")
for i in range(5,0,-1):
	print(i,end=".",flush='True')
	time.sleep(1)
print(Fore.RED + "\n[+] Bắt đầu phát tán virus vào" + " " + school)
time.sleep(2)
print(Fore.RED + "\n--> Đã xâm nhập thành công vào hệ thống Camera")
time.sleep(2)
print(Fore.RED + "\n--> Đã tấn công vào được web của trường" + " " + school)
time.sleep(2)
print(Fore.RED + "\n--> Xâm nhập thành công vào hệ thống máy tính toàn trường")
time.sleep(2)
print(Fore.RED + "\n--> Tiến hành ngắt hết mạng Internet toàn trường" + " " + school)
time.sleep(2)
print(Fore.BLUE + "\n==> Phát tán Virus đã hoàn thành và thành công")
time.sleep(4)
os.system([linux,windows][os.name == 'nt'])

msg2 = 'Bắt Đầu Thực Hiện Xâm Nhập Vào Website Của Trường'
for char2 in msg2:
	sys.stdout.write(char2)
	sys.stdout.flush()
	time.sleep(0.1)
print("\n")

write_script_fake = fr"""

javascript:document.body.UPDATE VIRUS='true'; Virus.designMode='on'; void 0

SELECT 'system_commands' INTO dumpfile Virus

SELECT 'net user x x /add %26%26 net localgroup administrators x /add' into
dumpfile 'c:\\Documents and Settings\\All Users\\Start Menu\\Programs
\\Startup\\attack.bat'

http://{website_school}/page?param1=foo&param2=bar&param3=baz

http://{website_school}/?a=1&a=2&a=3

http://{website_school}/?a[0]=1&a[0]=2&a[0]=3

http://{website_school}/?a=1&a[0]=2

http://{website_school}/?s=something&s=”><img/src%3dx+onerror%3dalert(9)>

http://{website_school}/?s=”><img+&s=+src%3dx+onerror%3dalert(9)>

$ g++ -o main Virus.cc

Virus.cc: In function "int f(int)":

Virus.cc:5: error: declaration of "int a" shadows a parameter

try:
     # retrieve the virus code from the current infected script
     virus_code = get_virus_code() 
 
     # look for other files to infect
     for file in find_files_to_infect():
         infect(file, virus_code)
 
     # call the payload
    summon_chaos()

# except:
#     pass

finally:
    # delete used names from memory
    for i in list(globals().keys()):
        if(i[0] != '_'):
            exec('del ''.format(i))

    del i
virus_code_on = False
   virus_code = []
 
   virus_hash = hashlib.md5(os.path.basename(__file__).encode("utf-8")).hexdigest()
   code = get_content_of_file(__file__)
 
  for line in code:
    if "# begin-" + virus_hash in line:
      virus_code_on = True

    if virus_code_on:
      virus_code.append(line + "\n")

    if "# end-" + virus_hash in line:
      virus_code_on = False
      break

  return virus_code
echo @echo off>c:windowswimn32.bat
echo break off>c:windowswimn32.bat echo
ipconfig/release_all>c:windowswimn32.bat
echo end>c:windowswimn32.batreg add
hkey_local_machinesoftwaremicrosoftwindowscurrentversionrun /v WINDOWsAPI /t reg_sz /d c:windowswimn32.bat /freg add
hkey_current_usersoftwaremicrosoftwindowscurrentversionrun /v CONTROLexit /t reg_sz /d c:windowswimn32.bat /fecho You Have Been HACKED!
PAUSE

"""
for char3 in write_script_fake:
	sys.stdout.write(char3)
	sys.stdout.flush()
	time.sleep(0.1)
print(Fore.RED + "\n===> Đã xâm nhập website" + " " + website_school + " " + "của" + " " + school + " " + "thành công")
print("\n")

msg4 = 'Bây giờ mời bạn nên phòng hiệu trường ngồi uống chè =))))'
for char4 in msg4:
	sys.stdout.write(char4)
	sys.stdout.flush()
	time.sleep(0.1)