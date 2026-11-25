temp_number_input=str(input("Enter temperature (Ex: 19C, 46F): "))
if "".join(char for char in temp_number_input if char in "0123456789") == "" or temp_number_input.count(".")>1:
    print("\033[31mERROR:\033[0m Entered temperature does not represent valid numeric value")
else:
    is_fahrenheit=None
    if temp_number_input.endswith("C") or temp_number_input.endswith("c"): is_fahrenheit=False
    elif temp_number_input.endswith("F") or temp_number_input.endswith("f"): is_fahrenheit=True
    else:
        is_fahrenheit_input=input("Is it in Fahrenheit? [Y/n]: ")
        if (
            len(is_fahrenheit_input)==0 or
            is_fahrenheit_input.lower()=="y" or
            is_fahrenheit_input.lower()=="yes" or
            is_fahrenheit_input.lower()=="true" or
            is_fahrenheit_input.lower()=="t"
        ):
            is_fahrenheit=True
        elif (
            is_fahrenheit_input.lower()=="n" or
            is_fahrenheit_input.lower()=="no" or
            is_fahrenheit_input.lower()=="false" or
            is_fahrenheit_input.lower()=="f"
        ):
            is_fahrenheit=False
    if is_fahrenheit is not None:
        num=float("".join(char for char in temp_number_input if char in "0123456789."))
        if is_fahrenheit:
            print(f"{num}F is {format((num - 32.0)/1.8,'.2f')}C")
        else:
            print(f"{num}C is {format(num * 1.8 + 32.0,'.2f')}F")
    else: print("\033[31mERROR:\033[0m invalid inputs to determine temperature type")
