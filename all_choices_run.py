

```python
import os

theTopScript = None

def set_top_script(top_script):
    global theTopScript
    theTopScript = top_script

def get_top_script():
    global theTopScript
    return theTopScript

def run_choice(choice):
    try:
        # Run the choice
        os.system(f"python {choice}")
    except Exception as e:
        print(f"Error running choice: {choice}. Error: {str(e)}")

def all_choices_run():
    if theTopScript is None:
        print("Top script not set")
        return

    if not os.path.exists(theTopScript):
        print("Top script file does not exist")
        return

    # Get all choices from the top script
    choices = get_choices_from_top_script(theTopScript)

    # Run all choices
    for choice in choices:
        run_choice(choice)

def get_choices_from_top_script(top_script):
    try:
        with open(top_script, 'r') as file:
            lines = file.readlines()
            choices = [line.strip() for line in lines if line.strip().endswith('.py')]
            return choices
    except Exception as e:
        print(f"Error reading top script file: {str(e)}")
        return []

if __name__ == "__main__":
    set_top_script("top_script.py")
    all_choices_run()
```