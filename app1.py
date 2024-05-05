from flask import Flask, render_template
from trial import out
app = Flask(__name__)

@app.route('/random', methods=['GET'])
def other():
    result = out()
    return render_template('random.html', number=result)
if __name__ == '__main__':
    app.run(debug=True)
