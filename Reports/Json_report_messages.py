"""
Author : Asif Khan M Pathan
Test Automation Framework
"""

import json


class JsonMessages:
    def __init__(self, filepath):
        self.file_path = filepath
        self.list_1 = []
        self.dict_1 = {}
        self.adv = "Advertise"
        self.con = "Connect"
        self.dis = "Disconnect"
        self.sec = "Secure_connect"

    def advertise_message(self, args):
        with open(self.file_path, 'a') as fptr:
            if args is True:
                self.write_file(self.list_1, fptr, True, self.adv)
            else:
                self.write_file(self.list_1, fptr, False, self.adv)

    def connect_message(self, args):
        with open(self.file_path, 'a') as fptr:
            if args is True:
                self.write_file(self.list_1, fptr, True, self.con)
            else:
                self.write_file(self.list_1, fptr, False, self.con)

    def disconnect_message(self, args):
        with open(self.file_path, 'a') as fptr:
            if args is True:
                self.write_file(self.list_1, fptr, True, self.dis)
            else:
                self.write_file(self.list_1, fptr, False, self.dis)

    def secure_connect_messages(self, args):
        with open(self.file_path, 'a') as fptr:
            if args is True:
                self.write_file(self.list_1, fptr, True, self.sec)
            else:
                self.write_file(self.list_1, fptr, False, self.sec)

    def write_file(self, arg1, arg2, arg3, arg4):
        if arg3 is True:
            self.dict_1 = {"Results": "PASS", "Test Name": arg4}
            arg1.append(self.dict_1.copy())
            json_object = json.dumps(arg1, indent=4)
            arg2.write(json_object)
        else:
            self.dict_1 = {"Results": "FAIL", "Test Name": arg4}
            arg1.append(self.dict_1.copy())
            json_object = json.dumps(arg1, indent=4)
            arg2.write(json_object)


if __name__ == "__main__":
    pass
