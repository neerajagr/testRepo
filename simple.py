from locust import HttpLocust
from locust import TaskSet
from locust import task
from locust.web import app

from src import report

# For reporting
app.add_url_rule('/htmlreport', 'htmlreport', report.download_report)


class UserBehavior(TaskSet):

    @task
    def index(self):
        self.client.get('/contents/v2/page/SC_Level_1_480487?state=Live&storeId=10151')


class MyLocust(HttpLocust):
    task_set = UserBehavior
    min_wait = 0
    max_wait = 0
