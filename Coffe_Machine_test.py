import unittest
from CoffeeMachine import CoffeMachine

class CoffeMachineTest(unittest.TestCase):
    
    def test_cas_nominal(self):
        # ETANT DONNE une machine à café
        machine = CoffeMachine()
        # QUAND on insère une pièce de 50cts
        machine.insert50cts()
        # ALORS un café est servi
        machine.serveCoffee()
        # ET l'argent est encaissé
        machine.cashMoney()
        
    def test_un_euro(self):
        # ETANT DONNE une machine à café
        machine = CoffeMachine()
        # QUAND on insère une pièce de un euro
        machine.insertOneEuro()
        # ALORS la machine sert un café
        machine.serveCoffee()
        # ET l'argent est encaissé
        machine.cashMoney()