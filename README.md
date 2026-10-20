# club-kit

Tools any student organization can use to run events and keep track of members. Built by LITSA at Suffolk Law from what we needed for our own events, and written so other clubs, at Suffolk or anywhere, can reuse it.

**Who it's for:** club officers who want events to run smoothly without reinventing the checklist every semester. Most of it is written guides; the tools are small scripts you can run in a browser-based Codespace without installing anything.

## What's here

| Piece | What it does | Status |
|---|---|---|
| [Event checklist](docs/event-checklist.md) | Every step for a Suffolk Law student-org event, from six weeks out to the follow-up, with who to contact | Ready |
| [RSVP with a short link](docs/rsvp.md) | An RSVP form plus a short link you print once and repoint for each event | Ready |
| [QR codes](qr/) | A print-quality QR code for any link | Ready |
| Flyers | Instagram post and story, letter, poster and TV sizes from one event description | Planned ([#1](https://github.com/suffolklitsa/club-kit/issues/1)) |
| Newsletter | An email template that survives Outlook | Planned ([#2](https://github.com/suffolklitsa/club-kit/issues/2)) |
| Roster | Turn sign-in sheets into a clean member list and reconcile it with your mailing list | Planned ([#3](https://github.com/suffolklitsa/club-kit/issues/3), [#4](https://github.com/suffolklitsa/club-kit/issues/4)) |

## Quick start

**Plan an event:** open the [event checklist](docs/event-checklist.md) and copy it into your club's shared notes. Work through it from the top; the deadlines are counted back from the event date.

**Make a QR code for your RSVP link:**

1. Click **Code → Codespaces → Create codespace on main** (free with a GitHub account).
2. In the terminal:
   ```
   pip install -r qr/requirements.txt
   python3 qr/make_qr.py https://yourclub.org/rsvp rsvp-qr.png
   ```
3. Download `rsvp-qr.png` from the file list.

## Using it at another school

The checklist names Suffolk Law offices (the Dean of Students, Professional and Career Development, Media Services). Swap in your school's equivalents; the steps and timing carry over. The tools don't depend on Suffolk at all. If you adapt the checklist for your school, we'd welcome it as a pull request: see [#7](https://github.com/suffolklitsa/club-kit/issues/7).

## Member data stays out

Names, emails, sign-in sheets and mailing lists never go in this repository, not even in a branch. Tools that handle member data work on files on your own computer and are tested with made-up examples only.

## Contributing

Pick an issue labeled [`good first issue`](https://github.com/suffolklitsa/club-kit/labels/good%20first%20issue) or [`no code needed`](https://github.com/suffolklitsa/club-kit/labels/no%20code%20needed), comment to claim it, and read [CONTRIBUTING.md](CONTRIBUTING.md). Questions go in the Build topic on the LITSA GroupMe, or comment on the issue.

## Roadmap and decisions

[docs/ROADMAP.md](docs/ROADMAP.md) · [docs/DECISIONS.md](docs/DECISIONS.md)

## Licenses

Code is [MIT](LICENSE). Written guides are [CC BY 4.0](LICENSE-docs.md). LITSA's own logo and typeface aren't part of club-kit; the flyer tools will ship with a neutral theme any club can recolor.
