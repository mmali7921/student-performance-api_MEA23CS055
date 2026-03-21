from pydantic import BaseModel, Field


class StudentInput(BaseModel):
    attendance: float = Field(..., ge=0, le=100, description="Attendance %", example=85)
    study_hours: float = Field(..., ge=0, le=24, description="Study hours per day", example=4)
    previous_gpa: float = Field(..., ge=0, le=10, description="GPA (0-10 scale)", example=7.5)
    internal_marks: float = Field(..., ge=0, le=100, description="Internal marks", example=70)
