# Supercell Tags Algorithm

A Python implementation of the **Supercell Tags Algorithm**, used across all Supercell games  
(Clash of Clans, Clash Royale, Brawl Stars, Boom Beach, Hay Day, etc.)  
to convert between **internal IDs** and their **public tags**.

---

## How it works
Supercell encodes IDs into tags using a custom base-14 alphabet:

0289PYLQGRJCUV

- Every player, clan, or club has an internal ID = (lowID * 256) + highID.
- That integer is converted into base-14 using the alphabet above.
- The result is the tag you see in-game (always prefixed with #).

Examples:
- (highID=0, lowID=1) → #2PP (the very first player ever created).
- (highID=0, lowID=2) → #8GG.
- (highID=0, lowID=3) → #9UU.

---

## Features
- Normalize tags (#, case-insensitive, replace O with 0)
- Convert tag → (highID, lowID)
- Convert (highID, lowID) → tag
- Pure Python, no external dependencies

---

## Quick Reference Table

Here are the first few IDs and their corresponding tags:

High ID | Low ID | Internal ID | Tag
------- | ------ | ----------- | ----
0       | 1      | 1           | #2PP
0       | 2      | 2           | #8QR
0       | 3      | 3           | #9UU
0       | 4      | 4           | #Y98
0       | 5      | 5           | #L9C
0       | 6      | 6           | #QJG
0       | 7      | 7           | #GR0
0       | 8      | 8           | #R2C
0       | 9      | 9           | #J8Y
0       | 10     | 10          | #C9P

(Internal ID = lowID * 256 + highID)

---

## Lookup Files
This repo also includes pre-generated CSV and JSON files  
containing the first 1000 mappings (highID, lowID → tag) for quick reference.
