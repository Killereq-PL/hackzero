from gpiozero import Button
import keyboard
import mouse

# GPIO Pins
UP_PIN = 0
DOWN_PIN = 1
LEFT_PIN = 2
RIGHT_PIN = 3
OK_PIN = 4
MODE_SWITCH_PIN = 5

MODE_SWITCH_TOGGLE = True # True for toggle mode, False for hold (switch) mode

class DpadInput():
    def __init__(self):
        self.up_btn = Button(UP_PIN)
        self.down_btn = Button(DOWN_PIN)
        self.left_btn = Button(LEFT_PIN)
        self.right_btn = Button(RIGHT_PIN)
        self.ok_btn = Button(OK_PIN)
        self.mode_switch_btn = Button(MODE_SWITCH_PIN)
        self.mode = 0 # 0 for DPad mode, 1 for Mouse mode
        self.button_map = {
            self.up_btn: 'up arrow',
            self.down_btn: 'down arrow',
            self.left_btn: 'left arrow',
            self.right_btn: 'right arrow',
            self.ok_btn: 'enter'
        }
        
        def press_callback(self, map):
            if self.mode == 0:  # DPad mode
                keyboard.press(map[1])
            elif self.mode == 1:  # Mouse mode
                btn = map[0]
                if btn == self.up_btn:
                    mouse.move(0, -10, absolute=False, duration=0.1)
                elif btn == self.down_btn:
                    mouse.move(0, 10, absolute=False, duration=0.1)
                elif btn == self.left_btn:
                    mouse.move(-10, 0, absolute=False, duration=0.1)
                elif btn == self.right_btn:
                    mouse.move(10, 0, absolute=False, duration=0.1)
                elif btn == self.ok_btn:
                    mouse.press('left')
        
        def release_callback(self, map):
            if self.mode == 0:  # DPad mode
                keyboard.release(map[1])
            elif self.mode == 1:  # Mouse mode
                btn = map[0]
                if btn == self.ok_btn:
                    mouse.release('left')
        
        for x in self.button_map.items():
            x[0].when_pressed = lambda: press_callback(self, x)
            x[0].when_released = lambda: release_callback(self, x)  

if __name__ == "__main__":
    dpadinput = DpadInput()
    print("DPad Input initialized. Press buttons to simulate input.")