import time, textwrap
import curses as cu
import curses.textpad as cut

def logger(logg_input):
    date = time.strftime('%A %d %b %H:%M:%S %Y')
    top = [100*'-',date,len(date)*'-']
    bot = [100*'-','  *    '+18*'*    '+'* ']
    output = '\n'.join(top+logg_input+bot)+'\n'
    with open('log.txt','a') as f:
        f.write(output)

def get_input():
    fetched = "" 
    print('Start writing, please')
    while 1:
        pre_fetch = input()
        if pre_fetch =="exit":
            print('thank you for your contribution, sucker...')
            break
        else:
            fetched += pre_fetch

    wrapped = textwrap.wrap(fetched,width=100)
    print(wrapped)
    return wrapped

def get_input_cu():
    stdscr = cu.initscr()
    stdscr.addstr(0, 0, "Log (Ctrl-G to end)")

    editwin = cu.newwin(8,100, 2,1)
    cut.rectangle(stdscr, 1,0, 1+8+1, 1+100+1)
    stdscr.refresh()

    box = cut.Textbox(editwin)

    box.edit()

    message = box.gather()
    cu.endwin()

    wrapped = textwrap.wrap(message,width=100)
    logger(wrapped)

if __name__=='__main__':
    #fetched = 99*'4'+' '+1*'2'
    #fetched = textwrap.wrap(fetched,width=100)
    #fetched = get_input()
    get_input_cu()
    #logger(fetched)
