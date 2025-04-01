

import os
import logging

class TestAppender:
    def __init__(self):
        self.tests = []
        self.logger = logging.getLogger(__name__)

    def append_test(self, test_file, description):
        if not isinstance(test_file, str) or not isinstance(description, str):
            self.logger.error("Invalid input type. Both test_file and description must be strings.")
            raise ValueError("Invalid input type. Both test_file and description must be strings.")
        if not os.path.isfile(test_file):
            self.logger.error("Test file does not exist.")
            raise FileNotFoundError("Test file does not exist.")
        try:
            self.tests.append({
                'test_file': test_file,
                'description': description
            })
        except Exception as e:
            self.logger.error(f"An error occurred while appending the test: {str(e)}")
            raise

    def get_tests(self):
        return self.tests

def main():
    appender = TestAppender()
    try:
        appender.append_test('test_file.py', 'This is a test file')
        print(appender.get_tests())
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR)
    main()