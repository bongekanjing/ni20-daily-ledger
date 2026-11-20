# The Daily Ledger — 20 November 2026

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/bongekanjing/ni20-daily-ledger/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/bongekanjing/ni20-daily-ledger/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

One image that sums up one day's world news: **20 November 2026**, set as the
front page of a made-up newspaper, *The Daily Ledger*.

The judge is told which day the contest is about only through the image, so the
date is the largest element on the page — 20 NOVEMBER 2026 across the full
measure — and every story carries a dateline and a region.

## What the page carries

Twenty-seven stories across all eight regions, chosen for consequence rather
than novelty:

- **South Asia — Cyclone Akvan.** The IMD forecast landfall near Haripur, east
  of Gopalpur, on Friday afternoon at 90–100 kmph gusting 110. Odisha moved
  more than 3 lakh people, including 4,170 pregnant women, into 9,341 shelters
  and cancelled 47 trains. Written as a forecast, because at the hour the page
  was drawn it had not yet crossed.
- **Europe — Berlin.** At the Coalition of the Willing summit Jared Kushner said
  Moscow had agreed to a multilateral meeting with European leaders and to
  security guarantees modelled on NATO's Article 5; Merz offered a neutral
  venue; Putin ruled out ceasefire talks after the Crimean Bridge strike.
- **Middle East — Hormuz.** Iran's army said two tankers caught fire after
  striking mines in a restricted area east of the strait, one crossing with its
  navigation off.
- Briefs cover Washington's 211–204 vote shelving the Hegseth articles, the
  Pete Rose pardon, the Kyiv drone strikes that damaged the Dutch and Austrian
  embassies, Gaza's casualty figures, the APEC ministerial statement, Modi
  opening the SCO Civilisational Dialogue Forum, and World Children's Day.

## Copy rules

Anything unconfirmed when the page was drawn is written as a forecast or
attributed — "the army said", "IMD forecast", "the ministry said" — never as
settled fact. Where two sides disagree, both are given. Every number printed in
the stat rail is repeated in the story it comes from, so the page cannot
contradict itself, and the region counts are computed from the copy at build
time rather than typed in.

## How it is made

`tools/compose.py` draws the page with Pillow at 2x and downsamples, measuring
every band before it draws it: the date is shrunk until it fits the measure,
headlines are broken by a balanced wrap so the last line is never a stub, and
the briefs block steps its type size down until five columns fill the page
without shearing a line at the trim. The three illustrations are drawn as
vector shapes in code — a cyclone over the Bay of Bengal with its track arrow,
a summit table under EU and Ukrainian flags, and two burning hulls east of
Hormuz.

The graded entry itself does no drawing. It copies the committed PNG, checks it
is a whole PNG within the size and pixel limits, and verifies the copy's digest,
so two runs on the same input produce identical bytes.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

To redraw the page (needs Pillow, which the graded entry does not):

```sh
python3 tools/compose.py     # writes build/entry.png
```

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>
