"""
Author : Asif Khan M Pathan
Test Automation Framework
"""
import json
from datetime import datetime


class JsonMessages:
    def __init__(self, filepath):
        self.file_path = filepath
        self.list_1 = []
        self.dict_1 = {}
        self.date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")

    def json_case(self, arg1, test_name):
        with open(self.file_path, 'a') as fptr:
            if arg1 is True:
                self.write_file(self.list_1, fptr, True, test_name)
            else:
                self.write_file(self.list_1, fptr, False, test_name)

    def write_file(self, arg1, arg2, arg3, arg4):
        if arg3 is True:
            self.dict_1 = {"Results": "PASS", "Test Name": arg4, "Time": self.date}
            arg1.append(self.dict_1.copy())
            json_object = json.dumps(arg1, indent=4)
            arg2.write(json_object)
        else:
            self.dict_1 = {"Results": "FAIL", "Test Name": arg4, "Time": self.date}
            arg1.append(self.dict_1.copy())
            json_object = json.dumps(arg1, indent=4)
            arg2.write(json_object)


if __name__ == "__main__":
    pass
