import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "qr"))

try:
    import make_qr
    from PIL import Image
except ImportError:
    make_qr = None


@unittest.skipIf(make_qr is None, "pip install -r qr/requirements.txt to run the QR tests")
class QR(unittest.TestCase):
    def test_writes_a_square_png(self):
        out = Path(tempfile.mkdtemp()) / "qr.png"
        make_qr.main("https://example.org/rsvp", str(out))
        with Image.open(out) as img:
            self.assertEqual(img.format, "PNG")
            self.assertEqual(img.size[0], img.size[1])
            self.assertGreaterEqual(img.size[0], 400)

    def test_longer_links_make_bigger_codes(self):
        d = Path(tempfile.mkdtemp())
        make_qr.main("https://example.org/r", str(d / "a.png"))
        make_qr.main("https://example.org/" + "x" * 200, str(d / "b.png"))
        with Image.open(d / "a.png") as a, Image.open(d / "b.png") as b:
            self.assertGreater(b.size[0], a.size[0])


if __name__ == "__main__":
    unittest.main()
