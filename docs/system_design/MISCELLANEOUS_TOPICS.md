# Miscellaneous Topics

> Publication note: reformatted from private study notes. Employer-specific personal details and confidential context have been removed or generalized.

Real-time Stock Trading / Market Data Platform

Core architecture:
Users
  ↓
Load Balancer
  ↓
API Gateway
  ↓
Order Service / Market Data API
  ↓
Kafka
  ↓
Stream Processing: Spark/Flink
  ↓
Redis for latest prices
  ↓
Snowflake/Data Lake for history

For trading/order flow:
User Order
  ↓
API Gateway
  ↓
Auth/Risk Check
  ↓
Order Management System
  ↓
Execution Engine / Broker Router
  ↓
Exchange
  ↓
Trade Confirmation
  ↓
Kafka Event
  ↓
Ledger + Reporting + Analytics

Key senior talking points:
Low latency
Exactly-once or idempotent processing
Auditability
Replayability
Risk checks before execution
Backpressure handling
Data quality checks
Schema evolution
Monitoring and alerting

## If they ask: Spark pipeline is slow — how do you debug?

Say this:

I first identify whether the bottleneck is data skew, shuffle, memory pressure,
bad partitioning, expensive joins, small files, or inefficient transformations.
I check the Spark UI stages, task duration, shuffle read/write, spill to disk, executor memory,
skewed partitions, and DAG lineage.

Then actions:
1. Check Spark UI
2. Identify slow stage
3. Look for shuffle-heavy operations
4. Check data skew
5. Check partition count
6. Check file sizes
7. Optimize joins
8. Cache only if reused
9. Tune executor memory/cores
10. Validate output counts and data quality

## If they ask: How do you manage complex pipelines?

Answer:
I break the pipeline into clear layers: raw, cleaned, conformed, business-ready, and serving.
I avoid one giant transformation chain. I use modular functions, config-driven logic, intermediate checkpoints,
data quality gates, logging, lineage, and unit tests around each transformation.

Medallion Architecture:
Bronze/raw
Silver/cleaned
Gold/business metrics
Serving/API/reporting

## If they ask: How do you test Spark pipelines?
Unit tests for transformations
Schema validation
Row count checks
Null checks
Duplicate checks
Reconciliation against source
Golden dataset tests
Regression tests
End-to-end test in lower environment
Data quality checks before publish
