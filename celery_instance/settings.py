broker_url = 'redis://localhost:6379/0'
broker_connection_retry_on_startup = True
beat_scheduler = 'django_celery_beat.schedulers:DatabaseScheduler'

acks_late = True

enable_utc = False
task_track_started = True
result_extended = True

timezone = 'UTC'

imports = (
    "celery_instance.schedule",
    "opendota_forcer.signals",
)

include=(
    "opendota_forcer.tasks.process_active_users",
    "opendota_forcer.tasks.process_user_last_match",
)