import csv
import json
from typing import List, Dict, Any


def export_to_json(data: List[Dict[str, Any]], filename: str) -> None:
    """Exports a list of dictionaries to a JSON file (UTF-8, pretty)."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def export_to_csv(data: List[Dict[str, Any]], filename: str) -> None:
    """Exports a list of dictionaries to a CSV file (UTF-8 with header)."""
    if not data:
        return
    keys = list(data[0].keys())
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=keys,
            extrasaction="ignore",
            quoting=csv.QUOTE_MINIMAL,
        )
        writer.writeheader()
        writer.writerows(data)
