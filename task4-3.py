print("Welcome to tree generator")
height=int(input("Enter tree height: "))
symbol=str(input("Enter tree leaves symbol: "))
for i in range(height):
    if i==0 or i==height-1: print(f"{" "*(height-2)*len(symbol)}||")
    else:
        print(f"{" "*((height-2)-i)*len(symbol)}{symbol*i}||{symbol*i}")
