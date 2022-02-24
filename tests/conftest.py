import pytest

from cron_explainer.cron_job import CronJob


@pytest.fixture
def cron_job():
    yield CronJob("*/15 0 1,15 * 1-5 /usr/bin/find")
