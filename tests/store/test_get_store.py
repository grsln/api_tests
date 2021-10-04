from fixtures.store.model import StoreModel


class TestStore:
    def test_get_stores(self, app, auth_user):
        """
        1. Add new store
        1. Try to get store
        2. Check that status code is 200
        """
        name_store = StoreModel.random()
        app.store.add_new_store(name_store=name_store, header=auth_user.header)
        res = app.store.get_stores(name_store=name_store, header=auth_user.header)
        assert res.status_code == 200
