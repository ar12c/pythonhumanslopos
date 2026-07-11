import datetime
import os
import sys
import pathlib 
import argparse
import shutil
import msvcrt
date = datetime.datetime.now()
version = "0.1 alpha"
dos = "OkemoDOS"
STARTING_BASE_DIR = os.path.basename(os.getcwd())

print("Labs21 OKEMO-DOS version",version,"\nOSS 2026 OkemoWare \n⚠ fiddled with bugs, proceed at your own caution")
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
    os.system('cls' if os.name == 'nt' else 'clear')

def rmdir(args_list):
    parser = argparse.ArgumentParser()
    parser.add_argument('dir_name', nargs='?')
    args = parser.parse_args(args_list)
    if args.dir_name == None:
        print('Which directory do you want to delete?')
        delnameofdir = input()
        if delnameofdir in os.listdir():
            os.removedirs(delnameofdir)
        else:
            print("Directory not found.")
        return
    if args.dir_name not in os.listdir():
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
    elif args.dir_name == "..":
        if STARTING_BASE_DIR == os.getcwd():
            print("Access Denied")
        else:
            os.chdir("..")
    elif args.dir_name not in os.listdir():
        print("Directory not found. Please use the command ls")
    else:
        os.chdir(args.dir_name)

def ls(args_list):
    path = args_list[0] if args_list else '.'
    print('\n'.join(os.listdir(path)))

def dir(*args):
    currentdir = os.path.basename(os.getcwd()) 
    print("Your current dir is", "root" if STARTING_BASE_DIR == currentdir else currentdir)

def rn(args_list):
    parser = argparse.ArgumentParser()
    parser.add_argument('dir_name', nargs='*')
    args = parser.parse_args(args_list)
    if len(args.dir_name) == 0:
        print("Which directory do you want to rename?")
        renamedir = input()
        if renamedir not in os.listdir():
            print("Directory not found. Please use the command ls")
            return
        print("What do you want to call it now?")
        newnamefordir = input()
        os.rename(renamedir, newnamefordir)
    elif len(args.dir_name) == 1:
        if args.dir_name[0] not in os.listdir():
            print("Directory not found. Please use the command ls")
        else:
            print("What do you want to call",args.dir_name[0],"now?")
            newnamefordir = input()
            os.rename(args.dir_name[0], newnamefordir)
    elif len(args.dir_name) == 2:
        if args.dir_name[0] not in os.listdir():
            print("Directory not found. Please use the command ls")
        else:
            os.rename(args.dir_name[0], args.dir_name[1])
        
def copy(args_list):
    parser = argparse.ArgumentParser()
    parser.add_argument('dir_name', nargs='*')
    args = parser.parse_args(args_list)
    if len(args.dir_name) == 0:
        print("What do you want to make a copy of?")
        src = input()
        if not os.path.exists(src):
            print("Please enter a valid value")
            return
        if os.path.isdir(src):
            print("You cannot copy a folder")
            return            
        print("What do you want the name to be?")
        dst = input()
        if os.path.exists(dst):
            print("File already exists")
            return
        shutil.copyfile(src, dst)        
    elif len(args.dir_name) == 1:
        src = args.dir_name[0]
        if not os.path.exists(src):
            print("File/Folder not found")
            return
        if os.path.isdir(src):
            print("You cannot copy a folder")
            return            
        print("What do you want the name to be?")
        dst = input()
        if os.path.exists(dst):
            print("File already exists")
            return
        shutil.copyfile(src, dst)        
    elif len(args.dir_name) == 2:
        src = args.dir_name[0]
        dst = args.dir_name[1]
        if not os.path.exists(src):
            print("File/Folder not found")
            return
        if os.path.isdir(src):
            print("You cannot copy a folder")
            return
        if os.path.exists(dst):
            print("File already exists")
            return
        shutil.copyfile(src, dst)        
    else:
        print("Too many arguments. Please provide only a source and a destination.")
        return

def text(*args):
    buffer = [""]
    cy, cx, vy = 0, 0, 0
    
    while True:
        w, h = shutil.get_terminal_size()
        
        out = "\033[?25l\033[2J\033[H" 
        out += f"\033[7m{' OkemoDOS TEXT '.ljust(w)}\033[0m"
        
        for i in range(h - 2):
            if vy + i < len(buffer):
                out += f"\033[{i + 2};1H{buffer[vy + i][:w-1]}"
        
        # Updated footer text
        footer = " ^O Save    ^X Exit "
        out += f"\033[{h};1H\033[7m{footer.ljust(w)}\033[0m"
        
        sy = cy - vy + 2
        sx = min(cx, w - 1) + 1
        if 2 <= sy <= h - 1:
            out += f"\033[{sy};{sx}H"
            
        out += "\033[?25h"
        sys.stdout.write(out)
        sys.stdout.flush()
        
        k = msvcrt.getwch()
        if k == '\x18': # Ctrl+X
            break 
        elif k == '\x0f': # Ctrl+O (Save)
            # Clear bottom row and prompt for filename
            sys.stdout.write(f"\033[{h};1H\033[K\033[0mFile Name to Write: ")
            sys.stdout.flush()
            filename = ""
            while True:
                sk = msvcrt.getwch()
                if sk == '\r': # Enter
                    break
                elif sk == '\x1b': # Esc to cancel
                    filename = ""
                    break
                elif sk == '\x08' and len(filename) > 0: # Backspace
                    filename = filename[:-1]
                    sys.stdout.write("\b \b")
                    sys.stdout.flush()
                elif sk.isprintable():
                    filename += sk
                    sys.stdout.write(sk)
                    sys.stdout.flush()
            
            if filename.strip():
                with open(filename.strip(), "w", encoding="utf-8") as f:
                    f.write("\n".join(buffer))
                    
        elif k == '\xe0': # Windows arrow keys
            k2 = msvcrt.getwch()
            if k2 == 'H' and cy > 0: 
                cy -= 1
                if cy < vy: vy = cy
            elif k2 == 'P' and cy < len(buffer) - 1: 
                cy += 1
                if cy >= vy + h - 2: vy += 1
            elif k2 == 'K' and cx > 0: cx -= 1
            elif k2 == 'M' and cx < len(buffer[cy]): cx += 1
        elif k == '\x08': # Backspace
            if cx > 0:
                buffer[cy] = buffer[cy][:cx-1] + buffer[cy][cx:]
                cx -= 1
        elif k == '\r': # Enter
            buffer.insert(cy + 1, buffer[cy][cx:])
            buffer[cy] = buffer[cy][:cx]
            cy += 1; cx = 0
            if cy >= vy + h - 2: vy += 1
        elif k.isprintable():
            buffer[cy] = buffer[cy][:cx] + k + buffer[cy][cx:]
            cx += 1

    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

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
    "rn": rn,
    "copy": copy,
    "text": text,
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