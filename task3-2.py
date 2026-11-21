input_number=int(input("Enter a natural number: "))
if input_number>=0:
    input_digit=0
    for char in str(input_number):
        if int(char)>input_digit: input_digit=int(char)
        if int(char) == 9: break
    print(f"The biggest digit in number {input_number} is {input_digit}")
else:
    print("Invalid Input")