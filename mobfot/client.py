import re
from logging import getLevelName, getLogger
from typing import Optional, Union

import requests
from cachecontrol import CacheControl

VERSION = "1.0.0"


class MobFot:
    BASE_URL = "https://www.fotmob.com/api"
    LOGGER = getLogger(__name__)

    def __init__(
        self, proxies: Optional[dict] = None, logging_level: Optional[str] = "WARNING"
    ) -> None:
        SESSION = requests.Session()
        if proxies:
            SESSION.proxies.update(proxies)
        CACHE_SESSION = CacheControl(SESSION)

        if logging_level:
            if logging_level.upper() in [
                "DEBUG",
                "INFO",
                "WARNING",
                "ERROR",
                "CRITICAL",
            ]:
                self.LOGGER.setLevel(getLevelName(logging_level.upper()))
            else:
                print(f"Logging level {logging_level} not recognized!")

        self.session = CACHE_SESSION
        self.matches_url = f"{self.BASE_URL}/matches?"
        self.leagues_url = f"{self.BASE_URL}/leagues?"
        self.teams_url = f"{self.BASE_URL}/teams?"
        self.player_url = f"{self.BASE_URL}/playerData?"
        self.match_details_url = f"{self.BASE_URL}/matchDetails?"
        self.search_url = f"{self.BASE_URL}/searchapi/"

    def _check_date(self, date: str) -> Union[re.Match, None]:
        pattern = re.compile(r"(20\d{2})(\d{2})(\d{2})")
        return pattern.match(date)

    def _execute_query(self, url: str):
        response = self.session.get(url)
        response.raise_for_status()
        self.LOGGER.debug(response)
        return response.json()

    def get_matches_by_date(self, date: str) -> dict:
        if self._check_date(date) != None:
            url = f"{self.matches_url}date={date}"
            return self._execute_query(url)
        return {}

    def get_league(
        self,
        id: int,
        tab: str = "overview",
        type: str = "league",
        time_zone: str = "America/New_York",
    ):
        url = f"{self.leagues_url}id={id}&tab={tab}&type={type}&timeZone={time_zone}"
        return self._execute_query(url)

    def get_team(
        self,
        id: int,
        tab: str = "overview",
        type: str = "league",
        time_zone: str = "America/New_York",
    ):
        url = f"{self.teams_url}id={id}&tab={tab}&type={type}&timeZone={time_zone}"
        return self._execute_query(url)

    def get_player(self, id: int):
        url = f"{self.player_url}id={id}"
        return self._execute_query(url)

    def get_match_details(self, match_id: int):
        url = f"{self.match_details_url}matchId={match_id}"
        return self._execute_query(url)
