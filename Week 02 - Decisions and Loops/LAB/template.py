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

# ==================================================================== INPUT
# 1. Ask for your three values.
#
while True:
    name = input("Enter hostname: ")
    if name == "quit":
        break
    used = float(input("Enter used GB: "))
    total = float(input("Enter total GB: "))

    # ================================================================== PROCESS
    # 2. Work out the difference and the percentage.       [Typical and above]

    difference = total - used
    percent = (used / total) * 100

    if percent >= 100:
        status = "OVER LIMIT"

    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    # =================================================================== OUTPUT
    # 4. Print the report.
    #
    #    Threshold : the three values you were given, plus status, inside a border
    #    Typical   : add difference and percent, 2 decimal places, right-aligned
    #    Excellent : wrap sections 1-4 in a loop so you can check as many records
    #                as you like in one run - type "quit" as the label to stop.
    #                Keep count of how many came back OVER LIMIT and print that
    #                once, after the loop ends.

    print("=" * 34)
    print(f"  RECORD CHECK  -  {name}")
    print("=" * 34)

    print(f"USED     : {used:>10.2f} GB")
    print(f"TOTAL    : {total:>10.2f} GB")
    print(f"FREE     : {difference:>10.2f} GB")
    print(f"PERCENT  : {percent:>10.2f} %")
    print(f"STATUS   : {status:>10}")

    print("=" * 34)


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds
