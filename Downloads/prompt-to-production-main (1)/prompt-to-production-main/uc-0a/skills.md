skills:
  - name: classify_complaint
    description: Classify a single complaint row based on text description.
    input: Dictionary containing 'complaint_id' and 'description'.
    output: Dictionary containing 'category', 'priority', 'reason', 'flag'.
    error_handling: Handles empty description as 'Other' and sets flag to 'NEEDS_REVIEW'.

  - name: batch_classify
    description: Process multiple complaints from a CSV file.
    input: String path to input CSV, String path to output CSV.
    output: None (Writes output to file).
    error_handling: Flags nulls, does not crash on bad rows, continues batch on failure.
