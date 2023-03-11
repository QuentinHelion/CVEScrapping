from Class import *
from Interfaces import *
#CVE-2022-23943

def main():
    print("Starting...")
    
    stdscr = curses.initscr()
    mainMenu(stdscr)
    
    print("Loading...")

    print("ending...")

if __name__ == "__main__":
    main()