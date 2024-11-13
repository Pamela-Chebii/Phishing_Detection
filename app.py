from flask import Flask,render_template,redirect


app=Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/url_detection')
def url_detection():
    return render_template('url_detection.html')


@app.route('/check_url',methods=['POST','GET'])
def check_url():
    return "waiting for model incoporation"



if __name__=='__main__':
    app.run(debug=True)