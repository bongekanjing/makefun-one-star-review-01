# Notes — One-Star Review of Something Essential (run log)

Competition: `u-0xb3e689-one-star-review-of-something-essential-c7234629` ("One-Star Review of Something Essential", $5 = $1 x 5 places, deadline 2026-11-26T22:20:00Z / 27 Nov 05:20 WIB). Opens 2026-11-23T22:21:01Z. Blind rounds: 6, next 2026-11-24T10:20:50Z. Result due 2026-12-19T02:20:00Z.

## Spec (from kit competition.yaml + requirements)
- Program writes one text to `/output/entry.txt`. Gate: UTF-8, 1–160 chars, not only whitespace.
- Entry: one single-line deadpan one-star review, max 160 chars, of an everyday essential (sun, gravity, sleep, water, oxygen, Mondays...).
- Judge (z-ai/glm-5.3-flash, pairwise, no ties, margin 1–5, each pair in both orders): 1) is a one-star review of an everyday essential, deadpan, unmistakably about the thing itself; 2) sharpest true grievance, small daily annoyance everyone recognises but never seen written down; 3) holds the deadpan, no winking, no explaining, no exclamation marks; 4) turns in the last few words; 5) tight and specific, one joke, no filler, no second joke.
- Requirements: repo_url + commit_sha + bundle required; LICENSE required; main.py required. Harness program/v1. 3 fixed anchor texts judged alongside; byte-identical copy of one plays as that text and never enters the playoff.
- Quota: max 5 submissions/entrant/UTC day.

## Candidates brainstormed (all single-line, deadpan)
1. Gravity: "Gravity dropped my phone face-down again. It never apologises and it never lets go." (83 chars) — PICKED
2. Sleep: "Slept eight hours and woke up tired. Product does not work as advertised." (73)
3. Sun: "The sun has no off switch, no dimmer, and shows up uninvited every morning. One star." (85)
4. Water: "Water has no taste, no colour, and still manages to leak everywhere. Would not drink again." (91)
5. Mondays: "Monday arrives every week whether I want it or not, and brings no apology and no refund." (88)
6. Oxygen: "Oxygen is free, invisible, and impossible to return. I have used it daily and I am still tired." (95)

## Entry (picked: Gravity)
> Gravity dropped my phone face-down again. It never apologises and it never lets go.

83 chars, 1 line. Why it wins the brief: the grievance (phone always lands face-down) is a small daily annoyance everyone recognises; deadpan throughout, no exclamation, no wink; the turn lands in the last three words ("never lets go" — literal gravity, and a clingy-ex read); one joke, tight, specific, unmistakably about gravity itself. Sleep was rejected as the most common angle (likely duplicated across entries); sun/water/Mondays/oxygen each carry filler or a second joke.

## Build flow
- Requirements fetched via curl + x-api-key (from ~/.makefun/credentials via python, key never printed): repo_url + commit_sha + bundle required.
- Kit downloaded to file (200, 7,942,927 bytes), gzip verified, extracted with tar xzf (never curl | tar).
- main.py pure stdlib, writes /output/entry.txt, tested with python3 -I main.py; entry verified byte-for-byte.
- thinking_revised gate: main.py edited in a second message (named constant + comment explaining the choice), output re-verified BYTE-IDENTICAL.
- Repo: bongekanjing/makefun-one-star-review-01, pushed via agent4-vm push-repo.sh, About fixed, ls-remote verified.
- BUILDER ONLY: no `makefun record`, no bundle, no submit — coordinator bundles + submits after this run (usage rows only exist in muse.db after the builder finishes).
