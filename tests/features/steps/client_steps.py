import json
from pathlib import Path
from re import Match

from behave import given, then, when


@given("there is a MobFot client")
def client(context):
    assert context.mobfot is not None


@when('the "{func_name}" function is called')
def called(context, func_name):
    pass


@then('the "{attr_name}" attribute equals "{value}"')
def attribute(context, attr_name, value):
    attr = getattr(context.mobfot, attr_name)
    assert attr == value


@when('the "{func_name}" function is called with parameters "{params}"')
def function_call(context, func_name, params):
    cwd = Path(__file__).parent.parent.parent

    if func_name == "get_league":
        file = Path(cwd, "./mocks/league.json")
    elif func_name == "get_match_details":
        file = Path(cwd, "./mocks/matchDetails.json")
    elif func_name == "get_matches_by_date":
        file = Path(cwd, "./mocks/matchesByDate.json")
    elif func_name == "get_player":
        file = Path(cwd, "./mocks/player.json")
    else:
        file = Path(cwd, "./mocks/team.json")

    context.response = json.load(file.open())


@then("there is a response")
def response(context):
    assert context.response is not None


@when('the "{func_name}" function is called with the following date "{date}"')
def check_date(context, func_name, date):
    func = getattr(context.mobfot, func_name)
    context.date = func(date)


@then("the function returns a Match")
def matched_date(context):
    assert type(context.date) == Match


@then("the function returns None")
def matched_date(context):
    assert context.date == None
