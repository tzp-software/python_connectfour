'''
    rows.py
'''
import os


def clear():
    x = os.system('clear')


class Row(object):
    def __init__(self):
        self.rows = [False,False,False,False,False]
        self.rtn = ''
        self.col = ['| |','| |','| |','| |','| |']

    def __str__(self):
        return ''.join(map(str,self.col))
        

    def __repr__(self):
        return str(self)

    def set_spot(self, row):
        if self.rows[row-1]:
            return False
        else:
            self.rows[row-1] = True
            return True

    def set_one(self, symbol):
        if self.set_spot(1):
            self.col[0] = '|' + symbol + '|'
            return True
        else:
            return False
    
    def set_two(self, symbol):
        if self.set_spot(2):
            self.col[1] = '|' + symbol + '|'
            return True
        else:
            return False

    def set_three(self, symbol):
        if self.set_spot(3):
            self.col[2] = '|' + symbol + '|'
            return True
        else:
            return False

    def set_four(self, symbol):
        if self.set_spot(4):
            self.col[3] = '|' + symbol + '|'
            return True
        else:
            return False

    def set_five(self, symbol):
        if self.set_spot(5):
            self.col[4] = '|' + symbol + '|'
            return True
    
    def set_six(self, symbol):
        if self.set_spot(6):
            self.col[5] = '|' + symbol + '|'
            return True
        else:
            return False


class Board(object):
    def __init__(self):
        #self.rows = [Row(),Row(),Row(),Row(),Row()]
        # this is more efficent
        self.rows = [Row() for i in range(5)]
        self.symbol = 'X'

    def __str__(self):
        rtn = ''
        x = range(len(self.rows))
        x.reverse()
        for i in x:
            rtn += str(self.rows[i]) + '\n'
        return rtn

    def add_to_one(self, sym):
        ''' add symbol to first open row in column one '''
        x = range(len(self.rows))
        for i in x:
            if self.rows[i].set_one(sym):
                return

    def add_to_two(self, sym):
        ''' see add_to_one'''
        for i in range(len(self.rows)):
            if self.rows[i].set_two(sym):
                return

    def add_to_three(self, sym):
        ''' see add_to_one'''
        for i in range(len(self.rows)):
            if self.rows[i].set_three(sym):
                return

    def add_to_four(self, sym):
        '''see add_to_one'''
        for i in range(len(self.rows)):
            if self.rows[i].set_four(sym):
                return

    def add_to_five(self, sym):
        '''see add_to_one'''
        for i in range(len(self.rows)):
            if self.rows[i].set_five(sym):
                return

    def add_to_six(self, sym):
        '''see add to one'''
        for i in range(len(self.rows)):
            if self.rows[i].set_six(sym):
                return

    def add_to_col(self, num):
        if int(num) == 1:
            self.add_to_one(self.symbol)
        elif int(num) == 2:
            self.add_to_two(self.symbol)
        elif int(num) == 3:
            self.add_to_three(self.symbol)
        elif int(num) == 4:
            self.add_to_four(self.symbol)
        elif int(num) == 5:
            self.add_to_five(self.symbol)
        elif int(num) == 6:
            self.add_to_six(self.symbol)
        else:
            print 'Error try again'
        self.change_symbol()
    
    def set_symbol(self, symbol):
        self.symbol = symbol


    def change_symbol(self):
        symbols = ['X','O']
        if self.symbol == 'O':
            self.set_symbol('X')
        else:
            self.set_symbol('O')
            # next commented line is for more than 2 players
            #self.set_symbol(symbols[symbols.index(self.symbol)+1])



def main_loop():
    b = Board()
    while True:
        clear()
        print b
        b.add_to_col(int(raw_input('What column to add {} to? : '.format(b.symbol))))


