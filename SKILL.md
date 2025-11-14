---
name: clock
description: Provides current timestamp and temporal awareness for Claude
---

# Clock Skill

This skill provides current timestamp information when Claude needs temporal awareness.

## When to use
- When discussing timing or duration
- When user asks about time
- When temporal context would improve response
- When documenting events with timestamps

## Usage
Call get_current_time() to retrieve:
- Current UTC time
- Local time (America/Toronto)
- Unix timestamp
- Human-readable format

## Output format
Returns dictionary with:
- utc: ISO format UTC timestamp
- local: ISO format local timestamp (Toronto)
- unix: Unix epoch timestamp
- readable: Human-friendly format
