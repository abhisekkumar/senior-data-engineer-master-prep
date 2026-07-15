# Interview Questions

> Publication note: reorganized as an educational template. Employer-specific details are removed; all scenarios, metrics, and identifiers are fictionalized placeholders and are not claims about the maintainer's employment.

First call with VP
Second call with engineering
Third call for coding Interview
Fourth call for onsite

## 1. What Types Of Integrations Have You Built?
At a fictionalized healthcare organization, most integrations involved healthcare operational systems and enterprise analytics platforms.

Examples include:

* SQL Server → Spark → Snowflake
* Provider systems → Enterprise Data Platform
* Claims systems → Analytics
* Eligibility systems → Reporting
* Clinical datasets → Data Science platforms

Although I wasn't directly integrating with EHR like Epic or Cerner, the core integration challenges were very similar:

* Schema evolution
* Incremental loading
* Batch processing
* Data quality
* Reconciliation
* Governance
* Reliability

2. Design A Healthcare Integration

Let's pretend: Adonis signs a new customer.
Customer uses Epic.

## How would you integrate Epic into our platform?

Step 1: Understand Source
Questions:
## * API?
## * HL7?
## * FHIR?
## * Batch?
## * CDC?

Step 2: Data Contracts
## What data?
* Patients
* Encounters
* Providers
* Billing
* Appointments

Step 3: Ingestion Layer
Land raw data.
Bronze.
No transformations.
Preserve history.

Step 4: Validation Layer
Check:
* Nulls
* Duplicates
* Schema drift
* Required fields

Step 5: Transformation Layer
Silver:
Normalize.
Standardize.
Clean.
Deduplicate.

Step 6: Business Layer
Gold.
Generate:
* Provider metrics
* Revenue metrics
* Operational metrics

Step 7: Consumption
* Product
* Analytics
## * Ai
* Reporting

## 3. What Types Of Integrations Have You Built?

At a fictionalized healthcare organization, most integrations involved healthcare operational systems and enterprise analytics platforms.

Examples include:

* SQL Server → Spark → Snowflake
* Provider systems → Enterprise Data Platform
* Claims systems → Analytics
* Eligibility systems → Reporting
* Clinical datasets → Data Science platforms

Although I wasn't directly integrating with Epic or Cerner, the core integration challenges were very similar:

* Schema evolution
* Incremental loading
* Data quality
* Reconciliation
* Governance
* Reliability

## 4. What Is The Hardest Part Of Healthcare Integrations?

The hardest challenge is usually not moving data.
It's ensuring the data is accurate, complete, consistent, and trustworthy.
Healthcare systems often have differing standards, missing values, schema variations, and business rule differences.
Building strong validation and reconciliation processes is usually more important than the ingestion itself.

## 5. How Do You Handle Schema Changes?

I generally try to separate ingestion from business logic.
New fields should flow through ingestion automatically whenever possible.
Schema validation identifies breaking changes.
Metadata-driven pipelines and versioned transformations help absorb source-system evolution without impacting downstream consumers.

6. Case Study 1:
Suppose Adonis signs a new hospital system using Epic.
Walk me through how you would design the integration from the moment the customer signs until the data is available for analytics.

Business Requirements -> Source Analysis -> Data Contract -> Bronze -> Validation -> Silver -> Gold -> Consumption -> Monitoring

Step 1: Understand The Integration Requirements
Before touching technology, I would understand:

## * What business problem are we solving?
## * What Epic data do we need?
## * Expected volume?
## * Refresh frequency?
## * Near real-time vs batch?
## * HIPAA requirements?
## * SLA expectations?

Step 2: Understand How Epic Exposes Data

I would identify whether Epic provides data through:

* FHIR APIs
* HL7 interfaces
* Flat file exports
* CDC feeds
* Vendor-managed integrations

The ingestion strategy depends on the source capabilities.

Step 3: Establish A Data Contract

Before ingestion I would define:

* Required entities
    * Patients
    * Providers
    * Encounters
    * Appointments
    * Clinical records
* Required fields
* Data ownership
* Quality expectations
* Schema versioning approach

This prevents downstream ambiguity.

Step 4: Bronze Layer

Raw ingestion.

Goals:

* Preserve source fidelity
* Preserve history
* Enable replay capability
* Support auditing

I generally avoid transformations here.

Step 5: Validation Layer

I would validate:

* Schema compatibility
* Required fields
* Null rates
* Duplicate records
* Referential integrity
* Record counts

I would also implement reconciliation against source-system totals.

Step 6: Silver Layer

Standardization.

Examples:

* Normalize patient identifiers
* Standardize provider identifiers
* Resolve code mappings
* Deduplicate records
* Handle schema evolution

This creates a trusted integration layer.

Step 7: Gold Layer

Create business-ready datasets:

* Revenue cycle metrics
* Provider performance
* Patient activity
* Operational KPIs
* AI-ready datasets

Step 8: Consumption

Support:

* Product features
* Analytics
* Reporting
* Machine Learning
* AI workflows

Step 9: Monitoring

I would implement:

* Data quality monitoring
* SLA monitoring
* Pipeline observability
* Alerting
* Reconciliation reporting

Follow-Up Question:

You're Adonis.
You onboarded a new hospital.
Three weeks later the hospital says:
“The patient count in Adonis is 2 million, but Epic shows 2.2 million.”

## What would you do?

Validate definition → isolate layer → inspect common failure modes → quantify impact → fix/backfill → prevent recurrence.

I would first avoid assuming the issue is in our platform.
I'd start with reconciliation between Epic/source counts and Adonis counts using the same date range, patient definition,
filters, and active/inactive criteria.

Then I'd isolate where the drop happened: source extract, Bronze ingestion, Silver deduplication/standardization,
or Gold business logic.

I'd check whether the missing [illustrative scale] were excluded because of watermark logic,
timestamp boundaries, failed batches, schema changes, null required fields, duplicate
logic, patient status filters, or identifier-mapping issues.

I'd also compare record counts by load date, facility, patient status, and source file/API response to narrow the gap.

Once identified, I'd either backfill the missing records, fix the transformation rule,
or update the data contract if the source definition changed. I'd communicate the root cause, impact, fix,
and prevention plan to stakeholders.

Next Question:
What if the 200K difference is because Epic includes inactive/deceased/test patients,
but Adonis only includes active billable patients? How would you handle that with Product and Engineering?

I'd confirm that this is a definition mismatch, not a data loss issue.
If Bronze has all [illustrative scale] and Silver/Gold only has 2M active billable patients,
then the pipeline is behaving as designed.
I'd explain to Product and Engineering that Epic's count includes inactive, deceased,
or test patients, while Adonis product metric is based on active billable patients.
Then I'd recommend making this explicit in the data contract and product documentation:

* raw_patient_count
* active_billable_patient_count
* exclusion rules
* patient status logic
* where the filter is applied

If Product wants visibility into inactive patients, we can expose a separate Gold dataset
or metric rather than changing the core patient definition.
This is a semantic definition mismatch, not necessarily a data quality issue.
