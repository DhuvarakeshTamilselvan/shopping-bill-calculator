FROM python:3.11-slim
WORKDIR /workspace
COPY app.py .
CMD ["python", "app.py"]
