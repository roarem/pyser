import time, textwrap

def logger(logg_input):
    date = time.strftime('%A %d %b %H:%M:%S %Y')
    top = [100*'-',date,len(date)*'-']
    bot = [100*'-',33*'|  ']
    wrapped = textwrap.wrap(testout,width=100)
    output = '\n'.join(top+wrapped+bot)+'\n'
    with open('log.txt','a') as f:
        f.write(output)

if __name__=='__main__':
    testout = 99*'4'+' '+1*'2'
    logger(testout)
