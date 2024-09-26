from celery.signals import after_task_publish, task_postrun, task_success, after_setup_logger, after_setup_task_logger

from .src import utils
from .tasks import get_matches

@task_postrun.connect()
def task_success_handler(
    sender=None, task_id = None, **kwargs
):
        if sender.name == get_matches.process_user_last_match:
            
            # TODO: transform into separate class LoggerHandler
            logger = utils.get_logger(
                f"Profile: {sender.profile_id}; Match: {sender.match_id}",
                # TODO: SET UP ENV VARIABLE
                log_level="INFO"
            )
            file_handler = utils.assign_filehandler_to_logger(
                logger=logger
            )
            logger.info(sender.message)
            logger.removeHandler(file_handler)