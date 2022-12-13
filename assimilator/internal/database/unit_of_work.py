from assimilator.core.database import UnitOfWork
from assimilator.core.database.repository import BaseRepository


class DictUnitOfWork(UnitOfWork):
    def __init__(self, repository: BaseRepository):
        super(DictUnitOfWork, self).__init__(repository)
        self._saved_data = None

    def begin(self):
        self._saved_data = self.repository.session
        self.repository.session = dict(self._saved_data)

    def rollback(self):
        self.repository.session = self._saved_data

    def commit(self):
        self._saved_data = self.repository.session

    def close(self):
        pass
