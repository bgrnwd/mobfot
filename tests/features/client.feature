Feature: Client usage

  Scenario: Client intialization
    Given there is a PyMob client
    When the "__init__" function is called
    Then the "BASE_URL" attribute equals "https://www.fotmob.com/api"
    And the "matches_url" attribute equals "https://www.fotmob.com/api/matches?"
    And the "leagues_url" attribute equals "https://www.fotmob.com/api/leagues?"
    And the "teams_url" attribute equals "https://www.fotmob.com/api/teams?"
    And the "player_url" attribute equals "https://www.fotmob.com/api/playerData?"
    And the "match_details_url" attribute equals "https://www.fotmob.com/api/matchDetails?"
    And the "search_url" attribute equals "https://www.fotmob.com/api/searchapi/"

  Scenario: get_matches_by_date
    Given there is a PyMob client
    When the "get_matches_by_date" function is called with parameters "20221205"
    Then there is a response

  Scenario: get_league
    Given there is a PyMob client
    When the "get_league" function is called with parameters "130"
    Then there is a response

  Scenario: get_team
    Given there is a PyMob client
    When the "get_team" function is called with parameters "4061710"
    Then there is a response

  Scenario: get_player
    Given there is a PyMob client
    When the "get_player" function is called with parameters "525631"
    Then there is a response

  Scenario: get_match_details
    Given there is a PyMob client
    When the "get_match_details" function is called with parameters "4050324"
    Then there is a response

  Scenario: Valid date format for the _check_date function
    Given there is a PyMob client
    When the "_check_date" function is called with the following date "20221205"
    Then the function returns a Match

  Scenario: Invalid date format for the _check_date function
    Given there is a PyMob client
    When the "_check_date" function is called with the following date "2022-12-05"
    Then the function returns None