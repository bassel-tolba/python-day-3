height = int(input("welcome to the rolecoster !. enter your height to know if you can play!"))
if height > 120:
    print("you can ride !")
    age = int(input("how old are you ?"))
    if age < 12:
        bill = int(5)
    elif age > 12 and age < 18:
        bill = int(7)
    elif age == 18 or age > 18:
        bill = int(12)
    elif age == 45 or age > 45 and age < 55 or age == 55:
        bill = int(0)
    photo = input("do you want a photo ?")
    if photo == "yes" and age == 45 or age > 45 and age < 55 or age == 55:
            bill = 0
            print(f"your bill is {bill} . yeah the bill is on us today for you :D")
    elif photo == "yes" or "yeah" or "yup" or "ok" or "alright" or "okay" and age < 45:
        bill += 3
        print(f"your bill is {bill}")
    elif photo == "no" or "nah" or "i pass" or "لا":
            bill = bill
            print(f"your bill is {bill}")
    
    else:
        print("you are nor supposed to be here xd")
    
    
else:
    print("you can't ride.")