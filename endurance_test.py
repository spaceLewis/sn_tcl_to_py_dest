

import os
import json

class EnduranceTest:
    def __init__(self):
        self.ReadParameterFile_Endurancetest_ON = False
        self.parameter_data = []

    def ReplayParameterFileforEnduranceTest(self):
        if not self.ReadParameterFile_Endurancetest_ON:
            try:
                self.read_parameter_files()
                self.process_parameter_data()
                self.ReadParameterFile_Endurancetest_ON = True
            except Exception as e:
                print(f"An error occurred: {e}")

    def read_parameter_files(self):
        files = ['file1.json', 'file2.json', 'file3.json']
        for file in files:
            if os.path.exists(file):
                with open(file, 'r') as f:
                    data = json.load(f)
                    self.parameter_data.append(data)
            else:
                print(f"File {file} not found")

    def process_parameter_data(self):
        # Process the parameter data
        pass