import requests

def make_iss_api_call(**kwargs):
    try:
        call_source = kwargs["call_source"]
    except:
        pass
        #TODO log failure to retrieve call_source
        #return error message

    if call_source == "iss_crew_names":
        result = requests.get("http://api.open-notify.org/astros.json")
        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as e:
            # Whoops it wasn't a 200
            return result.status_code, "Error: " + str(e)

    elif call_source == "iss_location_now":
        result = requests.get("http://api.open-notify.org/iss-now.json")
        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as e:
            # Whoops it wasn't a 200
            return result.status_code, "Error: " + str(e)

    return result.status_code, result.json()