num=str(input("enter a 4 digit number: "))
if len(num)!=4 or num.isdigit() == False: print("Input is not a 4 digit number")
else: print(f"Sum of 2 digit pairs (abcd -> ab+cd): {num[0:2]}+{num[2:4]}={int(num[0:2]) + int(num[2:4])}")