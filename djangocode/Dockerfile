# Use the official Python image from the Docker Hub
FROM python:3.12-alpine3.20
RUN apk update && \
    apk add --no-cache mariadb-dev build-base
RUN pip install django mysqlclient pillow

# Set the working directory
WORKDIR /app
# Copy the Django project files
COPY . /app/

# Expose the port that the app runs on
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
