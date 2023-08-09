from unittest import TestCase
import json
import preference
from pref_web import app

class TestCalculateScore(TestCase):
    def test_correct_calculation(self):
        """Test positive scenario"""
        Gw, Vwe, Vws = 322, 120, 124
        Ge, Ves, Vew = 124, 154, 240
        Gs, Vsw, Vse = 82, 28, 142

        w, e, s = preference.calculate_score(Gw, Vwe, Vws, Ge, Ves, Vew, Gs, Vsw, Vse)
        self.assertEqual((w, e, s), (-1484, 652, 832))

class TestWebCalculator(TestCase):
    def setUp(self):
        self.test_client = app.test_client()
    
    def test_incorrect_payload(self):
        """Incorrect payload should yield response with 400 Bad Reuqest status"""
        response = self.test_client.post('/api/v1/calculate')
        self.assertEquals(400, response.status_code)
    
    def test_positive_path(self):
        payload_dict = {
            "W": { "G": 322, "Ve": 120, "Vs": 124 },
            "E": { "G": 124, "Vs": 154, "Vw": 240 },
            "S": { "G": 82, "Vw": 28, "Ve": 142 }
        }
        payload_json = json.dumps(payload_dict)
        score_dict = { "W": -1484, "E": 652, "S": 832 }
        score_json = json.dumps(score_dict)
        response = self.test_client.post(
            '/api/v1/calculate',
            data=payload_json,
            content_type='application/json'
        )
        self.assertEquals(200, response.status_code)
        result_payload = response.get_json()
        self.assertEquals(score_json, result_payload)


    