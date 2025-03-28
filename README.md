# Project: Predicting diabetes outcome for women

## Desription
This project aims to predict the likelihood of diabetes in women based on key health indicators such as glucose levels, BMI, age, and other relevant factors. The goal is to build a machine learning model that can provide accurate predictions to assist in early diagnosis and proactive healthcare decisions.

## Project structure:
```
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── routes
│   │   └── __init__.py
│   └── services
│       └── __init__.py
├── models
│   └── __init__.py
├── storage
│   └── models
├── .gitingore
└── README.md
```

./app - package for web application

./models - package for ml models training

./storage - directory for ml models

## Results

- RFC: accuracy=0.95, AUC=0.98
- XGB: accuracy=0.96, AUC=0.99

## Choosen model - XGB

## How to start app
```shell
python3 -m venv venv
source venv/bin/activate
pip install -r app/requirements.txt
uvicorn app.main:app --reload 
```
App will run on http://0.0.0.0:8000/

Prediction page http://0.0.0.0:8000/prediction