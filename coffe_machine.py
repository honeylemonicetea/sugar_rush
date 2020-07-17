class CoffeeMachine:
    # isis: todo error catching for unexpected arguments
    # isis: added constructor
    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

    def get_action(self, action):
        self.action = action
        if self.action == 'buy':
            print("\n What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
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
        if coffee == '1':
            if self.water < 250:
                print('Sorry, not enough water!')
            elif self.beans < 16:
                print('Sorry, not enough beans!')
            elif self.cups < 1:
                print('Sorry, not enough cups!')
            elif self.water >= 250 and self.beans >= 16 and self.cups >= 1:
                print("I have enough resources, making you a coffee!")
                self.water -= 250
                self.beans -= 16
                self.cups -= 1
                self.money += 4
            print("\n Write action(buy, fill, take, remaining, exit):")
            self.get_action(input())
        elif coffee == '2':
            if self.water < 350:
                print('Sorry, not enough water!')
            elif self.milk < 75:
                print('Sorry, not enough milk!')
            elif self.beans < 20:
                print('Sorry, not enough beans!')
            elif self.cups < 1:
                print('Sorry, not enough cups!')
            elif self.water >= 350 and self.milk >= 75 and self.beans >= 20 and self.cups >= 1:
                print("I have enough resources, making you a coffee!")
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.cups -= 1
                self.money += 7
            print()
            print("Write action(buy, fill, take, remaining, exit):")
            self.get_action(input())
        elif coffee == '3':
            if self.water < 200:
                print('Sorry, not enough water!')
            elif self.milk < 100:
                print('Sorry, not enough milk!')
            elif self.beans < 12:
                print('Sorry, not enough beans!')
            elif self.cups < 1:
                print('Sorry, not enough cups!')
            elif self.water >= 200 and self.milk >= 100 and self.beans >= 12 and self.cups >= 1:
                print("I have enough resources, making you a coffee!")
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.cups -= 1
                self.money += 6
            print("\n Write action(buy, fill, take, remaining, exit):")
            self.get_action(input())
        elif coffee == 'back':
            print("\n Write action(buy, fill, take, remaining, exit):")
            self.get_action(input())

    def action_fill(self):
        print("\n Write how many ml of water do you want to add:")
        a_water = int(input())
        self.water = self.water + a_water
        print("Write how many ml of milk do you want to add:")
        a_milk = int(input())
        self.milk = self.milk + a_milk
        print("Write how many grams of coffee beans do you want to add:")
        a_beans = int(input())
        self.beans = a_beans + self.beans
        print("Write how many disposable cups of coffee do you want to add:")
        a_cups = int(input())
        self.cups = a_cups + self.cups
        print("Write action(buy, fill, take, remaining, exit):")
        self.get_action(input())

    def action_take(self):
        print("I gave you {}".format(self.money))
        self.money = 0
        print("\n Write action(buy, fill, take, remaining, exit):")
        self.get_action(input())

    def action_remaining(self):
        print("The coffee machine has:")
        print(f'{self.water} of water')
        # isis: use this!
        print(self.milk, "of milk")
        print(self.beans, "of coffee beans")
        print(self.cups, "of disposable cups")
        # isis: the method upper is more simple
        print("$ {} of money".format(self.money))
        print("\n Write action(buy, fill, take, remaining, exit):")
        self.get_action(input())

    def action_exit(self):
        return 0


a = CoffeeMachine(400, 540, 120, 9, 550)
print("Write action(buy, fill, take, remaining, exit):")
a.get_action(input())
