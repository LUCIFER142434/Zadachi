#1
# user = int(input("Number : "))
# print(user,user*2)
#2
# a = 46
# b = "Z"
# print(a,b*5)
#3
# a = 5
# b = "F"
# c = "Привет"
# d = 90.2
# z = {67}
# print(c)
#4
# a = input("Number : ")
# b = []
# for i in a:
#     b += i
# print(b)
#5
# name = input("Name : ")
# fname = input("Fname : ")
# age = int(input("Age : "))
# print(f"Привет {fname} {name} {age}")
#6
# num1 = int(input("Number1 : "))
# num2 = int(input("Number2 : "))
# num3 = int(input("Number3 : "))
# print(f"{num1} - {num2} * {num3} = {num1 - num2 * num3}")
#7
# num1 = int(input("Number1 : "))
# num2 = float(input("Number2 : "))
# num3 = input("Number3 : ")
# num1 = int(num1)
# num2 = int(num2)
# num3 = int(num3)
# print(num1 * num2 * num3)
#8
# num1 = int(input("Number1 : "))
# num2 = int(input("Number2 : "))
# num3 = int(input("Number3 : "))
# print(num1)
# print(num2)
# print(num1)
# print(num1+num2+num3)
#9
# pas = int(input("Parol : "))
# pas1 = int(input("Parol povtor : "))
# if pas == pas1:
#     print("Ok")
# else:
#     print("Idi doleko")
#11
num1 = int(input("Number1 : "))
num2 = int(input("Number2 : "))
dey = input("deystvie : ")
if num2 == 0 and dey == "/":
    print("На 0 делить нельзя")
elif dey == "-":
    print(num1 - num2)
elif dey == "+":
    print(num1 + num2)
elif dey == "*":
    print(num1 * num2)
elif dey == "/":
    print(num1 / num2)
else:
    print("Нет такого действия")