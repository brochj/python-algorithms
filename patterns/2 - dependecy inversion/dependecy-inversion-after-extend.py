# https://www.youtube.com/watch?v=Kv5jhbSkqLE

from abc import ABC, abstractmethod


class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class Dimmable(ABC):
    @abstractmethod
    def set_power(self):
        pass


class LightBulb(Switchable, Dimmable):
    def turn_on(self):
        print("LightBulb: turned on...")

    def turn_off(self):
        print("LightBulb: turned off...")

    def set_power(self, power: float):
        print(f"LightBulb: power set to {power * 100} %")


class Fan(Switchable):
    def turn_on(self):
        print("Fan: turned on...")

    def turn_off(self):
        print("Fan: turned off...")

    def set_power(self, power: float):
        print(f"Fan: power set to {power * 100} %")


class ElectricPowerSwitch:
    def __init__(self, c: Switchable):
        self.client = c
        self.on = False

    def press(self):
        if self.on:
            self.client.turn_off()
            self.on = False
        else:
            self.client.turn_on()
            self.on = True


class ElectricPowerDimmer:
    def __init__(self, c: Dimmable):
        self.client = c

    def set_power(self, power: float):
        self.client.set_power(power)


l = LightBulb()
f = Fan()
dimmer = ElectricPowerDimmer(f)
switch = ElectricPowerSwitch(f)
switch.press()
dimmer.set_power(0.5)
switch.press()
