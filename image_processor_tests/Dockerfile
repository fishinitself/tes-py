FROM ubuntu:24.04

RUN apt update
RUN apt install -y python3-all python3-pip python3-venv python3-tk

RUN mkdir /wrk /wrk/input /wrk/output && cd /wrk
WORKDIR /wrk

COPY requirements.txt ./

RUN python3 -m venv iptests-py-env && iptests-py-env/bin/pip install --no-cache-dir -r requirements.txt

COPY image_processor_tests.py .
RUN chmod +x ./image_processor_tests.py

COPY entrypoint.sh ./
RUN chmod +x /wrk/entrypoint.sh

ENTRYPOINT ["/bin/bash", "/wrk/entrypoint.sh"]

