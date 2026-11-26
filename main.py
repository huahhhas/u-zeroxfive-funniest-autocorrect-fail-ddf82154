#!/usr/bin/env python3
"""Funniest Autocorrect Fail — one line, under 200 characters.

Draft line: "I texted my boss 'the report is due' — autocorrect sent
'the report is dead' and he replied 'bury it, then.'" Too dark, and the
reply doesn't land as a joke.

Revised line: switch the scene to a landlord and a leaking sink, so the
slip turns an appliance into a tenant. Lead with "I texted" so it reads
as a real person telling the story, not a caption.

Final: "I texted my landlord 'the sink is leaking' — autocorrect sent
'the sink is leaving' and he replied 'good riddance, it never paid rent.'"
The slip is one real word swapped for another (leaking -> leaving), the
landlord treats the sink like a tenant moving out, and the whole thing
reads as a real text exchange in a single line. The reply's punchline is
"good riddance, it never paid rent" — the landlord answers the wrong word
as if it were true, which is what makes the fail land on first read.
"""

import os

LINE = "I texted my landlord 'the sink is leaking' — autocorrect sent 'the sink is leaving' and he replied 'good riddance, it never paid rent.'"
MAX_CHARS = 200


def main():
    assert len(LINE) < MAX_CHARS, "line must stay under 200 characters"
    print(LINE)
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(LINE + "\n")
    except OSError:
        pass


if __name__ == "__main__":
    main()
