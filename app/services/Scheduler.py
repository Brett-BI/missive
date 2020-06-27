from app import scheduler

import app.services.Messager

'''
    Needs:
        - Logic to handle the time (i.e. at 1500 user asks to send msg at 1100)
        - Logic to create a new scheduled task
        - Eventually, put the jobs in a job store
        - Some kind of administration panel for jobs
        - Actions:
            > Add
            > Remove
            > Update (maybe)

'''

class SMSScheduler():
    def addJob(self, times, job_id, missive_id):
        # validate the times
        foreach t in times:
            valid = TimeValidator.validate(t)
            if not valid:
                return False

        # calculate & convert times to datetimes (will be within 24 hours)
        scheduler.add_job(trigger='date', func=lambda : print(f'reminder: {job_id}'), id='my_job1', run_date=datetime(2020, 6, 11, 18, 38, 0))

class WebScheduler():
    # addJob
    def addJob(self, times, missive_id):
        # validate the times (return failure or call some method that returns a fail code)
        # calculate the time(s)
        # loop & schedule
        scheduler.add_job(trigger='date', func=lambda : print('from add_job1'), id='my_job1', run_date=datetime(2020, 6, 11, 18, 38, 0))

    # removeJob
    def removeJob(job_id):
        pass

    # updateJob
    def updateJob(self):
        pass

    # admin stuff

    # user stuff

    def __str__(self):
        print('Scheduler __str__')
    
    def __repr__(self):
        print('Scheduler __repr__')


# scheduler.add_job(trigger='date', func=lambda : print('from add_job1'), id='my_job1', run_date=datetime(2020, 6, 11, 18, 38, 0))
# scheduler.add_job(trigger='date', func=lambda : print('from add_job2'), id='my_job2', run_date=datetime(2020, 6, 11, 18, 39, 0))

# @scheduler.task('date', id='my_job0', run_date=datetime(2020, 6, 11, 18, 37, 0))
# def printed():
#     print('from add_job0')
#     scheduler.get_jobs()