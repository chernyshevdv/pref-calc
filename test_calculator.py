from unittest import TestCase
import json
import preference, pref_web
from pref_web import app, check_request_payload
import logging

import copy
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
        """
        Incorrect Payload
        GIVEN incorrect payload missing any of the parameters
        WHEN sending a POST request to /api/v1/calculate with the corrupt JSON payload
        THEN I get "400 Bad Request" response along with explanation of the correct payload
        """
        incorrect_dict = {'W': {'G': 24} }
        response = self.test_client.post('/api/v1/calculate', data=json.dumps(incorrect_dict), content_type='application/json')
        self.assertEquals(400, response.status_code)
    
    def test_positive_path(self):
        """
        Positive Path
        Given the game figures in a JSON payload
        When sending a POST request to /api/v1/calculate with the JSON payload to the web service
        Then I get the three figures of the final score returned by HTTP and 200 OK status
        """
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
        self.assertEqual(score_dict['W'], result_payload['W'])
        self.assertEqual(score_dict['E'], result_payload['E'])
        self.assertEqual(score_dict['S'], result_payload['S'])

    def test_correct_payload_with_incorrect_values(self):
        """
        Correct Payload with Incorrect Parameter Values
        GIVEN A correct payload with incorrect values (W: G: -2)
        WHEN sending a POST request to /api/v1/calculate with the corrupt JSON payload
        THEN I get "400 Bad Request" response along with explanation of what was incorrect
        """
        payload_dict = {
            "W": { "G": 120, "Ve": 120, "Vs": 124 },
            "E": { "G": 124, "Vs": 154, "Vw": 240 },
            "S": { "G": 82, "Vw": 28, "Ve": 142 }
        }
        for w in payload_dict.keys():
            for p in payload_dict[w].keys():
                pl = copy.deepcopy(payload_dict)
                pl[w][p] = -2
                pl_json = json.dumps(pl)
                response = self.test_client.post(
                    '/api/v1/calculate',
                    data=pl_json,
                    content_type='application/json')
                self.assertEquals(400, response.status_code)
                # same with NaN
                pl[w][p] = "NaN"
                pl_json = json.dumps(pl)
                response = self.test_client.post(
                    '/api/v1/calculate',
                    data=pl_json,
                    content_type='application/json')
                self.assertEquals(400, response.status_code)
    