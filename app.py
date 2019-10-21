from flask import Flask,render_template
from runner import main as get_results
app = Flask(__name__)


@app.route('/')
def hello():
	data = get_results()
	return render_template("results.html",data=data)
    
    
if __name__ == '__main__':
	app.run()
