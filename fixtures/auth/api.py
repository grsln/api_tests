from requests import Response

from common.deco import logging as log
from fixtures.auth.model import AuthUserModel, AuthUserResponse
from fixtures.validator import Validator


class LogIn(Validator):
    def __init__(self, app):
        self.app = app

    POST_AUTH = "/auth"

    @log("Auth user")
    def login(self, data: AuthUserModel, type_response=AuthUserResponse) -> Response:
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/auth/authUser # noqa
        """
        response = self.app.client.request(
            method="POST",
            url=f"{self.app.url}{self.POST_AUTH}",
            json=data.to_dict(),
        )
        return self.structure(response, type_response=type_response)
