import curses
from .CVE import *
from .CVEScraper import *
from .Menu import *

def addstrToWin(win,data):
    #win.addstr(3,2,str)
    for idx, (key, value) in enumerate(data):
        id = idx + 2
        win.addstr(id+1, 2, key , curses.color_pair(1))
        win.addstr(id+1, 30, value , curses.color_pair(1))
    win.refresh()

def detailsWin(stdscr,str,max_height,max_width):
    scraper = CVEScraper()
    cve = CVE()

    detmenu_win = curses.newwin(max_height, max_width, 0, 0)
    curses.curs_set(0)
    # Enable seting up color pairs
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    detmenu_win.box()
    detmenu_win.bkgd(0, curses.color_pair(1))
    # Get data
    details = scraper.details(str)
    # Write to TXT file
    cve.writeDetailstxt(str,details)
    # Write to JSON file
    cve.writeDetailsjson(str,details)
    # Print on screen result
    details = list(details.items())
    detmenu_win.addstr(1,2,"DETAILS :      (Press Enter to exit)")
    addstrToWin(detmenu_win,details)
    detmenu_win.getch()