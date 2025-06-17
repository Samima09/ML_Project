# 🎓 Student Exam Performance Predictor

This is a Machine Learning web application that predicts a student's **math exam score** based on attributes like gender, parental education, lunch type, and more.

🚀 **Live Demo:** [Click here to view app](https://ml-project-ibmc.onrender.com/)

---

## 📊 Project Overview

This project uses machine learning (Regression with CatBoost/XGBoost/RandomForest) to estimate the math score of a student based on:

- Gender  
- Race/Ethnicity  
- Parental level of education  
- Lunch type  
- Test preparation course  
- Reading score  
- Writing score  

---

## 🧠 ML Workflow

- Data Cleaning and Preprocessing
- Feature Engineering
- Model Training (Scikit-Learn)
- Evaluation
- Flask API for prediction
- Deployment on Render

---

## 🛠️ Tech Stack

| Technology | Purpose                         |
|------------|----------------------------------|
| Python     | Programming Language             |
| Flask      | Web Framework (Backend)          |
| HTML/CSS   | Frontend UI                      |
| Pandas     | Data Handling                    |
| Scikit-learn | ML Model Building              |
| Gunicorn   | WSGI Server for deployment       |
| Render     | Hosting Platform                 |

---
## 🚀 Deployment

The project is deployed on **Render**.  
To deploy your own version:

1. Fork this repo
2. Connect to Render
3. Add `render.yaml`
4. Set build command: `pip install -r requirements.txt`
5. Set start command: `gunicorn app:app`

## 🤝 Author

👩‍💻 **Samima Afroj**  
📧 samimaafroj0@gmail.com  
🌐 [GitHub Profile](https://github.com/Samima09)


