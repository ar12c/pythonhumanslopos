import datetime
import os
import pathlib 
date = datetime.datetime.now()
version = "0.1 alpha"
dos = "OkemoDOS"

print("Labs21 OKEMO-DOS version",version,"\nOSS 2026 OkemoWare \n⚠ fiddled with bugs, proceed at your own caution") # top 10 okemoware
print("\nLocal time is",date.strftime("%c"))

##COMMANDS
def help():
    print("cd, dir, md, rd, copy, del, ren, clear, ver, exit, mkdir, text")

def exit():
    print("Shutting Down OkemoDOS")
    quit()

def ver():
    print("""\\\\  //   Version""",version)
    print(""">>  <<  """,dos)
    print("""//  \\\\""")

Commands = {
    "help": help,
    "exit": exit,
    "ver": ver,
}

## While true loop
while True:
    user_input = input(">")
    if user_input in Commands: 
        inputted_command = Commands[user_input]
        inputted_command()
    else:
        print("Command not found")
