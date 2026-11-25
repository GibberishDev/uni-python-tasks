#data taken from https://goodmeteo.ru/pogoda-sankt-peterburg/god/#climate-months
monthly_precipitation={
    "Jan": 51.5,
    "Feb": 41.5,
    "Mar": 46.8,
    "Apr": 54.3,
    "May": 68.5,
    "Jun": 91.8,
    "Jul": 93.0,
    "Aug": 92.4,
    "Sep": 62.1,
    "Oct": 71.3,
    "Nov": 66.3,
    "Dec": 57.0,
}
def flip_dict(dict):
	values={}
	for key in dict:
		val = dict[key]
		if val in values:
			values[val].append(key)
		else:
			values[val]=[key]
	return values


flipped = flip_dict(monthly_precipitation)
print(flipped)
precipitation_values = list(monthly_precipitation.values())
precipitation_values.sort()
precipitation_values =list(dict.fromkeys(precipitation_values))
print(f"Monthly precipitation values from lowest to highest: {"".join(f"\n{", ".join(f"{month}" for month in flipped[value])}: {value}" for value in precipitation_values)}") #Second join handles the cases if several months have same value

