def dec2bin(num:int):
    output=""
    og_num=num
    while num>0:
        output=str(num%2)+output
        num//=2
    print(f"Decimal {og_num} is binary {output}")

dec2bin(int(input("Enter decimal number: ")))