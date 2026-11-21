def draw_tree(height=4, symbol="*"):
    for i in range(height):
        if i==0 or i==height-1: print(f"{" "*(height-2)*len(symbol)}||")
        else:
            print(f"{" "*((height-2)-i)*len(symbol)}{symbol*i}||{symbol*i}")
#invocation
draw_tree(int(input("Enter tree height: ")), str(input("Enter tree symbol: ")))