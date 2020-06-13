from app import scheduler

class Scheduler():
    def __init__(self):
        pass

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