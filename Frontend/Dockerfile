FROM python:3.10.9

WORKDIR /eass_project/frontend
COPY . .

RUN pip install -r requirements.txt

CMD ["streamlit", "run", "ui.py"]