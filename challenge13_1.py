class Shape:
    def __init__(self):
        self.my_name = 'I am shape!'
        
    def what_am_i(self):
        print(self.my_name)

class Rectangle(Shape):
    def __init__(self, base, height):
        super().__init__()
        self.base = base
        self.height = height

    def calculate_perimeter(self):
        return self.base * self.height

class Square(Shape):
    square_list = []
    
    def __init__(self, base):
        super().__init__()
        self.base = base
        self.square_list.append(self)

    def __repr__(self):
        return '{} by {} by {} by {}'.format(self.base, self.base, self.base, self.base)

    def calculate_perimeter(self):
        return self.base ** 2

    def change_size(self, val):
        self.base += val



if __name__ == '__main__':
    base_list = []
    
    sq1 = Square(10)
    sq2 = Square(20)
    sq3 = Square(30)
    sq4 = Square(40)
    for sq in Square.square_list:
        base_list.append(sq.base)
    print(base_list)
    for sq in Square.square_list:
        print(sq)


    """
    rec = Rectangle(10, 20)
    squ = Square(15)

    print(rec.calculate_perimeter())
    print(squ.calculate_perimeter())

    rec.base = 100
    squ.base = 100
    
    print(rec.calculate_perimeter())
    print(squ.calculate_perimeter())

    squ.change_size(-10)

    print(squ.calculate_perimeter())
    
    rec.what_am_i()
    squ.what_am_i()
    """
