from enum import Enum


class EnvVarKeys(Enum):
    """
    Enum of environment variables keys used by the application.
    """

    INITIAL_DATABASE_FOR_ANALYSIS_PATH_KEY = "INITIAL_DATABASE_FOR_ANALYSIS_PATH"
    LOG_FILE_PATH_KEY = "LOG_FILE_PATH"
