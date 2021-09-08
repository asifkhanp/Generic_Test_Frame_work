"""
Author : Asif Khan M Pathan
Test Automation Framework
"""

import sys
import json
import os
from time import sleep

from Template.basetest import TestBase


class AdvertiseTest(TestBase):
    """
    Advertise TestCase
    """
    def __init__(self):
        super().__init__()
        sys.path.append(os.getcwd())
        self.result_advertise = None

    def run(self):
        super().run()
        self.dut.get_to_initial_condition()

        TestBase.wait_for_advertisement()

        mytest.dut.send_message("ADVERTISE")
        sleep(0.25)
        data = mytest.dut.confirm_message("ADVERTISE_SUCCESSFULL")
        if data:
            print(f"====>Advertisement for DIS Application Successfully")
            print(f" Testcase Passed")
            filepath = os.path.join(os.getcwd(), './Testcase/json_report')
            with open(filepath, 'w') as fptr:
                list = [
                    {
                        "Results": "PASS",
                        "Test Name": "Advertise"
                    }]
                json_object = json.dumps(list, indent=4)
                fptr.write(json_object)
            return True

        else:
            print("====>Sorry There is some issue in Staring Advertisement")
            print("====>Testcase Failed")
            filepath = os.path.join(os.getcwd(), './Testcase/json_report')
            with open(filepath, 'w') as fptr:
                list = [
                    {
                        "Results": "FAIL",
                        "Test Name": "Advertise"
                    }]
                json_object = json.dumps(list, indent=4)
                fptr.write(json_object)
            self.result_advertise = False
            mytest.cleanup()
            return False


if __name__ == "__main__":

    sys.path.append(os.getcwd())
    mytest = AdvertiseTest()
    adver_res = mytest.run()