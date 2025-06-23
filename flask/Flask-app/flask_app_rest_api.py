from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///games.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    platform = db.Column(db.String(50), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/api/games', methods=['GET'])
def api_get_games():
    games = Game.query.all()
    return jsonify([
        {
            "id": game.id,
            "title": game.title,
            "genre": game.genre,
            "platform": game.platform
        }
        for game in games
    ]), 200

@app.route('/api/games', methods=['POST'])
def api_add_game():
    try:
        data = request.get_json()
        new_game = Game(
            title=data['title'],
            genre=data['genre'],
            platform=data['platform']
        )
        db.session.add(new_game)
        db.session.commit()
        return jsonify({"message": "Game added successfully"}), 200
    except:
        return jsonify({"error": "Failed to insert game"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
