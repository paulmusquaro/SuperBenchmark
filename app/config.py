import os

def get_debug_mode():
    """Get DEBUG mode from the environment variable."""
    return os.getenv("SUPERBENCHMARK_DEBUG", "True").lower() == "true"
