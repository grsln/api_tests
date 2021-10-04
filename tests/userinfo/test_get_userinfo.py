class TestGetUserInfo:
    def test_get_user_info(self, app, user_info):
        """
        Steps.
            1. Try to get user info
            2. Check that status code is 200
        """
        res = app.userinfo.get_user_info(
            user_id=user_info.uuid, header=user_info.header
        )
        assert res.status_code == 200
