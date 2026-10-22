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

    def test_good_link_and_png_name_pass(self):
        self.assertIsNone(make_qr.check_args("https://example.org/rsvp", "rsvp-qr.png"))

    def test_link_without_https_stops(self):
        with self.assertRaises(SystemExit) as caught:
            make_qr.check_args("example.org/rsvp", "rsvp-qr.png")
        self.assertIn("https://", str(caught.exception))

    def test_output_name_must_end_in_png(self):
        with self.assertRaises(SystemExit) as caught:
            make_qr.check_args("https://example.org/rsvp", "rsvp.jpg")
        self.assertIn(".png", str(caught.exception))

    def test_swapped_arguments_stop(self):
        with self.assertRaises(SystemExit) as caught:
            make_qr.check_args("rsvp-qr.png", "https://example.org/rsvp")
        self.assertIn("swapped", str(caught.exception))

    def test_main_stops_on_a_bad_link(self):
        with self.assertRaises(SystemExit):
            make_qr.main("example.org/rsvp", "rsvp-qr.png")


if __name__ == "__main__":
    unittest.main()
