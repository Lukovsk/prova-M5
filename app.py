# Primeiro, quero criar um servidor em flask para poder acessar as rotas que inserem os valores no banco de dados
from flask import Flask, render_template, request, redirect
# imports para o banco de dados
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models.game import Game

app = Flask(__name__)

engine = create_engine("sqlite:///games.db", echo=True)
Session = sessionmaker(bind=engine)

# Cria as tabelas se elas não existem:
session = Session()
Base.metadata.create_all(engine)


@app.route('/')
def index():
    session = Session()
    
    result = session.query(Game).all()
    
    return render_template('index.html', games=result)


@app.post('/post_game')
def post_game():
    game_name = request.form['game_name']
    platform = request.form['platform']
    price = request.form['price']
    quantity = request.form['quantity']
    
    new_game = Game(game_name = game_name,
                    platform = platform,
                    price = price, 
                    quantity = quantity)
    
    session = Session()
    session.add(new_game)
    session.commit()
    
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
    
    