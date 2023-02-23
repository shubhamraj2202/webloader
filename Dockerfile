FROM python:3-alpine
WORKDIR /fetch
COPY ci-test-requirements.txt .
RUN pip install -r ci-test-requirements.txt
COPY . ./
ENTRYPOINT ["python3", "fetch.py"]
