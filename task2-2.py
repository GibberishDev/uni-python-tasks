symbol_code=int(input("Enter your ASCII symbol code: "))
if symbol_code > 127 or symbol_code < 0:
    print("Invalid ASCII symbol code")
else:
    is_letter= "" if ((64 < symbol_code < 91) or (96 < symbol_code < 123)) else "not "
    print(f"The code {symbol_code} corresponds to ASCII symbol \"{chr(symbol_code)}\". It is {is_letter}a letter of english alphabet")
