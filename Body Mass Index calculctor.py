Name=input("Enter your Name here : ")
Height=float(input("Enter your height in cm : "))
Weigth=float(input("Enter your weight kg : "))
BMI=Weigth/(Height/100)**2

print(Name)
print(" Your Body Mass Index (BMI) is ",BMI)
if BMI <= 18:
    print("Your under weight")
elif BMI > 18 <= 24:
    print("Your normal")
elif BMI > 29:
    print("Your obise")