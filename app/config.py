import os
from dotenv import load_dotenv

load_dotenv()


def get_debug_mode():
    """Get DEBUG mode from the environment variable."""
    debug_mode = os.getenv("SUPERBENCHMARK_DEBUG", "True")
    print(f"DEBUG MODE: {debug_mode}")
    return debug_mode.lower() == "true"
