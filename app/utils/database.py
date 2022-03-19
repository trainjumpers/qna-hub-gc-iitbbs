from typing import List, Union, TypeVar, Type

from asyncpg import Record

T = TypeVar("T")


def deserialize_records(results: Union[Record, List[Record]], dataclass: Type[T]) -> Union[T, List[T]]:
    """Deserializes one or a list of database records into objects of the provided class type.
    Helps to convert data from psql db to python objects.
    Args:
        results: one or more database records
        dataclass: class into which the records are to be deserialized
    returns:
        one or a list of objects of the provided class type
    """

    def parse_record(entry: Record):
        record_dict = {k: v for k, v in entry.items()}
        return dataclass(**record_dict)

    if isinstance(results, Record):
        return parse_record(results)

    return list(map(lambda x: parse_record(x), results))