class Device:
    def __init__(self, brand, name, price, color, origin):
        self.brand = brand
        self.name = name
        self.price = price
        self.color = color
        self.origin = origin

    def run(self):
        return f'Its running: {self.brand} and {self.name}'


class laptop(Device):
    def __init__(self, brand, name, price, color, origin,  memory, ssd):
        self.memory = memory
        self.ssd = ssd
        super().__init__(brand, name, price, color, origin)

    def __repr__(self):
        return f'laptop:{self.brand} {self.name} {self.memory}'

    def coding(self):
        return f'I am coding here {self.brand}'


class phone(Device):
    def __init__(self, brand, name, price, color, origin, sim, ram):
        self.sim = sim
        self.ram = ram
        super().__init__(brand, name, price, color, origin)

    def __repr__(self):
        return f'phone:{self.brand} {self.name} {self.sim}'

    def using(self, number, text):
        return f'{self.number} sending massage : {self.text}'


myPhone = phone('Realme', 'Narzo 50', 17999,
                'black', 'china', 'dual sim', 4)
print(myPhone.brand)
print(myPhone)
myLaptop = laptop('lenovo', 'Thinkbook 15G2', 78000,
                  'Metal silver', 'China', '8gb', 125)
print(myLaptop)
print(myLaptop.origin)
