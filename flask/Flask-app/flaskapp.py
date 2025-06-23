from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "My Flask App"

@app.route('/about')
def about():
    return "Hi, I'm Mateusz. I'm learning about Flask!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)