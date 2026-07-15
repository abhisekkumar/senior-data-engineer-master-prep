-- Users active on at least three consecutive dates (SQL Server syntax).
WITH distinct_activity AS (
    SELECT DISTINCT user_id, activity_date
    FROM user_activity
),
numbered AS (
    SELECT
        user_id,
        activity_date,
        ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY activity_date) AS sequence_number
    FROM distinct_activity
),
islands AS (
    SELECT
        user_id,
        activity_date,
        DATEADD(day, -sequence_number, activity_date) AS island_key
    FROM numbered
)
SELECT
    user_id,
    MIN(activity_date) AS streak_start,
    MAX(activity_date) AS streak_end,
    COUNT(*) AS streak_days
FROM islands
GROUP BY user_id, island_key
HAVING COUNT(*) >= 3;
