
class monster:
    name = "e"
    def __init__(self, name, health, loot_dic):
        self.name = name
        self.health = health
        self.loot_dic = loot_dic

 

    def display(self):
        print("This is a ", self.name, " with " ,str(self.health) , " health. It's loot and chances of obtaining are:")
        for i in self.loot_dic:
            print("Drop: ", i, " |  Chance:", self.loot_dic[i])
    
if(__name__ == "__main__"):
    m1 = monster("chicken", 3, {"feather1": .5, "feather2": .25, "raw chicken": 1, "nothing": .25, "clue scroll (beginner)": 1/300.})

    m1.display()