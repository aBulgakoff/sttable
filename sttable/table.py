from typing import cast, Iterable, List, Dict


class Table(object):

    def __init__(self):
        self._fields = None
        self._rows = []
        self._columns = {}

    def __str__(self) -> str:
        return str(self.rows)

    def __repr__(self) -> str:
        return self.__str__()

    @property
    def fields(self) -> List['str']:
        return list(self._fields.keys())

    @fields.setter
    def fields(self, fields: Iterable[str]):
        composed_fields = {}
        for key in fields:
            composed_fields[key] = ''  # prepare rows structure
            self._columns[key] = []  # prepare columns structure
        self._fields = composed_fields

    @property
    def columns(self) -> Dict[str, List[str]]:
        return self._columns.copy()

    @property
    def rows(self) -> List[Dict[str, str]]:
        return self._rows[:]

    def add_row(self, row: Iterable[str]) -> None:
        row = cast(List[str], row)  # cast on Type hint level
        # if table does not have a header make it using indexes of elements in row 0
        if not self._fields:
            self.fields = [str(value) for value in range(len(row))]

        field_values_row = self._fields.copy()
        index = 0
        for field in field_values_row.keys():
            try:
                row_value = row[index]
            except IndexError as e:
                raise IndexError(f'Element with index {index} does not exist in the row. '
                                 f'Amount of fields is {len(field_values_row.keys())} '
                                 f'when amount of elements in the row is {len(row)}.') from e
            field_values_row[field] = row_value  # compose rows
            self._columns[field].append(row_value)  # compose columns
            index += 1
        self._rows.append(field_values_row)

    def get_row(self, index: int) -> Dict[str, str]:
        try:
            return self._rows[index].copy()
        except IndexError as e:
            raise IndexError(f'Row with index {index} does not exist. Amount of rows is {len(self._rows)}.') from e

    def get_column(self, index: int) -> List[str]:
        try:
            key_by_index = self.fields[index]
        except IndexError as e:
            raise IndexError(
                f'Column with index {index} does not exist. Amount of columns is {len(self.fields)}.') from e
        return self._columns[key_by_index][:]
