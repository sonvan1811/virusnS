import colorama
import time
import os
from colorama import Fore
colorama.init(autoreset=True)

linux = 'clear'
windows = 'cls'

os.system([linux,windows][os.name == 'nt'])

print(Fore.RED + "\n[+] Công cụ phát tán Virus")
print(Fore.RED + "\n[+] Tool Make By Văn Sơn")
print(Fore.GREEN + "\n=========================================")

school = input(Fore.CYAN + "\nYour School Update Virus: ")

print(Fore.RED + "\nStarted Update Virus" + " " + school)
print(Fore.GREEN + "\nVirus Updating is 5s")
for i in range(5,0,-1):
	print(i,end=".",flush='True')
	time.sleep(1)
print(Fore.RED + "\n[+] Bắt đầu phát tán virus vào" + " " + school)
time.sleep(0.2)
print(Fore.RED + "\n--> Đã xâm nhập thành công vào hệ thống Camera")
time.sleep(0.2)
print(Fore.RED + "\n--> Đã tấn công vào được web của trường" + " " + school)
time.sleep(0.2)
print(Fore.RED + "\n--> Xâm nhập thành công vào hệ thống máy tính toàn trường")
time.sleep(0.2)
print(Fore.RED + "\n--> Tiến hành ngắt hết mạng Internet toàn trường" + " " + school)
time.sleep(0.2)
print(Fore.BLUE + "\n==> Phát tán Virus đã hoàn thành và thành công")