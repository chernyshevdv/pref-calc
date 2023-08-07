from unittest import TestCase
from preference import calculate_score

class TestCalculateScore(TestCase):
    def test_correct_calculation(self):
        """Test positive scenario"""
        Gw, Vwe, Vws = 322, 120, 124
        Ge, Ves, Vew = 124, 154, 240
        Gs, Vsw, Vse = 82, 28, 142

        w, e, s = calculate_score(Gw, Vwe, Vws, Ge, Ves, Vew, Gs, Vsw, Vse)
        self.assertEqual(w, -1484)
        self.assertEqual(e, 652)
        self.assertEqual(s, 832)

