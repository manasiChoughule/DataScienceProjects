from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route("/classify_image", methods = ['GET','POST'])
def classify_image():
	image_data = request.form['image_data']

	response = jsonify(util.classify_image(image_data))

	response.headers.add('Access-Control-Allow-Origin','*')

	return response

if __name__ == "__main__":
	print("Startig Python Flask Server For Actor Image Classification")
	util.load_saved_artifacts()
	app.run(host = 'https://mason.gmu.edu/~mchoughu/ImageClassification/UI/app.html', port = 5000, debug=False ,use_reloader=False)