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
import time

from pyrobotium.robotium import Device 

def main():
    """
    This example creates a connection to device and uses the Android examples "NotePad" application
    to demonstrate the usage of the module.
    """
    device = Device("localhost", 4321, "emulator-5554")
    #device.set_port_forwarding(4321, 4321)
    #device.run_test_on_device("org.topq.jsystem.mobile", "RobotiumServer", "testMain")
    device.launch("org.topq.mobile.example.loginapp.LoginActivity")
    device.enter_text(0, "tal@tal.com")
    device.enter_text(1, "1234567")
    device.click_on_button_with_text("Sign in or register")
    time.sleep(5)
    device.click_on_button_with_text("Ok")
    device.click_on_button_with_text("Sign in or register")
    time.sleep(5)
    device.click_on_button_with_text("Ok")
    print "Finished"
    
    
    exit(0)
    
if __name__ == "__main__":
    main()
