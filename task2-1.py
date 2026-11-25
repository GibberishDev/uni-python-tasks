month=int(input("Enter the month: "))
if month<1 or month>12: print("Invalid month")
season_str="The season this month belongs to: "
match month:
    case 1|2|12: print(f"{season_str}Winter")
    case 3|4|5: print(f"{season_str}Spring")
    case 6|7|8: print(f"{season_str}Summer")
    case 9|10|11: print(f"{season_str}Fall")
