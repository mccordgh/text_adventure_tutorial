import items, enemies
 
class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError()
 
    def modify_player(self, player):
        raise NotImplementedError()

class StartingRoom(MapTile):
    def intro_text(self):
        return """
        You find yourself in a damaged space ship. The lights from a nearby console flickering on and off.
        You can make out four paths, each equally as dimly lit as the next. Looks like emergency power has been flipped on.
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass