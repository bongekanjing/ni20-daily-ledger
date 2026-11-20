"""The day's reporting, compiled from wire copy published on 20 November 2026.

Every count printed on the page is derived from the lists below, so the
arithmetic cannot disagree with itself.

Copy rules used throughout: anything the wires had not yet confirmed by the
time this page was drawn is written as a forecast or as what an official said
("the army said", "IMD forecast"), never as settled fact.  Where two sides
disagree, both are given.
"""

REGIONS = [
    ("AMERICAS", (26, 71, 111)),
    ("EUROPE", (94, 42, 84)),
    ("MIDDLE EAST", (138, 44, 30)),
    ("AFRICA", (54, 96, 44)),
    ("SOUTH ASIA", (166, 116, 28)),
    ("EAST ASIA", (35, 86, 88)),
    ("PACIFIC", (52, 54, 96)),
    ("GLOBAL", (48, 48, 48)),
]

LEADS = [
    ("SOUTH ASIA", "ODISHA",
     "Three lakh evacuated as Cyclone Akvan closes on Gopalpur",
     "The IMD forecast the severe cyclonic storm would cross the coast near "
     "Haripur, east of Gopalpur, on Friday afternoon with winds of 90-100 kmph "
     "gusting to 110. Odisha has moved more than 3 lakh people, including 4,170 "
     "pregnant women, into 9,341 shelters and cancelled 47 trains.",
     "akvan"),
    ("EUROPE", "BERLIN",
     "Moscow accepts a multilateral meeting, Kushner tells Kyiv's allies",
     "At the Coalition of the Willing summit the US envoy said Russia had agreed "
     "to sit down with European leaders and to security guarantees modelled on "
     "NATO's Article 5. Merz said he was ready to meet Putin at a neutral venue. "
     "Putin ruled out ceasefire talks after the strike on the Crimean Bridge.",
     "berlin"),
    ("MIDDLE EAST", "HORMUZ",
     "Two tankers burn after striking mines east of the strait, Iran's army says",
     "The Iranian navy said one vessel was crossing a restricted area with its "
     "navigation switched off when it hit a mine; a second had been hit earlier. "
     "Tehran urged ships to use its designated routes and said it had struck "
     "more than 140 vessels since the war began on 28 February.",
     "hormuz"),
]

