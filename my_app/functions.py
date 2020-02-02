#import requests
import requests
import sys

def notifyViaLine(first_name, last_name):
    #Send message via Line Notify
    url = "https://notify-api.line.me/api/notify"
    token = "8F1U3P0vZH7iZ2pZosAiN9kyitXsxwMfXzUFXRdVqaw"

    message = first_name+" " + last_name + " just submitted the form now. "

    headers = {"Authorization" : "Bearer "+ token}
    
    payload = {"message" :  message}

    try:
        requests.post(url ,headers = headers ,params=payload)
        return True
    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(1)
        return False
    