"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  IT     
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask the user for your three values.
#
hostname = input("Enter Hostname: ")
gb_used = float(input("Enter GB Used: "))
gb_total = float(input("Enter total GB: "))

# ================================================================== PROCESS
# 2. Work out what you were NOT given.       [Typical and above]
#
difference = gb_total - gb_used
percent = gb_used / gb_total * 100

# =================================================================== OUTPUT
# 3. Print the report.

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {hostname}")
print("=" * 34)

print(f"Used     : {gb_used:>10.2f}")
print(f"Total    : {gb_total:>10.2f}")
print(f"Free     : {gb_total - gb_used:>+10.2f}")
print(f"Percent  : {(gb_used / gb_total * 100):>10.2f} %")

print("=" * 34)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you
