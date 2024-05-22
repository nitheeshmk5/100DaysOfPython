from flask import Flask,render_template,request
from weather import get_weather
from waitress import serve

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather')
def get_climate():
    lat = request.args.get('lat')
    lng = request.args.get('lng')

    if not bool(lat.strip() or lng.strip()):
        lat = 11.016844
        lng = 76.955833
    weather_data = get_weather(lat,lng)

    if weather_data['cod'] != 200:
        return "City not found"
    
    return render_template(
        'weather.html',
        title=weather_data['name'],
        status = weather_data["weather"][0]["description"],
        temp = f'{weather_data['main']['temp']:.1f}',
        feels_like =f'{weather_data['main']['feels_like']}'
    )


if __name__ == "__main__":
    serve( app,host='0.0.0.0',port=8000)