class Cosmonaut():
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.fullname = first + ' ' + last
    #def fullname(self):
        #return f'{self.first} {self.last}'

cos = Cosmonaut('Yuri', 'Gagarin')
print(f'{cos.fullname}')