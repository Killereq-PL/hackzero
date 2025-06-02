from gpiozero import Button
import keyboard

# GPIO Pins
UP_PIN = 0
DOWN_PIN = 1
LEFT_PIN = 2
RIGHT_PIN = 3
OK_PIN = 4

class DpadInput():
    def __init__(self):
        self.up_btn = Button(UP_PIN)
        self.down_btn = Button(DOWN_PIN)
        self.left_btn = Button(LEFT_PIN)
        self.right_btn = Button(RIGHT_PIN)
        self.ok_btn = Button(OK_PIN)
        self.button_map = {
            self.up_btn: 'up arrow',
            self.down_btn: 'down arrow',
            self.left_btn: 'left arrow',
            self.right_btn: 'right arrow',
            self.ok_btn: 'enter'
        }
    
    def press_event(caller: Button):
        caller_pin = caller.pin
    
    def release_event(caller: Button):
        caller_pin = caller.pin

    def setup_events(self):
        for pair in self.button_map.items():
            pair[0].when_activated = self.press_event
            pair[0].when_deactivated = self.release_event

if __name__ == "__main__":
    dpadinput = DpadInput()
    dpadinput.setup_events()