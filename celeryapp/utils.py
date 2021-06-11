from celery.utils.log import get_logger
from django.conf import settings
logger = get_logger(__name__)


class TaskRunner:

    def __init__(self, func_code, func, args=[], kwargs={}, task_kwargs={}):
        self.func_code = func_code # This could be used to save to db
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.task_kwargs = task_kwargs

    @property
    def _task_kwargs(self):
        # retries
        retries_policy = settings.RETRIES_POLICY
        if not self.task_kwargs.get('retries_policy') and retries_policy:
            self.task_kwargs['retries_policy'] = retries_policy
            self.task_kwargs['retry'] = True

        return self.task_kwargs

    def handle_data(self, raw_data):
        # Use this save data to db or do whatever you want with it
        print(raw_data)

    def get(self, task):
        return task.get(on_message=self.handle_data, propagate=False) # Use show 


    def run(self):
        try:
            task = self.func.s(*self.args, **self.kwargs).apply_async(**self._task_kwargs)
            return task
        except self.func.OperationalError as exc:
            logger.exception('Sending task raised: %r', exc)
        

        
