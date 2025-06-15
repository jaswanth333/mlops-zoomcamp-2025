FROM agrigorev/zoomcamp-model:mlops-2024-3.10.13-slim

WORKDIR /app

COPY starter.py /app/

COPY Pipfile Pipfile.lock /app/
RUN pip install pipenv && pipenv install --deploy --system

CMD ["python", "starter.py", "2023", "04"]