from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
import streamlit as st
import pandas as pd
import joblib
import sklearn


def results(model):
    st.markdown('## Accuracy')
    st.write(model.score(X_test, y_test))
    st.markdown('## Confusion Matrix')
    st.dataframe(confusion_matrix(y_test, model.predict(X_test)))
    st.markdown('## Classification Report')
    st.text(classification_report(y_test, model.predict(X_test)))

def splitDataset(df):
   y_test =df['severity']
   X_test = df.drop(['severity'], axis = 1)
   return y_test,X_test
   


st.markdown('# Machine learning models')
st.write("""Generally speaking we can consider that accuracy scores:
                          - Over 90% - Very Good
                    - Between 70% and 90% - Good
                    - Between 60% and 70% - OK""")

choices = ['XGBOOST','XGBOOST Improved','Gradient Boosting','Gradient Boosting Improved']
#choices = ['Gradient Boosting']
option = st.selectbox(
         'Which model do you want to try ?',
         choices)

st.write('You selected :', option)

@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    return df



df = load_data('Datasets/X_test_sample.csv')

if df is not None:
    y_test =df['severity']
    X_test = df.drop(['severity','Unnamed: 0'], axis = 1)

if option=='Gradient Boosting':
   st.write('Gradient Boosting score train 69.96')
   #GBC=joblib.load('Models/gbcwohyperparms.dat')
   #results(GBC)

if option=='Gradient Boosting improved':
   st.write('Gradient Boosting score train 71.894')
   #GBCi=joblib.load('Models/gbc.dat')
   #results(GBCi)


if option=='XGBOOST':
   st.write('XGBOOST score train 71.998')
   xgb = joblib.load('Models/xgb_model.json')
   results(xgb)


if option=='XGBOOST improved':
   st.write('XGBOOST score train 72.052')
   xgbi = joblib.load('Models/xgb_model_improved.json')
   results(xgbi) 
