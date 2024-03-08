FROM python:3.11.2

WORKDIR /streamlit-app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD streamlit run app.py

