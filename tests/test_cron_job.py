from cron_explainer.cron_job import CronJob


def test_cron_job_minute(cron_job: CronJob):
    assert cron_job.minute == {0, 45, 30, 15}


def test_cron_job_hour(cron_job: CronJob):
    assert cron_job.hour == {0}


def test_cron_job_day(cron_job: CronJob):
    assert cron_job.day == {1, 15}


def test_cron_job_month(cron_job: CronJob):
    assert cron_job.month == {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}


def test_cron_job_day_week(cron_job: CronJob):
    assert cron_job.day_week == {1, 2, 3, 4, 5}


def test_cron_job_command(cron_job: CronJob):
    assert cron_job.command == '/usr/bin/find'
