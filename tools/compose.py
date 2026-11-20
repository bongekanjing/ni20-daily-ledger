"""Compose the front page.

Layout, top to bottom: masthead strip, nameplate, the date across the full
measure, a standfirst, a rail of hard numbers, a region index whose counts are
computed from the copy, a picture well with one wide lead and two stacked
second leads, then five columns of briefs.

Every band is measured before it is drawn; the briefs block raises rather than
shearing a line at the trim.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from pagelib import F, H, MARGIN, MEASURE, PAPER, Page, W  # noqa: E402
from stories import BRIEFS, LEADS, NUMBERS, REGIONS, counts, stories  # noqa: E402

INK = (20, 18, 16)
MID = (74, 69, 62)
GREY = (122, 116, 106)
RULE = (128, 121, 108)
HAIR = (198, 191, 177)
FINE = (216, 209, 195)
RED = (143, 20, 20)
WHITE = (252, 249, 242)

DATE = "20 NOVEMBER 2026"


def _plate(p, x, y, text, pad=4, size=6.2, ink=(250, 246, 236), back=(24, 26, 30)):
    """A small label on a solid plate, so it reads over any ground."""
    tw = p.measure(text, F("sansb", size))
    p.rect(x - pad, y - pad + 1, x + tw + pad, y + size + pad - 2, back)
    p.text(x, y, text, F("sansb", size), ink)
    return tw


def art_akvan(p, x, y, w, h):
    """The storm off the Odisha coast: a spiral, the shoreline, shelters inland."""
    sea, sky = (36, 58, 72), (74, 82, 86)
    p.rect(x, y, x + w, y + h, sky)
    p.rect(x, y, x + w, y + h * .34, (66, 74, 82))     # dark deck of cloud
    # the sea, with the coast running up the right-hand side
    p.rect(x, y + h * .34, x + w, y + h, sea)
    p.d.polygon([((x + w * .78) * 2, (y + h * .34) * 2), ((x + w) * 2, (y + h * .30) * 2),
                 ((x + w) * 2, (y + h) * 2), ((x + w * .66) * 2, (y + h) * 2)],
                fill=(88, 88, 62))
    # rain bands crossing the frame, heavier toward the centre
    for i in range(9):
        bx = x + w * (.04 + .085 * i)
        p.d.line([(bx * 2, (y + h * .30) * 2), ((bx + w * .10) * 2, (y + h * .86) * 2)],
                 fill=(96, 112, 122), width=1)
    # the cyclone: bands wound around a clear eye, left of centre
    cx, cy = x + w * .42, y + h * .52
    for k, rad in enumerate((.30, .23, .16, .09)):
        rw, rh = w * rad, h * rad * 1.12
        p.d.arc([(cx - rw) * 2, (cy - rh) * 2, (cx + rw) * 2, (cy + rh) * 2],
                start=200 + k * 24, end=110 + k * 24, fill=(214, 220, 224), width=int(5 - k))
    p.d.ellipse([(cx - w * .035) * 2, (cy - h * .035) * 2,
                 (cx + w * .035) * 2, (cy + h * .035) * 2], fill=(58, 66, 72))
    # the coast town: shelters as a row of low roofs behind the beach
    for k in range(7):
        tx = x + w * (.70 + .042 * k)
        p.d.polygon([(tx * 2, (y + h * .80) * 2), ((tx + w * .028) * 2, (y + h * .735) * 2),
                     ((tx + w * .056) * 2, (y + h * .80) * 2)], fill=(206, 198, 180))
    # the track arrow, north-west toward land
    p.d.line([((x + w * .55) * 2, (y + h * .70) * 2), ((x + w * .70) * 2, (y + h * .58) * 2)],
             fill=(232, 92, 48), width=3)
    p.d.polygon([((x + w * .70) * 2, (y + h * .58) * 2), ((x + w * .655) * 2, (y + h * .60) * 2),
                 ((x + w * .675) * 2, (y + h * .638) * 2)], fill=(232, 92, 48))
    _plate(p, x + w * .60, y + h * .385, "ODISHA COAST")
    _plate(p, x + 5, y + h - 15, "BAY OF BENGAL")
    _plate(p, x + w * .755, y + h * .665, "GOPALPUR", ink=(240, 236, 224))


def art_berlin(p, x, y, w, h):
    """A long table under two flags, chairs on the near side, a map of Ukraine."""
    room, floor = (96, 90, 92), (58, 54, 58)
    p.rect(x, y, x + w, y + h, room)
    p.rect(x, y + h * .82, x + w, y + h, floor)
    # a window wall behind, so the plate is not a black field
    for k in range(5):
        wx = x + w * (.04 + .19 * k)
        p.rect(wx, y + h * .06, wx + w * .13, y + h * .44, (132, 126, 128))
        p.rect(wx, y + h * .06, wx + w * .13, y + h * .09, (108, 102, 104))
    # two flags, hung flat against the back wall
    for fx, band, fut in ((.10, (44, 62, 116), (232, 230, 220)), (.78, (214, 196, 60), (44, 82, 152))):
        p.rect(x + w * fx, y + h * .08, x + w * fx + 30, y + h * .26, band)
        p.rect(x + w * fx, y + h * .17, x + w * fx + 30, y + h * .195, fut)
    p.text(x + w * .10 + 15, y + h * .285, "EU", F("sansb", 5.4), (206, 200, 188), anchor="ma")
    p.text(x + w * .78 + 15, y + h * .285, "UKRAINE", F("sansb", 5.4), (206, 200, 188), anchor="ma")
    # the table: a long slab seen from the near side
    p.d.polygon([(x * 2, (y + h * .56) * 2), ((x + w) * 2, (y + h * .56) * 2),
                 ((x + w * .95) * 2, (y + h * .80) * 2), ((x + w * .05) * 2, (y + h * .80) * 2)],
                fill=(140, 112, 86))
    # a document and a folded map lying on it
    p.d.polygon([(x + w * .30, y + h * .60), (x + w * .42, y + h * .60),
                 (x + w * .43, y + h * .74), (x + w * .29, y + h * .74)],
                fill=(246, 242, 232))
    for k in range(4):
        p.hline(x + w * .312, y + h * (.628 + .026 * k), x + w * .406, (170, 162, 148), 1)
    p.d.polygon([(x + w * .52, y + h * .615), (x + w * .68, y + h * .605),
                 (x + w * .695, y + h * .735), (x + w * .535, y + h * .745)],
                fill=(176, 198, 172))
    p.d.line([((x + w * .60) * 2, (y + h * .612) * 2), ((x + w * .615) * 2, (y + h * .740) * 2)],
             fill=(120, 142, 118), width=1)
    # six chairs on the near side, backs to us, two of them occupied
    for k in range(6):
        cx = x + w * (.12 + .152 * k)
        p.rect(cx - 11, y + h * .80, cx + 11, y + h * .90, (52, 46, 46))
        p.rect(cx - 11, y + h * .78, cx + 11, y + h * .815, (96, 86, 82))
    for cx in (x + w * .272, x + w * .576):
        p.d.ellipse([(cx - 6) * 2, (y + h * .745) * 2, (cx + 6) * 2, (y + h * .795) * 2],
                    fill=(24, 22, 24))
    _plate(p, x + 4, y + 4, "BERLIN", ink=(214, 208, 196))


def art_hormuz(p, x, y, w, h):
    """Two hulls burning at anchor, a mine lane, the far shore of Qeshm."""
    sky, sea = (86, 78, 88), (48, 70, 92)
    land = (82, 74, 70)
    fire, hot = (226, 96, 34), (248, 196, 104)
    p.rect(x, y, x + w, y + h, sky)
    p.rect(x, y + h * .34, x + w, y + h, sea)
    p.d.polygon([(x * 2, (y + h * .34) * 2), (x * 2, (y + h * .16) * 2),
                 ((x + w * .30) * 2, (y + h * .22) * 2), ((x + w * .38) * 2, (y + h * .34) * 2)],
                fill=land)
    p.d.polygon([((x + w) * 2, (y + h * .34) * 2), ((x + w) * 2, (y + h * .18) * 2),
                 ((x + w * .62) * 2, (y + h * .24) * 2), ((x + w * .55) * 2, (y + h * .34) * 2)],
                fill=land)
    for i in range(4):
        p.hline(x + w * (.04 + .05 * (i % 2)), y + h * (.48 + .13 * i),
                x + w * (.92 - .05 * (i % 3)), (74, 100, 124), 1)
    # two tankers, one large in front, one small and further off
    for hx, hy, hw, hh, lit in ((.14, .66, .34, .085, True), (.60, .52, .19, .050, False)):
        bx, by, bw, bh = x + w * hx, y + h * hy, w * hw, h * hh
        p.rect(bx, by, bx + bw, by + bh, (34, 34, 38))
        p.rect(bx + bw * .70, by - bh * 1.1, bx + bw * .88, by + bh * .2, (52, 52, 58))
        p.rect(bx + bw * .72, by - bh * 1.8, bx + bw * .84, by - bh * 1.1, (52, 52, 58))
        p.hline(bx, by + bh * .45, bx + bw, (120, 118, 116), 1)
        fx = bx + bw * .30
        p.d.ellipse([(fx - w * .020) * 2, (by - bh * .75) * 2,
                     (fx + w * .022) * 2, (by + bh * .30) * 2], fill=fire if lit else (150, 70, 34))
        if lit:
            p.d.ellipse([(fx - w * .009) * 2, (by - bh * .55) * 2,
                         (fx + w * .010) * 2, (by + bh * .10) * 2], fill=hot)
            for dx, dy, dw, dh, col in ((0, 0, .10, .34, (76, 74, 76)),
                                        (.02, .06, .07, .26, (94, 92, 92)),
                                        (-.02, .13, .045, .15, (116, 112, 110))):
                p.d.polygon([((fx + w * dx) * 2, (by - bh * .45) * 2),
                             ((fx + w * dx - w * dw) * 2, (by - bh * dy - h * dh) * 2),
                             ((fx + w * dx + w * dw * .5) * 2, (by - bh * dy - h * dh * .9) * 2)],
                            fill=col)
    # the mine lane: a dashed line of buoys across the water
    for k in range(9):
        bx = x + w * (.06 + .105 * k)
        p.d.ellipse([(bx - 2) * 2, (y + h * .925) * 2, (bx + 2) * 2, (y + h * .955) * 2],
                    fill=(168, 148, 96))
        if k < 8:
            p.hline(bx + 4, y + h * .938, bx + w * .095, (120, 106, 74), 1)
    _plate(p, x + w * .13, y + h * .225, "QESHM / IRAN")
    _plate(p, x + 5, y + h - 15, "EAST OF THE STRAIT OF HORMUZ")


ART = {"akvan": art_akvan, "berlin": art_berlin, "hormuz": art_hormuz}


def fit_head(p, head, maxw, cap, floor=13):
    """Largest size at which `head` sets in two balanced lines, else one line."""
    size = cap
    while size >= floor:
        f = F("serifb", size)
        lines = p.wrap_balanced(head, f, maxw, 2)
        if lines:
            return size, lines
        if p.measure(head, f) <= maxw:
            return size, [head]
        size -= 1
    return floor, p.wrap(head, F("serifb", floor), maxw)


def lead(p, x, y, w, art_h, item, head_size, deck_size, deck_lines):
    """Draw one lead story; returns the y just past its last line of copy."""
    region, kicker, head, text, art = item
    ART[art](p, x, y, w, art_h)
    ty = y + art_h + 8
    p.track(x, ty, f"{kicker} · {region}", F("sansb", 6.8), RED, 1)
    ty += 14
    size, lines = fit_head(p, head, w, head_size)
    for ln in lines:
        p.text(x, ty, ln, F("serifb", size), INK)
        ty += int(size * 1.06)
    return p.para(x, ty + 5, text, F("serif", deck_size), w, deck_size * 1.30, MID, deck_lines)


def compose():
    p = Page()

    # ---- masthead strip
    y = 12
    p.hline(MARGIN, y, MARGIN + MEASURE, RULE, 2)
    y += 5
    p.track(MARGIN, y, "THE WORLD IN ONE PAGE", F("sansb", 7.5), INK, 3)
    right = "COMPILED FROM THE DAY'S WIRE COPY"
    p.track(MARGIN + MEASURE - p.measure(right, F("sansb", 7.5), 3), y, right, F("sansb", 7.5), MID, 3)
    y += 15

    # ---- nameplate
    p.text(MARGIN, y, "The Daily Ledger", F("serifb", 25), INK)
    p.text(MARGIN + MEASURE, y + 8, "No. 324 · all the day on one page", F("serif", 9.5), MID,
           anchor="ra")
    y += 34
    p.hline(MARGIN, y, MARGIN + MEASURE, INK, 1)
    y += 5

    # ---- the date: the largest element, spanning the measure
    size = 84
    while p.measure(DATE, F("serifb", size)) > MEASURE:
        size -= 1
    p.text(MARGIN, y + 2, DATE, F("serifb", size), INK)
    y += int(size * 1.08) + 2
    p.hline(MARGIN, y, MARGIN + MEASURE, INK, 3)
    y += 6

    # ---- standfirst
    n = len(stories())
    blurb = (f"{n} stories from {len(REGIONS)} regions: a cyclone closing on the Odisha coast "
             f"with three lakh evacuated, two tankers burning on mines east of Hormuz, and "
             f"Moscow agreeing to a multilateral meeting in Berlin")
    f_stand = F("serif", 10.5)
    p.para(MARGIN, y, blurb, f_stand, MEASURE - 176, 14, MID, 2)
    rt = MARGIN + MEASURE
    p.track(rt - p.measure("READING TIME", F("sansb", 6.8), 2), y + 1, "READING TIME",
            F("sansb", 6.8), GREY, 2)
    p.text(rt, y + 12, "eight minutes", F("serifb", 11.5), RED, anchor="ra")
    y += 31

    # ---- numbers rail
    p.hline(MARGIN, y, MARGIN + MEASURE, HAIR, 1)
    y += 6
    colw = MEASURE / len(NUMBERS)
    caps = [p.wrap(cap, F("sans", 6.6), colw - 14, 2) for _n, cap in NUMBERS]
    for i, (num, _cap) in enumerate(NUMBERS):
        cx = MARGIN + colw * i
        p.text(cx, y, num, F("serifb", 25), RED)
        for j, ln in enumerate(caps[i]):
            p.text(cx, y + 29 + j * 8.6, ln, F("sans", 6.6), MID)
        if i:
            p.vline(cx - 7, y - 1, y + 38, HAIR, 1)
    y += 51

    # ---- region index, counts computed from the copy; tabs fill the measure
    p.hline(MARGIN, y, MARGIN + MEASURE, INK, 1)
    y += 4
    cnt = counts()
    gap = 3.5
    tab_w = (MEASURE - gap * (len(REGIONS) - 1)) / len(REGIONS)
    x = MARGIN
    for label, col in REGIONS:
        p.rect(x, y, x + tab_w, y + 15, col)
        p.text(x + 6, y + 4, label, F("sansb", 7.0), WHITE)
        p.text(x + tab_w - 6, y + 4, str(cnt[label]), F("sansb", 7.0), WHITE, anchor="ra")
        x += tab_w + gap
    y += 20
    p.hline(MARGIN, y, MARGIN + MEASURE, INK, 2)
    y += 9

    # ---- picture well: one wide lead, two stacked beside it
    wide_w, art_h = 452, 158
    nx = MARGIN + wide_w + 16
    nw = MARGIN + MEASURE - nx
    well_top = y

    bottom_a = lead(p, MARGIN, y, wide_w, art_h, LEADS[0], 30, 9.4, 5)

    y2 = y
    bottom_b = lead(p, nx, y2, nw, 70, LEADS[1], 15.5, 7.8, 4)
    y2 = bottom_b + 7
    p.hline(nx, y2 - 5, nx + nw, HAIR, 1)
    bottom_c = lead(p, nx, y2, nw, 70, LEADS[2], 15.5, 7.8, 4)
    p.vline(nx - 8, well_top, max(bottom_b, bottom_c) - 2, HAIR, 1)

    y = max(bottom_a, bottom_c) + 6
    p.hline(MARGIN, y, MARGIN + MEASURE, INK, 2)
    return p, y + 8


def fill_briefs(p, top, bottom):
    """Flow the briefs into five columns; returns (placed, lowest y used)."""
    cols, gutter = 5, 11
    cw = (MEASURE - gutter * (cols - 1)) / cols
    avail = bottom - top

    chosen = None
    for fs, ks in ((9.0, 9.4), (8.6, 9.0), (8.2, 8.6), (7.8, 8.2), (7.4, 7.8),
                   (7.0, 7.4), (6.6, 7.0), (6.2, 6.6), (5.8, 6.2)):
        body, kick = F("serif", fs), F("sansb", ks)
        lead_ = fs * 1.30
        bricks = []
        for _region, k, t in BRIEFS:
            lines = p.wrap(t, body, cw)
            bricks.append((k, lines, 3 + 9 + len(lines) * lead_ + 4))
        total = sum(b[2] for b in bricks)
        plan = balance(bricks, cols, total / cols, avail)
        if plan is not None:
            chosen = (body, kick, lead_, bricks, total, plan)
            break
    if chosen is None:
        raise SystemExit("briefs do not fit: cut copy or shorten the well")

    body, kick, lead_, bricks, total, plan = chosen
    idx, low = 0, top
    for c, group in enumerate(plan):
        x = MARGIN + c * (cw + gutter)
        y = top
        for i in group:
            k, lines, _hgt = bricks[i]
            p.hline(x, y, x + cw, HAIR, 1)
            y += 3
            kw = p.track(x, y, k.upper(), kick, RED, 1)
            p.text(x + kw + 3, y + 1, "·", kick, HAIR)
            y += 10
            for ln in lines:
                p.text(x, y, ln, body, INK)
                y += lead_
            y += 4
        idx += len(group)
        if c < cols - 1:
            p.vline(x + cw + gutter / 2, top, bottom - 14, FINE, 1)
        low = max(low, y)
    return idx, low


def balance(bricks, cols, target, avail):
    """Split bricks into `cols` ordered groups, each no taller than avail and
    as close to `target` as the greedy walk allows. Returns index groups."""
    n = len(bricks)
    for slack in (1.0, 1.03, 1.07, 1.12, 1.20):
        cap = min(avail, target * slack)
        groups, cur, height = [], [], 0.0
        for i in range(n):
            h = bricks[i][2]
            if cur and height + h > cap:
                groups.append(cur)
                cur, height = [], 0.0
            cur.append(i)
            height += h
        if cur:
            groups.append(cur)
        if len(groups) <= cols and height <= avail:
            while len(groups) < cols:            # never leave a column empty
                widest = max(range(len(groups)), key=lambda g: sum(bricks[i][2] for i in groups[g]))
                g = groups[widest]
                if len(g) < 2:
                    break
                half = len(g) // 2
                groups.insert(widest + 1, g[half:])
                groups[widest] = g[:half]
            if len(groups) == cols:
                return groups
    return None


def main():
    p, y = compose()
    bottom = H - 46
    used, low = fill_briefs(p, y, bottom)
    if low > bottom:
        raise SystemExit(f"briefs overrun the trim: {low:.0f} > {bottom}")

    p.hline(MARGIN, bottom + 6, MARGIN + MEASURE, INK, 2)
    left = "THE DAILY LEDGER · 20 NOVEMBER 2026 · CONTINUED ON PAGE TWO"
    p.track(MARGIN, bottom + 12, left, F("sansb", 6.4), MID, 2)
    right = f"{len(stories())} STORIES · {used} IN BRIEF · EIGHT REGIONS"
    p.track(MARGIN + MEASURE - p.measure(right, F("sansb", 6.4), 2), bottom + 12, right,
            F("sansb", 6.4), MID, 2)

    out = os.path.join(ROOT, "build")
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, "entry.png")
    p.emit().save(path, "PNG", optimize=True)
    print(f"briefs {used}/{len(BRIEFS)}  stories {len(stories())}  lowest {low:.0f}/{bottom}  "
          f"bytes {os.path.getsize(path)}")


if __name__ == "__main__":
    main()
