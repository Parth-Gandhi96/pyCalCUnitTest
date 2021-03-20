FROM python:3

COPY testCases/ /testCases/
RUN ls -la /testCases/*

ADD main.py /

ADD testingCode.py /

RUN pip install unittest2

CMD [ "python", "./testingCode.py" ]