from typing import Any, Generator

from pymongo import MongoClient
from pymongo.database import Database


def init_mongo_client() -> Generator[MongoClient[dict[str, Any]], None, None]:
    client: MongoClient[dict[str, Any]]
    with MongoClient("mongodb://root:example@0.0.0.0:27017") as client:  # TODO: Config
        yield client


def get_mongo_db(client: MongoClient[dict[str, Any]]) -> Database[dict[str, Any]]:
    return client["traffic"]  # TODO: Config
