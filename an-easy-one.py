year = input("what is the year now 🥱")
year = int(year)
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("this is a leap year. the surviover😎")
        else:
            print("this is not a leap year. the unfortuntate😛")
    else:
        print("this is a leap year. second surviover😀")    
else:
    print("this is not a leap year. early excution😁")