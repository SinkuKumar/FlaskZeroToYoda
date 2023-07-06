from flask import Flask, jsonify, request

app = Flask(__name__)

movies_data = [
    {
        "name": "Ready Player One",
        "cast": ["Tye Sheridan", "Olivia Cooke", "Ben Mendelsohn"],
        "genre": "Sci-Fi"
    },
    {
        "name": "The Matrix",
        "cast": ["Keanu Reeves", "Laurence Fishburne", "Carrie-Anne Moss"],
        "genre": "Action"
    },
    {
        "name": "The Lord of the Rings: The Fellowship of the Ring",
        "cast": ["Elijah Wood", "Ian McKellen", "Liv Tyler"],
        "genre": "Fantasy"
    },
    {
        "name": "The Shawshank Redemption",
        "cast": ["Tim Robbins", "Morgan Freeman", "Bob Gunton"],
        "genre": "Drama"
    },
    {
        "name": "The Godfather",
        "cast": ["Marlon Brando", "Al Pacino", "James Caan"],
        "genre": "Crime"
    }
]


@app.route('/')
def get_movies():
    return jsonify(movies_data)


@app.route('/movies', methods=['POST'])
def add_movie():
    movie = request.get_json()
    movies_data.append(movie)
    return {'id': len(movies_data)}, 200


@app.route('/movies/<int:index>', methods=['PUT'])
def update_movie(index):
    movie_data = request.get_json()
    movies_data[index] = movie_data
    return jsonify(movies_data[index]), 200


@app.route('/movies/<int:index>', methods=['DELETE'])
def delete_movie(index):
    movies_data.pop(index)
    return 'None', 200


app.run()
