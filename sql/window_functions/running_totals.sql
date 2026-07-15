-- Cumulative value and a three-day moving average.
SELECT
    account_id,
    event_date,
    amount,
    SUM(amount) OVER (
        PARTITION BY account_id ORDER BY event_date
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_total,
    AVG(amount) OVER (
        PARTITION BY account_id ORDER BY event_date
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS three_day_moving_average
FROM account_events;
