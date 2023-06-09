from mirage.core import module
from mirage.libs import utils,ble,io
from mirage.core import module,interpreter

class ble_BULB(module.WirelessModule):
	def init(self):
		self.technology = "ble"
		self.type = "JORDON"
		self.description = "Control smart bulb"
		self.args = {	'INTERFACE': 'hci0', 
	       				'TARGET': 'BE:58:97:00:1C:62',
						'SCENARIO':'ble_bulb_scene',
						"TIMEOUT":"3",
						"CONNECTION_TYPE":"public"}
		
		self.dependencies = ["ble"]

	# @module.scenarioSignal("ble_bulb_scene")
	# def hello(self,name):
	# 		io.info("Hello, "+name)


	@module.scenarioSignal("onStart")
	def startScenario(self):
		pass

	@module.scenarioSignal("onEnd")
	def endScenario(self):
		pass

	def checkCapabilities(self):
		return self.emitter.hasCapabilities("INITIATING_CONNECTION")

	def run(self):
		# Enter your code here.

		interface = self.args["INTERFACE"]
		self.emitter = self.getEmitter(interface=interface)
		self.receiver = self.getReceiver(interface=interface)
		timeout = utils.integerArg(self.args["TIMEOUT"])

		# return self.ok()

		if self.checkCapabilities():
			io.info("Trying to connect to : "+self.args["TARGET"]+" (type : "+self.args["CONNECTION_TYPE"]+")")
			self.emitter.sendp(ble.BLEConnect(self.args["TARGET"], type=self.args["CONNECTION_TYPE"]))

			while not self.receiver.isConnected() and timeout > 0:
				timeout -= 1
				utils.wait(seconds=1)

			if self.receiver.isConnected():
				io.success("Connected on device : "+self.args["TARGET"])

			if self.loadScenario():
				io.info("Scenario loaded !")
				self.startScenario()
				
			while True:
				pass
			if self.scenarioEnabled:
				self.endScenario()

			else:
				io.fail("Error during connection establishment !")
				self.emitter.sendp(ble.BLEConnectionCancel())
				return self.nok()
		else:
			io.fail("Interface provided ("+str(self.args["INTERFACE"])+") is not able to initiate connection.")
			return self.nok()
