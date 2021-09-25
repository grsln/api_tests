from time import time


class TestStore:
    def test_add_store(self, app, auth_user):
        """
        1. Try to add new store
        2. Check that status code is 201
        """
        timestamp = int(time())
        name_store = f"store_{timestamp}"
        app.store.add_new_store(name_store=name_store, header=auth_user.header)
        res = app.store.get_stores(name_store=name_store, header=auth_user.header)
        assert res.status_code == 200

    def test_get_stores(self, app, auth_user):
        """
        1. Add new store
        1. Try to get store
        2. Check that status code is 201
        """
        timestamp = int(time())
        name_store = f"store_{timestamp}"
        res = app.store.add_new_store(name_store=name_store, header=auth_user.header)
        assert res.status_code == 201