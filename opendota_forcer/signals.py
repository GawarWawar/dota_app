from celery.signals import after_task_publish, task_postrun, task_success, after_setup_logger, after_setup_task_logger

from .src import utils
from .tasks import process_user_last_match, process_active_users

@task_postrun.connect()
def task_success_handler(
    sender=None, task_id = None, **kwargs
):
        if sender.name == process_user_last_match.process_user_last_match.name:
            
            logger = utils.get_logger(
                f"Profile: {sender.profile_id}; Match: {sender.match_id}",
                # TODO: set up this as env variable
                log_level="INFO"
            )
            file_handler = utils.assign_filehandler_to_logger(
                logger=logger
            )
            logger.info(sender.message)
            logger.removeHandler(file_handler)
            
        elif sender.name == process_active_users.process_active_users.name:
            logger = utils.get_logger(
                f"Periodic_handler",
                # TODO: set up this as env variable
                log_level="INFO"
            )
            file_handler = utils.assign_filehandler_to_logger(
                logger=logger
            )
            message = "Last match check was started for: "
            for user_count, user in enumerate(sender.users_processed):
                if user_count == 0:
                    message += f"{user}"
                else:
                    message += f"-{user}"
            
            logger.info(message)
            logger.removeHandler(file_handler)