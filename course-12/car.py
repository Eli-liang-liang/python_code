class Car():
    def __init__(self, make, model, name):
        self.make = make
        self.model = model
        self.name = name
    
    def go(self):
        print(self.name.title() +" is now ready to go")



my_car = Car('audi', 'a4', "🚗")
your_car = Car("bama", "a7","🚘")

my_car.go()
your_car.go()
