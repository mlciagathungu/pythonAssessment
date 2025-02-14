num=int(input("Enter a number: "))
def num_is_even_odd(num):
    if num /2 or num==0:
        return f"{num} is even"
    else:
        return f"{num} is odd"
print(num_is_even_odd(num))