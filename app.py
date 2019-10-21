from flask import Flask,render_template,request
from runner import app_results as get_results,read_csv
import uuid
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'tmp' + os.sep
ALLOWED_EXTENSIONS = set(['txt', 'csv'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/results',methods=["POST"])
def results():
	
	error = False
	try:
		perasmena = read_csv("perasmena.csv",",")
		
		if 'mathimata' not in request.files:
			
			
			for s in perasmena:
				if s in request.form:
					if request.form[s].lower() == "on":
						perasmena[s]["Passed"] = "1"
					else:
						perasmena[s]["Passed"] = "0"
				else:
					perasmena[s]["Passed"] = "0"
		else:
		
			if "mathimata" in request.files:
				fl = request.files['mathimata']
				
				if fl.filename == "":
					error = True
					p
				elif fl and allowed_file(fl.filename):
					filename = UPLOAD_FOLDER + str(uuid.uuid4())
					fl.save(filename)
					
					file_data = read_csv(filename,",")
					print(file_data)
					
					for s in file_data:
						if "Passed" in file_data[s]:
							if file_data[s]["Passed"] == "1":
								if s in perasmena:
									perasmena[s]["Passed"] = "1"
							else:
								if s in perasmena:
									perasmena[s]["Passed"] = "0"
						
						else:
							if s in perasmena:
								perasmena[s]["Passed"] = "0"
								
							
					
				else:
					error = True
					
				
			else:
				error = True
		
		data = get_results(perasmena)
	except:
		error = True
		
		
	if error:
		return render_template("error.html")
	else:
		return render_template("results.html",data=data)

@app.route('/')
def index():
	subjects = read_csv("mathimata_pada.csv")
	
	return render_template("index.html",subjects=subjects)    
    
if __name__ == '__main__':
	app.run()
