"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  IT      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
def status_of(percent): 
    """This function returns the status based on the percentage worked out"""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"

def check(value, limit):
    """Works out the difference and percent and returns the values"""
    difference = limit - value
    percent = value / limit * 100
    return difference, percent

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

# ==================================================================== INPUT
count = 0

while True:
    label = input("Enter the hostname: ")
    if label == "quit":
        break
    value = float(input("Enter used GB: "))
    limit = float(input("Enter total GB: "))
    difference, percent = check(value, limit)
    status = status_of(percent)

    if status == "OVER LIMIT":
        count += 1

    print_report(label, value, limit, difference, percent, status)

print(f"Records over the limit: {count}")


# ==========================================================================
# 5. Before you finish:
#
#    With a total of 0, the error that comes up is that it can't divide by o.
