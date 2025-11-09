from abc import ABC, abstractmethod

class ISwitchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class LightBulb(ISwitchable):
    def turn_on(self):
        print("Лампочка: Увімкнено світло")

    def turn_off(self):
        print("Лампочка: Вимкнено світло")

class Fan(ISwitchable): 
    def turn_on(self):
        print("Вентилятор: Почав обертатися")

    def turn_off(self):
        print("Вентилятор: Зупинився")

class Switch:
    def __init__(self, device: ISwitchable):
        self.device = device
        self.is_on = False

    def operate(self):
        if self.is_on:
            self.device.turn_off()
            self.is_on = False
        else:
            self.device.turn_on()
            self.is_on = True

bulb = LightBulb()
fan = Fan()

switch_for_bulb = Switch(bulb)

switch_for_fan = Switch(fan)

print("--- Керуємо лампочкою ---")
switch_for_bulb.operate() 
switch_for_bulb.operate()

print("\n--- Керуємо вентилятором ---")
switch_for_fan.operate()
