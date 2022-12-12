class User():
    def sign_in(self):
        print('Logged in')

    def attack(self):
      print('do nothing')
# we use inheritance to acess the parent class
class Wizard(User):
    def __init__(self, name, power):
        # this allows user and wizard to use attack method default 'do nothing'
        User.attack(self)
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'Attacking with arrows: arrows left- {self.num_arrows}')

wizard1 = Wizard('goku', 9001)
archer1 = Archer('Robin', 1000)

#Although Archers and Wizards share the same method name .attack the output is different because polymorphism allows the same methods to do different things depending on the object that calls the function
print(wizard1.attack())
print(archer1.attack())

# another example of polymorphism
def player_attack(char):
  char.attack()

player_attack(wizard1)
player_attack(archer1)

# another example of polymorphism

for char in [wizard1, archer1]:
  char.attack()