# Fake News Detection Using Machine Learning

## 🗂️ Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Dataset](#dataset)
5. [Model Performance](#model-performance)
6. [How to Use](#how-to-use)
7. [Technologies Used](#technologies-used)
8. [License](#license)


## 📖 Project Overview

Fake News Detection is a machine learning project designed to classify news articles as either **real** or **fake**. Using natural language processing (NLP) and a logistic regression model, this project provides an automated solution to identify misinformation.

---

## 🛠️ Features

- **Preprocessing Pipeline**: Includes text cleaning and feature engineering.
- **TF-IDF Vectorization**: Converts text data into numerical features.
- **Classification Model**: Logistic Regression with high accuracy.
- **Interactive Streamlit App**: Test news articles in real-time.

---

## 🛠️ Installation

1. Clone the repository

```bash
git clone https://github.com/yourusername/fake-news-detection.git
cd fake-news-detection
```

2. Install the required Python packages:

``` bash
pip install -r requirements.txt
```

3. Dataset
    Place your dataset in the data/ directory. Ensure it has the following columns:
    ID, title, text, subject, date, and class.

4. Run the Streamlit app

```bash
streamlit run app.py
```

---

## 📈 Model Performance

The model achieved excellent performance on the test set:

    Accuracy: 98.97%
    Precision:
        99% for Real News
        99% for Fake News
    Recall:
        99% for Real News
        98% for Fake News
    F1-Score:
        99% for Real News
        98% for Fake News


---

## 🎮 How to Use

1. Run the streamlit app using the command

```bash
streamlit run app.py
```

2. Enter a news article into the text box provided.

3. Click "Analyze" to classify the article as Fake News or Real News.

---

## 🧰 Technologies Used

    Python: Core programming language for implementation.
    Scikit-learn: Machine learning algorithms and evaluation.
    Pandas: Data manipulation and analysis.
    Streamlit: Interactive user interface for testing the model.
    NLP Techniques: Text cleaning and TF-IDF vectorization.

---

## 📜 License

This project is licensed under the MIT License. See the LICENSE tab on the top for more details.