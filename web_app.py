import re
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        test_string = request.form.get('test_string')
        regex_pattern = request.form.get('regex_pattern')
        matches = find_matches(test_string, regex_pattern)
        return render_template('output.html', test_string=test_string, regex_pattern=regex_pattern, matches=matches)

    return render_template('home.html')

@app.route('/results', methods=['POST'])
def results():
    test_string = request.form.get('test_string')
    regex_pattern = request.form.get('regex_pattern')
    matches = find_matches(test_string, regex_pattern)
    return render_template('output.html', test_string=test_string, regex_pattern=regex_pattern, matches=matches)

def find_matches(test_string, regex_pattern):
    matches = re.findall(regex_pattern, test_string)
    return matches


@app.route("/validate_email", methods=["GET", "POST"])
def validate_email():
    is_valid_email = None
    if request.method == "POST":
        email = request.form["email"]
        # Simple regex for email validation
        is_valid_email = re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None
    return render_template("output.html", is_valid_email=is_valid_email)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)