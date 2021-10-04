class TestDeleteUserInfo:
    def test_delete_user_info(self, app, user_info):
        """
        Steps.
            1. Add user info
            1. Try to delete user info
            2. Check that status code is 200
        """
        res = app.userinfo.delete_user_info(
            user_id=user_info.uuid, header=user_info.header
        )
        assert res.status_code == 200
