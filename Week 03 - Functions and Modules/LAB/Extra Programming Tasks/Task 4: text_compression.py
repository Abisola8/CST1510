"""
## Task 4: Text Compression
Write a Python function called `compress_string` that takes a string as input and returns a compressed version of the string. The compression should replace repeated characters with the character followed by the count of repetitions. If the compressed string is longer than the original string, return the original string.

```python
compressed = compress_string("aaabbbbcccddeee")
# The expected output is "a3b4c3d2e3" because 'a' is repeated 3 times, 'b' 4 times, 'c' 3 times, etc.
compressed = compress_string("Hello")
# The expected output is "Hello", because the compressed string in this case H1e1l2o1 is longer than the original string "Hello"
"""
def compress_string(text):
    if text == "":
        return text

    compressed = ""
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            compressed += text[i - 1] + str(count)
            count = 1

    compressed += text[-1] + str(count)

    if len(compressed) < len(text):
        return compressed
    else:
        return text
    
print(compress_string("aaabbbbcccddeee"))
print(compress_string("Hello"))