# Behavioral Categories

> Publication note: reorganized as an educational template. Employer-specific details are removed; all scenarios, metrics, and identifiers are fictionalized placeholders and are not claims about the maintainer's employment.

Category 1: Incremental Ingestion Framework

Resume: Reduced processing from [illustrative scale] to [illustrative scale] using CDC and incremental processing.

Expect:
## How did you implement incremental processing?
## What column did you use?
## Timestamp or CDC?
## What happens if records arrive late?
## How do you backfill?
## How do you prevent duplicates?
## How do you recover from failures?

Source SQL Server -> Last Watermark Table -> Incremental Query -> Bronze -> Merge Logic -> Silver

Q: Tell me about your ingestion framework.

At a fictionalized healthcare organization, we had dozens of source systems generating healthcare data across claims,
provider, eligibility, and clinical domains.

Initially, many pipelines relied on full-refresh processing,
which caused long runtimes, excessive compute consumption, and operational complexity.

To address this, I designed a standardized ingestion framework that
leveraged change data capture principles and incremental processing.

The framework tracked watermarks, extracted only new or changed records,
validated incoming data, and merged changes into downstream datasets.

This reduced processing times from [illustrative scale] to [illustrative scale] while
significantly lowering compute consumption and improving reliability.

## Q: How do you handle late arriving data?
I avoid relying solely on current timestamps.
Typically, I use overlapping extraction windows or configurable lookback periods to capture late-arriving records.
Records are reconciled during merge operations to prevent duplication.
For critical systems, reconciliation checks validate source versus target counts to ensure completeness.

## Q: How do you prevent duplicates?
I use business keys or primary keys combined with merge logic.
Depending on the use case, duplicates are detected using:
* Composite business keys
* Hash comparisons
* Window functions
* Merge statements

Validation checks run before publishing data downstream.

Category 2: Data Quality Framework

Resume: Validation gates reduced incidents by [measurable percentage].

Expect:
## What validations?
## Where were they implemented?
## How many rules?
## Hard fail vs soft fail?
## What happens when validation fails?
## How do stakeholders know?

Strong answer:
* Schema validation
* Null checks
* Duplicate checks
* Referential integrity
* Count reconciliation
* Business rule validation

## Q: How do you ensure data quality?
Data quality should be enforced throughout the pipeline, not only at the end.

Our framework included:
* Schema validation
* Null validation
* Duplicate detection
* Referential integrity checks
* Record count reconciliation
* Business rule validation

Validation gates were implemented before data publishing.
If critical validations failed, the pipeline stopped and alerts were generated.
This significantly reduced downstream incidents.

## Q: What happens when validation fails?

The pipeline enters a failed state.
Alerts are sent to engineering teams.
The failed dataset is quarantined.
No downstream publication occurs until the issue is resolved.
This prevents bad data from propagating into analytics, reporting, or machine learning systems.

Category 3: PHI Governance

Expect:
## How does dynamic masking work?
## How did you store metadata?
## Why Snowflake?
## How were permissions managed?
## What challenges did you face?
## How did you save [cost-impact metric]?

You need a 5-minute architecture answer.

Q: Tell me about your PHI masking solution.

One of my largest initiatives was building a metadata-driven governance encryption platform in Snowflake.
Healthcare data contains sensitive information protected under HIPAA and are not allowed to share with
offshore users. this create an issue for other teams to consume uneven [measurable percentage] of the data.
Rather than manually maintaining access rules across hundreds of columns,
I designed a framework that stored masking policies as metadata for selective encryption.
The system dynamically applied masking rules based on:
* User role
* Geography
* Compliance requirements

This secured access for [illustrative scale] while reducing operational costs by approximately [cost-impact metric].

## Q: Why was this approach valuable?

It centralized governance logic.
Instead of updating permissions table-by-table, policy changes could be managed through metadata.
This improved compliance, reduced operational effort, and increased scalability.

Category 4: Medallion Architecture

a fictionalized healthcare organization uses Medallion.

Expect:
## Why Bronze/Silver/Gold?
## Why not one layer?
## What transformations belong in Silver?
## What transformations belong in Gold?
## How do you handle reprocessing?
## How do you handle schema evolution?

Q: Describe your Medallion Architecture.
Our healthcare platform followed a Bronze, Silver, and Gold architecture.

Bronze: Raw source data.
Goals:
* Preserve source fidelity
* Maintain history
* Support replay and auditing

Minimal transformations occur here.

Silver: Standardized data.

Activities:
* Data cleansing
* Deduplication
* Schema validation
* Business rule enforcement
* Data quality checks

This becomes the trusted integration layer.

Gold: Business-ready datasets.

Consumers include:
* Analytics
* Reporting
* Data Science
* Machine Learning
* Product applications

## Why not transform everything directly?
Layer separation improves:

* Traceability
* Governance
* Reusability
* Debugging
* Reproc

Category 5: Airflow

Resume: Airflow + KubernetesPodOperator.

Expect:
## Why Airflow?
## Why KPO?
## Why not SparkSubmitOperator?
## How do retries work?
## How do you monitor DAGs?
## How do you handle failures?
## How do you handle dependencies?

## Q: Why Airflow?

Airflow provides:

* Workflow orchestration
* Dependency management
* Scheduling
* Monitoring
* Retry handling

It allowed us to coordinate ingestion, transformation, validation, and publishing workflows.

## Q: Why KubernetesPodOperator?

KubernetesPodOperator provides workload isolation.
Benefits:
* Independent scaling
* Environment consistency
* Failure isolation
* Better resource utilization

Each workload executes in its own containerized environment.

