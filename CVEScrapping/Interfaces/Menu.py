import curses

def mainMenu(stdscr):
    # Create Window
    max_height, max_width = stdscr.getmaxyx()
    menu_win = curses.newwin(max_height, max_width, 0, 0)
    curses.curs_set(0)
    # Enable seting up color pairs
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    menu_win.box()
    menu_win.bkgd(0, curses.color_pair(1))
#
    ## Add text
    menu_win.addstr(1,2,"CVE : ")
    ## Print user clicked butons
    curses.echo()
    ## Get user input
    userInput = menu_win.getstr().decode()
    ## Hide user clicked buttons
    curses.noecho()
    curses.endwin()

    return userInput

def addstrToWin(win,data):
    #win.addstr(3,2,str)
    for idx, (key, value) in enumerate(data):
        id = idx + 1
        win.addstr(id+1, 2, key , curses.color_pair(1))
        win.addstr(id+1, 30, value , curses.color_pair(1))
    win.refresh()

def createWin(stdscr,str):
    max_height, max_width = stdscr.getmaxyx()
    menu_win = curses.newwin(max_height, max_width, 0, 0)
    curses.curs_set(0)
    # Enable seting up color pairs
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    menu_win.box()
    menu_win.bkgd(0, curses.color_pair(1))
    menu_win.addstr(1,2,"DETAILS : ")
    addstrToWin(menu_win,str)
    userInput = menu_win.getstr().decode()
    curses.endwin()