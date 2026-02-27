# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple RESTful web service using the FastAPI framework. Students will create endpoints, handle requests, and return JSON responses.

## 📝 Tasks

### 🛠️	Create basic API endpoints

#### Description
Build a FastAPI application with at least two different routes. One should return a welcome message and another should return user-provided data.

#### Requirements
Completed program should:

- Use `FastAPI` to create an application instance
- Define at least two `@app.get` routes
- Return JSON responses using dictionaries


### 🛠️	Add dynamic parameters and data validation

#### Description
Extend the API by adding path and query parameters. Validate the data types and return appropriate status codes.

#### Requirements
Completed program should:

- Accept a path parameter (e.g. `/items/{item_id}`)
- Accept a query parameter (e.g. `?q=search`)
- Use Pydantic models for request or response validation (optional but encouraged)


