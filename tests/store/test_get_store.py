from fixtures.store.model import StoreModel


class TestGetStore:
    def test_get_stores(self, app, auth_user):
        """
        1. Add new store
        2. Try to get store
        3. Check that status code is 200
        """
        store = StoreModel.random()
        app.store.add_new_store(name_store=store.name_store, header=auth_user.header)
        res = app.store.get_stores(name_store=store.name_store, header=auth_user.header)
        assert res.status_code == 200
