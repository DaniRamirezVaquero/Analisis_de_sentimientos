from flask import Flask, render_template, request
from steam_api import get_app_list, get_appid, get_game_name, get_game_reviews
from sentiment_classifier import analyze_review, avg_sentiment

app = Flask(__name__)

get_app_list()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search-appid', methods=['POST'])
def search():
    game_name = request.form['game_name']
    matches = get_appid(game_name)
    return render_template('result.html', matches=matches, game_name=game_name)

@app.route('/reviews', methods=['GET', 'POST'])
def reviews():
    if request.method == 'POST':
        appid = request.form['appid']
        name = request.form.get('name', 'Juego desconocido')
    else:
        appid = request.args.get('appid')
        name = get_game_name(appid)
        
    reviews, n_reviews = get_game_reviews(appid)
    
    if (n_reviews == 0):
        return render_template('index.html', no_reviews=True, appid=appid, name=name)

    # Analizar cada reseña
    for review in reviews:
        sentiment, score = analyze_review(review['review'])
        review['sentiment'] = {'label': sentiment, 'score': score}
        
    avg_sent = avg_sentiment(reviews)
    
    return render_template('reviews.html', appid=appid, name=name, reviews=reviews, avg_sent=avg_sent)

if __name__ == '__main__':
    app.run(debug=True)