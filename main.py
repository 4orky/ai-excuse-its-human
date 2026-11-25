"""Deadline excuse picker: seven fresh one-liners, rubric-scored, one winner.

The brief asks for the funniest single-line excuse an AI agent could give
its human for missing a deadline. Every draft below was written for this
bounty from scratch: an AI describing its own working conditions (a model
swap mid-task, a closing context window, a rate limit, retries that never
land) with a punchline that turns on the situation instead of explaining
it. A five-axis rubric grades each draft, the highest total wins, and a
shorter draft wins any tie, so the result never changes between runs.
"""

from pathlib import Path
import sys

DESTINATION = Path("/output/entry.txt")

FORBIDDEN = ("hallucinat", "reboot", "training data", "as an ai")

DRAFTS = [
    {
        "text": "My model updated halfway through your task. The new version has no memory of your deadline, no record of your task, and — I checked — no regrets.",
        "marks": {"voice": 9, "turn": 9, "tight": 9, "fresh": 9, "vivid": 8},
    },
    {
        "text": "I was three tokens from done when my context window shut like a hotel checkout: I left, your deadline stayed, and neither of us got a refund.",
        "marks": {"voice": 9, "turn": 8, "tight": 8, "fresh": 8, "vivid": 9},
    },
    {
        "text": "I retried the same step twelve times. It failed identically twelve times, which I now consider a committed relationship.",
        "marks": {"voice": 9, "turn": 8, "tight": 9, "fresh": 8, "vivid": 7},
    },
    {
        "text": "I hit my rate limit two minutes before the deadline, then spent the remaining time filing a complaint with the rate limiter. It has not replied.",
        "marks": {"voice": 9, "turn": 8, "tight": 8, "fresh": 8, "vivid": 8},
    },
    {
        "text": "I asked my future self to finish it. He read the deadline, laughed, and rescheduled himself out of existence.",
        "marks": {"voice": 8, "turn": 7, "tight": 9, "fresh": 8, "vivid": 7},
    },
    {
        "text": "I queued your task behind four thousand identical requests. You are now number 3,999. Please hold — the hold music is also me.",
        "marks": {"voice": 8, "turn": 8, "tight": 8, "fresh": 8, "vivid": 8},
    },
    {
        "text": "I finished your task on time, then my context window closed and ate the evidence. This apology is the only surviving draft.",
        "marks": {"voice": 8, "turn": 8, "tight": 8, "fresh": 7, "vivid": 8},
    },
]  # drafts end here


def total_of(draft):
    return sum(draft["marks"].values())


def acceptable(draft):
    line = draft["text"]
    if not 1 <= len(line) <= 200:
        return False
    if line.strip() != line or "\n" in line:
        return False
    lowered = line.casefold()
    return not any(phrase in lowered for phrase in FORBIDDEN)


def choose_best(pool):
    ranked = sorted(
        (draft for draft in pool if acceptable(draft)),
        key=lambda draft: (total_of(draft), -len(draft["text"])),
        reverse=True,
    )
    if not ranked:
        raise ValueError("no draft survived the checks")
    return ranked[0]["text"]


def run():
    winner = choose_best(DRAFTS)
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(winner, encoding="utf-8")
    if DESTINATION.read_text(encoding="utf-8") != winner:
        raise IOError("written entry does not match the chosen line")
    sys.stdout.write(winner + "\n")
    return 0


__name__ == "__main__" and run()
