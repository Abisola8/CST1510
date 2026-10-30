"""## Task 11: Population Projection (5 Years)
Assume current population is 312032486 and 1 year = 365 days.
Rates: birth every 7s, death every 13s, immigrant every 45s.
Compute projected population for each of the next 5 years using integer division (`//`).

**Example Output:**
```
Year 1: 315,xxx,xxx
...
Year 5: ...
```
*Optional hint:* Compute yearly net change once; then add each year."""

current_pop = 312032486
seconds_per_year = 365 * 24 * 60 * 60

births = seconds_per_year // 7
deaths = seconds_per_year // 13
immigrants = seconds_per_year // 45

change = births + immigrants - deaths

population = current_pop
for year in range(1, 6):
    population += change
    print(f"Year {year}: {population}")