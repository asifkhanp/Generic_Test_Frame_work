"""
Author : Asif Khan M Pathan
Test Automation Framework
"""

import sys
import os
from time import sleep

from Template.basetest import TestBase
from Reports.Json_report_messages import JsonMessages


class ConnectTest(TestBase):
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
            self.json_obj.json_case(True, "Advertise")
        else:
            self.logger.info("====>Sorry There is some issue in Staring Advertisement")
            self.logger.info("====>Testcase Failed")
            self.json_obj.json_case(False, "Advertise")

        self.logger.info("\n\nWaiting for the Mobile App to Connect with the Board  MAX Duration : 25 Seconds \n")
        for i in range(100):
            print(".", end="")
            sys.stdout.flush()
            sleep(0.25)
            data = mytest.dut.confirm_message("CONNECT")
            if data:
                self.logger.info("\n====>Mobile APP and NRF Board Connected Successfullly")
                self.logger.info("Testcase Passed")
                self.json_obj.json_case(True, "Connect")
                break
        else:
            self.logger.info("\n====>Connection Failed between Mobile APP and NRF Board")
            self.logger.info("\nTestcase Failed")
            self.json_obj.json_case(False, "Connect")

        mytest.cleanup()


if __name__ == "__main__":

    sys.path.append(os.getcwd())
    mytest = ConnectTest()
    mytest.run()
