# استفاده از تصویر رسمی پایتون
FROM python:3.11-slim

# تنظیم دایرکتوری کاری

# نصب وابستگی‌های سیستم
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# کپی فایل requirements.txt (اگر دارید) و نصب وابستگی‌ها
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY . .

# تنظیم متغیر محیطی برای اجرا
ENV PYTHONUNBUFFERED=1

# اجرای برنامه FastAPI با uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


#FROM python
#
##RUN apt update
#
##RUN mkdir -p /apps
##
##WORKDIR /apps
#RUN apt-get update && apt-get install -y wait-for-it
#
#COPY . .
#
#RUN pip install -U pip && pip install -r requirements.txt
## set environment variables
#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1