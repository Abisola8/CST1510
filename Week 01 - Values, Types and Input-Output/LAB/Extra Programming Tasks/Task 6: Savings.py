"""## Task 6: Savings Projection (3 Years)
Compute final savings after 3 years given:
- Save £10 every week for 3 years
- Year 1 bonus: +£20 each week
- Every 2 weeks: −£0.50 (sister)

Assume 52 weeks per year; use arithmetic and augmented assignment; no conditionals.

**Example Output:**
```
Final savings after 3 years: £4689.50"""

weeks_each_year = 52
years = 3
total_weeks = weeks_each_year * years

savings = 0
savings += 10 * total_weeks
savings += 20 * weeks_each_year # for 1 year, bonus
savings -= 0.5 * (total_weeks // 2)

print(f"Final savings after 3 years: £{savings:.2f}")
