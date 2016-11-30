import time, os

def store(number):
    filename = os.path.join(os.path.dirname(__file__), 'data/data.csv')
    time_string = time.strftime('%H,%M,%d,%m,%Y')
    store_string = '{},{}\n'.format(number,time_string)
    with open(filename,'a') as f:
        f.write(store_string)
