from unittest import TestCase
import preference

class TestCalculateScore(TestCase):
    def test_correct_calculation(self):
        """Test positive scenario"""
        Gw, Vwe, Vws = 322, 120, 124
        Ge, Ves, Vew = 124, 154, 240
        Gs, Vsw, Vse = 82, 28, 142

        w, e, s = preference.calculate_score(Gw, Vwe, Vws, Ge, Ves, Vew, Gs, Vsw, Vse)
        self.assertEqual((w, e, s), (-1484, 652, 832))