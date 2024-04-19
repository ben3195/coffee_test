import unittest
from coffe_machine.CoffeeMachine import CoffeMachine

class CoffeMachineTest(unittest.TestCase):
    
    def test_cas_nominal(self):
        # Etant donné une machine à Café
        machine = CoffeMachine()
        
        # Quand on insère une 50cts
        machine.insertCoin()
            
        # ALORS un café est servi
        machine.serveCoffee()
        
        # ET l'argent est encaissé
        machine.cashMoney()
        
    