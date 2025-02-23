import feepending
import feepaid
import otp

admin_username = input("Enter User name: ")
if admin_username == "admin":
    otp = otp.send_otp("shashi2028j@gmail.com")
    x = int(input("Enter OTP: "))
    if x == otp:
        print("Login Sucess !")
        print("*******************************************")
    else:
        print("Login Failed !")
        print("*******************************************")
        exit()
else:
    print("Invalid Username")
    print("*******************************************")
    exit()

userdetails = {
  
    101: ["Shashi","shashikumar2028j@gmail.com","true"],
    102 : ["Manohar","reddymanohar894@gmail.com","true"],
    103 : ["Poojitha","kodudhulapoojitha19@gmail.com","false"],
    104 : ["harshitha","harshithamudhiraj16@gmail.com","false"],
    105 :  ["Bindu Priya","gardasbindupriya4@gmail.com","true"],
    106 : ["Cherukuri Sahithi","cherukurisahithi486@gmail.com","false"]
    
    }
print("Welcome Admin")
while True:
    print("Choose your Option")
    print("1. Edit Information")
    print("2. Send mail to Fee Pending users")
    print("3. Send mail to Fee cleared users")
    print("4. Exit")
    print("*******************************************")
    x1 = int(input("Enter option: "))
    if x1 == 1:
        for user in userdetails:
            if userdetails[user][2] == "false":
                status = input(f"Enter the Status of {userdetails[user][0]}: ")
                userdetails[user][2] = status.lower()
                print(f"{userdetails[user][0]} Data Updated !")
            
        else:
            print("Data Edited")
        print("*******************************************")
    elif x1 == 2:
        res = []
        for user in userdetails:
            if userdetails[user][2] == "false":
                res.append([userdetails[user][0],userdetails[user][1]])
        feepending.send_mails(res)
        print("All mails sent to Fee pending users")
    elif x1 == 3:
        res = []
        for user in userdetails:
            if userdetails[user][2] == "true":
                res.append([userdetails[user][0],userdetails[user][1]])
        feepaid.send_mails(res)
        print("All mails sent to fee Cleared users !")
    elif x1==4:
        print("Thank You")
        print("visit again")
        break
    else:
        print("Enter the Valid input")
        break
