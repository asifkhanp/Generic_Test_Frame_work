"""
Author : Venkatesan Madappan
Test Automation Framework
"""

import sys
import os
from Template.basetest import TestBase


class ConnectTest(TestBase):
    """
    Connect TestCase
    """
    def __init__(self):
        super().__init__()
        sys.path.append(os.getcwd())

    def run(self):
        super().run()
        print("Send Advertise Command")
        command = 'ADVERTISE'#str(input())
        try:
            mytest.dut.send_message(command)
            print('Bluetooth application')
            print("Confirm/Response Advertise is received by NRF Board")
            data = mytest.dut.confirm_message(command)

            print(f"Received the {command} Message is : {data}")
            mytest.cleanup()
        except Exception as E:
            print(E)
            print('Command Not Found')
            exit()

if __name__ == "__main__":
    print("Connect Test Case Execution")
    sys.path.append(os.getcwd())
    mytest = ConnectTest()
    mytest.run()
