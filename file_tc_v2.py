

```python
import os
import logging

def fileTC_V2():
    global theTopScript
    theTopScript = "top_script.py"
    try:
        if os.path.exists(theTopScript):
            with open(theTopScript, 'r') as file:
                script = file.read()
                try:
                    exec(script)
                except SyntaxError as e:
                    logging.error(f"Syntax error in script: {e}")
        else:
            logging.error(f"File {theTopScript} not found")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

fileTC_V2()
```