"""
Author : Asif Khan M Pathan
Test Automation Framework
"""

import sys
import os
from time import sleep

from Template.basetest import TestBase
from Reports.Html import HtmlReport
from Reports.Json_report_messages import JsonMessages


class DisconnectTest(TestBase):
    """
    DISConnect TestCase
    """
    def __init__(self):
        super().__init__()
        sys.path.append(os.getcwd())
        filepath = os.path.join(os.getcwd(), './Reports/json_report')
        self.json_obj = JsonMessages(filepath)
        self.count = 0

    def run(self):
        super().run()
        self.dut.get_to_initial_condition()

        TestBase.wait_for_advertisement()

        mytest.dut.send_message("ADVERTISE")
        sleep(0.25)
        data = mytest.dut.confirm_message("ADVERTISE_SUCCESSFULL")
        if data:
            print(f"====>Advertisement for DIS Application Successfully")
            self.json_obj.advertise_pass()
            self.count += 1
        else:
            print("====>Sorry There is some issue in Staring Advertisement")
            print("====>Testcase Failed")
            self.json_obj.advertise_fail()

        print("\n\nWaiting for the Mobile App to Connect with the Board  MAX Duration : 25 Seconds \n")
        for i in range(100):
            print(".", end="")
            sys.stdout.flush()
            sleep(0.25)
            data = mytest.dut.confirm_message("CONNECT")
            if data:
                print("\n====>Mobile APP and NRF Board Connected Successfullly")
                self.json_obj.connect_pass()
                self.count +=1
                break
        else:
            print("\n====>Connection Failed between Mobile APP and NRF Board")
            print("\n====>Testcase Failed")
            self.json_obj.connect_fail()

        print("\n\nWaiting for the Mobile App to DISConnect with the Board  MAX Duration : 25 Seconds \n")
        for i in range(100):
            print(".", end="")
            sys.stdout.flush()
            sleep(0.25)
            data = mytest.dut.confirm_message("DISCONNECT")
            if data:
                print("\n====>Mobile APP and NRF Board DISConnected Successfullly")
                self.json_obj.disconnect_pass()
                self.count += 1
                break
        else:
            print("\n====>Connection Failed between Mobile APP and NRF Board")
            self.json_obj.disconnect_fail()
            print("\nTestcase Failed")
            print(f'count is{self.count}')
            if self.count == 1:
                self.json_obj.connect_fail()

        mytest.cleanup()


if __name__ == "__main__":

    sys.path.append(os.getcwd())
    mytest = DisconnectTest()
    mytest.run()
    html_r = HtmlReport()
    html_r.run()
