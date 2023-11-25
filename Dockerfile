# Python runtime
FROM python:3.11

# Working directory in the container
WORKDIR /app

# Copy required files to the container
COPY requirements.txt .
COPY app/ app/
COPY auth/ auth/
COPY utils/ utils/
# maybe add other directories later 

# Install required packages
RUN pip install --no-cache-dir -r requirements.txt

# Sesame, open the gate
EXPOSE 8501

# Execute the main app
CMD ["streamlit", "run", "app/main.py"]
