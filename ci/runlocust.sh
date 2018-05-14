#!/bin/sh
echo "inside run script"
docker run -i --rm -p 8089:8089 -e ROLE=standalone -e TARGET_HOST=https://content-v2.perf.apis.devops.mnscorp.net -e LOCUST_FILE=https://raw.githubusercontent.com/neerajagr/testRepo/master/simple.py -e SLAVE_MUL=4 -e AUTOMATIC=False -e users=100 -e hatch-rate=5 -e duration=30 mns-locust-image
