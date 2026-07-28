import streamlit as st
import pickle
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import string

def transform_text(text):

    # Lowercasing
    text = text.lower()

    # Tokenization
    text = nltk.word_tokenize(text)

    # Removing Special characters
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    # Removing stop words and punctuations
    for word in text:
        if word not in stopwords.words('english') and word not in string.punctuation:
            y.append(word)

    text = y[:]
    y.clear()

    # Stemming
    ps = PorterStemmer()
    for word in text:
        y.append(ps.stem(word))
        
    
    return " ".join(y)


tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.title('SMS Spam Classifier')

input_sms = st.text_area("Enter The Message ")

if st.button("Predict"):
    # 1. Preprocess
    transformed_sms = transform_text(input_sms)
    
    # 2. Vectorize
    vector_input = tfidf.transform([transformed_sms])
    
    # 3. Predict
    prediction = model.predict(vector_input)[0]
    
    # 4. Display
    if prediction == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")



