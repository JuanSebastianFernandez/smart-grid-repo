FROM python:3.12-slim

WORKDIR /workspace
COPY . /workspace

EXPOSE 8000
CMD ["python", "/workspace/app/server.py"]

