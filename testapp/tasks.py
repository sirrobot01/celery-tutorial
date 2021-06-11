from celeryapp import tasker


@tasker.task(bind=True)
def send_email(self, email):
    print(email)
    print('## sending Email')
    