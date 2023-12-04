## Letsbloom Assignment

This assignment is done using Flask as the backend framework and MongoDB as the database. It provides a foundation for creating RESTful APIs with CRUD operations.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [API Endpoints](#api-endpoints)

## Introduction

This task serves as a starting point for developing web applications with Flask and MongoDB. It includes the basic structure for setting up a RESTful API with endpoints for CRUD operations on a MongoDB database.

## Features

- MongoDB integration for data storage
- Basic CRUD operations (Create, Read, Update)
- RESTful API design

## Getting Started

Follow the steps below to get this project up and running on your local machine.

### Prerequisites

Ensure you have the following software installed:

- Python
- Flask
- MongoDB

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/AdityaRaj-007/letsbloom_assignment
   cd letsbloom_assignment
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure MongoDB:

   Update the MongoDB connection details in `main.py`:

   ```python
   # Configure your MongoDB connection
   client = MongoClient('your_mongodb_connection_string')
   ```

4. Run the application:

   ```bash
   python main.py
   ```

   The application should now be running on [http://localhost:5555](http://localhost:5555).

## API Endpoints

- `GET /api/books`: Retrieve all books
- `POST /api/books`: Add a new book
- `PUT /api/books/<id>`: Update a book by ID
