class Horse:
    def __init__(self, max_speed, capa, rider):
        self.max_speed = max_speed
        self.capa = capa
        self.legs = 4
        self.hungry = False
        self.rider = rider

    def ask_condition(self):
        if self.rider.weight > self.capa:
            print('重くて動けないよ！')
        else:
            print('これぐらいなら大丈夫！')
        

class Rider:
    def __init__(self, weight):
        self.weight = weight
        self.legs = 2
        self.condition = 'good'
        self.hungry = False

if __name__ == '__main__':

    r = Rider(40)
    h = Horse(90, 45, r)
    h.ask_condition()

        
