-- Compare each user's March 2026 average to the global March average.
WITH filtered AS (
    SELECT user_id, trade_amount
    FROM trades
    WHERE trade_date >= '2026-03-01' AND trade_date < '2026-04-01'
),
user_averages AS (
    SELECT user_id, AVG(trade_amount) AS user_average
    FROM filtered
    GROUP BY user_id
),
global_average AS (
    SELECT AVG(trade_amount) AS company_average
    FROM filtered
)
SELECT
    users.user_id,
    users.user_average,
    global_values.company_average,
    CASE
        WHEN users.user_average > global_values.company_average THEN 'higher'
        WHEN users.user_average < global_values.company_average THEN 'lower'
        ELSE 'same'
    END AS benchmark_status
FROM user_averages AS users
CROSS JOIN global_average AS global_values;
