"""Make a print-quality QR code PNG for a link.

    pip install "qrcode[pil]"
    python3 make_qr.py https://suffolklitsa.org/rsvp rsvp-qr.png
"""
import sys
from urllib.parse import urlparse

import qrcode


def check_args(url: str, out: str) -> None:
    """Stop with a plain message when the two arguments look wrong."""
    if url.endswith(".png") and out.startswith("http"):
        sys.exit("the arguments look swapped. Use: make_qr.py URL OUTPUT.png")
    if urlparse(url).scheme not in ("http", "https"):
        sys.exit(f"{url} is not a web link. Put https:// in front, as in https://example.org/rsvp")
    if not out.endswith(".png"):
        sys.exit(f"{out} does not end in .png. Name the file something like rsvp-qr.png")


def main(url: str, out: str, box: int = 20) -> None:
    check_args(url, out)
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=box, border=2)
    qr.add_data(url)
    qr.make(fit=True)
    qr.make_image(fill_color="black", back_color="white").save(out)
    print(f"wrote {out} for {url}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("usage: make_qr.py URL OUTPUT.png")
    main(sys.argv[1], sys.argv[2])
