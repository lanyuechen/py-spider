FROM python:3-alpine

COPY . /dev/py-spider/

RUN pip3 install aiohttp

EXPOSE 9001

CMD [ "python", "./app.py" ]