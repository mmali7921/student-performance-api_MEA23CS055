import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib


df = pd.read_csv("data/clean_student_data.csv")



def categorize_performance(gpa):
    if gpa >= 8.5:
        return "Excellent"
    elif gpa >= 7.0:
        return "Good"
    elif gpa >= 5.0:
        return "Average"
    else:
        return "At Risk"


df["performance"] = df["previous_gpa"].apply(categorize_performance)



X = df[['attendance', 'study_hours', 'previous_gpa', 'internal_marks']]



y = df['performance']



X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)



model = RandomForestClassifier(n_estimators=100, random_state=42)

model.fit(X_train, y_train)



predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("Model Accuracy:", accuracy)



joblib.dump(model, "student_model.pkl")

print("Model saved as student_model.pkl")