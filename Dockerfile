FROM python:3

ADD leap_year.py /

RUN pip install pystrich

CMD [ "python", "./leap_year.py 1985" ]
