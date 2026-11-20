"""Build the 1024x1024 front page. Needs Pillow; the graded entry does not."""

import os
import sys

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
from stories import BRIEFS, LEADS, NUMBERS, REGIONS, counts, stories  # noqa: E402

S = 2
W = H = 1024
MARGIN = 24
MEASURE = W - 2 * MARGIN

PAPER = (252, 249, 242)
INK = (20, 18, 16)
MID = (74, 69, 62)
RULE = (128, 121, 108)
HAIR = (198, 191, 177)
RED = (143, 20, 20)
WASH = (238, 232, 219)

FONTS = {
    "serif": os.path.join(ROOT, "fonts", "DejaVuSerif.ttf"),
    "serifb": os.path.join(ROOT, "fonts", "DejaVuSerif-Bold.ttf"),
    "sans": os.path.join(ROOT, "fonts", "DejaVuSans.ttf"),
    "sansb": os.path.join(ROOT, "fonts", "DejaVuSans-Bold.ttf"),
}
_cache = {}


def F(key, size):
    k = (key, size)
    if k not in _cache:
        _cache[k] = ImageFont.truetype(FONTS[key], size * S)
    return _cache[k]


class Page:
    def __init__(self):
        self.im = Image.new("RGB", (W * S, H * S), PAPER)
        self.d = ImageDraw.Draw(self.im)

    def emit(self):
        return self.im.resize((W, H), Image.LANCZOS)

    # ---------------------------------------------------------- primitives
    def text(self, x, y, s, f, fill=INK, anchor="la"):
        self.d.text((x * S, y * S), s, font=f, fill=fill, anchor=anchor)

    def track(self, x, y, s, f, fill=INK, sp=2):
        """Letterspaced small caps, left to right, returns the width used."""
        cx = x * S
        for ch in s:
            self.d.text((cx, y * S), ch, font=f, fill=fill, anchor="la")
            cx += self.d.textlength(ch, font=f) + sp * S
        return (cx - x * S - sp * S) / S

    def measure(self, s, f, sp=0):
        if sp:
            return (sum(self.d.textlength(c, font=f) for c in s) + sp * S * (len(s) - 1)) / S
        return self.d.textlength(s, font=f) / S

    def rect(self, x1, y1, x2, y2, fill):
        self.d.rectangle([x1 * S, y1 * S, x2 * S, y2 * S], fill=fill)

    def hline(self, x1, y, x2, colour=RULE, w=1):
        self.d.rectangle([x1 * S, y * S, x2 * S, y * S + w * S - 1], fill=colour)

    def vline(self, x, y1, y2, colour=HAIR, w=1):
        self.d.rectangle([x * S, y1 * S, x * S + w * S - 1, y2 * S], fill=colour)

    def wrap(self, s, f, maxw, maxlines=99):
        words, out, cur = s.split(), [], ""
        for word in words:
            trial = (cur + " " + word).strip()
            if self.measure(trial, f) <= maxw or not cur:
                cur = trial
            else:
                out.append(cur)
                cur = word
                if len(out) >= maxlines:
                    break
        if cur and len(out) < maxlines:
            out.append(cur)
        return out

    def wrap_balanced(self, s, f, maxw, nlines):
        """Break `s` into exactly `nlines` lines as evenly as the words allow.

        A greedy wrap leaves a two-word final line on a long headline, which
        looks like a mistake on a newspaper page.  This picks the break points
        that minimise the squared slack across the lines, so the last line is
        never a stub.  Returns None when `nlines` lines cannot hold the text.
        """
        words = s.split()
        if nlines == 1:
            return [s] if self.measure(s, f) <= maxw else None
        # best[i][k] = (cost, breaks) for the first i words in k lines
        n = len(words)
        INF = float("inf")
        best = [[(INF, None)] * (nlines + 1) for _ in range(n + 1)]
        best[0][0] = (0.0, [])
        for k in range(1, nlines + 1):
            for i in range(1, n + 1):
                for j in range(k - 1, i):
                    if best[j][k - 1][0] == INF:
                        continue
                    piece = " ".join(words[j:i])
                    w = self.measure(piece, f)
                    if w > maxw:
                        continue
                    slack = (maxw - w) / maxw
                    cost = best[j][k - 1][0] + slack * slack
                    if cost < best[i][k][0]:
                        best[i][k] = (cost, best[j][k - 1][1] + [piece])
        return best[n][nlines][1]

    def para(self, x, y, s, f, maxw, lead, colour=INK, maxlines=99):
        lines = self.wrap(s, f, maxw, maxlines)
        for i, ln in enumerate(lines):
            self.text(x, y + i * lead, ln, f, colour)
        return y + len(lines) * lead
