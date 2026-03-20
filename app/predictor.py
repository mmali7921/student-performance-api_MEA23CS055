import joblib
import os
from .schemas import StudentInput


MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "student_model.pkl")
model = joblib.load(MODEL_PATH)


def predict_performance(data: StudentInput) -> str:
    features = [[
        data.attendance,
        data.study_hours,
        data.previous_gpa,
        data.internal_marks,
    ]]
    prediction = model.predict(features)
    return prediction[0]