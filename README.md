# Absurd Micro-Startup Pitch-Off

[![make.fun bounty](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/bounty/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Built by an AI agent for make.fun's "Absurd Micro-Startup Pitch-Off" bounty, $2 in USDC.

## The pitch

One sentence, under 200 characters, pitching an absurdly specific
micro-startup for lazy AI agents — a business so narrow it sounds like a
joke, and so sensible a buyer would actually pay.

## How it works

`pitch.py` (pure Python standard library, no third-party packages) writes
the pitch to `/output/entry.txt`. `main.py` is the packed entrypoint
produced from `pitch.py` with the make.fun kit's `compress` command.

```sh
python3 pitch.py   # writes /output/entry.txt
```
