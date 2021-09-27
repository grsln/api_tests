from fixtures.userinfo.model import UserInfoModel


class TestUserInfo:
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

    def test_update_user_info(self, app, user_info):
        """
        Steps.
            1. Add user info
            1. Try to update user info
            2. Check that status code is 200
        """
        data = UserInfoModel.random()
        app.userinfo.add_user_info(
            user_id=user_info.uuid, data=data, header=user_info.header
        )
        data = UserInfoModel.random()
        res = app.userinfo.update_user_info(
            user_id=user_info.uuid, data=data, header=user_info.header
        )
        assert res.status_code == 200

    def test_get_user_info(self, app, auth_user):
        """
        Steps.
            1. Add user info
            1. Try to get user info
            2. Check that status code is 200
        """
        data = UserInfoModel.random()
        app.userinfo.add_user_info(
            user_id=auth_user.uuid, data=data, header=auth_user.header
        )
        res = app.userinfo.get_user_info(
            user_id=auth_user.uuid, header=auth_user.header
        )
        assert res.status_code == 200

    def test_delete_user_info(self, app, auth_user):
        """
        Steps.
            1. Add user info
            1. Try to delete user info
            2. Check that status code is 200
        """
        data = UserInfoModel.random()
        app.userinfo.add_user_info(
            user_id=auth_user.uuid, data=data, header=auth_user.header
        )
        res = app.userinfo.delete_user_info(
            user_id=auth_user.uuid, header=auth_user.header
        )
        assert res.status_code == 200
