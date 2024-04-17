from typing import Type, Generic

from sqlalchemy import Engine
from sqlalchemy.orm import Session

from app.db.decorator import repository_registry
from app.db.repository.respository_base import TRepositoryBase
from app.db.models.base import Base, TBase


class DbSession(Generic[TRepositoryBase]):
    def __init__(self, engine: Engine) -> None:
        self.session = Session(engine)

    def get_repository(self, model: Type[Base]) -> TRepositoryBase:
        """
        Returns an instantiated repository for the given model class

        :param model:
        :return:
        """
        repo_class = repository_registry.get(model)
        if repo_class:
            return repo_class(self.session)  # type: ignore
        raise ValueError(f"No repository registered for model {model}")

    def add_resource(self, entry: TBase) -> None:
        """
        Add a resource to the session, so it will be inserted/updated in the database on the next commit

        :param entry:
        :return:
        """
        self.session.add(entry)

    def delete_resource(self, entry: TBase) -> None:
        """
        Delete a resource from the session, so it will be deleted from the database on the next commit

        :param entry:
        :return:
        """
        # database cascading will take care of the rest
        self.session.delete(entry)

    def commit(self) -> None:
        """
        Commits any pending work in the session to the database

        :return:
        """
        self.session.commit()

    def rollback(self) -> None:
        """
        Rollback the current transaction

        :return:
        """
        self.session.rollback()
