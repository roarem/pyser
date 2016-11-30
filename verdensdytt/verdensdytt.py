import sys, time, subprocess, os
import datetime
import matplotlib.pyplot as plt

class VerdensDytt:

    def __init__(self,args):

        self.filename = os.path.join(os.path.dirname(__file__), 'data/data.csv')
        if len(args)==1:
            self.menu()
        elif len(args)==2:
            self.store(args[1])
        elif len(args) > 2:
            print("WTF!?")
            sys.exit(1)

    def store(self,number):

        time_string = time.strftime('%H,%M,%d,%m,%Y')
        store_string = '{},{}\n'.format(number,time_string)
        with open(self.filename,'a') as f:
            f.write(store_string)

    def menu(self):

        menu_string =  '1. Last entry\n'
        menu_string += '2. Plot progress\n'
        menu_string += '3. Plot per day\n'
        number = input(menu_string)
        if number == '1':
            self.lastEntry()
        elif number == '2':
            self.progressPlot()
        elif number == '3':
            self.perDatePlot()
        else:
            print("WTF?!")
            sys.exit(1)

    def lastEntry(self):

        last_line = subprocess.call(["tail","-n1",self.filename]) 

    def progressPlot(self):
        numbers = []
        dates   = []
        date_string = "{}:{} {}-{}-{}"
        with open(self.filename,'r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip().split(',')
                numbers.append(int(line[0]))
                date_line = date_string.format(*line[1:])
                dates.append(datetime.datetime.strptime(date_line,"%H:%M %d-%m-%Y"))
        plt.plot_date(dates,numbers)
        plt.show()

    def perDatePlot(self):

        numbers = []
        dates   = []
        date_string = "{}:{} {}-{}-{}"
        with open(self.filename,'r') as f:
            lines = f.readlines()
            old_date_object = datetime.datetime.strptime("03:25 24-06-1986","%H:%M %d-%m-%Y") 
            for line in lines:
                line = line.strip().split(',')
                date_line = date_string.format(*line[1:])
                date_object = datetime.datetime.strptime(date_line,"%H:%M %d-%m-%Y") 
                if date_object > old_date_object:
                    dates.append(date_object)
                    numbers.append(int(line[0]))
                    old_date_object = date_object
                else:
                    numbers[-1] += int(line[0])
        plt.plot_date(dates,numbers)
        plt.show()

if __name__=="__main__":
    VerdensDytt(sys.argv)
