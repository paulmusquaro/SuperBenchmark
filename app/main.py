import json
import os
from datetime import datetime
from fastapi import FastAPI, HTTPException
from app.config import get_debug_mode
from app.models import BenchmarkingResult

app = FastAPI()

# Load DEBUG mode
DEBUG_MODE = get_debug_mode()

# File path to the mock database
TEST_DATABASE_FILE = "app/test_database.json"


# Function to load benchmarking results with validation
def load_benchmarking_results():
    if not DEBUG_MODE:
        raise HTTPException(
            status_code=503, detail="The feature is not ready for live yet."
        )
    try:
        with open(TEST_DATABASE_FILE, "r") as f:
            data = json.load(f)
        # Validate each result with Pydantic
        results = [BenchmarkingResult(**r) for r in data["benchmarking_results"]]
        return results
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="Test database file not found.")
    except KeyError:
        raise HTTPException(status_code=500, detail="Malformed test database file.")
    except json.JSONDecodeError:
        raise HTTPException(
            status_code=500, detail="Error decoding the test database JSON."
        )


# Endpoint to calculate average performance statistics
@app.get("/results/average")
def get_average_results():
    results = load_benchmarking_results()
    if not results:
        raise HTTPException(status_code=404, detail="No benchmarking results found.")

    # Calculate averages
    avg_results = {
        "avg_token_count": sum(r.token_count for r in results) / len(results),
        "avg_time_to_first_token": sum(r.time_to_first_token for r in results)
        / len(results),
        "avg_time_per_output_token": sum(r.time_per_output_token for r in results)
        / len(results),
        "avg_total_generation_time": sum(r.total_generation_time for r in results)
        / len(results),
    }
    return avg_results


# Endpoint to calculate average performance statistics within a time window
@app.get("/results/average/{start_time}/{end_time}")
def get_average_results_within_window(start_time: str, end_time: str):
    try:
        start_dt = datetime.fromisoformat(start_time)
        end_dt = datetime.fromisoformat(end_time)
    except ValueError:
        raise HTTPException(
            status_code=400, detail="Invalid timestamp format. Use ISO 8601 format."
        )

    results = load_benchmarking_results()
    filtered_results = [r for r in results if start_dt <= r.timestamp <= end_dt]
    if not filtered_results:
        raise HTTPException(
            status_code=404,
            detail="No benchmarking results found in the specified time window.",
        )

    # Calculate averages for the filtered results
    avg_results = {
        "avg_token_count": sum(r.token_count for r in filtered_results)
        / len(filtered_results),
        "avg_time_to_first_token": sum(r.time_to_first_token for r in filtered_results)
        / len(filtered_results),
        "avg_time_per_output_token": sum(
            r.time_per_output_token for r in filtered_results
        )
        / len(filtered_results),
        "avg_total_generation_time": sum(
            r.total_generation_time for r in filtered_results
        )
        / len(filtered_results),
    }
    return avg_results
