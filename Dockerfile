FROM python:2.7

ADD requirements.txt /usr/src/
RUN pip install -r /usr/src/requirements.txt
ADD *.py /usr/src

EXPOSE 8080

CMD ["/usr/src/app.py", "8080"]
