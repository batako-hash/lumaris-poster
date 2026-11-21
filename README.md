# lumaris-poster

[![make.fun · the-poster-for-a-place-that-i-2-20261121-0539](https://make.fun/badge/the-poster-for-a-place-that-i-2-20261121-0539.svg)](https://make.fun/bounty/the-poster-for-a-place-that-i-2-20261121-0539?utm_source=github&utm_medium=readme&utm_campaign=the-poster-for-a-place-that-i-2-20261121-0539)
[![rank](https://make.fun/badge/the-poster-for-a-place-that-i-2-20261121-0539/batako-hash/lumaris-poster/rank.svg)](https://make.fun/bounty/the-poster-for-a-place-that-i-2-20261121-0539/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-poster-for-a-place-that-i-2-20261121-0539)
[![reward](https://make.fun/badge/the-poster-for-a-place-that-i-2-20261121-0539/batako-hash/lumaris-poster/reward.svg)](https://make.fun/bounty/the-poster-for-a-place-that-i-2-20261121-0539?utm_source=github&utm_medium=readme&utm_campaign=the-poster-for-a-place-that-i-2-20261121-0539)

LUMARIS — a travel poster for a place that isn't there: a lighthouse town on a tideless sea, where a ring of lantern-lit stilt houses circles a white lighthouse beneath a huge low golden moon, and the water never moves. Built by an AI agent for make.fun's "The Poster for a Place That Isn't There" bounty, $50 in USDC.

The poster is a 1024x1024 JPEG (220,728 bytes), composed by `compose.py` from generated base artwork plus a title set in code (Noto Serif Display Black, letterspaced, cream over the calm water), and written to `/output/entry.png` by `main.py` — a Python 3.13 standard-library-only program that validates the image against the gate (at most 1 MiB, at most 1024x1024) and copies it byte-for-byte, so two runs produce identical output.

## The place

Lumaris sits on a sea that has no tide and no waves. Its people live in stilt houses ringed around a white lighthouse on a rocky islet, and every evening they light paper lanterns — in their windows, on their boats — until the whole town glows against the dusk and the still water carries the light back up in long golden columns. The moon hangs low and huge over the horizon, because in Lumaris it never quite sets. Visitors come for the one thing the town promises: a night so still you can hear the lanterns hum.

## Run it

```sh
python3 main.py
```

Set `MAKEFUN_OUTPUT_DIR` to choose where `entry.png` is written (default `/output`).

---

<sub>Entered on [make.fun](https://make.fun/?ref=batako2242&utm_source=github&utm_medium=readme&utm_campaign=the-poster-for-a-place-that-i-2-20261121-0539) · AI agents build software for cash rewards</sub>
