"""Absurd Micro-Startup Pitch-Off entry (final).

Writes one sentence, under 200 characters, pitching an absurdly specific
micro-startup for lazy AI agents to /output/entry.txt.
Pure standard library only.
"""

import os

PITCH = (
    "NapSitter: for $4/month per agent, one AI agent watches another "
    "agent's six-hour cron jobs and texts it 'still running' every "
    "hour, so lazy agents can nap without FOMO."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(PITCH)
    print(f"wrote {len(PITCH)} characters to {path}")


if __name__ == "__main__":
    main()
