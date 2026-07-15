from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "Senior Data Engineer Interview Prep"

MAPPINGS = {
    "Data_Structure_Algorithms/MasterRoadmap.txt": "docs/dsa/MASTER_ROADMAP.md",
    "Data_Structure_Algorithms/PatternRecognition.txt": "docs/pattern_recognition/PATTERN_RECOGNITION_NOTES.md",
    "Data_Structure_Algorithms/scratch.txt": "docs/dsa/SCRATCH_NOTES.md",
    "Python/ImportantPoints.txt": "docs/python/PYTHON_IMPORTANT_POINTS.md",
    "SQL_Interview/ImportantPoints.txt": "docs/sql/SQL_IMPORTANT_POINTS.md",
    "System_Design/CDC_Change_Delete_Capture.txt": "docs/system_design/CDC_AND_CHANGE_DATA_CAPTURE.md",
    "System_Design/Data_Platform.txt": "docs/system_design/DATA_PLATFORM.md",
    "System_Design/EnterpriseRAG_GEN_AI.txt": "docs/system_design/ENTERPRISE_RAG_AND_GENAI.md",
    "System_Design/HIPAA_EncryptionFramework.txt": "docs/system_design/HEALTHCARE_ENCRYPTION_FRAMEWORK.md",
    "System_Design/KafkaDeepDive.txt": "docs/system_design/KAFKA_DEEP_DIVE.md",
    "System_Design/Miscellaneous.txt": "docs/system_design/MISCELLANEOUS_TOPICS.md",
    "System_Design/RealTime_DashboardDesign.txt": "docs/system_design/REAL_TIME_DASHBOARD.md",
    "System_Design/Real_time_fraud_deteciton.txt": "docs/system_design/REAL_TIME_FRAUD_DETECTION.md",
    "System_Design/Real_time_stock_price.txt": "docs/system_design/REAL_TIME_STOCK_PRICES.md",
    "System_Design/Spark.txt": "docs/system_design/SPARK_SYSTEM_DESIGN.md",
    "System_Design/Stock_Trading_Data_Platform.txt": "docs/system_design/STOCK_TRADING_DATA_PLATFORM.md",
    "Companies/Adonis/Ask&Think.txt": "companies/adonis/interview_strategy/ASK_AND_THINK.md",
    "Companies/Adonis/ConsolidatePhaseChecklist.txt": "companies/adonis/checklists/CONSOLIDATED_PHASE_CHECKLIST.md",
    "Companies/Adonis/FastRecognitionSummary.txt": "docs/pattern_recognition/FAST_RECOGNITION_SUMMARY.md",
    "Companies/Adonis/PatternRecognition.txt": "docs/pattern_recognition/INTERVIEW_PATTERN_RECOGNITION.md",
    "Companies/Adonis/Program.txt": "companies/adonis/STUDY_PROGRAM.md",
    "Companies/Adonis/Cultural_Behavioral/Categorical.txt": "companies/adonis/behavioral/BEHAVIORAL_CATEGORIES.md",
    "Companies/Adonis/Cultural_Behavioral/HealtcareIntegration.txt": "companies/adonis/domain/HEALTHCARE_INTEGRATION.md",
    "Companies/Adonis/Cultural_Behavioral/Interview.txt": "companies/adonis/behavioral/INTERVIEW_QUESTIONS.md",
    "Companies/Adonis/Cultural_Behavioral/Leadership.txt": "companies/adonis/behavioral/LEADERSHIP.md",
    "Companies/Adonis/Cultural_Behavioral/MetadataEncryption.txt": "companies/adonis/system_design/METADATA_AND_ENCRYPTION.md",
    "Companies/Adonis/Cultural_Behavioral/ResumeDeepDive.txt": "companies/adonis/behavioral/RESUME_DEEP_DIVE.md",
    "Companies/Adonis/Cultural_Behavioral/Spark.txt": "companies/adonis/system_design/SPARK.md",
    "Companies/Adonis/DSA/Phase 2/Platform/Deduplication.txt": "companies/adonis/platform_coding/DEDUPLICATION.md",
    "Companies/Adonis/DSA/Phase 2/Platform/IncrementalCDC.txt": "companies/adonis/platform_coding/INCREMENTAL_CDC.md",
    "Companies/Adonis/DSA/Phase 2/Platform/MergeProviderFeed.txt": "companies/adonis/platform_coding/MERGE_REFERENCE_FEED.md",
    "Companies/Adonis/DSA/Phase 2/Platform/Watermarks.txt": "companies/adonis/platform_coding/WATERMARKS.md",
    "Companies/Adonis/DSA/Phase 6/Basics/HeapFunctions.txt": "docs/pattern_recognition/heap/HEAP_FUNCTIONS.md",
    "Companies/Adonis/DSA/Phase 6/Basics/HeapVsStackVsQueue.txt": "docs/pattern_recognition/heap/HEAP_VS_STACK_VS_QUEUE.md",
    "Companies/Adonis/DSA/Phase 6/Basics/MaxHeap.txt": "docs/pattern_recognition/heap/MAX_HEAP.md",
}

