import flask
from sklearn.linear_model import LogisticRegression
import numpy as np

X = np.linspace(1,1000,50).reshape(-1,1)
Y = np.zeros(50,)

Y[25:] = np.ones(25,)
PREDICTOR = LogisticRegression().fit(X,Y)

app = flask.Flask(__name__)

@app.route('/')
def hello():
	return 'This is an app!'

@app.route('/predict', methods=['POST'])
def predict():
	data = flask.request.json
	x = np.array(data['example']).reshape(-1,1)
	y_pred = PREDICTOR.predict(x)

	y_pred = list(y_pred)

	results = {'predicted': y_pred}

	return flask.jsonify(results)