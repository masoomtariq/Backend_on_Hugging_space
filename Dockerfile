# Example for a Python/FastAPI RAG backend
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Create a non-root user (Security requirement for HF Spaces)
RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH

# Expose the port (Hugging Face defaults to 7860)
EXPOSE 7860

# Command to run the application (e.g., uvicorn for FastAPI)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]
