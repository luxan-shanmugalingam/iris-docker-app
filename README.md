# 🌺 Iris Flower Classification – Project Documentation

## 📌 Project Title
**Iris Flower Species Prediction Using Random Forest and Flask API**

---

## 🧠 Project Overview

This project demonstrates a simple machine learning application that predicts the species of an Iris flower based on its physical attributes. The web API is developed using Flask, and the trained model is deployed using Docker.

It is designed for educational purposes and is easy to test and reproduce.

---

## 🎯 Objective

- Train a classification model using the classic Iris dataset.
- Build a Flask API to serve predictions.
- Provide Swagger documentation for easy API testing.
- Package the entire project in a Docker container for seamless deployment.

---

## 📂 Folder Structure

```
iris_app/
├── app.py         # Flask application with prediction API
├── rf.pkl         # Trained Random Forest model
├── Dockerfile     # Docker instructions for containerization
└── README.md      # Usage guide
```

---

## 🔧 Technologies Used

- Python (v3.8+)
- Flask
- Scikit-learn
- Docker
- Swagger (Flasgger)

---

## 🧪 Dataset

- **Name**: Iris Flower Dataset
- **Source**: UCI Machine Learning Repository
- **Features**:
  - Sepal length (cm)
  - Sepal width (cm)
  - Petal length (cm)
  - Petal width (cm)
- **Target**: Species (Setosa, Versicolor, Virginica)

---

## 🧠 Model

- Algorithm: Random Forest Classifier
- Accuracy: ~97% (cross-validation on training data)
- Saved as: `rf.pkl` using joblib

---

## 🌐 API Documentation

### Endpoint: `/predict`

**Method**: `GET`

**Parameters**:
- `Sepal length`: float
- `Sepal width`: float
- `Petal length`: float
- `Petal width`: float

**Response**:
```json
{
  "prediction": "versicolor"
}
```

**Swagger UI**: Accessible at `http://localhost:5000/apidocs`

---

## 🐳 Docker Deployment

To run the app using Docker:

```bash
docker build -t iris_app .
docker run -p 5000:5000 iris_app
```

Then, open your browser at: `http://localhost:5000`

---

## 📢 Contributors

- **S. Luxan** – Developer and Author

---

## 📃 License

This project is released under the MIT License.

---

## 📬 Contact

For questions or collaborations, please contact: `luxanscience@gmail.com`