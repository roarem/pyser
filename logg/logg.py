import time, textwrap

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
        if pre_fetch =="doneexit":
            print('thank you for your contribution, sucker...')
            break
        else:
            fetched += pre_fetch

    wrapped = textwrap.wrap(fetched,width=100)
    print(wrapped)
    return wrapped

if __name__=='__main__':
    fetched = 99*'4'+' '+1*'2'
    fetched = textwrap.wrap(fetched,width=100)
    #fetched = get_input()
    logger(fetched)
