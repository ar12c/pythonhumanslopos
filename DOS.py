import datetime
import os
import pathlib 
import argparse
date = datetime.datetime.now()
version = "0.1 alpha"
dos = "OkemoDOS"

print("Labs21 OKEMO-DOS version",version,"\nOSS 2026 OkemoWare \n⚠ fiddled with bugs, proceed at your own caution") # top 10 okemoware
print("\nLocal time is",date.strftime("%c"))

##COMMANDS
def help():
    print("cd, dir, rd, copy, del, ren, clear, ver, exit, mkdir, text")

def exit():
    print("Shutting Down OkemoDOS")
    quit()

def ver():
    print("""\\\\  //   Version""",version)
    print(""">>  <<  """,dos)
    print("""//  \\\\""")

def mkdir():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir_name', nargs='?')
    args = parser.parse_args()
    if args.dir_name == None:
        print("What do you want to call the directory?")
        os.mkdir(input())
    else:
        os.mkdir(args.dir_name)

def clear():
    os.system('cls' if os.name == 'nt' else clear)

Commands = {
    "help": help,
    "exit": exit,
    "ver": ver,
    "mkdir": mkdir,
    "clear": clear,
}

## super cool main interface totally no malware
while True:
    user_input = input(">")
    if user_input in Commands: 
        inputted_command = Commands[user_input]
        inputted_command()
    else:
        print("Command not found")
