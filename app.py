from flask import Flask, jsonify

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


@app.route('/movies')
def get_movies():
    return jsonify(movies_data)


app.run()
