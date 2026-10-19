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

# =================================================================== FUNCTIONS

def check(value, limit):
    """Works out the difference, percent and status and returns the values"""
    difference = limit - value
    percent = value / limit * 100
    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"
    return difference, percent, status

def print_report(label, value, limit, difference, percent, status):
    """Prints the report lines"""
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f" Value:      {value:>10.2f}")
    print(f" Limit:      {limit:>10.2f}")
    print(f" Difference: {difference:>10.2f}")
    print(f" Percent:    {percent:>10.2f}")
    print(f" Status:     {status:>10}")
    print("=" * 34)

# ====================================================================== STORE
with open("records_file.txt", "w") as f:
    f.write("srv-01,87,120\n")
    f.write("srv-02,45,150\n")
    f.write("srv-03,120,80\n")

def load_records(path):
    records = []
    with open(path, "r") as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            records.append({"label": label, "value": float(value), "limit": float(limit)})         
    return records
    
records = load_records("records_file.txt")
print(records)
# =============================================================== PROCESS + OUTPUT

over_limit = 0

with open("records_results.txt", "w") as f:
    for r in records:
        difference, percent, status = check(r["value"], r["limit"])
        f.write(f"{r["label"]}, {status}\n")
        if status == "OVER LIMIT":
            over_limit += 1

print(f"Records over the limit: {over_limit}")

# ==========================================================================