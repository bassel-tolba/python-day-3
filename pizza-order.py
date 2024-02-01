hello = input("do you want pizza🍕 ?answer with Y for yes or N for no 😐")

if hello == "Y":
    size = input("what size do you want? S, M or L🍕")
    if size == "S":
        print("that will be the small size!😏")
        bill = int(15)
        answer = input("do you want peperone?😁")
        if answer == "Y":
            bill += int(2)
        else:
            bill += int(0)
    elif size == "M":
        print("that will be the mediam size!😄")
        bill = int(20)
        answer =  input("do you want peperone?😄")
        if answer =="Y":
            bill += int(3)
        else:
            bill += int(0)
    else:
        print("that will be the big size!🥵")
        bill = int(25)
        answer =  input("do you want peperone?🥵")
        if answer == "Y":
            bill += int(3)
        else:
            bill += int(0)
    cheese = input("do you want chesse?🧀 answer with ok 👍 or nah 🙄")
    if cheese == "ok":
        bill += int(1)
    print(f"your pizza will cost ➡ {bill}💰⬅")
elif hello == N:
    print("well then have a nice day !😉")
        


