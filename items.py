class Item(object):
    """Base class for all items"""

    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)

class Credit(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Credit",
                         description="A space buck with '{} credits' stamped on the front.".format(str(self.amt)),
                         value=self.amt)

class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)
 
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)
 
 
class Rock(Weapon):
    def __init__(self):
        super().__init__(name="Rock",
                         description="A fist-sized rock, suitable for bludgeoning.",
                         value=0,
                         damage=5)
 
 
class FlareGun(Weapon):
    def __init__(self):
        super().__init__(name="FlareGun",
                         description="A gun that shoots flares. Can cause minimal damage to enemies.",
                         value=10,
                         damage=10)
