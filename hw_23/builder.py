from typing import Optional, Iterable

from functions import filter_query, map_query, unique_query, sort_query, limit_query

FILE_NAME = 'data/apache_logs.txt'


CMD_FUNC = {
    'filter': filter_query,
    'map': map_query,
    'unique': unique_query,
    'sort': sort_query,
    'limit': limit_query
}


def iterat_file(file_name: str):
    with open(file_name) as file:
        for row in file:
            yield row


def build_query(cmd, value, data: Optional[Iterable[str]]):
    if data is None:
        prepared_data = iterat_file(FILE_NAME)
    else:
        prepared_data = data
    # filtered = filter_query(value, generator)
    # mapped = list(map_query('0', filtered))
    # unique = list(unique_query(mapped))
    # sort = sort_query(param='asc', data=unique)
    # limited = limit_query(param='1', data=sort)
    res = CMD_FUNC[cmd](param=value, data=prepared_data)
    return list(res)






