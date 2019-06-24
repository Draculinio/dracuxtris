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
    screen.addstr(25,10,"______________")
    for i in range(5,25):
        screen.addstr(i,9,"|")
        screen.addstr(i,25,"|")
    screen.refresh()    


def juego(screen):
    '''
    **
    **
    '''
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
    
    '''
    *
    **
     *
    '''
    for i in range(0,24):
        screen.addstr(i,12,'*')
        screen.addstr(i+1,12,'**')
        screen.addstr(i+2,12,' *')
        screen.refresh()
        time.sleep(0.1)
        if i<23:
            screen.addstr(i,12,' ')
            screen.addstr(i+1,12,'  ')
            screen.addstr(i+2,12,'  ')
            screen.refresh()
        time.sleep(0.1)
    
    '''
     *
    **
    *
    '''
    for i in range(0,24):
        screen.addstr(i,14,' *')
        screen.addstr(i+1,14,'**')
        screen.addstr(i+2,14,'*')
        screen.refresh()
        time.sleep(0.1)
        if i<23:
            screen.addstr(i,14,'  ')
            screen.addstr(i+1,14,'  ')
            screen.addstr(i+2,14,' ')
            screen.refresh()
            time.sleep(0.1)

    '''
    **
     *
     *
    '''
    for i in range(0,24):
        screen.addstr(i,16,'**')
        screen.addstr(i+1,16,' *')
        screen.addstr(i+2,16,' *')
        screen.refresh()
        time.sleep(0.1)
        if i<23:
            screen.addstr(i,16,'  ')
            screen.addstr(i+1,16,'  ')
            screen.addstr(i+2,16,'  ')
            screen.refresh()
            time.sleep(0.1)

    '''
    **
    *
    *
    '''
    for i in range(0,24):
        screen.addstr(i,18,'**')
        screen.addstr(i+1,18,'*')
        screen.addstr(i+2,18,'*')
        screen.refresh()
        time.sleep(0.1)
        if i<23:
            screen.addstr(i,18,'  ')
            screen.addstr(i+1,18,' ')
            screen.addstr(i+2,18,' ')
            screen.refresh()
            time.sleep(0.1)
    
    '''
    *
    *
    *
    *
    '''
    for i in range(0,24):
        screen.addstr(i,20,'**')
        screen.addstr(i+1,20,'*')
        screen.addstr(i+2,20,'*')
        screen.refresh()
        time.sleep(0.1)
        if i<23:
            screen.addstr(i,20,'  ')
            screen.addstr(i+1,20,' ')
            screen.addstr(i+2,20,' ')
            screen.refresh()
            time.sleep(0.1)

#MAIN
def main():
    screen = curses.initscr()
    curses.noecho()
    curses.curs_set(0)
    screen.border(2)
    #win = curses.newwin(0,0,24,70)
    presentacion(screen)
    tablero(screen)
    juego(screen)
    time.sleep(1)
    curses.endwin()

if __name__=='__main__':
    main()