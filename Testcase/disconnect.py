"""
Author : Asif Khan M Pathan
Test Automation Framework
"""

import sys
import json
import os
from time import sleep

from Template.basetest import TestBase
from Testcase.Html import HtmlReport

class DisconnectTest(TestBase):
    """
    DISConnect TestCase
    """
    def __init__(self):
        super().__init__()
        sys.path.append(os.getcwd())

    def run(self):
        super().run()
        self.dut.get_to_initial_condition()

        TestBase.wait_for_advertisement()

        mytest.dut.send_message("ADVERTISE")
        sleep(0.25)
        data = mytest.dut.confirm_message("ADVERTISE_SUCCESSFULL")
        if data:
            print(f"====>Advertisement for DIS Application Successfully")
        else:
            print("====>Sorry There is some issue in Staring Advertisement")
            print("====>Testcase Failed")

        print("\n\nWaiting for the Mobile App to Connect with the Board  MAX Duration : 25 Seconds \n")
        for i in range(100):
            print(".", end="")
            sys.stdout.flush()
            sleep(0.25)
            data = mytest.dut.confirm_message("CONNECT")
            if data:
                print("\n====>Mobile APP and NRF Board Connected Successfullly")
                break
        else:
            print("\n====>Connection Failed between Mobile APP and NRF Board")
            print("\n====>Testcase Failed")

        print("\n\nWaiting for the Mobile App to DISConnect with the Board  MAX Duration : 25 Seconds \n")
        for i in range(100):
            print(".", end="")
            sys.stdout.flush()
            sleep(0.25)
            data = mytest.dut.confirm_message("DISCONNECT")
            if data:
                print("\n====>Mobile APP and NRF Board DISConnected Successfullly")
                filepath = os.path.join(os.getcwd(), './Testcase/json_report')
                with open(filepath, 'w') as fptr:
                    list = [
                        {
                            "Results": "PASS",
                            "Test Name": "Advertise"
                        },
                        {
                            "Results": "PASS",
                            "Test Name": "Connect"
                        },
                        {
                            "Results": "PASS",
                            "Test Name": "Disconnect"
                        }
                    ]
                    json_object = json.dumps(list, indent=4)
                    fptr.write(json_object)
                break
        else:
            print("\n====>Connection Failed between Mobile APP and NRF Board")
            filepath = os.path.join(os.getcwd(), './Testcase/json_report')
            with open(filepath, 'w') as fptr:
                list = [
                    {
                        "Results": "PASS",
                        "Test Name": "Advertise"
                    },
                    {
                        "Results": "PASS",
                        "Test Name": "Connect"
                    },
                    {
                        "Results": "FAIL",
                        "Test Name": "Disconnect"
                    }
                ]
                json_object = json.dumps(list, indent=4)
                fptr.write(json_object)
            print("\nTestcase Failed")

        mytest.cleanup()


if __name__ == "__main__":

    sys.path.append(os.getcwd())
    mytest = DisconnectTest()
    mytest.run()
    html_r = HtmlReport()
    html_r.run()
