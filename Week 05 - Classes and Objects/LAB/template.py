"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  : IT      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS
# 1. Define a class called Record.

class Record:
    def __init__(self, label, value, limit):
        """Stores the label, value and limit for each record"""
        self.label = label
        self.value = float(value)
        self.limit = float(limit)

    def status(self):
        """Returns the status of each record"""
        percent = (self.value / self.limit) * 100
        if percent >= 100:
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"

over_limit_count = 0

# ==================================================================== RECORDS
# 2. Create your records.

def load_records(path):
    """Reads a file and returns the label, value and limit for each record"""
    records = []
    with open(path, "r") as f:
        for line in f:
            if line.strip():
                label, value, limit = line.strip().split(",")
                records.append(Record(label, value, limit))
    return records

records = load_records("record_data.txt")

# ==================================================================== OUTPUT
# 3. Print a report for each record.

for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)

    # your report lines go here
    print(f" Value : {record.value}")
    print(f" Limit : {record.limit}")
    print(f" Status: {record.status()}")

    print("=" * 34)

    if record.status() == "OVER LIMIT":
        """Counts the number of records that are over the limit"""
        over_limit_count += 1

    print(f"{over_limit_count} of {len(records)} records are over the limit.")
# ==========================================================================

