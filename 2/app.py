from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/weatherapp", methods=["POST", "GET"])
def get_weather_data():
    if request.method == "POST":
        url = "https://api.weatherbit.io/v2.0/current"
        params = {
            "lat": float(request.form.get("lat")),
            "lon": float(request.form.get("lon")),
            "key": request.form.get("api"),
            "include": request.form.get("include")
        }
        response = requests.get(url, params=params)
        data = response.json()
        return render_template("index1.html", weather_data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
