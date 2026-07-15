from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
START = "<!-- architecture-overview:start -->"
END = "<!-- architecture-overview:end -->"

DIAGRAMS = {
    "docs/system_design/CDC_AND_CHANGE_DATA_CAPTURE.md": (
        "Change Data Capture Flow",
        """flowchart LR
    A[Source database] --> B[Transaction log]
    B --> C[CDC connector]
    C --> D[Event stream]
    D --> E[Raw immutable storage]
    E --> F[Validated current-state table]
    D --> G[Real-time consumers]
    F --> H[Analytics and reporting]
    C -. schema and offset state .-> I[Checkpoint store]""",
        "Use log-based CDC when low source impact and ordered changes matter. Discuss deletes, schema evolution, replay, idempotency, ordering, and checkpoint recovery.",
        "At-least-once delivery requires idempotent consumers; exactly-once claims must define the boundary precisely.",
    ),
    "docs/system_design/DATA_PLATFORM.md": (
        "Layered Data Platform",
        """flowchart LR
    A[Operational sources] --> B[Batch and streaming ingestion]
    B --> C[Raw / Bronze]
    C --> D[Validated / Silver]
    D --> E[Curated / Gold]
    E --> F[BI and analytics]
    E --> G[ML and AI]
    E --> H[Data products]
    I[Catalog, lineage, quality, security] -. governs .-> B
    I -. governs .-> C
    I -. governs .-> D
    I -. governs .-> E""",
        "Separate immutable ingestion, validated canonical data, and consumer-oriented products. Make ownership, contracts, lineage, quality gates, and recovery explicit.",
        "Layer names are less important than clear responsibilities and enforceable interfaces.",
    ),
    "docs/system_design/ENTERPRISE_RAG_AND_GENAI.md": (
        "Enterprise RAG Architecture",
        """flowchart TD
    A[Approved enterprise sources] --> B[Extraction and parsing]
    B --> C[Chunking and metadata]
    C --> D[Embedding model]
    D --> E[Vector index]
    U[User question] --> F[Authentication and policy]
    F --> G[Query rewrite]
    G --> E
    E --> H[Authorized retrieval]
    H --> I[Prompt construction]
    I --> J[Language model]
    J --> K[Citations and guardrails]
    K --> L[Response]
    L -. feedback and evaluation .-> M[Observability]""",
        "A production RAG design must cover authorization before retrieval, source freshness, citations, evaluation, prompt-injection defense, latency, and cost.",
        "Retrieval quality and access control usually matter more than model size.",
    ),
    "docs/system_design/HEALTHCARE_ENCRYPTION_FRAMEWORK.md": (
        "Defense-in-Depth Encryption",
        """flowchart LR
    A[Client] -->|TLS| B[API gateway]
    B -->|TLS| C[Processing service]
    C -->|Encrypted write| D[Data store]
    E[Identity provider] -. short-lived identity .-> B
    F[Key management service] -. data encryption keys .-> C
    G[Secrets manager] -. credentials .-> C
    H[Audit log] -. records access .-> B
    H -. records key use .-> F
    I[Policy and classification] -. controls .-> D""",
        "Explain encryption in transit, at rest, and at field level alongside identity, key rotation, least privilege, auditability, retention, and incident response.",
        "Encryption does not replace authorization, data minimization, or monitoring.",
    ),
    "docs/system_design/KAFKA_DEEP_DIVE.md": (
        "Kafka Partition and Consumer Model",
        """flowchart LR
    P[Producers] --> T0[Topic partition 0]
    P --> T1[Topic partition 1]
    P --> T2[Topic partition 2]
    T0 --> C0[Consumer group member 0]
    T1 --> C1[Consumer group member 1]
    T2 --> C2[Consumer group member 2]
    T0 -. replicate .-> R0[Follower replica]
    T1 -. replicate .-> R1[Follower replica]
    T2 -. replicate .-> R2[Follower replica]
    C0 --> S[Checkpointed offsets]
    C1 --> S
    C2 --> S""",
        "Partition keys control ordering and data distribution. Consumer-group parallelism is bounded by partition count; replication provides availability, not consumer parallelism.",
        "Discuss skew, rebalancing, retention, replay, idempotency, delivery semantics, and dead-letter handling.",
    ),
    "docs/system_design/REAL_TIME_DASHBOARD.md": (
        "Real-Time Dashboard Pipeline",
        """flowchart LR
    A[Event producers] --> B[Message broker]
    B --> C[Stream processing]
    C --> D[Real-time aggregate store]
    C --> E[Durable object storage]
    D --> F[Query API]
    F --> G[Dashboard]
    E --> H[Backfill and recomputation]
    H --> D
    I[Metrics and alerts] -. observes .-> B
    I -. observes .-> C
    I -. observes .-> F""",
        "Precompute bounded aggregates for predictable latency, retain raw events for replay, and define freshness and correctness service levels.",
        "Separate event-time correctness from dashboard refresh frequency.",
    ),
    "docs/system_design/REAL_TIME_FRAUD_DETECTION.md": (
        "Streaming Fraud Decision Path",
        """flowchart LR
    A[Transaction event] --> B[Schema validation]
    B --> C[Feature enrichment]
    C --> D[Rules engine]
    C --> E[Online model]
    D --> F[Decision service]
    E --> F
    F --> G{Risk decision}
    G -->|Allow| H[Complete transaction]
    G -->|Review| I[Case management]
    G -->|Block| J[Decline and alert]
    A --> K[Immutable event store]
    I -. labels .-> L[Offline training]""",
        "Optimize the synchronous path for latency while preserving explainability, feature freshness, fallback behavior, and human review.",
        "Discuss false positives, model drift, feedback delay, hot-key skew, and safe degradation.",
    ),
    "docs/system_design/REAL_TIME_STOCK_PRICES.md": (
        "Market Data Distribution",
        """flowchart LR
    A[Market feeds] --> B[Feed handlers]
    B --> C[Normalized event stream]
    C --> D[Latest-price cache]
    C --> E[Time-series store]
    C --> F[Aggregation service]
    D --> G[Quote API]
    F --> G
    G --> H[WebSocket gateway]
    H --> I[Clients]
    E --> J[Historical queries]
    K[Sequence-gap detector] -. monitors .-> C""",
        "Preserve symbol ordering, detect sequence gaps, separate latest-value serving from historical storage, and apply client backpressure.",
        "Market-data correctness requires explicit late, duplicate, and out-of-order event handling.",
    ),
    "docs/system_design/SPARK_SYSTEM_DESIGN.md": (
        "Spark Execution and Data Flow",
        """flowchart TD
    A[Driver] --> B[Logical plan]
    B --> C[Optimized physical plan]
    C --> D[Stages]
    D --> E1[Executor tasks]
    D --> E2[Executor tasks]
    E1 --> F[Shuffle boundary]
    E2 --> F
    F --> G1[Downstream tasks]
    F --> G2[Downstream tasks]
    H[Object storage / tables] --> E1
    H --> E2
    G1 --> I[Output tables]
    G2 --> I""",
        "Reason from the physical plan: partitioning, shuffle, skew, joins, serialization, memory pressure, and small files determine performance.",
        "Do not prescribe caching or repartitioning until the bottleneck is visible in the plan and metrics.",
    ),
    "docs/system_design/STOCK_TRADING_DATA_PLATFORM.md": (
        "Trading Data Platform",
        """flowchart LR
    A[Orders and executions] --> B[Event backbone]
    C[Reference and market data] --> B
    B --> D[Real-time validation]
    D --> E[Operational stores]
    B --> F[Immutable lakehouse]
    F --> G[Curated positions and P&L]
    G --> H[Risk and compliance]
    G --> I[Analytics]
    E --> J[Low-latency APIs]
    K[Reconciliation] -. compares .-> E
    K -. compares .-> G""",
        "Separate low-latency operational state from replayable analytical history, then reconcile them with stable event identifiers.",
        "Ordering, auditability, corrections, market calendars, and deterministic replay are core requirements.",
    ),
    "companies/adonis/system_design/METADATA_AND_ENCRYPTION.md": (
        "Metadata-Driven Secure Pipeline",
        """flowchart LR
    A[Source registry] --> B[Metadata configuration]
    B --> C[Generic ingestion engine]
    C --> D[Validation and classification]
    D --> E[Encrypted storage]
    F[Key management] -. keys .-> E
    G[Catalog and lineage] -. metadata .-> D
    H[Policy engine] -. access rules .-> E
    I[Audit events] <-->|observability| C""",
        "Use metadata to configure repeatable ingestion, but validate configuration and isolate security policy from pipeline code.",
        "A metadata-driven design still needs versioning, tests, safe rollout, and escape hatches.",
    ),
    "companies/adonis/system_design/SPARK.md": (
        "Spark Troubleshooting Loop",
        """flowchart TD
    A[Slow or failed job] --> B[Inspect Spark UI]
    B --> C{Dominant symptom}
    C -->|Skew| D[Salt, rebalance, or change join]
    C -->|Large shuffle| E[Filter early and improve partitioning]
    C -->|Memory pressure| F[Reduce state and tune partitions]
    C -->|Small files| G[Compact and control output]
    D --> H[Measure again]
    E --> H
    F --> H
    G --> H
    H --> B""",
        "Diagnose from stage and task metrics before tuning. Compare median and tail tasks, shuffle volume, spill, input size, and executor failures.",
        "Every proposed optimization should name the observed bottleneck and expected metric change.",
    ),
    "companies/adonis/platform_coding/DEDUPLICATION.md": (
        "Deterministic Deduplication",
        """flowchart LR
    A[Incoming records] --> B[Validate business key]
    B --> C[Partition by key]
    C --> D[Order by event time and tie-breaker]
    D --> E[Keep winning row]
    D --> F[Quarantine duplicates and conflicts]
    E --> G[Curated output]
    F --> H[Quality metrics]""",
        "Define the winner deterministically and retain enough evidence to explain discarded records.",
        "A plain distinct operation is insufficient when duplicate rows disagree.",
    ),
    "companies/adonis/platform_coding/INCREMENTAL_CDC.md": (
        "Incremental CDC Merge",
        """flowchart LR
    A[CDC batch] --> B[Validate sequence and operation]
    B --> C[Deduplicate within batch]
    C --> D{Operation}
    D -->|Insert| E[Insert row]
    D -->|Update| F[Update current row]
    D -->|Delete| G[Delete or tombstone]
    E --> H[Advance checkpoint]
    F --> H
    G --> H
    H --> I[Audit counts]""",
        "Apply changes idempotently and advance checkpoints only after a durable successful merge.",
        "Handle deletes, replay, out-of-order changes, schema evolution, and partial failure explicitly.",
    ),
    "companies/adonis/platform_coding/MERGE_REFERENCE_FEED.md": (
        "Reference Feed Merge",
        """flowchart LR
    A[New reference feed] --> B[Schema and quality checks]
    B --> C[Normalize business keys]
    C --> D[Compare with current dimension]
    D --> E[Insert new keys]
    D --> F[Update changed attributes]
    D --> G[Retain or expire missing keys]
    E --> H[Published dimension]
    F --> H
    G --> H""",
        "Decide whether absence means deletion, late delivery, or no change before merging a reference feed.",
        "State the slowly changing dimension policy and deterministic change-detection rule.",
    ),
    "companies/adonis/platform_coding/WATERMARKS.md": (
        "Watermark and Late-Data Handling",
        """flowchart LR
    A[Events] --> B[Read event time]
    B --> C{Within watermark?}
    C -->|Yes| D[Update window state]
    C -->|No| E[Late-data policy]
    E --> F[Drop with metric]
    E --> G[Quarantine]
    E --> H[Correction / backfill]
    D --> I[Finalize eligible windows]
    J[Checkpoint] -. restores .-> D""",
        "Choose a watermark from observed lateness and business tolerance, not convenience.",
        "Explain how finalized results are corrected when materially late data still arrives.",
    ),
    "companies/adonis/domain/HEALTHCARE_INTEGRATION.md": (
        "Healthcare Integration Boundary",
        """flowchart LR
    A[Clinical and administrative systems] --> B[Secure integration layer]
    B --> C[Standards normalization]
    C --> D[Identity and consent controls]
    D --> E[Validated canonical records]
    E --> F[Operational workflows]
    E --> G[Analytics]
    H[Audit, lineage, and quality] -. governs .-> B
    H -. governs .-> E""",
        "Use public interoperability concepts and synthetic examples. Address consent, minimum necessary access, identity resolution, provenance, and data quality.",
        "Never place real patient data or protected health information in interview examples.",
    ),
}


def block(title: str, diagram: str, framing: str, tradeoff: str) -> str:
    return f"""{START}
## Architecture at a glance

```mermaid
{diagram}
```

### Interview framing

{framing}

> **Key trade-off:** {tradeoff}
{END}
"""


def enrich() -> None:
    for relative, details in DIAGRAMS.items():
        path = ROOT / relative
        content = path.read_text(encoding="utf-8")
        if START in content:
            before, remainder = content.split(START, 1)
            _, after = remainder.split(END, 1)
            content = before.rstrip() + "\n\n" + after.lstrip()
        lines = content.splitlines()
        insert_at = 1
        if len(lines) > 2 and lines[1] == "":
            insert_at = 2
        if len(lines) > insert_at and lines[insert_at].startswith("> Publication note:"):
            insert_at += 1
            if len(lines) > insert_at and lines[insert_at] == "":
                insert_at += 1
        addition = block(*details).splitlines()
        updated = lines[:insert_at] + addition + [""] + lines[insert_at:]
        path.write_text("\n".join(updated).rstrip() + "\n", encoding="utf-8")
    print(f"Enriched {len(DIAGRAMS)} documents with Mermaid architecture diagrams.")


if __name__ == "__main__":
    enrich()
