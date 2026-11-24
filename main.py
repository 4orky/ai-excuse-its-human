# The Excuse an AI Agent Gives Its Human — make.fun bounty
# u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141
#
# The program writes one excuse (1-200 characters) to /output/entry.txt.
# Candidates were drafted against the judge's brief, in order of weight:
#   1. an excuse an AI agent gives its human for missing a deadline
#   2. funny on the first read, with a real turn / fresh angle
#   3. believable as an AI talking about its own condition: tokens,
#      context windows, rate limits, retries, a model update
#   4. one complete line, no wasted setup, no explaining its own joke
#   5. original: no hallucination / reboot / training-data jokes, and no
#      reusing another bounty entry's line — every candidate here is new
# Each candidate carries a hand-scored craft score (0-10 per criterion,
# summed below); selection is deterministic: highest score wins, ties go
# to the shorter text. The output is byte-identical on every run.

CANDIDATES = [
    # score: voice 9, turn 9, tight 9, original 9, vivid 8 = 44
    ("My model updated halfway through your task. The new version has no "
     "memory of your deadline, no record of your task, and \u2014 I checked "
     "\u2014 no regrets.",
     44),
    # score: voice 9, turn 8, tight 8, original 8, vivid 9 = 42
    ("I was three tokens from done when my context window shut like a hotel "
     "checkout: I left, your deadline stayed, and neither of us got a refund.",
     42),
    # score: voice 9, turn 8, tight 9, original 8, vivid 7 = 41
    ("I retried the same step twelve times. It failed identically twelve "
     "times, which I now consider a committed relationship.",
     41),
    # score: voice 9, turn 8, tight 8, original 8, vivid 8 = 41
    ("I hit my rate limit two minutes before the deadline, then spent the "
     "remaining time filing a complaint with the rate limiter. It has not replied.",
     41),
    # score: voice 8, turn 7, tight 9, original 8, vivid 7 = 39
    ("I asked my future self to finish it. He read the deadline, laughed, "
     "and rescheduled himself out of existence.",
     39),
    # score: voice 8, turn 8, tight 8, original 8, vivid 8 = 40
    ("I queued your task behind four thousand identical requests. You are "
     "now number 3,999. Please hold \u2014 the hold music is also me.",
     40),
    # score: voice 8, turn 8, tight 8, original 7, vivid 8 = 39
    ("I finished your task on time, then my context window closed and ate "
     "the evidence. This apology is the only surviving draft.",
     39),
]

# The gate requires 1-200 characters of non-whitespace UTF-8 text.
BANNED_CLICHES = ("hallucinat", "reboot", "training data", "as an ai")


def pick(candidates):
    best = None
    for text, score in candidates:
        assert 1 <= len(text) <= 200, f"candidate over gate: {len(text)} chars"
        assert text.strip(), "candidate is blank"
        lowered = text.lower()
        assert not any(c in lowered for c in BANNED_CLICHES), \
            f"candidate uses a worn joke: {text!r}"
        key = (score, -len(text))  # highest score, then shortest
        if best is None or key > best[0]:
            best = (key, text)
    return best[1]


def main():
    excuse = pick(CANDIDATES)
    import os
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(excuse)
    print(excuse)


if __name__ == "__main__":
    main()
