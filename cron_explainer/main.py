import sys

from cron_explainer.cron_job import CronJob


def main():
    try:
        if len(sys.argv) < 2:
            raise ValueError("Cron expression must be provided.")

        expression = sys.argv[1]
        cron_job = CronJob(expression)

        columns = [
            ("minute", cron_job.minute),
            ("hour", cron_job.hour),
            ("day of month", cron_job.day),
            ("month", cron_job.month),
            ("day of week", cron_job.day_week),
            ("command", cron_job.command),
        ]

        for name, data in columns:
            name = f"{name}:".ljust(15)
            print(name, data)

    except Exception as exception:
        print(f"ERROR: {exception}")


if __name__ == "__main__":
    main()
