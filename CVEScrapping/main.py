from Interfaces import *
#CVE-2022-23943

def main():
    print("Starting...")

    stdscr = curses.initscr()
    mainMenu(stdscr)

    # result = CVEScraper()
    # print(result.search("apache2"))

    print("Loading...")

    print("ending...")

if __name__ == "__main__":
    main()
