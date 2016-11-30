import os

def read_mail():
    filename = os.path.join(os.path.dirname(__file__), 'mail_results')
    with open(filename,'r') as f:
        reply = f.readline().strip()
    return reply

if __name__=='__main__':
    print(read_mail())
