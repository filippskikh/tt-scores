from flask import Flask, render_template, request

import database
import view_models

app = Flask(__name__)


@app.route("/add_game")
def add_game():
    team1_id = request.args.get('team1_id', '')
    team2_id = request.args.get('team2_id', '')
    score1 = request.args.get('score1', '')
    score2 = request.args.get('score2', '')
    if not team1_id or not team2_id or not score1 or not score2:
        return "Failure"
    elif team1_id == team2_id:
        return "Failure"
    elif int(score1) == 0 and int(score2) == 0:
        return "Failure"
    else:
        database.add_game(team1_id, score1, team2_id, score2)
        return "Success"


@app.route("/add_team")
def add_team():
    team_name = request.args.get('team_name', '')
    if not team_name:
        return "Failure"
    else:
        database.add_team(team_name)
        return "Success"


@app.route("/")
def index():
    teams = database.get_teams()
    games = database.get_games()

    teams_view, games_view = view_models.convert_to_view_model(teams, games)
    return render_template('index.html.j2', teams=teams_view, games=games_view)


database.init()

if __name__ == "__main__":
    app.run(debug=True)
