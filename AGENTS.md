# AGENTS.md

Instructions for AI coding agents working in this repo, and for the people using them. Read README.md and CONTRIBUTING.md too.

## What this repo is

Guides and small tools any student organization can use: the event checklist, RSVP short links, a QR code maker, and (planned) flyers, a newsletter template and roster tools.

## Commands

```
pip install -r qr/requirements.txt
python3 -m unittest discover -s tests
python3 qr/make_qr.py https://example.org/rsvp qr.png
```

## Rules for this repo

- **Member data never enters the repo,** not in tests, samples or screenshots. Roster tools run on files on the user's own computer.
- **Works for any club.** Keep Suffolk- and LITSA-specific details in clearly marked places so another school can swap them.
- **No LITSA identity.** Visual tools use the neutral theme; LITSA's torch, wordmark and typeface stay in suffolklitsa/design-system.
- **Each tool in its own folder,** with a README and its own `requirements.txt` if it needs packages.

## Rules for every LITSA repo

- **No secrets.** Never write API keys, tokens or passwords into a file, a commit, an issue or a test. Keys come from environment variables. If you find one committed, stop and tell a maintainer.
- **No personal data.** No real names, emails, student records, sign-in sheets or mailing lists in code, tests, fixtures, screenshots or commit messages. Use made-up examples (`jane.doe@example.edu`).
- **No invented law.** Anything stating a rule, statute, case or requirement must come from a source you can link. Never make up a citation. If you can't find the source, say so in the pull request instead of guessing.
- **Small changes.** One issue per pull request. Don't reformat or rename things the issue didn't ask about.
- **Run the checks** listed above before saying the work is done, and report what they printed. If one fails, fix it or say plainly that it fails.
- **Plain writing.** Docs and messages use short, ordinary sentences a first-year law student would follow.
- **Disclose AI use.** The person opening the pull request notes which AI tools helped, in the description. They own every line either way.
