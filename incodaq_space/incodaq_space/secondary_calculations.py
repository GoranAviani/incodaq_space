import json

def api_response_to_string(api_response):
    return json.dumps(api_response.json())