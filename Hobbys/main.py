from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/autor')
def autor():
    return render_template('autor.html')

@app.route('/about_site')
def aboute_site():
    return render_template('about_site.html')


app.run(debug=True)