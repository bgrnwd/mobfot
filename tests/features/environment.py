import json
from pathlib import Path

import responses

from pymob import PyMob


@responses.activate
def before_all(context):
    cwd = Path.cwd()

    leagues_file = Path(cwd, "./mocks/league.json")
    details_file = Path(cwd, "./mocks/matchDetails.json")
    matches_file = Path(cwd, "./mocks/matchesByDate.json")
    player_file = Path(cwd, "./mocks/player.json")
    team_file = Path(cwd, "./mocks/team.json")

    responses.add(
        responses.GET,
        "https://www.fotmob.com/api/leagues?",
        json=json.load(leagues_file.open()),
        status=200,
    )

    responses.add(
        responses.GET,
        "https://www.fotmob.com/api/matchDetails?",
        json=json.load(details_file.open()),
        status=200,
    )

    responses.add(
        responses.GET,
        "https://www.fotmob.com/api/matches?",
        json=json.load(matches_file.open()),
        status=200,
    )

    responses.add(
        responses.GET,
        "https://www.fotmob.com/api/playerData?",
        json=json.load(player_file.open()),
        status=200,
    )

    responses.add(
        responses.GET,
        "https://www.fotmob.com/api/team?",
        json=json.load(team_file.open()),
        status=200,
    )

    context.pymob = PyMob()
