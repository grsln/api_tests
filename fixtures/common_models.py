import attr

from fixtures.base import BaseClass
from fixtures.register.model import RegisterUserModel
from fixtures.userinfo.model import UserInfoModel


@attr.s
class MessageResponse:
    message: str = attr.ib()


@attr.s
class UserStore(BaseClass):
    user: RegisterUserModel = attr.ib(default=None)
    uuid: int = attr.ib(default=None)
    header: dict = attr.ib(default=None)
    user_info: UserInfoModel = attr.ib(default=None)


@attr.s
class AuthInvalidResponse:
    description: str = attr.ib()
    error: str = attr.ib()
    status_code: int = attr.ib()
