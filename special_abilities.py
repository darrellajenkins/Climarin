
falcon = 1
demi_god = 2
god = 3

abilities = {   'falcon': 1,
                'demi_god':2,
                'god':3
            }

ability = [     abilities['falcon'],
                abilities['demi_god'],
                abilities['god']
        ]

def escape(name):
    esc = "ZARIN"
    return f"{name} has escaped to the realm of {esc} and cannot be attacked or damaged.", esc

def reflect(attacker, power, defender):
    """Takes argument of power level used in an attack from the attacker and reflects it back + 0.50."""
    reflect = power + 0.50
    return f"{defender} reflects the attack from {attacker} with Power {reflect}!"




