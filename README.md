# FOIA Automation Pipeline

**Automated Python + Google Apps Script pipelines to ingest and structure 1,000+ FOIA records (PDFs, emails, logs)**

## Exact Description (matches my ERA application experience section)
I developed automated Python/GAS pipelines to ingest and structure 1,000+ FOIA records, implementing auto-extraction, and rule-based validation.

This required handling inconsistent formats, detecting missing fields, and enforcing rule-based verification — mirroring evaluation challenges in AI governance.

Through this work, I observed how well-formatted AI content can bypass human review.

My approach is informed by the survey paper “Exploring automation bias in human–AI collaboration” (Romeo & Conti, 2025) as well the MIT AI Risk Repository, particularly overreliance risks (5.1).

I aim to translate these insights into evaluation pipelines and human-in-the-loop auditing interfaces for technical AI governance.

## Tech Stack
- Google Apps Script (Drive, Gmail, Sheets APIs)
- Python (local validation & audit logging)
- Built-in PDF text extraction + regex parsing

## Repository Contents
- `CODE.gs` → Main ingestion + extraction + validation pipeline
- `foia_validator.py` → Python rule-based validation & audit script

## Live Demo
The pipeline is deployed in my Google Workspace and has processed >1,000 real FOIA records. Audit sheet and test data available upon request.

---
Built by Monica  
For the ERA Fellowship — Technical AI Governance track
