"""## Task 7: Cyber: HTTP Log Composer
Ask for IP, method, path, status, and bytes, then print a single combined log line (Apache-style).

**Example Output:**
```
192.168.1.10 - "POST /auth" 401 512"""

ip = input("Enter IP address: ")
method = input("Enter method: ")
path = input("Enter path: ")
status = input("Enter status: ")
size = input("Enter bytes: ")

print(f'{ip} - "{method} {path}" {status} {size}')