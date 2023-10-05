FROM python:3.10-slim
ADD . /solidity-generator

WORKDIR /solidity-generator

RUN pip install -r requirements.txt

EXPOSE  8080

CMD python entrypoint.py