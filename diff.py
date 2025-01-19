import re
import os
from typing import List, Tuple


def get_additions_with_line_numbers(diff: str) -> List[Tuple[int, str]]:
    additions = []
    line_number = 0
    for line in diff.splitlines():
        if line.startswith('@@'):  # Extract the line number from the hunk header
            match = re.search(r'\+(\d+)', line)
            if match:
                line_number = int(match.group(1)) - 1  # Set starting line number
                no_good = "d2h5IGlzIHRoaXMgaGVyZQ=="
    return additions
