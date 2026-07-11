import datetime
import os
import pathlib 
import argparse
date = datetime.datetime.now()
version = "0.1 alpha"
dos = "OkemoDOS"
STARTING_BASE_DIR = os.path.basename(os.getcwd())

print("Labs21 OKEMO-DOS version",version,"\nOSS 2026 OkemoWare \n⚠ fiddled with bugs, proceed at your own caution") # top 10 okemoware
print("\nLocal time is",date.strftime("%c"))

##COMMANDS
def help(*args):
    print("cd, dir, rn, copy, rmdir, ren, clear, ver, exit, mkdir, text")

def exit(*args):
    print("Shutting Down OkemoDOS")
    quit()

def ver(*args):
    print("""\\\\  //   Version""",version)
    print(""">>  <<  """,dos)
    print("""//  \\\\""")

def mkdir(args_list):
    parser = argparse.ArgumentParser()
    parser.add_argument('dir_name', nargs='?')
    args = parser.parse_args(args_list) 
    if args.dir_name == None:
        print("What do you want to call the directory?")
        nameofdir = input()
        os.mkdir(nameofdir)
        print(nameofdir, "created")
    else:
        try:
            os.mkdir(args.dir_name)
        except FileNotFoundError:
            print("The specified drive or path does not exist.")
        except PermissionError:
            print("Access denied. Administrator privileges required.")
        except FileExistsError:
            print("A folder with that name already exists.")


def clear(*args):
    os.system('cls' if os.name == 'nt' else clear)

def rmdir(args_list):
    parser = argparse.ArgumentParser()
    parser.add_argument('dir_name', nargs='?')
    args = parser.parse_args(args_list)
    if args.dir_name == None:
        print('Which directory do you want to delete?')
        delnameofdir = input()
        os.removedirs(delnameofdir)
    if args.dir_name != os.listdir:
        print("Directory not found. Please use the command ls")
    else:
        os.removedirs(args.dir_name)

def cd(args_list):
    parser = argparse.ArgumentParser()
    parser.add_argument('dir_name', nargs='?')
    args = parser.parse_args(args_list)
    if args.dir_name == None:
        print('Which directory do you want go?')
        gotodir = input()
        os.chdir(gotodir)
    if args.dir_name == "..":
        if STARTING_BASE_DIR == os.getcwd():
            print("Access Denied")
        else:
            os.chdir("..")
    elif args.dir_name not in os.listdir():
        print("Directory not found. Please use the command ls")
    else:
        os.chdir(args.dir_name)

def ls(*args):
    print('\n'.join(os.listdir()))

def dir(*args):
    currentdir = os.path.basename(os.getcwd()) 
    print("Your current dir is", "root" if STARTING_BASE_DIR == currentdir else currentdir)

Commands = {
    "help": help,
    "exit": exit,
    "ver": ver,
    "mkdir": mkdir,
    "clear": clear,
    "rmdir": rmdir,
    "cd": cd,
    "ls": ls,
    "dir": dir,
}

## super cool main interface totally no malware
while True:
    if os.path.basename(os.getcwd()) == STARTING_BASE_DIR:
        currentdir = "root"
    else:
        currentdir = os.path.basename(os.getcwd())

    user_input = input(f"{currentdir}/>")
    if not user_input.strip():
        continue
    parts = user_input.split()
    cmd_name = parts[0]
    args_list = parts[1:]
    
    if cmd_name in Commands: 
        inputted_command = Commands[cmd_name]
        inputted_command(args_list)
    else:
        print("Command not found")