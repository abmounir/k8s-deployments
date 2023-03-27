FROM python:3.9-slim-buster
WORKDIR /app
ADD . .
RUN  pip3 install --no-cache-dir -r requirements.txt
# RUN pip install uwsgi
EXPOSE 1097
EXPOSE 8000
CMD uvicorn whois_check:app --reload --port 1097 --host 0.0.0.0
