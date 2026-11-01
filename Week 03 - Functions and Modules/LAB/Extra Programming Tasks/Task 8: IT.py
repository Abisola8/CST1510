"""
## Task 8: IT: Path Decomposition Report
Ask for a file or directory path and print its absolute path, parent, name, stem, and suffix.

**Example Output:**
```
Absolute path: /home/user/project/service.log
Parent: /home/user/project
Name: service.log
Stem: service
Suffix: .log
```
*Optional hint:* `from pathlib import Path`
"""

from pathlib import Path

path = Path(input("Enter a file or directory path: "))

print(f"Absolute path: {path.resolve()}")
print(f"Parent: {path.resolve().parent}")
print(f"Name: {path.name}")
print(f"Stem: {path.stem}")
print(f"Suffix: {path.suffix}")