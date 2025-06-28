try :
  from time import strftime
  from datetime import datetime, timedelta
  import re,requests,os,sys
  from datetime import date
  from time import sleep 
  from datetime import datetime 
except ImportError:
  os.system("pip install requests")
  os.system("pip install art")
  os.system("pip install colorama")
  os.system("pip install tabulate")
  os.system("pip install bs4")
  os.system("pip install pystyle")
  os.system("pip install curl_cffi")
  os.system("pip cài đặt random2")
  os.system("pip cài đặt selenium")
den = "\033[1;90m"
luc = "\033[1;32m"
trang = "\033[1;37m"
red = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
lamd = "\033[1;34m"
lam = "\033[1;36m"
hong = "\033[1;95m"
thanh_xau= trang + red + "[" + vang+ "⟨⟩" + red + "] " + trang + "➩ "
thanh_dep= trang + red + "[" + luc + "✓" + red + "] " + trang + "➩ "
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
tim = '\033[1;39m'
hong = "\033[1;35m"
trang = "\033[1;37m"
whiteb = "\033[1;37m"
red = "\033[0;31m"
redb = "\033[1;31m"
end = '\033[0m'
import os,sys
os.system('cls')
green = '\033[92m'
red = '\033[91m'
yellow = '\033[93m'
blue = '\033[94m'
cyan = '\033[96m'
purple = '\033[95m'
bold = '\033[1m'
reset = '\033[0m'
def loading_bar():
    os.system("clear" if os.name != "nt" else "cls")
    title = f"{bold}{cyan}🚀 Đang Loading Vào BETAPCODE"
    spinner = ["◐", "◓", "◑", "◒"]
    for i in range(100):
        spin = spinner[i % len(spinner)]
        bar = '█' * (i // 2) + '-' * ((100 - i) // 2)
        sys.stdout.write(f"\r{title} {purple}[{spin}] {i+1}% [{bar}]{reset}")
        sys.stdout.flush()
        sleep(0.01)
    os.system("clear" if os.name != "nt" else "cls")
loading_bar()
banner1=f'''
\033[1;39m┌────────────────────── Bé Tập Code TOOL ──────────────────────┐
\033[1;32m║ * Tool chạy trên cmd,codespace,teramux(ubuntu) (teramux thường không chạy đc)
\033[1;32m║ * Về Phía lỗi tool thì tool đẫ được test trước khi phát hành 
\033[1;32m║ * Nếu có lỗi thì liên hệ AD hoặc cài lại python đúng phiên bản
\033[1;32m║ * tool reg toktok có căn mới chạy đc
\033[1;39m└──────────────────────────────────────────────────────────────┘'''
banner = f""" 
\033[0;31m██╗░░██╗██╗░░░██╗██╗░░██╗  ████████╗░█████╗░░█████╗░██╗░░░░░
\033[1;32m██║░░██║██║░░░██║██║░░██║  ╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
\033[1;31m███████║╚██╗░██╔╝███████║  ░░░██║░░░██║░░██║██║░░██║██║░░░░░
\033[1;32m██╔══██║░╚████╔╝░██╔══██║  ░░░██║░░░██║░░██║██║░░██║██║░░░░░
\033[1;31m██║░░██║░░╚██╔╝░░██║░░██║  ░░░██║░░░╚█████╔╝╚█████╔╝███████╗
\033[1;32m╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝  ░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝
\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
\033[1;39m┌────────────────────── Bé Tập Code TOOL ──────────────────────┐
\033[1;32m║   \033[1;39mTOOL BY\033[1;32m            :  Bé Tập Code                          \033[1;32m║
\033[1;32m║   \033[1;39mYOUTUBER\033[1;32m           :  HVHTOOL                         \033[1;32m     ║
\033[1;32m║   \033[1;39mYOTUBE_LINK\033[1;32m        :  https://www.youtube.com/@HVHTOOL\033[1;32m     ║
\033[1;39m└──────────────────────────────────────────────────────────────┘
\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
"""


print(banner1)
#os.system("")

# màu


ngay=int(strftime('%d'))
time=datetime.now().strftime("%H:%M:%S")
from pystyle import *
data_machine = []
today = date.today()
now = datetime.now()
thu = now.strftime("%A")
ngay_hom_nay = now.strftime("%d")
thang_nay = now.strftime("%m")
nam_ = now.strftime("%Y")
os.system('cls')
print(banner)
print('Chạy tiến trình')



######################################################################################
os.system('cls')
print(banner)
os.system('cls')
print(banner)
### nhap key


os.system("cls")
time=datetime.now().strftime("%H:%M:%S")
data_machine = []
today = date.today()
now = datetime.now()
thu = now.strftime("%A")
ngay_hom_nay = now.strftime("%d")
thang_nay = now.strftime("%m")
nam_ = now.strftime("%Y")
os.system('cls')
print(banner)
print(banner1)
print('Chạy tiến trình')
print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;37m╔═════════════════════╗")
print("\033[1;37m║ \033[1;33m GOLIKE PC|IOS|ANR\033[1;37m  ║")
print("\033[1;37m╚═════════════════════╝")
print("\033[1;31m[\033[1;37mBé Tập Code\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m✨ 1 \033[1;31m] \033[1;32mTool GOLIKE AutoLinkedin\033[1;31m[\033[1;33m PC|CODESPACES\033[1;31m]")
print("\033[1;31m[\033[1;37mBé Tập Code\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m✨ 2 \033[1;31m] \033[1;32mTool GOLIKE INSTAGRAM AUTO RANDOM User_Agent \033[1;31m[\033[1;33m PC|CODESPACES|termux\033[1;31m]")
print("\033[1;31m[\033[1;37mBé Tập Code\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m✨ 3 \033[1;31m] \033[1;32mTool GOLIKE X \033[1;31m[\033[1;33m PC|CODESPACES|termux\033[1;31m]")
print("\033[1;31m[\033[1;37mBé Tập Code\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m✨ 4 \033[1;31m] \033[1;32mTool GOLIKE Theads \033[1;31m[\033[1;33m PC|CODESPACES|termux\033[1;31m]")
print("\033[1;31m[\033[1;37mBé Tập Code\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m✨ 5 \033[1;31m] \033[1;32mTool GOLIKE TIKTOK \033[1;31m[\033[1;33m termux\033[1;31m] ")
print("\033[1;31m[\033[1;37mBé Tập Code\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m✨ 6 \033[1;31m] \033[1;32mTool GOLIKE LAZADA \033[1;31m[\033[1;33m PC|CODESPACES|termux\033[1;31m]")
print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;37m╔═══════════════════════╗")
print("\033[1;37m║  \033[1;33m TOOL TTC  \033[1;37m         ║")
print("\033[1;37m╚═══════════════════════╝")
print("\033[1;31m[\033[1;37mBé Tập Code\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m✨ 7 \033[1;31m] \033[1;32mTool TTC INSTAGRAM RANDOM User_Agent \033[1;31m[\033[1;33m PC|CODESPACES|termux\033[1;31m]")
print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;37m╔═════════════════════╗")
print("\033[1;37m║  \033[1;33mTool FACEBOOK      \033[1;37m║")
print("\033[1;37m╚═════════════════════╝")
print("\033[1;31m[\033[1;37mBé Tập Code\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m✨ 8 \033[1;31m] \033[1;32m TOOL GET CMT BÀI VIẾT PORT FACEBOOK")
print("\033[1;31m[\033[1;37mBé Tập Code\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m✨ 9 \033[1;31m] \033[1;32mTool BUFF LIKE PAGE")
print("\033[1;31m[\033[1;37mBé Tập Code\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m✨ 10 \033[1;31m] \033[1;32mTool Share Ảo Cookie")
print("\033[1;31m[\033[1;37mBé Tập Code\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m✨ 11 \033[1;31m] \033[1;32mTool BUFF LIKE COMMENT")
print("\033[1;31m[\033[1;37mBé Tập Code\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m✨ 12 \033[1;31m] \033[1;32mTool BUFF FOLLOW PAGE ")
print("\033[1;31m[\033[1;37mBé Tập Code\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m✨ 13 \033[1;31m] \033[1;32mTool GET THÔNG TIN BÀI VIẾT ")
print("\033[1;31m[\033[1;37mBé Tập Code\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m✨ 14 \033[1;31m] \033[1;32mTool Tool REGPAGE PRO5 ")
print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;37m╔═════════════════════╗")
print("\033[1;37m║  \033[1;33mTool REG TIKTOK,FB\033[1;37m  ║")
print("\033[1;37m╚═════════════════════╝")
print("\033[1;31m[\033[1;37mBé Tập Code\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m✨ 15 \033[1;31m] \033[1;32mTool Tool REG TIKTOK CHROME(ĐA LUỒNG) (chrome driver tự đọng cập nhật)")
print("\033[1;31m[\033[1;37mBé Tập Code\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m✨ 16 \033[1;31m] \033[1;32mTool Tool REG FACEBOOK NOVERY CHROME(ĐA LUỒNG) (chrome driver tự đọng cập nhật)")
#print("\033[1;31m[\033[1;37mBé Tập Code\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m00\033[1;31m] \033[1;32mThoát Tool")
print("\033[1;31m────────────────────────────────────────────────────────────")
chon = int(input('\033[1;31m[\033[1;37mBé Tập Code\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;37m: \033[1;33m'))
#tool golike pc
if chon == 1 :
  exec(requests.get('https://raw.githubusercontent.com/Hoanghuy200/toolgop/refs/heads/main/TOOL_G%E1%BB%98P_HVHTOOOL/TOOL-GOLIKE/AutoLinkedin/AutoLinkedin_PC.py').text)
if chon == 2 :
  exec(requests.get('https://raw.githubusercontent.com/Hoanghuy200/toolgop/refs/heads/main/TOOL_G%E1%BB%98P_HVHTOOOL/TOOL-GOLIKE/IG/AUTOGOLIKEIG.py').text)
if chon == 3 :
  exec(requests.get('https://raw.githubusercontent.com/Hoanghuy200/toolgop/refs/heads/main/TOOL_G%E1%BB%98P_HVHTOOOL/TOOL-GOLIKE/X/AUTO-X_PC.py').text) 
if chon == 4 :
  exec(requests.get('https://raw.githubusercontent.com/Hoanghuy200/toolgop/refs/heads/main/TOOL_G%E1%BB%98P_HVHTOOOL/TOOL-GOLIKE/THRADS/AutoTheads.py').text)
elif chon == 5 : 
  exec(requests.get('https://raw.githubusercontent.com/Hoanghuy200/toolgop/refs/heads/main/TOOL_G%E1%BB%98P_HVHTOOOL/TOOL-GOLIKE/TIKTOK/goliketiktok.py').text)
elif chon == 6 :
  exec(requests.get('https://raw.githubusercontent.com/Hoanghuy200/toolgop/refs/heads/main/TOOL_G%E1%BB%98P_HVHTOOOL/TOOL-GOLIKE/LAZADA/LAZADA-PC/lazada.py').text)
if chon == 7 :
  exec(requests.get('https://raw.githubusercontent.com/Hoanghuy200/toolgop/refs/heads/main/TOOL_G%E1%BB%98P_HVHTOOOL/TTC/TTC%20INSTAGRAM/TTCIG_user-agent.py').text)
if chon == 8 :
  exec(requests.get('https://raw.githubusercontent.com/Hoanghuy200/toolgop/refs/heads/main/TOOL_G%E1%BB%98P_HVHTOOOL/TOOL%20TI%E1%BB%86N%20%C3%8DCH%20FACEBOOK/TOOL_GET_CMT_FB.py').text) 
if chon == 9 :
  exec(requests.get('https://raw.githubusercontent.com/Hoanghuy200/toolgop/refs/heads/main/TOOL_G%E1%BB%98P_HVHTOOOL/TOOL%20TI%E1%BB%86N%20%C3%8DCH%20FACEBOOK/LIKE%20PAGE%20PRO5%20VIP.py').text)
if chon == 10 :
  exec(requests.get('https://raw.githubusercontent.com/Hoanghuy200/toolgop/refs/heads/main/TOOL_G%E1%BB%98P_HVHTOOOL/TOOL%20TI%E1%BB%86N%20%C3%8DCH%20FACEBOOK/Tool%20Share%20%E1%BA%A2o%20Cookie%20%5BPRO5%5D.py').text)
if chon == 11 :
  exec(requests.get('https://raw.githubusercontent.com/Hoanghuy200/toolgop/refs/heads/main/TOOL_G%E1%BB%98P_HVHTOOOL/TOOL%20TI%E1%BB%86N%20%C3%8DCH%20FACEBOOK/LIKE_PAGE_BINHLUAN.py').text)
if chon == 12 :
  exec(requests.get('https://raw.githubusercontent.com/Hoanghuy200/toolgop/refs/heads/main/TOOL_G%E1%BB%98P_HVHTOOOL/TOOL%20TI%E1%BB%86N%20%C3%8DCH%20FACEBOOK/Tool%20Buff%20Follow%20B%E1%BA%B1ng%20Page%20Pro5.py').text)
if chon == 13 :
  exec(requests.get('https://raw.githubusercontent.com/Hoanghuy200/toolgop/refs/heads/main/TOOL_G%E1%BB%98P_HVHTOOOL/TOOL%20TI%E1%BB%86N%20%C3%8DCH%20FACEBOOK/GET_NOIDUNGFB.py').text)
if chon == 14 :
  exec(requests.get('https://raw.githubusercontent.com/Hoanghuy200/toolgop/refs/heads/main/TOOL_G%E1%BB%98P_HVHTOOOL/TOOL%20TI%E1%BB%86N%20%C3%8DCH%20FACEBOOK/%5B21%5D%20Tool%20Reg%20Page%20Pro5.py').text)
if chon == 15 :
  exec(requests.get('https://raw.githubusercontent.com/Hoanghuy200/toolgop/refs/heads/main/TOOL_G%E1%BB%98P_HVHTOOOL/regtiktok.py').text)
if chon == 16 :
  exec(requests.get('https://raw.githubusercontent.com/Hoanghuy200/toolgop/refs/heads/main/TOOL_G%E1%BB%98P_HVHTOOOL/regfb_novery.py').text)
if chon == 00 :
  exit()
else :
    exit()
