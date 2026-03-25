import argparse
import csv
import os
import re

# Allowed values based on README.md
CATEGORIES = [
    "Pothole", "Flooding", "Streetlight", "Waste", "Noise", 
    "Road Damage", "Heritage Damage", "Heat Hazard", "Drain Blockage", "Other"
]

URGENT_KEYWORDS = [
    "injury", "child", "school", "hospital", "ambulance", "fire", "hazard", "fell", "collapse"
]

# Simple keyword mapping for categorization
# Prioritized search order
CATEGORY_MAPPING = {
    "Pothole": [r"pothole", r"sinkhole", r"crater"],
    "Flooding": [r"flood", r"water clog", r"inundated", r"overflowing water", r"underwater"],
    "Streetlight": [r"streetlight", r"street light", r"dark road", r"lamp post", r"lighting out"],
    "Waste": [r"garbage", r"trash", r"waste", r"dump", r"stink", r"bins", r"dead animal"],
    "Noise": [r"noise", r"loud", r"music", r"party", r"disturbance", r"speaker"],
    "Heritage Damage": [r"heritage", r"statue", r"monument", r"historic"],
    "Heat Hazard": [r"heat", r"sunstroke", r"dehydration", r"burn", r"hot"],
    "Drain Blockage": [r"drain", r"sewage", r"gutter", r"manhole", r"blocked"],
    "Road Damage": [r"road", r"concrete", r"broken road", r"pavement", r"cracked surface", r"footpath"]
}

def classify_complaint(row: dict) -> dict:
    """
    Classify a single complaint row using rule-based keyword matching.
    Follows R.I.C.E. rules from agents.md.
    """
    description = row.get("description", "").lower()
    complaint_id = row.get("complaint_id", "UNKNOWN")
    
    category = "Other"
    priority = "Standard"
    reason_parts = []
    flag = ""
    
    if not description.strip():
        return {
            "complaint_id": complaint_id,
            "category": "Other",
            "priority": "Standard",
            "reason": "Description is empty.",
            "flag": "NEEDS_REVIEW"
        }

    # 1. Category Detection
    matched_cat = None
    for cat, patterns in CATEGORY_MAPPING.items():
        for pattern in patterns:
            if re.search(pattern, description):
                matched_cat = cat
                reason_parts.append(f"categorized as {cat} because of '{pattern}'")
                break
        if matched_cat:
            break
    
    if matched_cat:
        category = matched_cat
    else:
        category = "Other"
        flag = "NEEDS_REVIEW"
        reason_parts.append("no specific category keywords found")

    # 2. Priority Detection
    matched_urgent = []
    for word in URGENT_KEYWORDS:
        if re.search(r'\b' + re.escape(word) + r'\b', description):
            matched_urgent.append(word)
    
    if matched_urgent:
        priority = "Urgent"
        reason_parts.append(f"urgent priority due to keywords: {', '.join(matched_urgent)}")
    elif re.search(r'\blow\b', description) or re.search(r'\bminor\b', description):
        priority = "Low"
        reason_parts.append("low priority suggested by text")
    else:
        priority = "Standard"

    # 3. Final Reason Assembly (One sentence citing specific words)
    reason = " ".join(reason_parts).capitalize() + "."
    
    return {
        "complaint_id": complaint_id,
        "category": category,
        "priority": priority,
        "reason": reason,
        "flag": flag
    }


def batch_classify(input_path: str, output_path: str):
    """
    Read input CSV, classify each row, and write structured results.
    """
    if not os.path.exists(input_path):
        print(f"Error: {input_path} not found.")
        return

    input_data = []
    try:
        with open(input_path, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            input_data = list(reader)
    except Exception as e:
        print(f"Failed to read input: {e}")
        return

    results = []
    for row in input_data:
        try:
            # Handle nulls/missing fields
            if not row or "description" not in row:
                results.append({
                    "complaint_id": row.get("complaint_id", "N/A"),
                    "category": "Other",
                    "priority": "Standard",
                    "reason": "Invalid or missing row data.",
                    "flag": "NEEDS_REVIEW"
                })
                continue
            
            classification = classify_complaint(row)
            results.append(classification)
        except Exception as e:
            # Produce output even if individual rows fail
            results.append({
                "complaint_id": "ERROR",
                "category": "Other",
                "priority": "Standard",
                "reason": f"System error: {str(e)}",
                "flag": "NEEDS_REVIEW"
            })

    if results:
        fieldnames = ["complaint_id", "category", "priority", "reason", "flag"]
        try:
            with open(output_path, mode='w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(results)
        except Exception as e:
            print(f"Failed to write results: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="UC-0A Complaint Classifier")
    parser.add_argument("--input",  required=True, help="Path to input CSV")
    parser.add_argument("--output", required=True, help="Path to output CSV")
    args = parser.parse_args()
    batch_classify(args.input, args.output)
    print(f"Done. Results written to {args.output}")
