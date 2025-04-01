

import os
import stat
import logging
import subprocess

theTopScript = "top_script.py"

def campaign_launching():
    try:
        # Check if the top script file exists
        if os.path.isfile(theTopScript):
            # Check if the top script file is executable
            if os.access(theTopScript, os.X_OK):
                # Check if the top script file is a Python file
                if theTopScript.endswith('.py'):
                    # Launch the campaign by executing the top script
                    subprocess.run(['python', theTopScript])
                else:
                    logging.error("Error: Top script file is not a Python file.")
            else:
                logging.error("Error: Top script file is not executable.")
        else:
            logging.error("Error: Top script file not found.")
    except Exception as e:
        logging.error("Error launching campaign: ", str(e))

if __name__ == "__main__":
    logging.basicConfig(level=logging.ERROR)
    campaign_launching()