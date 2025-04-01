

```python
# test_initializer.py

TestModus = False
theTestFileList = []

def append_test(theTestFileList, testFile, comment):
    if not isinstance(theTestFileList, list):
        raise TypeError("theTestFileList must be a list")
    if not isinstance(testFile, str):
        raise TypeError("testFile must be a string")
    if not isinstance(comment, str):
        raise TypeError("comment must be a string")
    try:
        theTestFileList.append({"testFile": testFile, "comment": comment})
    except Exception as e:
        print(f"An error occurred: {e}")

append_test(theTestFileList, "test_file_1.txt", "This is a test file")
append_test(theTestFileList, "test_file_2.txt", "This is another test file")

print(theTestFileList)
```