#official Python image from the Docker Hub
FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

COPY th.jpeg /app/images

COPY IPL-2020-all-teams-logos.jpg /app/images

EXPOSE 8501

CMD ["streamlit", "run", "home.py"]
