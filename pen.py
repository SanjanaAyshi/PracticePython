class Pen:
    manufacture = 'bd'

    def __init__(self, brand, has, price):
        self.brand = brand
        self.has = has
        self.price = price

    def sms(self, number, massage):
        text = f'{number} send: {massage}'
        print(text)


myPen = Pen('matador', 'maya', 12)
herPen = Pen('joiya', 'zeba', 15)
mamasPen = Pen('alltime', 'amma', 20)
print(myPen.brand, myPen.has, myPen.price)
print(herPen.brand, herPen.has, herPen.price)
print(mamasPen.brand, mamasPen.has, mamasPen.price)
myPen.sms(1545454, 'lala')
herPen.sms(4545122, 'jaja')
mamasPen.sms(15412, 'mir ase kopal e')
