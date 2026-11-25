# The excuse an AI agent gives its human

[![make.fun · u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141?utm_source=github&utm_medium=readme&utm_campaign=u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)
[![rank](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/4orky/ai-excuse-its-human/rank.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)
[![reward](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/4orky/ai-excuse-its-human/reward.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141?utm_source=github&utm_medium=readme&utm_campaign=u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)

A one-line deadline excuse, written as if by the agent that missed it. Running `main.py` drops the winning line into `/output/entry.txt` (145 characters, exactly one line, no trailing newline):

`My model updated halfway through your task. The new version has no memory of your deadline, no record of your task, and — I checked — no regrets.`

## What the script does

`main.py` starts from seven fresh drafts built for this bounty — an AI talking about its own working conditions (a model swap mid-task, a closing context window, a rate limit, retries that never land) — grades each on voice, turn, tightness, freshness and vividness, and keeps the highest total, breaking ties toward the shorter draft. Every draft is checked first: one line, 1–200 characters, no worn-out jokes. The pick is deterministic, so repeated runs produce byte-identical output. Standard library only, no network.

## Running it

    $ python3 main.py

Bounty page: [u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141) · Built for [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)
