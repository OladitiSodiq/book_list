from flask import Flask, Blueprint,request, jsonify
import mysql.connector
import datetime


book_api = Blueprint('book_api', __name__, url_prefix='/api/v1/books')

app = Flask(__name__)

# MySQL Configuration
mysql_host = 'localhost'
mysql_user = 'root'
mysql_password = ''
mysql_db = 'book_list'

# Connect to MySQL
db = mysql.connector.connect(
    host=mysql_host,
    user=mysql_user,
    password=mysql_password,
    database=mysql_db
)

@book_api.route('/', methods=['GET'])
def get_todos():
    cursor = db.cursor()
    cursor.execute('SELECT * FROM books')
    todos = cursor.fetchall()
    cursor.close()
    column_names = [col[0] for col in cursor.description]

    formatted_todos = []
    for todo in todos:
        formatted_todo = {column_names[i]: todo[i] for i in range(len(todo))}
        formatted_todos.append(formatted_todo)

    response = {
        "status_code": 200,
        "status": "success",
        "data": formatted_todos
    }

    return jsonify(response)

@book_api.route('/external-books', methods=['GET'])
def get_external_books():
    name_of_a_book = request.args.get('name')

    if name_of_a_book:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM books where name='+name_of_a_book) 
        todos = cursor.fetchall()
        cursor.close()
        column_names = [col[0] for col in cursor.description]

        formatted_todos = []
        for todo in todos:
            formatted_todo = {column_names[i]: todo[i] for i in range(len(todo))}
            formatted_todos.append(formatted_todo)

        response = {
            "status_code": 200,
            "status": "success",
            "data": formatted_todos
        }

    else:
         response = {
            "status_code": 200,
            "status": "success",
            "data": []
        }
    return jsonify(response)
    

@book_api.route('/', methods=['POST'])
def add_books():
    data = request.get_json()
    task = data.get('name')
    isbn = data.get('isbn')
    authors = data.get('authors')
    country = data.get('country')
    number_of_pages = data.get('number_of_pages')
    publisher = data.get('publisher')
    release_date = data.get('release_date')

    try:
        # Execute the INSERT statement
        cursor = db.cursor()
        cursor.execute('INSERT INTO books (name, isbn, authors, country, number_of_pages, publisher, release_date) VALUES (%s, %s, %s, %s, %s, %s, %s)', (task, isbn, authors, country, number_of_pages, publisher, release_date))
        db.commit()
        book_id = cursor.lastrowid
        
        # Close the cursor
        cursor.close()
        
        # Prepare the response data
        data = {
            "authors": authors,
            "country": country,
            "id": book_id,
            "isbn": isbn,
            "name": task,
            "number_of_pages": number_of_pages,
            "publisher": publisher,
            "release_date": release_date
        }

        response = {
            "status_code": 200,
            "status": "success",
            "data": [data]
        }
        
        return jsonify(response), 201
    except Exception as e:
        db.rollback()
        return jsonify({"error": str(e)}), 500


@book_api.route('/<int:book_id>', methods=['PATCH'])
def update_book(book_id):
    
    try:
        
        # Get data from the request
        data = request.get_json()
        # Extract fields to update
        fields_to_update = {key: value for key, value in data.items() if value is not None}

        if not fields_to_update:
            return jsonify({"error": "No fields to update provided"}), 400

        # Prepare SET clause for SQL query
        set_clause = ', '.join([f"{key} = '{value}'" for key, value in fields_to_update.items()])


        
        print(set_clause)
        # Execute the UPDATE statement
        cursor = db.cursor()
        cursor.execute(f"UPDATE books SET {set_clause} WHERE id = %s", (book_id,))
        db.commit()
    

        # Fetch the updated record from the database
        cursor.execute('SELECT * FROM books WHERE id = %s', (book_id,))
        updated_book = cursor.fetchone()

        cursor.close()

        if updated_book is None:
            return jsonify({"error": "Book not found"}), 404

        # Prepare the response data
        response_data = {
            "id": updated_book[0],
            "name": updated_book[1],
            "authors": updated_book[2],
            "isbn": updated_book[3],
            "country": updated_book[4],
            "publisher": updated_book[5],
            "number_of_pages": updated_book[6],
           "release_date": updated_book[7]
        }

        return jsonify({"data": response_data}), 200
    except Exception as e:
        db.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/api/v1/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    try:
        # Execute the DELETE statement
        cursor = db.cursor()
        cursor.execute('DELETE FROM books WHERE id = %s', (book_id,))
        db.commit()

        # Check if any rows were affected
        if cursor.rowcount == 0:
            return jsonify({"error": "Book not found"}), 404

        cursor.close()
        
        return jsonify({"message": "Book deleted successfully"}), 200
    except Exception as e:
        db.rollback()
        return jsonify({"error": str(e)}), 500



app.register_blueprint(book_api)

if __name__ == '__main__':
    app.run(debug=True)
