class CoffeeMachine:
    # isis: todo error catching for unexpected arguments
    # isis: added constructor
    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

    # why create an attribute if you can just use the parameter?
    def get_action(self):
        action = input('\n Write action(buy, fill, take, remaining, exit):')
        if action == 'buy':
            self.action_buy()
        elif action == 'fill':
            self.action_fill()
        elif action == 'take':
            self.action_take()
        elif action == 'remaining':
            self.action_remaining()
        elif action == 'exit':
            self.action_exit()

    def action_buy(self):
        coffee = input("\n What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
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
            self.get_action()
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
            self.get_action()
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
            self.get_action()
        elif coffee == 'back':
            self.get_action()

    def action_fill(self):
        a_water = int(input("\n Write how many ml of water do you want to add:"))
        self.water += a_water
        a_milk = int(input("Write how many ml of milk do you want to add:"))
        self.milk += a_milk
        a_beans = int(input("Write how many grams of coffee beans do you want to add:"))
        self.beans += a_beans
        a_cups = int(input("Write how many disposable cups of coffee do you want to add:"))
        self.cups += a_cups
        self.get_action()

    def action_take(self):
        print(f"I gave you {self.money}")
        self.money = 0
        self.get_action()

    def action_remaining(self):
        print("The coffee machine has:")
        print(f'\n{self.water} of water\n{self.milk} of milk\n{self.beans} of coffee beans\n{self.cups} of disposable cups')
        # isis: the method upper is more simple
        print(f"{self.money} of money")
        self.get_action()

    def action_exit(self):
        return 0


a = CoffeeMachine(400, 540, 120, 9, 550)
a.get_action()
