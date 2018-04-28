import RPi.GPIO as GPIO

class component(object):
    """contains generic behavior for component objects"""

    def _init_(self, state, gpio):
        self.state = state
        self.gpio = gpio

    @property
    def state(self):
        return self._state

    @property
    def gpio(self):
        return self._gpio

    @state.setter
    def state(self, state):
        self._state = state

    @gpio.setter
    def gpio(self, gpio):
        self._gpio = gpio



    


