"""## Task 5: Total Time to Watch a Series
Compute total viewing time (no breaks) for a series:
- 5 seasons, 10 episodes per season
- Season 1: 45 minutes 35 seconds per episode
- Seasons 2–5: 35 minutes 15 seconds per episode

Display the total as hours, minutes, and seconds.

**Example Output:**
```
Total time: 39h 30m 0s"""

season_episodes = 10
season_1_episode = 45 * 60 + 35
other_season_episode = 35 * 60 +15

total_seconds = (season_episodes * season_1_episode) + (4 * season_episodes * other_season_episode)

hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print(f"Total time: {hours}h {minutes}m {seconds}s")