from celery import shared_task
from .views import iss_crew_api, iss_location_api
# periodic task
@shared_task
def save_iss_crew_info(*args, **kwargs):
    iss_crew_api()
# periodic task
@shared_task
def save_iss_location_now_info(*args, **kwargs):
    iss_location_api()