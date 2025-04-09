

package crc.pop

def pop(lst, nth):
    try:
        if nth < 0 or nth >= len(lst):
            raise IndexError("Index out of range")
        element = lst[nth]
        lst[:] = lst[:nth] + lst[nth+1:]
        return element
    except Exception as e:
        raise e