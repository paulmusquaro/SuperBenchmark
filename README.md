# **SuperBenchmark**

SuperBenchmark is a FastAPI-based application designed to manage and query benchmarking results for a Large Language Model (LLM). It allows users to efficiently calculate and retrieve average performance statistics, providing insights into the behavior of LLMs across various metrics.

---

## **Libraries Used**

This project utilizes several key libraries, each playing a vital role in ensuring the functionality, scalability, and maintainability of the application. Here’s an overview of the libraries used:

### **1. FastAPI**
- **Description**: A modern, high-performance web framework for building APIs with Python, based on standard Python type hints.
- **Creator**: **Sebastián Ramírez**, introduced in 2018.
- **Purpose**: Powers the API endpoints, enabling efficient routing, type validation, and automatic OpenAPI documentation.

### **2. Pydantic**
- **Description**: A data validation and settings management library using Python type annotations.
- **Creator**: **Samuel Colvin**, introduced in 2018.
- **Purpose**: Validates and enforces the structure of the benchmarking data with ease.

### **3. Uvicorn**
- **Description**: A lightning-fast ASGI server implementation for Python.
- **Creator**: **Tom Christie**, introduced in 2018.
- **Purpose**: Hosts the FastAPI application, ensuring performance and scalability.

### **4. Pytest**:
  - **Description**: A testing framework for Python that makes it easy to write simple and scalable test cases.
  - **Creator**: **Holger Krekel**, introduced in 2004.
  - **Purpose**: Provides a simple way to write tests, offering powerful tools to write complex testing scenarios.

### **5. Black**:
  - **Description**: An opinionated code formatter for Python that ensures consistent code style across a project.
  - **Creator**: **Łukasz Langa**, introduced in 2018.
  - **Purpose**: Automatically formats Python code according to a specific style, ensuring consistency and readability.

---

## **Project Overview**

SuperBenchmark is built to support the following functionalities:

### **Endpoints**
1. **GET `/results/average`**
   - **Purpose**: Calculates and returns the average performance metrics across all benchmarking results.
   - **Metrics**:
     - Token count
     - Time to first token
     - Time per output token
     - Total generation time

2. **GET `/results/average/{start_time}/{end_time}`**
   - **Purpose**: Calculates and returns the average performance metrics for benchmarking results within a specified time window.
   - **Time Format**: ISO 8601 (`YYYY-MM-DDTHH:MM:SS`).

### **Features**
- **Data Fields**:
  Each benchmarking result contains:
  - `request_id`: Unique identifier
  - `prompt_text`: Input prompt used for LLM
  - `generated_text`: Output generated by the LLM
  - `token_count`: Number of tokens in the output
  - `time_to_first_token`: Time taken to generate the first token
  - `time_per_output_token`: Average time per token
  - `total_generation_time`: Total generation time
  - `timestamp`: Time of benchmarking

- **DEBUG Mode**:
  - Reads data directly from a JSON file (`test_database.json`) to mimic a database.
  - Configurable via the `SUPERBENCHMARK_DEBUG` environment variable.
  - If `DEBUG=False`, an error will indicate that the feature is unavailable in production mode.

- **Code Quality**:
  - Enforces strict formatting, type-checking, and linting to ensure maintainable and reliable code.

---

## **Installation and Setup**

Follow these steps to set up the SuperBenchmark application on your system.

### **1. Clone the Repository**
```bash
git clone https://github.com/paulmusquaro/SuperBenchmark.git
```

### **2. Install Dependencies**
```bash
poetry install
```

### **3. Activate the Virtual Environment**
```bash
poetry shell
```

### **4. Install Development Dependencies**
To install all dependencies in the `dev` group (such as Black, Pytest, etc.), use:
```bash
poetry install --with dev
```

### **5. Configure Environment Variables**
Create a `.env` file in the project root directory and add the following:
```
SUPERBENCHMARK_DEBUG=True
```

### **6. Run the Application**
Start the FastAPI server using Uvicorn:
```bash
uvicorn app.main:app --reload
```

The application will be available at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

### **7. Run Tests**
To ensure everything is working correctly:
```bash
pytest tests/test_main.py
```

### **8. Check Code Formatting with Black**
To check whether your code follows the Black formatting rules without making any changes, use:
```bash
black --check .
```
If your code meets the standards, you will see: `All done!` If there are issues, Black will list the files that need to be fixed.

---

## **Project Improvements and Future Features**

While **SuperBenchmark** is already a powerful tool for managing benchmarking results, there are several potential improvements and additional features that could enhance its functionality:

### **1. Enhanced User Interface**
Currently, the project is focused on backend functionality. Adding a user interface, possibly with **Jinja2 templates**, could allow users to view the benchmarking results more interactively. This could include features like filtering, sorting, or visualizing results with charts.

### **2. Additional Endpoints**
- **GET `/results/{request_id}`**: To retrieve the details of a specific benchmark result by its `request_id`.
- **POST `/results`**: To allow users to submit new benchmarking data.

### **3. Extended Testing**
To ensure robustness, more comprehensive unit and integration tests can be added, including:
- Testing various edge cases, such as missing or malformed data.
- Simulating large volumes of data to test performance under load.
- Adding tests for new endpoints (e.g., GET, POST).

### **4. Performance Optimizations**
- **Caching**: Implement caching mechanisms for frequently requested data to reduce computation time.
- **Asynchronous Processing**: Some long-running benchmarking tasks could be offloaded to background workers using tools like **Celery** for better scalability.

### **5. API Authentication and Authorization**
Implement authentication and authorization to restrict access to sensitive benchmarking data, ensuring that only authorized users can query or submit results.

---

## **Summary**

SuperBenchmark is a robust application designed to provide actionable insights into the performance of Large Language Models. By leveraging modern Python frameworks and tools like FastAPI, Pydantic, and Uvicorn, it achieves high performance and maintainability. The DEBUG mode allows developers to quickly test the application using a mock database, ensuring a smooth development process.

This application is an excellent starting point for anyone looking to manage, query, and analyze benchmarking results for LLMs effectively. Additionally, there are plenty of opportunities to extend and improve the project with new features, better UI, more tests, and further optimizations.

