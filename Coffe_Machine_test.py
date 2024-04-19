import unittest
from CoffeeMachine import CoffeMachine

class CoffeMachineTest(unittest.TestCase):
    
    def test_cas_nominal(self):
        # ETANT DONNE une machine à café
        machine = CoffeMachine()
        # QUAND on insère une pièce de 50cts
        fifty_cts = 50
        machine.insertCoin(fifty_cts)
        # ALORS un café est servi
        machine.serveCoffee()
        # ET l'argent est encaissé
        machine.cashMoney()
        
    def test_un_euro(self):
        # ETANT DONNE une machine à café
        machine = CoffeMachine()
        # QUAND on insère une pièce de un euro
        one_euro = 100
        machine.insertCoin(one_euro)
        # ALORS la machine sert un café
        machine.serveCoffee()
        # ET l'argent est encaissé
        machine.cashMoney()