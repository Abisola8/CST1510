"""## Task 9: IT: INI-style Config Printer
Ask for three `key=value` pairs (via separate prompts) and print them as an INI block with indentation.

**Example Output:**
```
[config]
	max_connections = 200
	timeout = 30
	region = eu-west-2
```"""
max_connections = input("Enter max connections: ")
timeout = input("Enter timeout: ")
region = input("Enter region: ")

print(f"[config] \n\tmax connections = {max_connections} \n\ttimeout = {timeout} \n\tregion = {region}")