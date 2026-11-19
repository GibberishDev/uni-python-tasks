a=int(input("enter first number: "))
b=int(input("enter second number: "))
f=0
if b!=0:
    f=a/b
else:
    f="Invalid: cannot divide by zero"
print(f"A: {a}, B: {b}\nA+B: {a+b}\nA-B: {a-b}\nA*B: {a*b}\nA/B: {f}")