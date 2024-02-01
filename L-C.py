myname = input("what is your name?")
myname = myname.lower()
hername = input("what is her name?")
hername = hername.lower()

numberlove = str(myname.count("l") + hername.count("l") +
 myname.count("o") + hername.count("o") + myname.count("v") + 
 hername.count("v") + myname.count("e") + hername.count("e"))

numbertrue = str(myname.count("t") + hername.count("t") + 
myname.count("r") + hername.count("r") + myname.count("u") + 
hername.count("u") + myname.count("e") + hername.count("e"))

love = numberlove + numbertrue

if int(love) < 10 or int(love) > 90:
    print(f"your score is {love}, you go together like cola and mentos.")
elif int(love) > 40 and int(love) < 50:
    print(f"your score is {love}, you are alright together.")
else:
    print(f"your score is {love}")