Category 6: Data Modeling

Expect:How would you model:
* Patient
* Provider
* Encounter
* Appointment
* Claim

## Fact vs Dimension?
## Slowly Changing Dimensions?
## Surrogate Keys?
## Natural Keys?

## Q: How would you model healthcare data?

I typically separate dimensions and facts.

Dimensions:
Patient
Provider
Facility
Payer
Time

Facts:
Claims
Encounters
Appointments
Procedures
Payments

Why?

Dimensions describe entities.
Facts capture business events.

This structure supports analytics, reporting, and operational use cases.

Category 7: Stakeholder Management

Expect: Tell me about a disagreement.
Product wanted X, Engineering wanted Y.

## What did you do?
## Prioritization conflict?
## Deadline conflict?

Q: Tell me about a stakeholder conflict.

I start by understanding the underlying business objective rather than immediately discussing technical implementation.
In one situation, stakeholders wanted rapid delivery while engineering teams raised concerns about data quality risks.
I facilitated discussions around business impact, risk, and technical effort.
We agreed on a phased rollout that delivered value quickly while maintaining reliability.
The outcome satisfied both groups and reduced overall project risk.

Category 8: Leadership

Resume: Mentored engineers.

Expect:
## How many engineers?
## What did mentoring involve?
## Code reviews?
## Design reviews?
## Architecture standards?
## Difficult engineer?

Q: Tell me about mentoring engineers.

I regularly mentored engineers through:
* Code reviews
* Design reviews
* Architecture discussions
* Debugging sessions
* Platform best practices

My goal is to create reusable standards and help engineers make sound technical decisions independently.

## Q: What's your leadership style?

I lead through technical clarity, collaboration, and enablement.
I establish architectural direction while giving engineers autonomy in implementation.

Category 9: Spark

Expect:
Explain partitioning.
Explain skew.
Explain broadcast joins.
Explain shuffle.
Explain caching.
Explain adaptive query execution.
Explain a Spark performance issue you solved.

Q: Tell me about a Spark optimization.

One example involved large healthcare datasets where Spark jobs experienced long runtimes due to excessive shuffling.
I analyzed execution plans, identified skewed joins, and implemented:
* Partitioning improvements
* Broadcast joins
* Adaptive Query Execution
* Reduced shuffles
The result was improved runtime stability and reduced compute costs.

## Q: What causes Spark performance problems?

Common causes include:
* Data skew
* Excessive shuffling
* Poor partitioning
* Small files
* Wide transformations
* Incorrect join strategies

Category 10: Startup Adaptability

Expect:
## How would you work without perfect requirements?
## What if requirements change every week?
## What if product changes priorities?
## What if there are only 2 engineers?

Answer:
Ownership.
Pragmatism.
Speed.
Tradeoffs.

## Q: Why leave a large company?
I've enjoyed working at enterprise scale and learned a tremendous amount.
What excites me now is broader ownership.
I want to work closer to product decisions, customer challenges, and business
outcomes while helping shape architecture and engineering direction.

## Q: How do you handle ambiguity?
I focus on understanding the desired outcome first.
Then I make reasonable assumptions, validate them quickly, and iterate with stakeholders.
In startup environments, progress is often more valuable than waiting for perfect information.

## Questions:

1. Tell me about the healthcare systems you've integrated.

I've spent most of my career working with healthcare data across claims,
provider, eligibility, and clinical domains. My work involved integrating,
standardizing, validating, governing, and publishing healthcare datasets for analytics,
reporting, compliance, and machine learning use cases.

2. Walk me through your ingestion framework.

Business Requirements → Source Analysis → Data Contract → Bronze → Validation → Silver → Gold → Consumption → Monitoring
The framework standardized onboarding of new healthcare datasets while improving reliability and reducing operational
effort.

## 3. How do you handle schema evolution?

I separate ingestion from business logic.
New fields should flow through Bronze with minimal disruption.
Metadata-driven validation identifies breaking changes while downstream transformations evolve independently.
This minimizes impact to consumers.

## 4. How do you design a new integration?

Requirements → Source Analysis → Data Contract → Bronze → Validation → Silver → Gold → Monitoring → Consumption
The goal is not simply moving data but creating trusted, reliable, and governed datasets.

5. Tell me about your PHI masking solution.

I designed a metadata-driven governance framework in Snowflake that dynamically applied masking policies
based on role and geography.
The platform supported [illustrative scale] and reduced annual costs by approximately [cost-impact metric]

6. Describe your Medallion architecture.

Bronze preserves source history.
Silver standardizes and validates data.
Gold delivers business-ready datasets.
This improves traceability, governance, and reusability.

## 7. How do you ensure data quality?

Validation occurs throughout the pipeline using schema checks, null validation, duplicate detection, reconciliation,
referential integrity, and business rule validation.
Bad data never reaches consumers.

8. Tell me about a difficult stakeholder situation.

I focus on understanding business goals, communicating tradeoffs clearly, and
finding phased solutions that balance delivery speed with engineering reliability.

## 9. Why do you want a startup?

I bring a combination of healthcare domain expertise, large-scale data platform experience,
governance, integration architecture, stakeholder management, and technical leadership.
I've spent years building trusted healthcare systems that process billions of records
while maintaining compliance, reliability, and scalability. That experience aligns strongly
with the mission and technical challenges of Adonis.

## 10. Why are you the right fit for Adonis?

Adonis sits at the intersection of healthcare, data platforms, integrations, and operational intelligence.
My experience building healthcare data platforms aligns closely with the challenges Adonis is solving,
and I'm excited about having broader ownership in a high-growth environment.
