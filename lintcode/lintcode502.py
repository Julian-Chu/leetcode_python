"""
Definition of Column:
class Column:
    def __init__(self, key, value):
        self.key = key
        self.value = value
"""


class MiniCassandra:

    def __init__(self):
        self.dict = {}

    """
    @param: row_key: a string
    @param: column_key: An integer
    @param: value: a string
    @return: nothing
    """

    def insert(self, row_key, column_key, value):
        if not self.dict.get(row_key, None):
            self.dict[row_key] = {}
        self.dict[row_key][column_key] = value

    """
    @param: row_key: a string
    @param: column_start: An integer
    @param: column_end: An integer
    @return: a list of Columns
    """

    def query(self, row_key, column_start, column_end):
        if not self.dict.get(row_key, None):
            return []
        keys = []
        for key in self.dict[row_key].keys():
            if column_start <= key <= column_end:
                keys.append(key)
        keys.sort()
        return ['(%s, \"%s\")' % (key, self.dict[row_key][key]) for key in keys]
