from flask import Flask, render_template, request, url_for

app = Flask(__name__)  

@app.route('/')
def navbar():
    return render_template('navbar.html')

if __name__ == '__main__':
    app.run(debug=True)
