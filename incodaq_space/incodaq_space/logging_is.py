import logging
from datetime import datetime

#Custom loggers
api_errors = logging.getLogger("api_error")
api_logs = logging.getLogger("api_logs")

#Handlers level
api_errors.setLevel(logging.ERROR)
api_errors.setLevel(logging.INFO)

#Handlers
api_errors_handler = logging.FileHandler('logs/api_errors.log')
api_logs_handler = logging.FileHandler('logs/api_logs.log')

#Create formatters and add them to handlers
error_format = logging.Formatter('%(asctime)s - %(message)s')
full_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

api_errors_handler.setFormatter(error_format)
api_logs_handler.setFormatter(full_format)

#Connect handlers and loggers
api_errors.addHandler(api_errors_handler)
api_logs.addHandler(api_logs_handler)
