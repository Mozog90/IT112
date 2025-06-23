from flask import Flask, request
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
        if Game.query.count() == 0:
            db.session.add_all([
                Game(title="The Legend of Zelda", genre="Adventure", platform="Switch"),
                Game(title="Halo Infinite", genre="Shooter", platform="Xbox"),
                Game(title="Stardew Valley", genre="Simulation", platform="PC"),
                Game(title="God of War", genre="Action", platform="PlayStation")
            ])
            db.session.commit()

@app.route('/')
def home():
        return '''
            <h1>Welcome to the App</h1>
            <ul>
                <li><a href="/games">View games</a></li>
            </ul>
        '''

@app.route('/games')
def show_games():
        games = Game.query.all()
        output = "<h1>Video Games</h1><ul>"
        for game in games:
            output += f"<li><a href='/games/{game.id}'>{game.title}</a></li>"
        output += "</ul><a href='/'>Back to home</a>"
        return output

@app.route('/games/<int:game_id>')
def game_detail(game_id):
        game = Game.query.get_or_404(game_id)
        return f'''
            <h1>{game.title}</h1>
            <p><strong>Genre:</strong> {game.genre}</p>
            <p><strong>Platform:</strong> {game.platform}</p>
            <a href="/games">Back to games list</a>
        '''

app.run(host='0.0.0.0', port=81)