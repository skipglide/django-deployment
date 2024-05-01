import logging
from celery import shared_task
from django.utils import timezone
from .models import Counter

logger = logging.getLogger(__name__)

@shared_task
def restart_counter():
    logger.info("restart_counter task started")
    Counter.objects.all().update(count=0)
    logger.info("Restarted count")