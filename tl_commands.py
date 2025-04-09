

```python
import time

class TlError(Exception):
    pass

def TlPrint(message):
    print(message)

def TlWrite(param, value):
    if param is None:
        raise TlError("Param object is None")
    if not hasattr(param, 'value'):
        raise TlError("Param object does not have a 'value' attribute")
    if not isinstance(value, int) or value < 0 or value > 255:
        raise TlError("Invalid ASCII value")
    param.value = value

def doWaitForObject(param, value, timeout=10):
    if param is None:
        raise TlError("Param object is None")
    if not hasattr(param, 'value'):
        raise TlError("Param object does not have a 'value' attribute")
    start_time = time.time()
    while time.time() - start_time < timeout:
        if param.value == value:
            return True
        time.sleep(0.1)
    return False
```