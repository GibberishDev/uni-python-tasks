import os
import re
from os import write

global file

invalid_characters=["/","\\",":","*","?","\"","<",">","|"]

def create_file(group_name:str):
    global file
    try:
        if not os.path.isdir(os.path.join(os.getcwd(),"task7data")): os.mkdir(os.path.join(os.getcwd(),"task7data"))
    except IOError as e:
        print(f"Error: could not create folder {os.path.join(os.getcwd(),"task7data")} - error: {e}")
    try:
        group_name = "".join(f"{char if char not in invalid_characters else "_"}" for char in group_name)
        file=open(os.path.join(os.getcwd(),"task7data",group_name+".txt"),"w+",encoding="utf8")
    except IOError as e:
        print(f"Error: could not create file {group_name}.txt - error: {e}")



def validate_input(user_input:str):
    email_str=None
    if user_input.count("|") == 1:
        name_str=user_input.split("|")[0].strip()
        email_str=user_input.split("|")[1].strip()
        email_str = re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",email_str)
    else:
        name_str=user_input

    if email_str is None:
        while True:
            email_str = input("Enter a valid email address: ")
            email_str = re.search(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email_str)
            if email_str is not None: break

    if email_str is not None:
        email_str = email_str.string.strip()
    data_entry=(name_str, email_str)
    return data_entry

data = []

def save_file():
    if len(data)==0:
        print("No entries to save")
        return
    data_lines="\n".join(f"{data_entry[0]} | {data_entry[1]}" for data_entry in data)
    file.writelines(data_lines)
    print("File saved")
    print(f"File data:\n{data_lines}")
    file.close()

create_file(str(input("Enter the name of the group: ")))
if file is not None:
    print("Enter student surname and email address separated by \"|\". Enter -1 to stop entering names and save the file")
    i=0
    while True:
        i+=1
        user_input=str(input(f"Entry [{i}]: "))
        if user_input == "-1": break
        entry=validate_input(user_input)
        data.append(entry)
    save_file()