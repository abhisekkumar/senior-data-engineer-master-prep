-- Time since the previous synthetic transaction.
WITH history AS (
    SELECT
        user_id,
        transaction_date,
        LAG(transaction_date) OVER (
            PARTITION BY user_id ORDER BY transaction_date
        ) AS previous_transaction_date
    FROM transactions
)
SELECT
    user_id,
    transaction_date,
    previous_transaction_date,
    DATEDIFF(day, previous_transaction_date, transaction_date) AS days_since_previous
FROM history;

-- Dates on which a synthetic stock price increased.
WITH prices AS (
    SELECT
        symbol,
        trade_date,
        price,
        LAG(price) OVER (PARTITION BY symbol ORDER BY trade_date) AS previous_price
    FROM stock_prices
)
SELECT symbol, trade_date, price
FROM prices
WHERE price > previous_price;
