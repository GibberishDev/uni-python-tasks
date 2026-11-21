next_input=int(input("Enter a number to sum it up. Enter \"-1\" to end: "))
input_sum=0
while next_input!=-1:
    input_sum= input_sum + next_input
    next_input=int(input("Enter a number to sum it up. Enter \"-1\" to end: "))
print(f"Sum of all numbers: {input_sum}")

