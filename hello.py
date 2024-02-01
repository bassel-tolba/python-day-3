# num = input("what number do you check ?")
# num_g = int(num) % 2
# if num_g == 1:
#     print("this number is odd")
# else:
#     print("this number is even")


height = input("what is your height ? ")
weight = input("what is your weight ? ")
bmi = float(weight) / float(height) ** 2
bmi_1 = round(bmi, 2)
if bmi <= 18.5:
    print(f"your bmi is {bmi_1},you are underwight.")
elif bmi <= 25:
    print(f"your bmi is {bmi_1},you are normalwight.")    
elif bmi <= 30:
    print(f"your bmi is {bmi_1},you are overwight.")    
elif bmi <= 35:
    print(f"your bmi is {bmi_1},you are obese.")    
elif bmi > 35:
    print(f"your bmi is {bmi_1},you are clincally obese.")    
else:
    print("those numbers aint real :)")
