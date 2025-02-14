name=str(input("Enter your name: "))
age=int(input("Enter your age: "))
def give_name_age(name,age):
    return f"Hello {name} , you are {age} years old."
print(give_name_age(name,age))