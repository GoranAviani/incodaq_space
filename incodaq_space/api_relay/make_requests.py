import requests

def make_iss_api_call(**kwargs):
    try:
        call_source = kwargs["call_source"]
    except:
        pass
        #TODO log failure to retrieve call_source
        #return error message

    if call_source == "iss_crew_names":
        try:
            result = requests.get("http://api.open-notify.org/astros.json1")
            result.raise_for_status()
        except requests.exceptions.Timeout:
        # Maybe set up for a retry, or continue in a retry loop
            return "error", "The call had timeout"
        except requests.exceptions.TooManyRedirects:
        # Tell the user their URL was bad and try a different one
            return "error", "Too many redirects"
        except requests.exceptions.RequestException as e:
            return "error", "Error: {} ,in iss_crew_names" .format(result.status_code)
            # catastrophic error. bail.

    elif call_source == "iss_location_now":
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