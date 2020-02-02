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
            result = requests.get("http://api.open-notify.org/astros.json")
        except:
            pass
            #TODO log faiulre to make a call
            #return error message or exit fun

    if call_source == "iss_location_now":
        try:
            result = requests.get("http://api.open-notify.org/iss-now.json")
        except:
            pass
            #TODO log faiulre to make a call
            #return error message or exit fun

    try:
        #if the call was succesfull the result var will exist
        if result.status_code == 200:
            return result.json()
        else:
            pass
            #TODO log that call had a failure
            #return error message or exit fun
    except:
        pass