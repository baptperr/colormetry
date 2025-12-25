FROM python:3.10.6-buster

COPY backend /backend
COPY pages /pages
COPY requirements.txt /requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD streamlit run 1_Home.py
