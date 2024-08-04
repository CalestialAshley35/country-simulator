import sys

class Country:
    def __init__(self, name):
        self.name = name
        self.resources = {
            "population": 1000000,
            "money": 1000000,
            "food": 50000,
            "technology": 1000
        }
        self.happiness = 50

    def show_status(self):
        print(f"\nCountry: {self.name}")
        print(f"Population: {self.resources['population']}")
        print(f"Money: ${self.resources['money']}")
        print(f"Food: {self.resources['food']} units")
        print(f"Technology: {self.resources['technology']}")
        print(f"Happiness: {self.happiness}%")

    def change_population(self, amount):
        self.resources['population'] += amount
        print(f"Population {'increased' if amount > 0 else 'decreased'} by {abs(amount)}.")

    def change_money(self, amount):
        self.resources['money'] += amount
        print(f"Money {'increased' if amount > 0 else 'decreased'} by ${abs(amount)}.")

    def change_food(self, amount):
        self.resources['food'] += amount
        print(f"Food {'increased' if amount > 0 else 'decreased'} by {abs(amount)} units.")

    def change_technology(self, amount):
        self.resources['technology'] += amount
        print(f"Technology {'increased' if amount > 0 else 'decreased'} by {abs(amount)}.")

    def change_happiness(self, amount):
        self.happiness += amount
        if self.happiness > 100:
            self.happiness = 100
        elif self.happiness < 0:
            self.happiness = 0
        print(f"Happiness {'increased' if amount > 0 else 'decreased'} by {abs(amount)}%.")

def show_help():
    print("\nHelp - Available Commands:")
    print("1. Show status: Displays the current status of your country.")
    print("2. Increase population: Increase the population by a specified amount.")
    print("3. Decrease population: Decrease the population by a specified amount.")
    print("4. Increase money: Increase the amount of money by a specified amount.")
    print("5. Decrease money: Decrease the amount of money by a specified amount.")
    print("6. Increase food: Increase the amount of food by a specified amount.")
    print("7. Decrease food: Decrease the amount of food by a specified amount.")
    print("8. Increase technology: Increase the technology level by a specified amount.")
    print("9. Decrease technology: Decrease the technology level by a specified amount.")
    print("10. Increase happiness: Increase the happiness level by a specified amount.")
    print("11. Decrease happiness: Decrease the happiness level by a specified amount.")
    print("12. Exit: Exits the game.")
    print("13. Help: Shows this help message.")

def main():
    country_name = input("Enter the name of your country: ")
    country = Country(country_name)

    while True:
        print("\nCommands:")
        print("1. Show status")
        print("2. Increase population")
        print("3. Decrease population")
        print("4. Increase money")
        print("5. Decrease money")
        print("6. Increase food")
        print("7. Decrease food")
        print("8. Increase technology")
        print("9. Decrease technology")
        print("10. Increase happiness")
        print("11. Decrease happiness")
        print("12. Exit")
        print("13. Help")

        command = input("Enter command number: ")

        if command == "1":
            country.show_status()
        elif command == "2":
            amount = int(input("Enter amount to increase population by: "))
            country.change_population(amount)
        elif command == "3":
            amount = int(input("Enter amount to decrease population by: "))
            country.change_population(-amount)
        elif command == "4":
            amount = int(input("Enter amount to increase money by: "))
            country.change_money(amount)
        elif command == "5":
            amount = int(input("Enter amount to decrease money by: "))
            country.change_money(-amount)
        elif command == "6":
            amount = int(input("Enter amount to increase food by: "))
            country.change_food(amount)
        elif command == "7":
            amount = int(input("Enter amount to decrease food by: "))
            country.change_food(-amount)
        elif command == "8":
            amount = int(input("Enter amount to increase technology by: "))
            country.change_technology(amount)
        elif command == "9":
            amount = int(input("Enter amount to decrease technology by: "))
            country.change_technology(-amount)
        elif command == "10":
            amount = int(input("Enter amount to increase happiness by: "))
            country.change_happiness(amount)
        elif command == "11":
            amount = int(input("Enter amount to decrease happiness by: "))
            country.change_happiness(-amount)
        elif command == "12":
            print("Exiting the game.")
            sys.exit()
        elif command == "13":
            show_help()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
      
