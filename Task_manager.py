import schedule
import time

# Define the Time_Reminder function.
def Time_Reminder():
    print("Task executed at", time.strftime("%Y-%m-%d %H:%M:%S"))

# Schedule a task to run every day at a specific time (e.g., 14:30).
daily_job = schedule.every().day.at("14:30").do(Time_Reminder)

# Schedule a task to run every hour.
hourly_job = schedule.every().hour.do(Time_Reminder)

# Schedule a task to run every 5 minutes.
every_5_minutes_job = schedule.every(5).minutes.do(Time_Reminder)

# Main loop to execute scheduled tasks.
while True:
    schedule.run_pending()
    time.sleep(1)

# To update a job's schedule, you can use the reschedule method on the job object.
def update_daily_schedule(new_time):
    daily_job.reschedule(schedule.every().day.at(new_time))

# To delete a specific job, you can use the cancel method on the job object.
# For example, to cancel the daily job:
def delete_daily_schedule():
    daily_job.cancel()

# To cancel other jobs, use the appropriate job objects (e.g., hourly_job, every_5_minutes_job).
