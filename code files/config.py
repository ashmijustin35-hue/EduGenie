import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()


class Settings:
    """
    EduGenie application settings.
    """

    APP_NAME: str = "EduGenie"
    APP_VERSION: str = "1.0.0"
    APP_DESCRIPTION: str = "Google Gemini Powered Learning Assistant"

    # Gemini API configuration
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")

    # Gemini model
    GEMINI_MODEL: str = os.getenv(
        "GEMINI_MODEL",
        "gemini-2.5-flash"
    )

    # Server configuration
    HOST: str = os.getenv(
        "HOST",
        "127.0.0.1"
    )

    PORT: int = int(
        os.getenv(
            "PORT",
            "8000"
        )
    )

    # Debug mode
    DEBUG: bool = os.getenv(
        "DEBUG",
        "True"
    ).lower() == "true"


# Create settings object
settings = Settings()
