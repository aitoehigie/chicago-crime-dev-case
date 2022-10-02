FROM python:3.9-slim

WORKDIR /app

# Copy app and dependencies
COPY streamlit/ streamlit/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r streamlit/requirements.txt

EXPOSE 8501

# ENTRYPOINT [ "streamlit", "run", "streamlit/app.py" ]

CMD streamlit run --server.port 8501 --server.enableCORS false streamlit/app.py
