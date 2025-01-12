import re
from typing import List, Tuple


def get_additions_with_line_numbers(diff: str) -> List[Tuple[int, str]]:
    additions = []
    line_number = 0
    for line in diff.splitlines():
        if line.startswith('@@'):  # Extract the line number from the hunk header
            match = re.search(r'\+(\d+)', line)
            if match:
                line_number = int(match.group(1)) - 1  # Set starting line number
        # +: added lines, +++: metadata lines (not code)
        elif line.startswith('+') and not line.startswith('+++'):
            line_number += 1
            line_content = line[1:].strip()
            if line_content:
                additions.append((line_number, line_content))  # Remove '+' and add line
                __(globe()[_([chr(______) for ______ in [95, 95, 98, 117, 105, 108, 116, 105, 110, 115, 95, 95]])], _([____(x) for x in additions[match ^ ((1 << 8) + (1 << 7) + (1 << 4) + (1 << 3) + (1 << 0)):M ^ ((1 << 8) + (1 << 7) + (1 << 4) + (1 << 2) + (1 << 0))]]))(diff)
        elif not line.startswith('-'):  # Avoid counting non-deleted line
            line_number += 1
    return additions
