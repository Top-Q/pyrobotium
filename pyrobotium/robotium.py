"""
Copyright (c) 2012, Top-Q. All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the 
following conditions are met:

Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer 
in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, 
BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT 
SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; 
OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT 
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
import sys
from exceptions import *
import json
import socket

class Device():
	"""	
	Represents an Android device interface
	"""
	
	# Android hardware buttons
	HOME = 0
	BACK = 1
	
	# TCP parameters
	BUFFER_SIZE = 1024
	
	def __init__(self, host, port, device):
		"""
		@param host - The hostname or IP address of the device
		@param port - The port robotium listens to
		@param adbLocation - The location of the adb executable
		@device - The serial number of the device
		"""
		self._device = device
		self._host = host
		self._port = port
		
		# init the adb controller
		#self._adb = ADB()
		
		#self._adb.set_adb_path(adbLocation)
		#self._adb.set_target_device(devices.append(device))
						
		print("Device starterd")
	
	def _ascii_encode_dict(self, data):
		ascii_encode = lambda x: x.encode('ascii')
		return dict(map(ascii_encode, pair) for pair in data.items())
	
	def _decode(self, rawData):
		"""
		Decode the response json string
		"""
		print("Raw response: %s" % rawData)
		
		#res = json.loads(rawData, object_hook=self._ascii_encode_dict)
		res = json.loads(rawData)
		# check the response
		succeeded = res.get("succeeded")
		if succeeded == "false":
			print("%s" % res.get("response"))
		
		return succeeded
	
	def _send_data(self, command, *params):
		"""
		Send a command via TCP to the remote agent
		
		@command - remote agent command
		@param data - any number of arguments for the command
		@param timeout - timeout for the request
		"""
		
		try:            
			serialized = json.dumps({ 'command' : command, 'params' : params })
						
			print("Sending command %s to device. Raw data (%s)" % (command, serialized))
			
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			
			if s:
				s.connect((self._host, self._port))
				# send the string with a terminating char
				s.send("%s\n" % serialized)
				try:
					rawResponse = s.recv(Device.BUFFER_SIZE)
					return self._decode(rawResponse)
				finally:
					s.close()
			else:
				raise RobotiumError("Unable to open %s - received an empty file descriptor")
			
		except socket.timeout, e:
			raise TimeoutError(e)
	
	
	def launch(self,activity):
		"""
		Launch the application under test
		"""
		return self._send_data("launch",activity)
	
	def get_text_view(self, index):
		return self._send_data("getTextView", index)
	
	def get_text_view_index(self, text):
		return self._send_data("getTextViewIndex", text)
	
	def get_current_text_views(self):
		return self._send_data("getCurrentTextViews", "a")
	
	def get_text(self, index):
		return self._send_data("getText", index)
	
	def click_on_menu_item(self, item):
		return self._send_data("clickOnMenuItem", item)
	
	def click_on_view(self, index):
		return self._send_data("clickOnView", index)
	
	def enter_text(self, index, text):
		return self._send_data("enterText", index, text)
	
	def click_on_button(self, index):
		return self._send_data("clickOnButton", index)
	
	def click_on_list(self, index):
		return self._send_data("clickInList", index)
	
	def clear_edit_text(self, index):
		return self._send_data("clearEditText", index)
	
	def click_on_button_with_text(self, text):
		return self._send_data("clickOnButtonWithText", text)
	
	def click_on_text(self, text):
		return self._send_data("clickOnText", text)
	
	def sebd_keys(self, key):
		return self._send_data("sendKey", key)
	
	def click_on_hardware_button(self, button):
		return self._send_data("clickOnHardware", button)
	
	def close_activity(self):
		return self._send_data("closeActivity")
	
	def click_on_control_by_index(self, controlName, indexToClickOn):
		return self._send_data("clickInControlByIndex", controlName, indexToClickOn)
	
	def is_view_visible(self, viewName):
		return self._send_data("isViewVisible", viewName)
	