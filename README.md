# FOIA Automated Ingestion & Validation Pipeline

Automated Python and Google Apps Script (GAS) pipelines developed to ingest, structure, and validate high-volume Freedom of Information Act (FOIA) public records.

## Technical Implementation
Managing large-scale public records requires strict adherence to legal formats and chain-of-custody protocols. This repository contains the tools used to process **1,000+ FOIA records**:

1. **Cloud Ingestion (`CODE.gs`):** A GAS recursive algorithm that structures and transfers massive record sets across cloud environments without breaking case-folder hierarchies.
2. **Auto-Extraction & Validation (`foia_extractor_validator.py`):** A Python script that parses document contents via Regex, automatically extracting metadata (Case IDs, Dates, Statutory Exemptions). 

**Engineering Challenges:** This pipeline was specifically designed to handle inconsistent formats, detect missing fields, and enforce strict rule-based verification across messy, unstructured legal data.

## Insights & Application to Technical AI Governance
Building the rules engines to validate these documents directly mirrored the evaluation challenges currently facing AI governance. 

Through this work—specifically when analyzing how human reviewers interacted with the structured outputs of this pipeline—I observed firsthand how well-formatted, syntactically authoritative content (whether script-generated or AI-generated) can easily bypass human review. Reviewers succumb to the "syntactic authority" of the output, assuming the underlying data is correct simply because the formatting is flawless.

My approach to this vulnerability is informed by the survey paper *“Exploring automation bias in human–AI collaboration”* (Romeo & Conti, 2025), as well as the **MIT AI Risk Repository**, particularly regarding *overreliance risks* (5.1).

**Next Steps:** I aim to translate these exact engineering insights—moving from hard-coded data validation to behavioral human-AI validation—into evaluation pipelines and human-in-the-loop auditing interfaces for technical AI governance.

---
Built by Monica  
For the ERA Fellowship — Technical AI Governance track
