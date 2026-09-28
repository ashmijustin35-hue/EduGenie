from pydantic import BaseModel, Field
from typing import Optional


class QuestionRequest(BaseModel):
    """
    Model for receiving a student's question.
    """

    question: str = Field(
        ...,
        min_length=1,
        description="Question asked by the student"
    )


class AnswerResponse(BaseModel):
    """
    Model for returning EduGenie's answer.
    """

    question: str
    answer: str
    success: bool = True


class LearningRequest(BaseModel):
    """
    Model for learning-related requests.
    """

    topic: str = Field(
        ...,
        min_length=1,
        description="Topic the student wants to learn"
    )

    difficulty: Optional[str] = Field(
        default="Beginner",
        description="Difficulty level"
    )

    language: Optional[str] = Field(
        default="English",
        description="Preferred response language"
    )


class QuizRequest(BaseModel):
    """
    Model for generating a quiz.
    """

    topic: str = Field(
        ...,
        min_length=1,
        description="Topic for the quiz"
    )

    number_of_questions: int = Field(
        default=5,
        ge=1,
        le=20,
        description="Number of quiz questions"
    )
