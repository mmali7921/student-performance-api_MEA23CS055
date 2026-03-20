from pydantic import BaseModel


class StudentInput(BaseModel):
    attendance: float
    study_hours: float
    previous_gpa: float
    internal_marks: float