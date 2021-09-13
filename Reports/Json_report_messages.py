import json

class JsonMessages:

    def __init__(self, filepath):
        self.file_path = filepath

    def advertise_pass(self):
        with open(self.file_path, 'w') as fptr:
            list = [
                {
                    "Results": "PASS",
                    "Test Name": "Advertise"
                }]
            json_object = json.dumps(list, indent=4)
            fptr.write(json_object)

    def advertise_fail(self):
        with open(self.file_path, 'w') as fptr:
            list = [
                {
                    "Results": "PASS",
                    "Test Name": "Advertise"
                }]
            json_object = json.dumps(list, indent=4)
            fptr.write(json_object)

    def connect_pass(self):
        with open(self.file_path, 'w') as fptr:
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

    def connect_fail(self):
        with open(self.file_path, 'w') as fptr:
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

    def disconnect_pass(self):
        with open(self.file_path, 'w') as fptr:
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

    def disconnect_fail(self):
        with open(self.file_path, 'w') as fptr:
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

    def all_fail(self):
        with open(self.file_path, 'w') as fptr:
            list = [
                {
                    "Results": "FAIL",
                    "Test Name": "Advertise"
                },
                {
                    "Results": "FAIL",
                    "Test Name": "Connect"
                },
                {
                    "Results": "FAIL",
                    "Test Name": "Disconnect"
                }
            ]
            json_object = json.dumps(list, indent=4)
            fptr.write(json_object)
if __name__ == "__main__":

    pass
