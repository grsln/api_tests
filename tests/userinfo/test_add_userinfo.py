from fixtures.userinfo.model import UserInfoModel


class TestAddUserInfo:
    def test_add_user_info(self, app, auth_user):
        """
        Steps.
            1. Try to add user info
            2. Check that status code is 200
        """
        data = UserInfoModel.random()
        res = app.userinfo.add_user_info(
            user_id=auth_user.uuid, data=data, header=auth_user.header
        )
        assert res.status_code == 200

    def test_double_add_user_info(self, app, user_info):
        """
        Steps.
            1. Try to add user info
            2. Try again to add user info
            3. Check that status code is 400
        """
        res = app.userinfo.add_user_info(
            user_id=user_info.uuid, data=user_info.user_info, header=user_info.header
        )
        assert res.status_code == 400
