-- Keep the most recent synthetic record for each normalized email.
WITH ranked AS (
    SELECT
        user_id,
        email,
        created_at,
        ROW_NUMBER() OVER (
            PARTITION BY LOWER(TRIM(email))
            ORDER BY created_at DESC, user_id DESC
        ) AS recency_rank
    FROM users
)
SELECT user_id, email, created_at
FROM ranked
WHERE recency_rank = 1;

-- Rows that would be removed by the same rule.
WITH ranked AS (
    SELECT
        user_id,
        email,
        created_at,
        ROW_NUMBER() OVER (
            PARTITION BY LOWER(TRIM(email))
            ORDER BY created_at DESC, user_id DESC
        ) AS recency_rank
    FROM users
)
SELECT user_id, email, created_at
FROM ranked
WHERE recency_rank > 1;
