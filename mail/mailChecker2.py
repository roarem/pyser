#!/usr/bin/env python

from imapclient import IMAPClient
import time, sys#, plyer

sadface = "        /\ /\ \n        \/ \/ \n        ____ \n       /    \\"
passord = sys.stdin.readline().strip().split(",")
ginfo = ['Gmail','imap.gmail.com','emuofpower','Inbox',passord[0]]
hinfo = ['Hotmail','imap-mail.outlook.com','roaremaus@hotmail.com','Inbox',passord[1]]
uinfo = ['UIO','imap.uio.no','roarem','Inbox',passord[2]]
uioSinfo = ['UIO','imap.uio.no','roarem','Sonia',passord[2]]
uioLinfo = ['UIO','imap.uio.no','roarem','Larissa',passord[2]]
uioVinfo = ['UIO','imap.uio.no','roarem','Vakt',passord[2]]
#ginfo.append(str(sys.argv[1]))
#hinfo.append(str(sys.argv[2]))
#uinfo.append(str(sys.argv[3]))
servers = [ginfo,hinfo,uinfo,uioSinfo,uioLinfo,uioVinfo]

teller = 0
output_string = ""

clock = time.strftime("%a, %d %b %H:%M:%S\n\n",time.localtime())
i3bar = [0,0,0,0,0,0]

for i,current in enumerate(servers):
    error_log = ""
    error_log_string = ""
    try:
        server = IMAPClient (current[1],use_uid=True,ssl=True)
        server.login (current[2],current[4])
        new = int(server.folder_status(current[3], b'UNSEEN')[b'UNSEEN'])
    except Exception as error:
        error_log = str(error)
        new = 0

    if error_log != "":
        error_log_string += current[0]+": "+error_log+"\n"

    if new != 0:
        output_string += str(new)+" i "+current[0]+"-"+current[3]+"\n"
        teller += 1
        i3bar[i] = new
    try:
        server.logout()
    except:
        pass

if teller==0:
    output_string += "Ingen nye\n"+sadface

output_string = clock+error_log_string+output_string
newlines = 7 - output_string.count('\n')
for new in range(newlines):
    output_string+='\n'

f = open('mail_results','r')
old_i3bar_string = f.readline()
f.close()
with open("mail_results",'w') as f:
    pseudo = ['S','L','V']
    i3bar_string = ''
    for i,j in zip(pseudo,i3bar[3:]):
        if j:
            i3bar_string += '({}{}) '.format(i,j)
    
    i3bar_string += '{} {} {}\n'.format(i3bar[0],i3bar[1],i3bar[2])
    #if i3bar_string != old_i3bar_string:
    #    plyer.notification.notify(title="MAIL",message=i3bar_string,timeout=3)
    f.write(i3bar_string)

output_string +=chr(13)
sys.stdout.write('\033[2J')
sys.stdout.write('\033[H')
sys.stdout.write(output_string)
sys.stdout.flush()
#print(output_string)

