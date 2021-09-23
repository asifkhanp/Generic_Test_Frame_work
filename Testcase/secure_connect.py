"""
Author : Venkatesan Madappan
Test Automation Framework
"""

import sys
import os
import time
from time import sleep

from Template.basetest import TestBase
from Reports.Html import HtmlReport
from Reports.Json_report_messages import JsonMessages


class SecureConnectTest(TestBase):
    """
    Connect TestCase
    """
    def __init__(self):
        super().__init__()
        sys.path.append(os.getcwd())
        filepath = os.path.join(os.getcwd(), './Reports/json_report.json')
        self.json_obj = JsonMessages(filepath)

    def run(self):
        super().run()
        self.dut.get_to_initial_condition()

        TestBase.wait_for_advertisement()

        mytest.dut.send_message("ADVERTISE")

        data = mytest.dut.confirm_message("ADVERTISE_SUCCESSFULL")
        if data:
            self.logger.info(f"====>Advertisement for DIS Application Successfully")
            self.json_obj.advertise_message(True)
        else:
            self.logger.info("====>Sorry There is some issue in Staring Advertisement")
            self.logger.info("====>Testcase Failed")
            self.json_obj.advertise_message(False)

        self.logger.info("\n\nWaiting for the Mobile App to Connect with the Board  MAX Duration : 25 Seconds \n")

        mytest.dut.send_message("AUTHENTICATION_CONFIRMED")
        #mytest.dut.send_message("AUTHENTICATION_CANCELED")

        for i in range(100):
            print(".", end="")
            sys.stdout.flush()
            sleep(0.25)
            data = mytest.dut.confirm_message("CONNECT")
            if data:
                self.logger.info("\n====>Mobile APP and NRF Board Connected Successfully")
                self.logger.info("Connect Passed")
                self.json_obj.connect_message(True)
                break
        else:
            self.logger.info("\n====>Connection Failed between Mobile APP and NRF Board")
            self.logger.info("\nConnect Failed")
            self.json_obj.connect_message(False)

        time.sleep(5)
        mytest.dut.send_message("GET_SECURITY_LEVEL")

        for i in range(10):
            sleep(0.25)
            data = mytest.dut.confirm_message("BT_SECURITY_L4")
            if data:
                self.logger.info("\nSecurity Level is 4\nSecure Connect Test has Passed\n")
                self.json_obj.secure_connect_messages(True)
                break
        else:
            self.logger.info("\nSecure Connect Test has Failed\n")
            self.json_obj.secure_connect_messages(False)
        mytest.cleanup()


if __name__ == "__main__":

    sys.path.append(os.getcwd())
    mytest = SecureConnectTest()
    mytest.run()
    html_r = HtmlReport()
    html_r.run()