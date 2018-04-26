from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')

@app.route('/')
def index():
    friends = mysql.query_db("SELECT * FROM friends")
    print friends
    return render_template('index.html', all_friends=friends)

@app.route('/friends', methods=['POST'])
def create():
     # we want to insert into our query.
     # We'll then create a dictionary of data from the POST data received.
     # Run query, with dictionary values injected into the query.
    query = "INSERT INTO friends (name, age, friends_since, created_at, updated_at) VALUES (:name, :age, NOW(), NOW(), NOW())"
    data = {
             'name': request.form['name'],
             'age':  request.form['age'],
           }
    mysql.query_db(query, data)
    print request.form['name']
    print request.form['age']
    return redirect('/')

# @app.route('/friends/<friend_id>')
# def show(friend_id):
#     query = "SELECT * FROM friends WHERE id = :specific_id"
#     data = {'specific_id': friend_id}  
#     print friend_id
#     friends = mysql.query_db(query, data)
#     return render_template('index.html', one_friend=friends[0])
#     # Write query to select specific user by id. At every point where
    # we want to insert data, we write ":" and variable name.
    # Then define a dictionary with key that matches :variable_name in query.
    # Run query with inserted data.
    # Friends should be a list with a single object,
    # so we pass the value at [0] to our template under alias one_friend.

# # Say we wanted to update a specific record, we could create another page and add a form that would submit to the following route:
# @app.route('/update_friend/<friend_id>', methods=['POST'])
# def update(friend_id):
#     query = "UPDATE friends SET first_name = :first_name, age = :age WHERE id = :id"
#     data = {
#              'first_name': request.form['first_name'],
#              'age':  request.form['age'],
#              'id': friend_id
#            }
#     mysql.query_db(query, data)
#     return redirect('/')

# @app.route('/remove_friend/<friend_id>', methods=['POST'])
# def delete(friend_id):
#     query = "DELETE FROM friends WHERE id = :id"
#     data = {'id': friend_id}
#     mysql.query_db(query, data)
#     return redirect('/')

app.run(debug=True)