class Apple:
    def __init__(self, variety, color, size, suger_content):
        """ りんご、そのもの
        """
        self.variety = variety
        self.color = color
        self.size = size
        self.suger_content = suger_content


apple1 = Apple('王林', 'green', 15, 8)
apple2 = Apple('サンふじ', 'red', 12, 6)
apples = [apple1, apple2]

for apple in apples:
    print('品種 : {}、色 : {}、大きさ : {}、糖度 : {}'.format(apple.variety, apple.color, apple.size, apple.suger_content))
