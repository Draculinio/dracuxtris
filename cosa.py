import curses
import time

def presentacion(screen):
    screen.clear()
    for i in range(0,40):
        time.sleep(0.1)
        screen.addstr(12,i+6,'Dracux Presenta')
        screen.refresh()
        time.sleep(0.1)
        screen.addstr(12,i+6,' '*20)
        screen.refresh()
    time.sleep(2)
    screen.clear()

def tablero(screen):
    screen.addstr(25,10,"_______")
    for i in range(5,25):
        screen.addstr(i,9,"|")

screen = curses.initscr()
curses.noecho()
curses.curs_set(0)
presentacion(screen)
tablero(screen)


for i in range(0,25):
    screen.addstr(i,10,'**')
    screen.addstr(i+1,10,'**')
    screen.refresh()
    time.sleep(0.1)
    if i<24:
        screen.addstr(i,10,'  ')
        screen.addstr(i+1,10,'  ')
        screen.refresh()
        time.sleep(0.1)
    
    screen.refresh()
    time.sleep(0.1)
for i in range(0,24):
    screen.addstr(i,12,'*')
    screen.addstr(i+1,12,'**')
    screen.addstr(i+2,12,' *')
    screen.refresh()
    time.sleep(0.1)
    screen.addstr(i,12,' ')
    screen.addstr(i+1,12,'  ')
    screen.addstr(i+2,12,' ')
    screen.refresh()
    time.sleep(0.1)

curses.endwin()

