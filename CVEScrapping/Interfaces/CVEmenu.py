import curses
from .detailsMenu import *

def createCVEWin(stdscr,max_height,max_width):

    CVEmenu_win = curses.newwin(max_height, max_width, 0, 0)
    curses.curs_set(0)
    # Enable seting up color pairs
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    CVEmenu_win.box()
    CVEmenu_win.bkgd(0, curses.color_pair(1))
    ## Add text
    CVEmenu_win.addstr(1,2,"CVE : ")
    ## Print user clicked butons
    curses.echo()
    ## Get user input
    userInput = CVEmenu_win.getstr().decode()
    detailsWin(stdscr,userInput,max_height,max_width)
    ## Hide user clicked buttons
    CVEmenu_win.erase()
    CVEmenu_win.refresh()
    curses.noecho()