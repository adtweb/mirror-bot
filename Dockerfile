FROM python:3.9-slim

# Set UTF-8 locale
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "bot.py"]