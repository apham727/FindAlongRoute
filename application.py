from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_directions', methods = ['POST'])
def generate_map():
    start = request.form['start_location']
    end = request.form['end_location']
    user_venues = request.form['venue']
    max_distance = float(request.form['max_deviation']) * 1.60934

    return render_template('map.html', start_location=start, end_location=end, venues=user_venues, max_deviation=max_distance)





if __name__ == "__main__":
    app.run(debug=True)


