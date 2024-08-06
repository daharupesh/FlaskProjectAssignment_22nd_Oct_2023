from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
app.config['SECRET_KEY'] = '2b3@5d!_w7qz6^V&fR#n8KjE2*4M9oL@3P7r8CzV0d1X5G6H'
socketio = SocketIO(app, cors_allowed_origins="*")

def scrape_youtube():
    url = 'https://www.youtube.com/results?search_query=flask+tutorial'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    videos = []
    for video in soup.select('a#video-title'):
        title = video['title']
        link = 'https://www.youtube.com' + video['href']
        videos.append({'title': title, 'link': link})
    return videos

def scrape_amazon():
    url = 'https://www.amazon.com/s?k=laptop'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    products = []
    for product in soup.select('.s-title'):
        title = product.get_text().strip()
        products.append({'title': title})
    return products

@app.route('/')
def index():
    youtube_videos = scrape_youtube()
    amazon_products = scrape_amazon()
    return render_template('index.html', youtube_videos=youtube_videos, amazon_products=amazon_products)

@app.errorhandler(404)
def not_found_error(error):
    return render_template('error.html', message="404 Not Found"), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('error.html', message="500 Internal Server Error"), 500

if __name__ == '__main__':
    socketio.run(app, debug=True)
