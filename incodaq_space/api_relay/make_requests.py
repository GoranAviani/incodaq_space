import requests
#from incodaq_space.logging_is import api_errors, api_logs
from incodaq_space.logging_is import api_errors, api_logs
from incodaq_space.constants import ASTRONAUTS_IN_SPACE_URL, ISS_LOCATION_URL

def process_api_response(name_of_call_function, result, url):
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as e:
        status_code = result.status_code
        api_errors.error(("status code: {},error: {}, Function name: {}: Url: {}".format(status_code, e,
                                                                                       name_of_call_function,
                                                                                       url)))
        api_logs.error(("status code: {},error: {}, Function name: {}: Url: {}".format(status_code, e,
                                                                                     name_of_call_function,
                                                                                 url)))

    except requests.exceptions.RequestException as e:
        api_errors.error(("Error: {}, Function name: {}: Url: {}".format(e,
                                                                       name_of_call_function,
                                                                       url)))
        api_logs.error(("Error: {}, Function name: {}: Url: {}".format(e,
                                                                     name_of_call_function,
                                                                     url)))

    else:
        api_logs.info(
        "Function name: {}: Url: {}, result: {}".format(name_of_call_function, url,
                                                       result.json()))
        return result

def fetch_iss_crew_names():
    name_of_call_function = 'fetch_iss_crew_names'
    api_logs.info("Api request: {}: Url: {}".format(name_of_call_function, ASTRONAUTS_IN_SPACE_URL))
    result = requests.get(ASTRONAUTS_IN_SPACE_URL)
    result = process_api_response(name_of_call_function, result, ASTRONAUTS_IN_SPACE_URL)

    return result

def fetch_iss_location():
    try:
        api_logs.info("Api request: {}: Url: {}".format("Function fetch_iss_location", ASTRONAUTS_IN_SPACE_URL))
        result = requests.get(ISS_LOCATION_URL)
        result.raise_for_status()
    except requests.exceptions.HTTPError as e:
        status_code = result.status_code
        api_errors.error(("status code: {},error: {}, Api request: {}: Url: {}".format(status_code, e,
                                                                                       "Function fetch_iss_location",
                                                                                       ASTRONAUTS_IN_SPACE_URL)))
        api_logs.error(("status code: {},error: {}, Api request: {}: Url: {}".format(status_code, e,
                                                                                       "Function fetch_iss_location",
                                                                                       ASTRONAUTS_IN_SPACE_URL)))
    except requests.exceptions.RequestException as e:
        api_errors.error(("Error: {}, Api request: {}: Url: {}".format(e,
                                                                       "Function fetch_iss_location",
                                                                       ASTRONAUTS_IN_SPACE_URL)))
        api_logs.error(("Error: {}, Api request: {}: Url: {}".format(e,
                                                                       "Function fetch_iss_location",
                                                                       ASTRONAUTS_IN_SPACE_URL)))
    else:
        api_logs.info(
            "Api response: {}: Url: {}, result: {}".format("Function fetch_iss_location", ASTRONAUTS_IN_SPACE_URL,
                                                           result.json()))
        return result