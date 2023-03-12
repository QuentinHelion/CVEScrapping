import curses
from .CVE import *
from .CVEScraper import *
from .CVEmenu import *
from .detailsMenu import *
from .SearchMenu import *

def mainMenu(stdscr):
    # Create Window
    menu = ['Scrap details of a specific CVE', 'Search','Exit']
    max_height, max_width = stdscr.getmaxyx()
    menu_win = curses.newwin(max_height, max_width, 0, 0)
    curses.curs_set(0)
    # Enable seting up color pairs
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    menu_win.box()
    menu_win.bkgd(0, curses.color_pair(1))
    curses.noecho()
    current_item = 0
    while True:
        enumAndHL(menu_win,menu,current_item)
        c = menu_win.getch()

        if c == ord("z"):
            if current_item > 0:
                current_item -= 1

        elif c == ord("s"):
            if current_item < len(menu) - 1:
                current_item += 1

        elif c == ord("\n"): # ord("\n") is the key code for the enter key
            if current_item == 0:
                createCVEWin(stdscr,max_height,max_width)
            if current_item == 1:
                menu_win.erase()
                menu_win.refresh()
                createSearchWin(stdscr,max_height,max_width)
            if current_item == 2:
                menu_win.erase()
                menu_win.refresh()
                break
                
        elif c == 27:
            menu_win.erase()
            menu_win.refresh()
            break
    
    curses.endwin()    

def enumAndHL(menuWindowName,menuItemsList,current_item):
    for idx, item in enumerate(menuItemsList):
            if idx == current_item:
                menuWindowName.addstr(idx + 1, 2, item, curses.color_pair(1)| curses.A_REVERSE)
            else:
                menuWindowName.addstr(idx + 1, 2, item, curses.color_pair(1))
    menuWindowName.refresh()