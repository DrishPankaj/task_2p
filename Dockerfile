FROM python:3
WORKDIR /usr/src/app
COPY . .
CMD ["task_2.py"]
ENTRYPOINT ["python3"]
