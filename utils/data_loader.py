import json
import pathlib
from typing import Any, Dict

"""
Utility for loading test data from JSON files
"""

def load_json(file_name: str) -> Dict[str, Any]:
    base = pathlib.Path(__file__).resolve().parent.parent / "testdata"
    path = base / file_name
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


