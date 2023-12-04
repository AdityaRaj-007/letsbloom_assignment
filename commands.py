from flask import Flask, Response, request, jsonify
from pymongo.mongo_client import MongoClient
from bson.objectid import ObjectId
import json
import time

uri = "mongodb+srv://iamadityaraj2001:test@cluster0.mnale5f.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

max_retry = 3
wait_before_retry = 5

for tries in range(max_retry):
    try:
        # Send a ping to confirm a successful connection
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")

        database_name = "library"
        db = client[database_name]

        collection_name = "books"
        records = db[collection_name]

        break
    except Exception as e:
        print(f"Error connecting to the database (Attempt {tries + 1}/{max_retry}): {e}")
        # Sleep before the next retry
        time.sleep(wait_before_retry)
else:
    raise ConnectionError("Failed to connect to the database after multiple retries.")

app = Flask(__name__)


@app.route("/api/books", methods=["GET"])
def get_details_of_all_the_books():
    try:
        data = list(db.books.find())
        for books in data:
            books["_id"] = str(books["_id"])
        return Response(
            response=json.dumps(data),
            status=200
        )
    except Exception as ex:
        print(ex)


@app.route("/api/books", methods=["POST"])
def add_book():
    try:
        # Parse incoming JSON data
        data = request.get_json()

        # Set default values if not provided
        book_details = {
            "name": data.get("name"),
            "author": data.get("author"),
            "quantity": data.get("quantity", 1),
        }

        existing_book = db.books.find_one({"name": book_details["name"]})

        if existing_book:
            # Book already exists, return a response indicating it's not added again
            response = {
                "message": "Book already exists in the database",
                "existing_book_id": str(existing_book["_id"])
            }
        else:
            # Insert book details into the database
            db_response = db.books.insert_one(book_details)

            # Return a response to the client
            response = {
                "message": "Book added successfully",
                "inserted_id": str(db_response.inserted_id),
            }
        return jsonify(response)

    except Exception as ex:
        print(ex)
        return jsonify({"error": "An error occurred while processing the request"}), 500


@app.route("/api/books/<string:id>", methods=["PUT"])
def update_book_data(id):
    try:
        data = request.get_json()

        # Construct filter criteria based on the book's ObjectId
        filter_criteria = {"_id": ObjectId(id)}

        # Update the book details
        update_result = db.books.update_one(filter_criteria, {"$set": data})

        if update_result.modified_count > 0:
            response = {
                "message": f"Book with id {id} updated successfully",
                "modified_count": update_result.modified_count,
            }
            return jsonify(response)
        else:
            return jsonify({"error": f"No book found with id {id}"}), 404
    except Exception as e:
        print(e)
        return Response(
            response=json.dumps({"message":"Cannot update book details"}),
            status=500
        )


if __name__ == "__main__":
    app.run(port=5555, debug=True)
