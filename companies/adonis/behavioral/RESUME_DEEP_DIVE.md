# Resume Deep Dive

> Publication note: reorganized as an educational template. Employer-specific details are removed; all scenarios, metrics, and identifiers are fictionalized placeholders and are not claims about the maintainer's employment.

Topic 1: Tell Me About Yourself

Why They Ask
This isn't an icebreaker.
The hiring manager wants to know:

## * Can you communicate clearly?
## * Are you technical?
## * Do you understand the business?
## * Are you a platform engineer or just someone who writes Spark jobs?

I'm a senior data engineer with [illustrative scale] of experience desinging and building large healthcare data
platforms. My background has been primarily been in regulated healthcare environment, where I've worked across
claims, eligibility, provider and clinical data domains.

At a fictionalized healthcare organization, I've own the architecture, ingestion, transformations, goverance, and data quality frameworks that
process [illustrative record volume]. One of my primary focuses is replacing fragmented
one-off pipelines with reusable platform capabilities, including metadata driver ingestion, medallion architecture,
schema evolution and goverance frameworks.

A few examples include designing an incremental ingestion framework that reduced processing time from [illustrative scale]
to [illustrative scale], building a metadata-driven PHI governance solution in Snowflake that supported [illustrative scale] while saving approximately [cost-impact metric], and establishing platform-wide data quality standards
that significantly reduced downstream production issues.

What excites me about Adonis is that it's solving healthcare problems closer to the operational side of the business.
Rather than only building internal platforms, I'd have the opportunity to work on integrations, healthcare
interoperability, and AI-ready data systems that directly improve healthcare operations.

Topic 2: Walk Me Through Your Current Team

I'm part of a healthcare data engineering organization responsible for building and maintaining enterprise
data platforms.
I work closely with product owners, business analysts, data scientists, reporting teams, architects,
compliance teams, and downstream consumers.

My responsibilities include designing ingestion frameworks, improving platform architecture, establishing
governance standards, implementing data quality controls, optimizing Spark and Snowflake workloads,
and mentoring engineers.

I also participate in architecture discussions, production support, and roadmap planning for new
healthcare datasets and platform capabilities.

Topic 3: Explain Your Ingestion Framework

Business Problem:
Initially, every source system had its own ingestion logic.
Some pipelines performed full-refresh loads, others had custom transformations,
and operational maintenance became increasingly difficult.
The result was long execution times, duplicated logic, and inconsistent onboarding of new datasets.

Solution:
I designed a metadata-driven ingestion framework.

Instead of building custom logic for every source system, the framework stored metadata describing:

* Source system
* Tables
* Primary keys
* Watermark columns
* Load strategy
* Validation rules
* Destination mappings

The ingestion engine interpreted this metadata and automatically generated the appropriate ingestion workflow.
Benefits:
* Standardized onboarding
* Less duplicated code
* Faster development
* Easier maintenance
* Consistent monitoring
* Reusable framework

## Why Metadata Driven?

Because new datasets could be onboarded by updating metadata rather than writing new ingestion logic.
This reduced engineering effort while improving consistency and maintainability across the platform.

## Topic 4: Why Incremental Instead of Full Refresh?

Full-refresh processing becomes inefficient as datasets grow.
Most healthcare datasets only change incrementally.

Processing only new or modified records significantly reduces:
* Compute costs
* Network traffic
* Processing time

while improving operational efficiency.

Follow-Up
## What if Incremental Processing Misses Records?

I don't rely solely on timestamps.
I implement overlapping extraction windows or configurable lookback periods.
Combined with merge operations and reconciliation checks, this ensures late-arriving
records are captured without introducing duplicates.

Topic 5: Explain Medallion Architecture
We organized our platform into Bronze, Silver, and Gold layers.

Bronze:
Raw data.
No significant transformations.
Preserve source history.
Support replay and auditing.

Silver:
Standardization.
Activities include:
* Data cleansing
* Deduplication
* Schema validation
* Business rule enforcement
* Identifier normalization
This becomes the trusted integration layer.

Gold:
Business-ready datasets.
Consumed by:
* Analytics
* Reporting
* Machine Learning
* Product teams

Separating these layers improves governance, debugging, and reprocessing while allowing downstream
consumers to rely on consistent, curated datasets.

Interviewer's Follow-Up:
## Why not transform everything directly into Gold?

Because each layer serves a distinct purpose.
Bronze preserves source fidelity and enables replay.
Silver standardizes and validates data independently of business use cases.
Gold contains business-specific models and metrics.
Keeping these concerns separate improves traceability, reuse, and operational resilience.

Topic 6: Schema Evolution

## How do you handle schema evolution?

Schema evolution is inevitable, especially when integrating multiple healthcare systems.
I try to isolate schema changes from business logic.
New columns should flow into the Bronze layer with minimal disruption.
Validation detects incompatible schema changes, while downstream transformations evolve
independently using metadata-driven mappings or versioned logic.
This minimizes disruption to consumers and supports backward compatibility.
