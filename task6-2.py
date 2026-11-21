import random

group_a_surnames=[
    "Ivanov",
    "Smirnov",
    "Petrov",
    "Sokolov",
    "Volkov",
    "Popov",
    "Morozov",
    "Kuznetsov",
    "Lebedev",
    "Orlov"
]
group_b_surnames=[
    "Ivanov",
    "Fedorov",
    "Pavlov",
    "Nikitin",
    "Vasiliev",
    "Borisov",
    "Mikhailov",
    "Zaitsev",
    "Kozlov",
    "Dmitriev",
]
sample_a=random.sample(group_a_surnames,5)
sample_b=random.sample(group_b_surnames,5)
team=(*sample_a,*sample_b)
print(f"[2.1]: Team - {team}")
print(f"[2.2]: Group A - {group_a_surnames}\n       Group B - {group_b_surnames}")
print(f"[2.3]: Team Size - {len(team)}")
sorted_team = list(team)
sorted_team.sort()
print(f"[2.4]: Team in alphabetic order - {sorted_team}")
print(f"[2.5]: Is Ivanov specifically in team? - {"yes" if "Ivanov" in sorted_team else "no"}{f"\n       Appears {sorted_team.count("Ivanov")} times" if "Ivanov" in sorted_team else ""}")

#Ngl this task is stupid and has IMO wrong usage of tuples and needs to be redesigned