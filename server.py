from flask import render_template,request,Flask,redirect

app = Flask(__name__,template_folder='templates')

@app.route('/')
def index():
    return render_template('hello.html')

if __name__=="__main__":
    app.debug = True
    app.run(host='0.0.0.0')
