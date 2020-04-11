import requests
from incodaq_space.logging_is import api_errors

def retrieve_iss_crew_names(**kwargs):
    try:
        result = requests.get("http://api.open-notify.org/astros.json")
        result.raise_for_status()
    except requests.exceptions.HTTPError as e:
        status_code = result.status_code
        api_errors.error("{}".format("status code: {},error: {}".format(status_code, e)))
    except requests.exceptions.RequestException as e:
        api_errors.error("{}".format(e))
    else:
        return result

def retrieve_iss_location_now(**kwargs):
    try:
        result = requests.get("http://api.open-notify.org/iss-now.json")
        result.raise_for_status()
    except requests.exceptions.HTTPError as e:
        status_code = result.status_code
        api_errors.error("{}".format( "status code: {},error: {}".format(status_code, e)))
    except requests.exceptions.RequestException as e:
        api_errors.error("{}".format(e))
    else:
        return result

def make_iss_api_call(**kwargs):
    api_functions = {
        "iss_crew_names": retrieve_iss_crew_names,
        "iss_location_now": retrieve_iss_location_now,
    }
    try:
        call_source = kwargs["call_source"]
    except KeyError as e:
        api_errors.error("{}".format("Location: make_iss_api_call. Field producing error: {}" .format(e)))
    else:
        #returns result object if response status code is 200
        result = api_functions[call_source](**kwargs)
        return result
