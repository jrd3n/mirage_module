 
from mirage.core import scenario
from mirage.libs import io,ble,bt,utils

class ble_trial_scene(scenario.Scenario):

        def onStart(self):
                return True

        def onEnd(self):
                return True

        def send_to_scene(self,key):
                io.warning("I'M HERE")
                io.info(key)
                return True