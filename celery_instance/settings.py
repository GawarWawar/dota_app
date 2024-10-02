# Link to the redis broker
broker_url = 'redis://localhost:6379/0' # FUTURE TODO: make a secret in production


# Where is database for the beat instace is located
beat_scheduler = 'django_celery_beat.schedulers:DatabaseScheduler'

broker_connection_retry_on_startup = True
acks_late = True

# Disabled to set up timezone itself
enable_utc = False
# Timezone should be the same as a Django TIME_ZONE
timezone = 'UTC'
task_track_started = True
result_extended = True

# Where signals and schedule laying in
imports = (
    "celery_instance.schedule",
    "opendota_forcer.signals",
)

# Where to look for the tasks
include=(
    "opendota_forcer.tasks.process_active_users",
    "opendota_forcer.tasks.process_user_last_match",
)