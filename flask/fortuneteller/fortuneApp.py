from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/fortune', methods=['GET', 'POST'])
def fortune():
    if request.method == 'POST':
        name = request.form['user']
        color = request.form['color']
        number = request.form['number']

        if color == 'red':
            if number == '1':
                fortune = "You will have a lucky day!"
            elif number == '2':
                fortune = "Adventure is on your horizon."
            elif number == '3':
                fortune = "An old friend will reappear soon."
            elif number == '4':
                fortune = "Today is a day for bold moves."
        elif color == 'yellow':
            if number == '1':
                fortune = "Happiness will find you."
            elif number == '2':
                fortune = "You’ll stumble upon a surprise."
            elif number == '3':
                fortune = "Your kindness will be repaid."
            elif number == '4':
                fortune = "Success is coming your way."
        elif color == 'blue':
            if number == '1':
                fortune = "A peaceful moment is near."
            elif number == '2':
                fortune = "You’ll solve a tricky problem."
            elif number == '3':
                fortune = "A new opportunity will arise."
            elif number == '4':
                fortune = "Trust your instincts today."
        elif color == 'green':
            if number == '1':
                fortune = "A financial surprise is coming."
            elif number == '2':
                fortune = "Creativity will guide you."
            elif number == '3':
                fortune = "Take time for yourself today."
            elif number == '4':
                fortune = "A message from afar will arrive."
        else:
            fortune = "Your future is a mystery."

        return render_template('fortune.html', name=name, fortune=fortune)

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
