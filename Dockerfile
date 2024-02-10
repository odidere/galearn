FROM python:3.12

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt

# If I add a flash application to this project, I may want to expose some ports
# ARG APP_PORT
# ENV APP_PORT=$APP_PORT
# EXPOSE $APP_PORT

CMD ["python", "app.py"]
