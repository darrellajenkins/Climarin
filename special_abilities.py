
class Enhancers:
    def __init__(self):
        """ """
        self.falcon = 1
        self.demi_god = 2
        self.god = 4
        self.fly = 2

    def escape(self, name):
        esc = "ZARIN"
        return f"{name} has escaped to the realm of {esc} and cannot be attacked or damaged.", esc

    def reflect(self, attacker, power, defender):
        """Takes argument of power level used in an attack from the attacker and reflects it back + 0.50."""
        reflect = power + 0.50
        return f"{defender} reflects the attack from {attacker} with Power {reflect}!"




