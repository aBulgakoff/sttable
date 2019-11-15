class Table(object):

    def __init__(self):
        self._fields = None
        self._columns = []
        self._rows = []

    def __str__(self) -> str:
        return str(self.rows)

    def __repr__(self) -> str:
        return self.__str__()

    @property
    def fields(self):
        return list(self._fields.keys())

    @fields.setter
    def fields(self, fields):
        self._fields = {key: '' for key in fields}

    @property
    def row(self, index):
        return self._rows[:][index]

    @row.setter
    def row(self, row, index):
        self._rows[index] = row

    def add_row(self, row):
        self._rows.append(dict(zip(self._fields.copy(), row)))

    @property
    def rows(self):
        return self._rows[:]

    @rows.setter
    def rows(self, rows):
        for row in rows:
            self.add_row(row)


def parse_str_table(data: str) -> Table:
    """
    Parser of string representation tables

    :param data: string representation table
    with header in first line, columns divided by "|" and rows divided by EOL "\n"
    :return Table object

    Example of data variable:
    | header_1st_col   | header_2nd_col   | header_3rd_col   |\n
    | row_1_of_1st_col | row_1_of_2nd_col | row_1_of_3rd_col |\n
    | row_2_of_1st_col | row_2_of_2nd_col | row_2_of_3rd_col |

    Example of basic usage:
    >>> parse_str_table(f'| head |\\n| body_1 |\\n| body_2 |')
    [{'head': 'body_1'}, {'head': 'body_2'}]

    """
    table = Table()
    unformatted_header, unformatted_body = split_str_table(data)
    table.fields = extract_values_from_row(unformatted_header)
    for line in unformatted_body:
        table.add_row(extract_values_from_row(line))
    return table


def split_str_table(data: str) -> tuple:
    """
    :param data: string representation table with rows divided by EOL "\n"
    :return: tuple where 1st element is a Table Header's line and 2nd is an array with Table Body lines

    Example:
    >>> split_str_table(f'| head |\\n| body_1 |\\n| body_2 |')
    ('| head |', ['| body_1 |', '| body_2 |'])
    """
    splitted_data = data.split("\n")
    return splitted_data[0], splitted_data[1:]


def extract_values_from_row(line: str) -> list:
    """
    Example:
    >>> extract_values_from_row('| head1 | head2 |')
    ['head1', 'head2']
    """
    return [value.strip() for value in line.split('|') if value.strip()]
