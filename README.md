# 🌺 Iris Classifier Web App with Docker

## 📌 Project Overview
This project is a simple web application that predicts the species of an Iris flower based on its physical attributes using a trained Random Forest model. The app is built with Python and Flask, and containerized with Docker for easy deployment.

---

## 🎯 Objective
- Predict Iris flower species (Setosa, Versicolor, Virginica) from user input features.
- Provide a web API endpoint to make predictions.
- Package the application in a Docker container for easy setup and running.

---

## 📂 Repository Contents
- `docker_app.py` — Flask application serving the prediction API.
- `rf.pkl` — Pre-trained Random Forest model.
- `Dockerfile` — Instructions to build the Docker image.
- `requirements.txt` — Python dependencies.
- `README.md` — This file.

---

## 🐳 How to Run the Docker Image

### Prerequisites:
- Docker installed on your machine.  
  You can download and install Docker from: https://www.docker.com/get-started

### Steps to build and run:

1. **Clone the repository (if you haven't already):**

   ```bash
   git clone https://github.com/luxan-shanmugalingam/iris-docker-app.git
   cd iris-docker-app
````

2. **Build the Docker image:**

   ```bash
   docker build -t iris_app .
   ```

3. **Run the Docker container:**

   ```bash
   docker run -p 5000:5000 iris_app
   ```

4. **Access the app:**

   Open a browser and go to:
   `http://localhost:5000`

5. **Use the API:**

   You can send requests to the `/predict` endpoint. For example, access Swagger UI at:
   `http://localhost:5000/apidocs`

---

## 📬 Contact

For any questions or issues, please contact:
**S. Luxan** — `luxan.shanmugalingam@gmail.com`
