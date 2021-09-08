"""
Author : Asif Khan M Pathan
Test Automation Framework
"""

import sys
import json
import os
from time import sleep

from Template.basetest import TestBase

class ConnectTest(TestBase):
    """
    Connect TestCase
    """
    def __init__(self):
        super().__init__()
        sys.path.append(os.getcwd())
        self.result_connect = None

    def run(self):
        super().run()
        self.dut.get_to_initial_condition()

        TestBase.wait_for_advertisement()

        mytest.dut.send_message("ADVERTISE")

        data = mytest.dut.confirm_message("ADVERTISE_SUCCESSFULL")
        if data:
            print(f"====>Advertisement for DIS Application Successfully")
            filepath = os.path.join(os.getcwd(), './Testcase/json_report')
            with open(filepath, 'w') as fptr:
                list = [
                    {
                        "Results": "PASS",
                        "Test Name": "Advertise"
                    }
                ]
                json_object = json.dumps(list, indent=4)
                fptr.write(json_object)
            self.result_connect = True
        else:
            print("====>Sorry There is some issue in Staring Advertisement")
            print("====>Testcase Failed")
            filepath = os.path.join(os.getcwd(), './Testcase/json_report')
            with open(filepath, 'w') as fptr:
                list = [
                    {
                        "Results": "FAIL",
                        "Test Name": "Advertise"
                    }
                ]
                json_object = json.dumps(list, indent=4)
                fptr.write(json_object)
                print('file created from connected')
            self.result_connect = False

        print("\n\nWaiting for the Mobile App to Connect with the Board  MAX Duration : 25 Seconds \n")
        for i in range(100):
            print(".", end="")
            sys.stdout.flush()
            sleep(0.25)
            data = mytest.dut.confirm_message("CONNECT")
            if data:
                print("\n====>Mobile APP and NRF Board Connected Successfullly")
                print("Testcase Passed")
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
                        }
                    ]
                    json_object = json.dumps(list, indent=4)
                    fptr.write(json_object)
                    print('file created from connect for loop')

                    break

        else:
            print("\n====>Connection Failed between Mobile APP and NRF Board")

            print("\nTestcase Failed")
            filepath = os.path.join(os.getcwd(), './Testcase/json_report')
            with open(filepath, 'w') as fptr:
                list = [
                    {
                        "Results": "PASS",
                        "Test Name": "Advertise"
                    },
                    {
                        "Results": "FAIL",
                        "Test Name": "Connect"
                    }
                ]
                json_object = json.dumps(list, indent=4)
                fptr.write(json_object)
        mytest.cleanup()


if __name__ == "__main__":

    sys.path.append(os.getcwd())
    mytest = ConnectTest()
    mytest.run()


