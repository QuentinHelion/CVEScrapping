import curses
from .detailsMenu import *
from .CVE import *
from .CVEScraper import *


def createSearchWin(stdscr,max_height,max_width):
    scraper = CVEScraper()
    cve = CVE()

    
    searchenu_win = curses.newwin(max_height, max_width, 0, 0)
    curses.curs_set(0)
    # Enable seting up color pairs
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    searchenu_win.box()
    searchenu_win.bkgd(0, curses.color_pair(1))
    ## Add text
    searchenu_win.addstr(1,2,"Search : ")
    ## Print user clicked butons
    curses.echo()
    ## Get user input
    userInput = searchenu_win.getstr().decode()
    results = scraper.search(userInput)
    cve.writeSearch(userInput,str(results))
    ## Hide user clicked buttons
    searchenu_win.erase()
    searchenu_win.refresh()
    curses.noecho()