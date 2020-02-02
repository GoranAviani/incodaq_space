from celery import shared_task
from .views import iss_crew_api
# periodic task
@shared_task
def save_iss_crew_info(*args, **kwargs):
    iss_crew_api()
