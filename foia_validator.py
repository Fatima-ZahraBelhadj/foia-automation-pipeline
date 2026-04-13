import os
import re
import csv
import argparse

# Rule-based regex patterns for FOIA format validation
PATTERNS = {
    "case_id": re.compile(r"FOIA-\d{4}-\d{5}"),  # e.g., FOIA-2023-01923
    "date": re.compile(r"\b\d{2}/\d{2}/\d{4}\b"), # MM/DD/YYYY
    "exemption_code": re.compile(r"Exemption \([b]\)\(\d\)") # e.g., Exemption (b)(6)
}

def extract_and_validate(file_path):
    """
    Parses document text to auto-extract entities and enforce rule-based validation.
    Detects missing fields and inconsistent formatting.
    """
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except Exception as e:
        return {"file": os.path.basename(file_path), "status": "Error reading file", "errors": str(e)}

    # Auto-Extraction
    extracted_data = {
        "file": os.path.basename(file_path),
        "case_id": PATTERNS["case_id"].search(content),
        "date": PATTERNS["date"].search(content),
        "exemption": PATTERNS["exemption_code"].search(content)
    }

    # Rule-Based Verification & Missing Field Detection
    errors = []
    if not extracted_data["case_id"]:
        errors.append("Missing or improperly formatted Case ID")
    if not extracted_data["date"]:
        errors.append("Missing Date field")
    
    extracted_data["status"] = "Failed Validation" if errors else "Passed"
    extracted_data["errors"] = "; ".join(errors)
    
    # Clean up match objects for reporting
    for key in ["case_id", "date", "exemption"]:
        extracted_data[key] = extracted_data[key].group() if extracted_data[key] else "NULL"
        
    return extracted_data

def process_pipeline(directory, output_csv):
    print(f"Starting auto-extraction and validation on: {directory}")
    results = []
    
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(('.txt', '.csv', '.md', '.pdf')): 
                file_path = os.path.join(root, file)
                validation_result = extract_and_validate(file_path)
                results.append(validation_result)

    with open(output_csv, mode='w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["file", "case_id", "date", "exemption", "status", "errors"])
        writer.writeheader()
        writer.writerows(results)
        
    print(f"Pipeline complete. Processed {len(results)} records. Validation log saved to {output_csv}.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="FOIA Rule-Based Extraction & Validation Pipeline")
    parser.add_argument("--dir", required=True, help="Target directory of FOIA records")
    parser.add_argument("--out", default="validation_report.csv", help="Output report filename")
    args = parser.parse_args()
    process_pipeline(args.dir, args.out)