BRIEFS = [
    ("AMERICAS", "Washington", "The House voted 211-204 to send articles of "
     "impeachment against defence secretary Pete Hegseth to the Judiciary "
     "Committee, shelving them for the rest of this Congress. Thomas Massie, "
     "who brought them, was the only Republican opposed; 11 Democrats missed "
     "the vote."),
    ("AMERICAS", "White House", "Trump was due to hold a press conference at "
     "noon Eastern on his Asia trip, which he announced on Truth Social after "
     "returning from Shenzhen."),
    ("AMERICAS", "Baseball", "Trump said he had posthumously pardoned Pete "
     "Rose, baseball's all-time hits leader, who pleaded guilty in 1990 to two "
     "counts of filing false tax returns. Rose died in 2024."),
    ("AMERICAS", "Labour", "Americans filing for unemployment benefits rose by "
     "1,000 to 203,000 last week, the Labor Department reported."),
    ("AMERICAS", "Wall Street", "All three indexes closed more than 2% lower on "
     "Thursday, the S&P 500's sixth straight loss, as the war and the Iran "
     "timeline weighed on sentiment."),

    ("EUROPE", "Kyiv", "Russian drones and anti-ship missiles struck 18 "
     "locations; debris shattered windows at St Volodymyr's Cathedral and "
     "damaged the Dutch and Austrian embassies. One man was killed and five "
     "people injured, the mayor said."),
    ("EUROPE", "Paris", "UNESCO launched the 2026 Global Report on Early "
     "Childhood Care and Education on World Children's Day, alongside a "
     "regional edition for the Arab States."),
    ("EUROPE", "Vienna", "The IAEA Board of Governors closed its November "
     "session with the EU and Iran still divided over Tehran's safeguards "
     "obligations under the NPT."),

    ("MIDDLE EAST", "Ramallah", "The Palestinian Foreign Ministry said more "
     "than 22,000 children have been killed and over 45,000 injured in Gaza "
     "since October 2023."),
    ("MIDDLE EAST", "Taiz", "The toll from a strike on a guesthouse in "
     "Al-Mukha rose to 19 dead and injured, a health official said, as "
     "protests were held in Hodeidah."),
    ("MIDDLE EAST", "United Nations", "A seventh session of the conference on a "
     "Middle East zone free of nuclear weapons and other weapons of mass "
     "destruction closed in New York without an agreed text."),

    ("AFRICA", "Middelburg", "Acting President Paul Mashatile launched the 16 "
     "Days of Activism campaign against gender-based violence, which runs from "
     "25 November to 10 December."),
    ("AFRICA", "Mombasa", "The Africa Festival of Pensions closed with the "
     "public launch of the Women in Pensions Initiative and its first list of "
     "100 women."),

    ("SOUTH ASIA", "Bhopal", "India dedicated its first H5N1 vaccine for "
     "poultry at the ICAR-National Institute of High Security Animal Diseases, "
     "the government said."),
    ("SOUTH ASIA", "Goa", "The International Film Festival of India opened in "
     "Panaji for its 57th edition."),

    ("EAST ASIA", "Shenzhen", "APEC's 21 member economies issued a joint "
     "statement closing the 37th Ministerial Meeting, welcoming a statement on "
     "the Free Trade Area of the Asia-Pacific agenda and conceding that more "
     "work remains on integration."),
    ("EAST ASIA", "Beijing", "The People's Bank of China set its loan prime "
     "rates, with most economists surveyed expecting no change."),

    ("PACIFIC", "Suva", "Fiji's health ministry took delivery of about $1m of "
     "medical equipment for rural facilities at a handover in Vatuwaqa."),

    ("GLOBAL", "World Children's Day", "The day was marked with new financing "
     "figures for early childhood care, which UNESCO said still leaves millions "
     "of children under eight without quality pre-primary education."),
    ("GLOBAL", "Aid", "UNICEF and the OECD joined the Paris launch, warning "
     "that financing gaps are widest in low-income and conflict-affected "
     "states."),

    ("SOUTH ASIA", "Delhi", "Narendra Modi opened the first SCO Civilisational "
     "Dialogue Forum at Purana Qila, a three-day meeting on culture, art, "
     "language and philosophy. Pakistan sent its climate minister, Musadik "
     "Masood Malik."),
    ("EAST ASIA", "Tokyo", "Japan signed a deal with Vietnam on a new "
     "training-and-employment system for Vietnamese workers, the labour "
     "ministry said."),
    ("SOUTH ASIA", "Islamabad", "Pakistan and Sweden held the 20th round of their "
     "bilateral political consultations in Islamabad, led for Pakistan by "
     "Ambassador Ayesha Ali."),
    ("AMERICAS", "Denver", "A federal judge in Denver heard arguments on the "
     "administration's bid to lift protections for Venezuelan migrants, a case "
     "the Justice Department has asked the Supreme Court to settle."),
]

NUMBERS = [
    ("3 lakh", "people evacuated in Odisha before landfall"),
    ("9,341", "cyclone shelters readied, 2,623 of them open"),
    ("47", "trains cancelled, 28 rescheduled"),
    ("22,000", "children killed in Gaza, its ministry says"),
    ("203,000", "US jobless claims last week, up 1,000"),
    ("18", "locations struck across Ukraine on Thursday"),
    ("211", "to 204: the vote shelving Hegseth articles"),
    ("19", "dead and injured in a strike on Taiz"),
]


def stories():
    """Every story printed on the page, leads first."""
    out = [(r, k, h + ". " + d) for (r, k, h, d, _a) in LEADS]
    out.extend(BRIEFS)
    return out


def counts():
    """Region name -> number of stories under it. Sums to len(stories())."""
    c = {name: 0 for name, _col in REGIONS}
    for region, _k, _t in stories():
        c[region] += 1
    return c
