import logging
from datetime import datetime

#Custom loggers
api_errors = logging.getLogger("api_error")

#Handlers
api_errors_handler = logging.FileHandler('api_errors.log')

#Handlers level
api_errors_handler.setLevel(logging.INFO)

#Create formatters and add them to handlers
error_format = logging.Formatter('%(asctime)s - %(message)s')
api_errors_handler.setFormatter(error_format)

#Connect handlers and loggers
api_errors.addHandler(api_errors_handler)