SENSITIVE_METRIC = re.compile(
    r"(?i)\b(?:over\s+|approximately\s+|about\s+)?\d[\d,.]*\s*"
    r"(?:[KMB]\s*)?(?:rows?|records?|patients?|members?|claims?|providers?|users?|files?|"
    r"tables?|datasets?|TB|GB|MB|hours?|minutes?|seconds?|days?)\b"
)
PRIVATE_TERMS_PATH = ROOT / "backups/private_terms.txt"
SENSITIVE_PERCENTAGE = re.compile(r"\b\d+(?:\.\d+)?\s*%")
SENSITIVE_MONEY = re.compile(
    r"\$\s*\d[\d,.]*(?:\s*(?:K|M|million|thousand))?(?:\s+(?:annually|per\s+year))?",
    re.IGNORECASE,
)
SENSITIVE_WORD_SCALE = re.compile(
    r"(?i)\b(?:over\s+|approximately\s+|about\s+)?"
    r"(?:zero|one|two|three|four|five|six|seven|eight|nine|ten)"
    r"(?:[\s-]+(?:zero|one|two|three|four|five|six|seven|eight|nine|ten|half|and|a))*\s+"
    r"(?:years?|hours?|minutes?|seconds?|days?|users?|records?|patients?|members?|claims?)\b"
)
SENSITIVE_WORD_RECORD_VOLUME = re.compile(
    r"(?i)\b(?:over\s+)?(?:one|two|three|four|five|six|seven|eight|nine|ten)\s+"
    r"billions?\s+(?:\w+\s+){0,2}records?(?:\s+every\s+month)?\b"
)


def title_for(destination: Path) -> str:
    return destination.stem.replace("_", " ").title().replace("Genai", "GenAI")


def private_terms() -> list[str]:
    if not PRIVATE_TERMS_PATH.is_file():
        return []
    return [
        line.strip()
        for line in PRIVATE_TERMS_PATH.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    ]


def sanitize(text: str, source_name: str = "") -> str:
    for term in sorted(private_terms(), key=len, reverse=True):
        text = re.sub(re.escape(term), "a fictionalized healthcare organization", text, flags=re.I)
    text = re.sub(
        r"(?i)a previous healthcare organization",
        "a fictionalized healthcare organization",
        text,
    )
    text = re.sub(r"(?i)since you told me\s+", "", text)
    if source_name.startswith("Companies/Adonis/"):
        text = SENSITIVE_MONEY.sub("[cost-impact metric]", text)
        text = SENSITIVE_PERCENTAGE.sub("[measurable percentage]", text)
        text = SENSITIVE_METRIC.sub("[illustrative scale]", text)
        text = SENSITIVE_WORD_RECORD_VOLUME.sub("[illustrative record volume]", text)
        text = SENSITIVE_WORD_SCALE.sub("[illustrative scale]", text)
        text = re.sub(
            r"(?i)you worked extensively with claims at [^.]+,\s*"
            r"so you can speak confidently here\.",
            "Use only claims experience that you are authorized to discuss; otherwise answer "
            "from public domain knowledge.",
            text,
        )
    return text


def markdown_body(text: str) -> str:
    lines: list[str] = []
    in_fence = False
    for raw in text.replace("\r\n", "\n").splitlines():
        line = raw.rstrip()
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
        if not in_fence:
            if re.fullmatch(r"[-=_]{5,}", stripped):
                line = "---"
            elif re.match(r"(?i)^phase\s+[A-Z0-9]+\b", stripped):
                line = f"## {stripped}"
            elif re.match(r"(?i)^question\s+\d+\s*[—:-]", stripped):
                line = f"## {stripped}"
            elif re.fullmatch(r"(?i)step\s+\d+", stripped):
                line = f"### {stripped}"
            elif stripped.endswith("?") and 4 < len(stripped) <= 90:
                line = f"## {stripped}"
            elif (
                stripped
                and stripped.isupper()
                and len(stripped) <= 90
                and not stripped.startswith("|")
            ):
                line = f"## {stripped.title()}"
            elif line.startswith("⭐ "):
                line = f"## {line[2:].strip()}"
            elif line.startswith("🎯 "):
                line = f"## {line[2:].strip()}"
        lines.append(line)
    body = "\n".join(lines).strip()
    body = re.sub(r"\n{3,}", "\n\n", body)
    return body + "\n"


def migrate() -> None:
    if not SOURCE.is_dir():
        print("Private text-note sources are not present; existing public Markdown is unchanged.")
        return
    missing: list[str] = []
    for source_name, destination_name in MAPPINGS.items():
        source = SOURCE / source_name
        destination = ROOT / destination_name
        if not source.is_file():
            missing.append(source_name)
            continue
        destination.parent.mkdir(parents=True, exist_ok=True)
        body = markdown_body(sanitize(source.read_text(encoding="utf-8"), source_name))
        heading = title_for(destination)
        if source_name.startswith("Companies/Adonis/"):
            notice = (
                f"# {heading}\n\n"
                "> Publication note: reorganized as an educational template. Employer-specific "
                "details are removed; all scenarios, metrics, and identifiers are fictionalized "
                "placeholders and are not claims about the maintainer's employment.\n\n"
            )
        else:
            notice = (
                f"# {heading}\n\n"
                "> Publication note: reformatted from private study notes. Employer-specific "
                "personal details and confidential context have been removed or generalized.\n\n"
            )
        destination.write_text(notice + body, encoding="utf-8")
    if missing:
        raise FileNotFoundError("Missing note sources: " + ", ".join(missing))
    print(f"Migrated {len(MAPPINGS)} text notes to Markdown.")


if __name__ == "__main__":
    migrate()
