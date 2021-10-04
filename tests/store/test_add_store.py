from fixtures.store.model import StoreModel


class TestAddStore:
    def test_add_store(self, app, auth_user):
        """
        1. Try to add new store
        2. Check that status code is 201
        """
        store = StoreModel.random()
        res = app.store.add_new_store(
            name_store=store.name_store, header=auth_user.header
        )
        assert res.status_code == 201
