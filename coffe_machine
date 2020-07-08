class CoffeeMachine():
    water = 400
    milk = 540
    beans = 120
    cups = 9
    money = 550
    def get_action(self, action):
        self.action = action
        if self.action == 'buy':
            print()
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
            self.action_buy(input())
        elif self.action == 'fill':
            self.action_fill()
        elif action == 'take':
            self.action_take()
        elif action == 'remaining':
            self.action_remaining()
        elif action == 'exit':
            self.action_exit()
    def action_buy(self, coffee):
        self.coffee = coffee
        if self.coffee == '1':
            if CoffeeMachine.water < 250:
                print('Sorry, not enough water!')
            elif CoffeeMachine.beans < 16:
                print('Sorry, not enough beans!')
            elif CoffeeMachine.cups < 1:
                print('Sorry, not enough cups!')
            elif CoffeeMachine.water >= 250 and CoffeeMachine.beans >= 16 and CoffeeMachine.cups >= 1:
                print("I have enough resources, making you a coffee!")
                CoffeeMachine.water -= 250
                CoffeeMachine.beans -= 16
                CoffeeMachine.cups -= 1
                CoffeeMachine.money += 4
            print()
            print("Write action(buy, fill, take, remaining, exit):")
            self.get_action(input())
        elif self.coffee == '2':
            if CoffeeMachine.water < 350:
                print('Sorry, not enough water!')
            elif CoffeeMachine.milk < 75:
                print('Sorry, not enough milk!')
            elif CoffeeMachine.beans < 20:
                print('Sorry, not enough beans!')
            elif CoffeeMachine.cups < 1:
                print('Sorry, not enough cups!')
            elif CoffeeMachine.water >= 350 and  CoffeeMachine.milk >=75 and  CoffeeMachine.beans >= 20 and  CoffeeMachine.cups >= 1:
                print("I have enough resources, making you a coffee!")
                CoffeeMachine.water -= 350
                CoffeeMachine.milk -= 75
                CoffeeMachine.beans -= 20
                CoffeeMachine.cups -= 1
                CoffeeMachine.money += 7
            print()
            print("Write action(buy, fill, take, remaining, exit):")
            self.get_action(input())
        elif self.coffee == '3':
            if CoffeeMachine.water < 200:
                print('Sorry, not enough water!')
            elif CoffeeMachine.milk < 100:
                print('Sorry, not enough milk!')
            elif CoffeeMachine.beans < 12:
                print('Sorry, not enough beans!')
            elif CoffeeMachine.cups < 1:
                print('Sorry, not enough cups!')
            elif CoffeeMachine.water >= 200 and CoffeeMachine.milk >=100 and CoffeeMachine.beans >= 12 and CoffeeMachine.cups >= 1:
                print("I have enough resources, making you a coffee!")
                CoffeeMachine.water -= 200
                CoffeeMachine.milk -= 100
                CoffeeMachine.beans -= 12
                CoffeeMachine.cups -= 1
                CoffeeMachine.money += 6
            print()
            print("Write action(buy, fill, take, remaining, exit):")
            self.get_action(input())
        elif self.coffee == 'back':
            print()
            print("Write action(buy, fill, take, remaining, exit):")
            self.get_action(input())
    def action_fill(self):
        print()
        print("Write how many ml of water do you want to add:")
        a_water = int(input())
        CoffeeMachine.water = CoffeeMachine.water + a_water
        print("Write how many ml of milk do you want to add:")
        a_milk = int(input())
        CoffeeMachine.milk = CoffeeMachine.milk + a_milk
        print("Write how many grams of coffee beans do you want to add:")
        a_beans = int(input())
        CoffeeMachine.beans = a_beans + CoffeeMachine.beans
        print("Write how many disposable cups of coffee do you want to add:")
        a_cups = int(input())
        CoffeeMachine.cups = a_cups + CoffeeMachine.cups
        print("Write action(buy, fill, take, remaining, exit):")
        self.get_action(input())
    def action_take(self):
        print("I gave you {}".format(CoffeeMachine.money))
        CoffeeMachine.money = 0
        print()
        print("Write action(buy, fill, take, remaining, exit):")
        self.get_action(input())
    def action_remaining(self):
        print("The coffee machine has:")
        print(CoffeeMachine.water, 'of water')
        print(CoffeeMachine.milk, "of milk")
        print(CoffeeMachine.beans, "of coffee beans")
        print(CoffeeMachine.cups, "of disposable cups")
        print("$ {} of money".format(CoffeeMachine.money))
        print()
        print("Write action(buy, fill, take, remaining, exit):")
        self.get_action(input())
    def action_exit(self):
        return 0
a = CoffeeMachine()
print("Write action(buy, fill, take, remaining, exit):")
a.get_action(input())
