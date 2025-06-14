FROM python:3.9.7-slim

WORKDIR /app

RUN pip install flask scikit-learn pandas gunicorn

COPY [ "predict.py", "lin_reg.bin", "./" ]

EXPOSE 9696

ENTRYPOINT [ "gunicorn", "--bind=0.0.0.0:9696", "--timeout", "120", "predict:app" ]