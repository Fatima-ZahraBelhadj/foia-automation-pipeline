# FOIA Mixed-Media Automation Pipeline

An automated data engineering pipeline designed to manage, transfer, and audit high-volume Freedom of Information Act (FOIA) public records. This system handles mixed-media datasets, including massive police bodycam/dashcam video files alongside highly sensitive legal documents and inter-agency memos.

## Overview
Processing hundreds of FOIA requests involves navigating strict legal exemptions (e.g., National Security, Personal Privacy, Law Enforcement Records, and Privileged Communications). Moving these mixed-media files across disparate cloud architectures manually is highly error-prone and risks breaking the chain of custody. This repository contains the automation scripts used to securely transfer over 1,000 files while preserving strict, nested case-folder hierarchies.

## Architecture
* **Google Apps Script (`CODE.gs`):** A recursive traversal algorithm that interacts directly with the Google Workspace API to securely clone nested folder structures, migrating massive `.mp4` evidentiary files and `.pdf` legal memos between cloud environments.
* **Python Audit Tool (`foia_validator.py`):** A local script used post-sync to traverse the directories and generate immutable CSV audit logs. It automatically categorizes files (Evidentiary Media vs. Legal Documents) and logs ingestion timestamps for compliance.

## Insights & Future Work: Transition to AI Governance
Building and operating this pipeline provided direct insight into the systemic vulnerabilities of institutional oversight. While this pipeline successfully automated the infrastructure of FOIA processing, it revealed a critical bottleneck in the human review phase, specifically regarding statutory exemptions.

When law enforcement and legal reviewers were presented with highly structured, AI-generated summaries of these legal documents—such as automated justifications for withholding records based on "Personal Privacy" or "Law Enforcement Techniques"—I observed a severe tendency toward Automation Bias. Human operators were rubber-stamping outputs due to the "syntactic authority" (formal legalese, confident tone) of the generated text, failing to properly verify the underlying documents.

Next Steps: My current research pivots from automating data infrastructure to securing the human-AI oversight layer. This pipeline served as the foundational use-case for my proposed Aegis Active Auditor Framework—an adversarial UX interface designed to mitigate automation bias and enforce meaningful human control in high-stakes legal workflows.

---
Built by Monica  
For the ERA Fellowship — Technical AI Governance track
