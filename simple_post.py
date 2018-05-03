import json
import os
from random import randint

from locust import HttpLocust
from locust import TaskSet
from locust import task
from locust.web import app

from src import report

# For reporting
app.add_url_rule('/htmlreport', 'htmlreport', report.download_report)

# Read json file
json_file = os.path.join(os.path.dirname(__file__), 'payloads.json')


class SimplePostBehavior(TaskSet):

    def __init__(self, parent):
        super(SimplePostBehavior, self).__init__(parent)
        with open(json_file) as file:
            self.payloads = json.load(file, 'utf-8')
        self.length = len(self.payloads) - 1

    @task
    def post_random_payload(self):
        l_inputJSON = self.payloads[randint(0, self.length)]
        weight = l_inputJSON.get('weight',1)
        l_method = l_inputJSON.get('method','GET')
        l_url = l_inputJSON.get('url','/')
        l_headers = l_inputJSON.get('headers',None)
        l_cookies = l_inputJSON.get('cookies',None)
        #self.client.request("{}".format(l_inputJSON.get('method')), "{}".format(l_inputJSON.get('url')),headers=l_headers,cookies=l_cookies)
        self.client.request("{}".format(l_method), "{}".format(l_url),headers=l_headers,cookies=l_cookies)


class MyLocust(HttpLocust):
    task_set = SimplePostBehavior
    min_wait = 0
    max_wait = 0
