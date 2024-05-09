#variables declaration
age = 12
name = 'karan'
gpa = 1.2
student = True

# type() function

print("age is",type(age))
print("name is",type(name))
print("gpa is",type(gpa))
print("student is",type(student))

print("")

# explicit conversion

age = float(age)
name = bool(name)
gpa = int(gpa)
student = str(student)

print("age is",type(age))
print("name is",type(name))
print("gpa is",type(gpa))
print("student is",type(student))

print("")
# implicit conversion

num1 = 5
num2 = 1.1
num3 = num1/num2
print(num3)

print(type(num1))
print(type(num2))
print(type(num3))