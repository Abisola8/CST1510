"""
## Task 9: System Info Banner
Ask for a hostname and print OS and Python version as a simple banner (one value per line).

**Example Output:**
```
Host: server01
OS: Linux
Python: 3.11.5
```
*Optional hint:* `import platform; platform.system(); platform.python_version()`
"""
import platform

hostname = input("Enter a hostname: ")
print(f"Host: {hostname}")
print(f"OS: {platform.system()}")
print(f"Python: {platform.python_version()}")