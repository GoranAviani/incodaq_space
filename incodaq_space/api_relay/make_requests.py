import requests

def retrieve_iss_crew_names(**kwargs):
    try:
        result = requests.get("http://api.open-notify.org/astros.json")
    except requests.exceptions.HTTPError as e:
        status_code = result.status_code
        return "error", "status code: {},error: {}".format(status_code, e)
    except requests.exceptions.RequestException as e:
        return "error", "RequestException: {}".format(e)
        # catastrophic error. bail.
    return "success", result

def retrieve_iss_location_now(**kwargs):
    pass

def make_iss_api_call(**kwargs):
    api_functions = {
        "iss_crew_names": retrieve_iss_crew_names,
        "iss_location_now": retrieve_iss_location_now,
    }

    try:
        call_source = kwargs["call_source"]
    except KeyError as e:
        return "error", e

    result_status, result = api_functions[call_source](**kwargs)
    ###


    if call_source == "iss_location_now":
        try:
            result = requests.get("http://api.open-notify.org/iss-now.json")
            result.raise_for_status()
        except requests.exceptions.Timeout:
        # Maybe set up for a retry, or continue in a retry loop
            return "error", "The call had timeout"
        except requests.exceptions.TooManyRedirects:
        # Tell the user their URL was bad and try a different one
            return "error", "Too many redirects"
        except requests.exceptions.RequestException as e:
            return "error", "Other error"
            # catastrophic error. bail.

        return result.status_code, result.json()