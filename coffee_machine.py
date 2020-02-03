class CoffeeMachine:
    def __init__(self):
        self.milk = 1000
        self.coffee = 1000
        self.sugar = 1000

    def make_coffee(self, milk, coffee, sugar):
        if self.milk < milk and self.coffee < coffee and self.sugar < sugar:
            m = milk - self.milk
            c = coffee - self.coffee
            s = sugar - self.sugar

            print(f'Пополните запасы молока на {m} мл! ')
            print(f'Пополните запасы кофе на {c} гр!')
            print(f'Пополните запасы сахара на {s} гр!')
            
                
        else:
            print('Процесс приготовления кофе завершен!')
            self.__subtract_milk(milk)
            self.__subtract_coffee(coffee)
            self.__subtract_sugar(sugar)


    def __subtract_milk(self, milk):
        self.milk -= milk
    
    def __subtract_coffee(self, coffee):
        self.coffee -= coffee
    
    def __subtract_sugar(self, sugar):
        self.sugar -= sugar




machine = CoffeeMachine()
machine.make_coffee(1050, 2000, 2000)