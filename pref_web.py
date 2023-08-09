from flask import Flask, request, jsonify, make_response
import json
import preference
import logging

app = Flask(__name__)

def check_request_payload(payload_json):
    """Returns 0 if the payload is correct, otherwise returns string with error message"""
    if 'W' in payload_json:
        if 'G' in payload_json['W'] and 'Ve' in payload_json['W'] and 'Vs' in payload_json['W']:
            try:
                if int(payload_json['W']['G']) < 0:
                    return "W:G is negative"
                if int(payload_json['W']['Ve']) < 0:
                    return "W:Ve is negative"
                if int(payload_json['W']['Vs']) < 0:
                    return "W:Vs is negative"
            except ValueError:
                return "One of W parameters are not a number"
        else:
            return "Missing a subsection in W section of the payload"
    else:
        return "No W section found in the payload"
    
    if 'E' in payload_json:
        if 'G' in payload_json['E'] and 'Vw' in payload_json['E'] and 'Vs' in payload_json['E']:
            try:
                if int(payload_json['E']['G']) < 0:
                    return "E:G is negative"
                if int(payload_json['E']['Vw']) < 0:
                    return "E:Vw is negative"
                if int(payload_json['E']['Vs']) < 0:
                    return "E:Vs is negative"
            except ValueError:
                return "One of E parameters are not a number"
        else:
            return "Missing a subsection in E section of the payload"
    else:
        return "No E section found in the payload"
    
    if 'S' in payload_json:
        if 'G' in payload_json['S'] and 'Vw' in payload_json['S'] and 'Ve' in payload_json['S']:
            try:
                if int(payload_json['S']['G']) < 0:
                    return "S:G is negative"
                if int(payload_json['S']['Ve']) < 0:
                    return "S:Ve is negative"
                if int(payload_json['S']['Vw']) < 0:
                    return "S:Vw is negative"
            except ValueError:
                return "One of S parameters are not a number"
        else:
            return "Missing a subsection in S section of the payload"
    else:
        return "No S section found in the payload"
    
    return 0 # everything is fine

@app.route('/api/v1/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    logging.debug(f"Request data: {data}")

    check = check_request_payload(data)
    if check != 0:
        logging.debug(f"Incorrect payload in request: {check}")
        return make_response(json.dumps({'error': check})), 400
    
    params = [] # now add g_w, v_we, v_ws, g_e, v_es, v_ew, g_s, v_se, v_sw
    params.append(int(data['W']['G']))
    params.append(int(data['W']['Ve']))
    params.append(int(data['W']['Vs']))
    params.append(int(data['E']['G']))
    params.append(int(data['E']['Vs']))
    params.append(int(data['E']['Vw']))
    params.append(int(data['S']['G']))
    params.append(int(data['S']['Vw']))
    params.append(int(data['S']['Ve']))
    w, e, s = preference.calculate_score(*params)

    response_data = {'W': w, 'E': e, 'S': s }
    return jsonify(response_data)