# 📩 SMS Spam Classifier

A Machine Learning based web application that classifies SMS messages as **Spam** or **Not Spam** using Natural Language Processing (NLP) techniques and Machine Learning algorithms.

The project includes text preprocessing, feature extraction, model training, and a Streamlit-based user interface for real-time predictions.

---

## 🚀 Demo

Enter any SMS message in the application, and the model will predict whether it is:

✅ **Not Spam**  
❌ **Spam**

---

## 📌 Features

- Text preprocessing using NLP techniques
- Converts SMS text into numerical features using TF-IDF Vectorization
- Machine Learning model for spam classification
- Real-time prediction through Streamlit web application
- Simple and user-friendly interface

---

## 🛠️ Tech Stack

### Programming Language
- Python

### Libraries & Frameworks
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- NLTK

### Machine Learning
- Natural Language Processing (NLP)
- Text Classification
- TF-IDF Vectorization
- Supervised Learning

---

## 📂 Project Structure

```
SMS-Spam-Classifier/
│
├── app.py                  # Streamlit application
├── sms-spam-classifier.ipynb # Model training notebook
├── model.pkl               # Trained ML model
├── vectorizer.pkl          # Saved text vectorizer
├── requirements.txt        # Required Python packages
├── README.md               # Project documentation
└── spam.csv                # Dataset
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/SMS-Spam-Classifier.git
```

### 2. Navigate to the project directory

```bash
cd SMS-Spam-Classifier
```

### 3. Create a virtual environment (optional)

```bash
python -m venv venv
```

Activate environment:

**Windows**
```bash
venv\Scripts\activate
```

**Linux/Mac**
```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Streamlit application

```bash
streamlit run app.py
```

---

## 🧠 Machine Learning Workflow

The project follows these steps:

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Text Preprocessing
   - Lowercasing
   - Tokenization
   - Removing special characters
   - Removing stopwords
   - Stemming
5. Feature Extraction using TF-IDF
6. Model Training
7. Model Evaluation
8. Deployment using Streamlit

---

## 📊 Model Evaluation

The model was evaluated using classification metrics such as:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

---

## 🔮 Future Improvements

- Deploy the application on cloud platforms
- Add multiple ML models comparison
- Improve accuracy with Deep Learning approaches
- Add support for multiple languages
- Create an API using FastAPI

---

## 👨‍💻 Author

**Deep Patel**

- GitHub: https://github.com/Deeppatel124
- LinkedIn: https://linkedin.com/in/deep-patel124

---

⭐ If you found this project useful, consider giving it a star!