import pytest

from fixtures.common_models import AuthInvalidResponse, MessageResponse
from fixtures.constants import ResponseText
from fixtures.userinfo.model import UserInfoModel


class TestUpdateUserInfo:
    def test_update_user_info(self, app, user_info):
        """
        Steps.
            1. Try to update user info
            2. Check that status code is 200
        """
        data = UserInfoModel.random()
        res = app.userinfo.update_user_info(
            user_id=user_info.uuid, data=data, header=user_info.header
        )
        assert res.status_code == 200, "Check status code"
        assert res.data.message == ResponseText.MESSAGE_UPDATE_USER_INFO

    def test_update_user_info_wo_auth_header(self, app, user_info):
        """
        1. Try to update user info wo auth header
        2. Check that status code is 401
        3. Check response
        """
        data = UserInfoModel.random()
        res = app.userinfo.update_user_info(
            user_id=user_info.uuid,
            data=data,
            header=None,
            type_response=AuthInvalidResponse,
        )
        assert res.status_code == 401, "Check status code"
        assert res.data.description == ResponseText.DESCRIPTION_AUTH_ERROR
        assert res.data.error == ResponseText.ERROR_AUTH_TEXT
        assert res.data.status_code == 401, "Check status code"

    def test_update_user_with_none_exist_user_id(
        self, app, user_info, none_exist_user=1000
    ):
        """
        1. Try to update user info with none exist user id
        2. Check that status code is 404
        3. Check response
        """
        data = UserInfoModel.random()
        res = app.userinfo.update_user_info(
            user_id=none_exist_user,
            data=data,
            header=user_info.header,
            type_response=MessageResponse,
        )
        assert res.status_code == 404, "Check status code"
        assert res.data.message == ResponseText.MESSAGE_INFO_NOT_FOUND_DOT

    @pytest.mark.parametrize("uuid", ["ffddass", "@/&", -55, True])
    def test_update_invalid_id_userinfo(self, app, user_info, uuid):
        """
        Steps.
            1. Try to login user with valid data
            2. Add user info
            3. Change user data
            4. Check that status code is 404
            5. Check response
        """
        data = UserInfoModel.random()
        res = app.userinfo.update_user_info(
            user_id=uuid,
            data=data,
            type_response=None,
            header=user_info.header,
        )
        assert res.status_code == 404

    def test_update_userinfo_invalid_header(self, app, user_info):
        """
        Steps.
            1. Try to login user with valid data
            2. Add user info
            3. Change user data
            4. Check that status code is 401
            5. Check response
        """
        data = UserInfoModel.random()
        header = {"Authorization": "JWT 895241"}
        res = app.userinfo.update_user_info(
            user_id=user_info.uuid, data=data, type_response=None, header=header
        )
        assert res.status_code == 401

    @pytest.mark.xfail(reason="Ожидается 400 ошибка")
    def test_invalid_phone_userinfo(self, app, user_info, phone="1" * 10000):
        """
        Steps.
            1. Try to login user with valid data
            2. Add user info
            3. Change user data
            4. Check that status code is 400
            5. Check response
        """
        data = UserInfoModel.random()
        setattr(data, "phone", phone)
        res = app.userinfo.update_user_info(
            user_id=user_info.uuid,
            data=data,
            type_response=None,
            header=user_info.header,
        )
        assert res.status_code == 400
