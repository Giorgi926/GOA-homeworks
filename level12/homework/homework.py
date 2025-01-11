# ზოგჯერ მონაცემები გადმოგვეცემა არა საჭირო სახით, თუ ჩვენ გვინდა მათზე ვიმუშაოთ უნდა გადავაქციოთ საჭირო მონაცემთა ტიპად
# მაგალითად: გადმოგვეცემა string რიცხვი და ჩვენი დავალებაა მივუმატოთ ის ნებისმიერ მათემატიკურ რიცხვს, ამ შემთხვევაში
# დაგვჭირდება მონაცემთა ტიპის კონვერტაცია(შეცვლა)

age1 = int(input("Please enter your age: "))
age2 = int(input("Please enter your age: "))
age3 = int(input("Please enter your age: "))

print((age1 + age2 + age3) / 3)

name = int(input("enter your age: "))
future_age = name + 5
print(future_age)

num1 = 5
num2 = 10
print(num2 > num1)

num1 = 15
num3 = 5
print(num1 > num3)

num5 = 5
num6 = 3
print(num5 >= num6) 

num7 = 8
num8 = 10
print(num7 <= num8)

num9 = 8
num10 = 6
print(num9 != num10)

num11 = 150
num12 = 150
print(num11 == num12)