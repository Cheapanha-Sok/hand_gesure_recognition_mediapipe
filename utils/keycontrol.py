import pyautogui
from utils.constant import Constant

class KeyControl:
    def __init__(self):
        self.command = 0 # 0 : nothing , 1 : down , 2 : Turn left , 3 : Turn Right , Up : 4
        self.last_detected_class = -1

    def key_control(self, predicted_class):
        
        CONSTANT = Constant()
        
        if predicted_class != self.last_detected_class:
            if predicted_class == CONSTANT.UP and self.command != CONSTANT.UP:
                print("Jump / Press UP")
                pyautogui.press('up')
                self.command = CONSTANT.UP

            elif predicted_class == CONSTANT.DOWN and self.command != CONSTANT.DOWN:
                print("Roll / Press DOWN")
                pyautogui.press('down')
                self.command = CONSTANT.DOWN

            elif predicted_class == CONSTANT.TURN_LEFT and self.command != CONSTANT.TURN_LEFT :
                print("Move Left / Press LEFT")
                pyautogui.press('left')
                self.command = CONSTANT.TURN_LEFT 

            elif predicted_class == CONSTANT.TURN_RIGHT and self.command != CONSTANT.TURN_RIGHT:
                print("Move Right / Press RIGHT")
                pyautogui.press('right')
                self.command = CONSTANT.TURN_RIGHT

            elif predicted_class == CONSTANT.NOTHING and self.command != CONSTANT.NOTHING :
                print("Do Nothing")
                self.command = CONSTANT.NOTHING

            self.last_detected_class = predicted_class