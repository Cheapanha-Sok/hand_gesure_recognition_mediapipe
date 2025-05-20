class Constant:
    def __init__(self):
        self.CLASS_NAMES = ['nothing','down','turn_left','turn_right','up']
        self.NOTHING = 0
        self.DOWN = 1
        self.TURN_LEFT = 2
        self.TURN_RIGHT = 3
        self.UP = 4
        
    def getClassNameByIndex(self , class_int):
        return self.CLASS_NAMES[class_int]
    
    def getIndexByClassName(self , class_name):
        return self.CLASS_NAMES.index(class_name)   