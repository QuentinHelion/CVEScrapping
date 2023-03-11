from Class import *
from Interfaces import *
#CVE-2022-23943
def returnFromCurses(value):
    return value

def main():
    print("Starting...")
    scraper = CVEScraper()
    cve = CVE()
    # results = scraper.search("apache2")
    # for result in results:
        # print(result)
    stdscr = curses.initscr()
    userInput= mainMenu(stdscr)
    print("Loading...")
    details = scraper.details(userInput)
    #write to txt file
    cve.writeDetails(userInput,details)
    data = list(details.items())
    print(data)
    createWin(stdscr,data)

    print("ending...")

if __name__ == "__main__":
    main()