# Contributing to club-kit

The org-wide guide is at [suffolklitsa/.github](https://github.com/suffolklitsa/.github/blob/main/CONTRIBUTING.md). This page covers what's specific here.

## Rules for this repo

- **No member data, ever.** Test with invented names and `example.edu` addresses. If you commit real data by accident, tell a maintainer right away; deleting it in a later commit isn't enough.
- **Works for any club.** Keep Suffolk- or LITSA-specific details in clearly marked spots (a settings file, a "Suffolk Law" note) so another school can swap them.
- **Small tools, few dependencies.** Each tool lives in its own folder with a README and a `requirements.txt` if it needs packages.
- **Guides are written to be followed.** Numbered steps, who to contact, and how far ahead.

## Checks

```
pip install -r qr/requirements.txt
python3 -m unittest discover -s tests
```

CI runs the same on every pull request.
