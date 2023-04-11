from flask import Flask, render_template, request
import requests
app = Flask(__name__,static_url_path='/static')

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        input_text = request.form['text']
        output = predict_genres(input_text)[0]
        print(output)
        # data = [{'label': 'General', 'confidence': 0.118407034873962}, {'label': 'Action', 'confidence': 0.2966817617416382}, {'label': 'Strategy', 'confidence': 0.15596598386764526}, {'label': 'Adventure', 'confidence': 0.13903513550758362}, {'label': 'Arcade', 'confidence': 0.11551061272621155}]
        # filtered_data = [{'label': d['label'], 'confidence': d['confidence']} for d in output['confidences'] if d['confidence'] >= 0.3]
        filtered_data = [{'label': d['label'], 'confidence': round(d['confidence']*100, 2)} for d in output['confidences'] if d['confidence'] >= 0.3]
        print(filtered_data)
        if filtered_data:
            print('result')
            return render_template('index.html', results=filtered_data,show='result',initial_text = input_text) 
            
        else:
            print('empty')
            return render_template('index.html', results=filtered_data,show='empty',initial_text = input_text) 
    else:
        return render_template('index.html',show=False) 

def predict_genres(input_text):
    response = requests.post("https://abrar-adnan-game-classifier.hf.space/run/predict", json={
	"data": [
		input_text
	]}).json()
    data = response["data"]
    return data


if __name__ == '__main__':
    app.run(debug=True)