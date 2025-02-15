a=47
b=34
c=21
def get_max(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
print(get_max(a,b,c))
