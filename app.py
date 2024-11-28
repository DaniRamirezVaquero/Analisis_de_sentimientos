from flask import Flask, render_template, request
from steam_api import get_app_list, get_appid

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

@app.route('/reviews/<int:appid>')
def reviews(appid):
    # Aquí puedes agregar el código para obtener y mostrar las reseñas del juego
    # Por ahora, solo mostramos una página de ejemplo
    return render_template('reviews.html', appid=appid)

if __name__ == '__main__':
    app.run(debug=True)