import requests
#from incodaq_space.logging_is import api_errors, api_logs
from incodaq_space.logging_is import api_errors, api_logs
from incodaq_space.constants import ASTRONAUTS_IN_SPACE_URL, ISS_LOCATION_URL

def retrieve_iss_crew_names():
    try:
        api_logs.info("Api request: {}: Url: {}".format("Function retrieve_iss_crew_names", ASTRONAUTS_IN_SPACE_URL))
        result = requests.get(ASTRONAUTS_IN_SPACE_URL)
        result.raise_for_status()
    except requests.exceptions.HTTPError as e:
        status_code = result.status_code
        api_errors.error(("status code: {},error: {}, Api request: {}: Url: {}" .format(status_code, e, "Function retrieve_iss_crew_names", ASTRONAUTS_IN_SPACE_URL)))
        api_logs.error(("status code: {},error: {}, Api request: {}: Url: {}".format(status_code, e,
                                                                                       "Function retrieve_iss_crew_names",
                                                                                       ASTRONAUTS_IN_SPACE_URL)))

    except requests.exceptions.RequestException as e:
        api_errors.error(("Error: {}, Api request: {}: Url: {}".format(e,
                                                                                       "Function retrieve_iss_crew_names",
                                                                                       ASTRONAUTS_IN_SPACE_URL)))
        api_logs.error(("Error: {}, Api request: {}: Url: {}".format(e,
                                                                       "Function retrieve_iss_crew_names",
                                                                       ASTRONAUTS_IN_SPACE_URL)))

    else:
        api_logs.info(
            "Api response: {}: Url: {}, result: {}".format("Function retrieve_iss_crew_names", ASTRONAUTS_IN_SPACE_URL,
                                                           result.json()))
        return result

def retrieve_iss_location_now():
    try:
        api_logs.info("Api request: {}: Url: {}".format("Function retrieve_iss_location_now", ASTRONAUTS_IN_SPACE_URL))
        result = requests.get(ISS_LOCATION_URL)
        result.raise_for_status()
    except requests.exceptions.HTTPError as e:
        status_code = result.status_code
        api_errors.error(("status code: {},error: {}, Api request: {}: Url: {}".format(status_code, e,
                                                                                       "Function retrieve_iss_crew_names",
                                                                                       ASTRONAUTS_IN_SPACE_URL)))
        api_logs.error(("status code: {},error: {}, Api request: {}: Url: {}".format(status_code, e,
                                                                                       "Function retrieve_iss_crew_names",
                                                                                       ASTRONAUTS_IN_SPACE_URL)))
    except requests.exceptions.RequestException as e:
        api_errors.error(("Error: {}, Api request: {}: Url: {}".format(e,
                                                                       "Function retrieve_iss_crew_names",
                                                                       ASTRONAUTS_IN_SPACE_URL)))
        api_logs.error(("Error: {}, Api request: {}: Url: {}".format(e,
                                                                       "Function retrieve_iss_crew_names",
                                                                       ASTRONAUTS_IN_SPACE_URL)))
    else:
        api_logs.info(
            "Api response: {}: Url: {}, result: {}".format("Function retrieve_iss_location_now", ASTRONAUTS_IN_SPACE_URL,
                                                           result.json()))
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
