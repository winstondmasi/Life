#function that represents the entire game world 

class World:
    def rule1(self):
        print("A live cell with fewer than two live neighbors dies")

    def rule2(self):
        print("A live cell with more than three live neighbors also dies")