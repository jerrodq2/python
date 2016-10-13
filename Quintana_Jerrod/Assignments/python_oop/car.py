class Car(object):
    def __init__(self, price, speed, fuel, mileage, tax = 'basic'):
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.price = price
        if price > 10000:
            self.tax = '15%'
        else:
            self.tax = '12%'
    def display_all(self):
        print self.price, self.speed, self.fuel, self.mileage, self.tax
dodge = Car(2000, 35, 'full', '15mpg')
mustang = Car(2000, 5, 'Not Full', '105 mpg')
toyota = Car(2000, 15, 'Kind of Full', '95mpg')
suv = Car(2000, 25, 'Full', '25mpg')
sudan = Car(2000, 45, 'Empty', '25mpg')
last = Car(20000000, 35, 'Empyt', '15mpg')

dodge.display_all()
mustang.display_all()
toyota.display_all()
suv.display_all()
sudan.display_all()
last.display_all()
