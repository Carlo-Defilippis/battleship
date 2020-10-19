from flask import Flask, render_template, request, jsonify, url_for, redirect
from app import app

@app.route('/')

@app.route('/index', methods = ['GET', 'POST'])
def index():
    user = {'username': 'Damian'}

    if request.method == 'POST':
        board = request.form.get('board')
        
        return redirect(url_for('board', board=board))
    return render_template('index.html', title='Home', user=user)

@app.route('/board')
def board():
    board = request.args.get('board', None)
    print(board)
    e_board = [
            ["A","  ","  ","  ","  ","  ","  ","  ","  ","  "," "],
            ["B","  ","  ","  ","  ","  ","  ","  ","  ","  "," "],
            ["C","  ","  ","  ","  ","  ","  ","  ","  ","  "," "],
            ["D","  ","  ","  ","  ","  ","  ","  ","  ","  "," "],
            ["E","  ","  ","  ","  ","  ","  ","  ","  ","  "," "],
            ["F","  ","  ","  ","  ","  ","  ","  ","  ","  "," "],
            ["G","  ","  ","  ","  ","  ","  ","  ","  ","  "," "],
            ["H","  ","  ","  ","  ","  ","  ","  ","  ","  "," "],
            ["I","  ","  ","  ","  ","  ","  ","  ","  ","  "," "],
            ["J","  ","  ","  ","  ","  ","  ","  ","  ","  "," "]
        ]

    m_board = [ 
            ["A","  ","  ","  ","  ","  ","  ","  ","  ","  "," "],
            ["B","  ","  ","  ","  ","  ","  ","  ","  ","  "," "],
            ["C","  ","  ","  ","  ","  ","  ","  ","  ","  "," "],
            ["D","  ","  ","  ","  ","  ","  ","  ","  ","  "," "],
            ["E","  ","  ","  ","  ","  ","  ","  ","  ","  "," "],
            ["F","  ","  ","  ","  ","  ","  ","  ","  ","  "," "],
            ["G","  ","  ","  ","  ","  ","  ","  ","  ","  "," "],
            ["H","  ","  ","  ","  ","  ","  ","  ","  ","  "," "],
            ["I","  ","  ","  ","  ","  ","  ","  ","  ","  "," "],
            ["J","  ","  ","  ","  ","  ","  ","  ","  ","  "," "]
        ]


    return render_template('board.html', 
            title='Battleship', 
            e_board=e_board,
            m_board=m_board)

if __name__ == '__main__':
    app.run(debug=True)
