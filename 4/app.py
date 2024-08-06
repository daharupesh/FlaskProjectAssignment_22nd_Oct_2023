from flask import Flask, render_template, request

app = Flask(__name__)

# Sample content data
content = [
    {"id": 1, "title": "Science Video", "tags": ["science", "education"]},
    {"id": 2, "title": "Nature Documentary", "tags": ["nature", "documentary"]},
    {"id": 3, "title": "Tech Talk", "tags": ["technology", "innovation"]},
    {"id": 4, "title": "Wildlife Exploration", "tags": ["nature", "wildlife"]},
    {"id": 5, "title": "Physics Lecture", "tags": ["science", "physics"]},
    {"id": 6, "title": "AI Innovations", "tags": ["technology", "AI"]},
]

# Recommendation function
def recommend_content(user_prefs, content_list):
    recommendations = []
    for content in content_list:
        if any(tag in content['tags'] for tag in user_prefs):
            recommendations.append(content)
    return recommendations

@app.route('/', methods=['GET', 'POST'])
def home():
    recommendations = []
    if request.method == 'POST':
        user_prefs = request.form.getlist('preferences')
        recommendations = recommend_content(user_prefs, content)
    return render_template('index.html', recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
