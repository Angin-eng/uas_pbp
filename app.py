from flask import Flask, request, render_template, redirect, url_for
import os
import traceback

# Konfigurasi Flask
app = Flask(__name__)


# Halaman utama
@app.route('/')
def index():
  
    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)
