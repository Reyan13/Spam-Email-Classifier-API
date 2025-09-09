import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib
from sklearn.preprocessing import LabelEncoder

# LOADING DATASET
data = pd.read_csv("spam.csv", encoding="latin1")

# ADJUSTMENT OF COLUMN NAMES
data = data.rename(columns={'v1': 'label', 'v2': 'message'})
x = data['message']
y = data['label']

# ENCODING LABELS TO NUMERICS
le = LabelEncoder()
y = le.fit_transform(y)


# SPLITTING DATASET
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)


# BUILDING PIPELINE (VECTORIZER + CLASSIFIER)
model = make_pipeline(CountVectorizer(), MultinomialNB())

# TRAINING MODEL
model.fit(x_train, y_train)

# SAVING TRAINED MODEL
joblib.dump(model, "spam_model.pkl")
print("Model trained and saved!")