def parse_str_table(unformatted_data):
    """
    Parser of string representation tables

    :param unformatted_data: string representation table
    with header in first line, columns divided by "|" and EOL "\n"

    Example of unformatted_data:
    | header_1st_col   | header_2nd_col   | header_3rd_col   |\n
    | row_1_of_1st_col | row_1_of_2nd_col | row_1_of_3rd_col |\n
    | row_2_of_1st_col | row_2_of_2nd_col | row_2_of_3rd_col |

    Example of basic usage:
    >>> parse_str_table(f'| head |\\n| body_1 |\\n| body_2 |')
    {'head': ['body_1', 'body_2']}

    """
    table = Table()
    unformatted_header = _extract_table_header(unformatted_data)
    unformatted_body = _extract_table_body(unformatted_data)
    table.fields = _extract_values_from_row(unformatted_header)

    [table.add_row(_extract_values_from_row(line)) for line in unformatted_body]
    return table


def _extract_values_from_row(line):
    """

    :param line:
    :return:

    >>> _extract_values_from_row('| head1 | head2 |')
    ['head1', 'head2']
    """
    return [value.strip() for value in line.split('|') if value.strip()]


def _extract_table_header(table):
    """
    >>> _extract_table_header(f'| head |\\n| body_1 |\\n| body_2 |')
    '| head |'
    """
    return table.split("\n")[0]


def _extract_table_body(table):
    """
    >>> _extract_table_body(f'| head |\\n| body_1 |\\n| body_2 |')
    ['| body_1 |', '| body_2 |']
    """
    return table.split("\n")[1:]


class Table(object):

    def __init__(self):
        self._fields = None
        self._columns = []
        self._rows = []

    @property
    def fields(self):
        return list(self._fields.keys())

    @fields.setter
    def fields(self, fields):
        self._fields = {key: '' for key in fields}

    @property
    def row(self):
        return self._rows.copy()

    @row.setter
    def row(self, row):
        self._rows.append(dict(zip(self._fields.copy(), row)))

    def add_row(self, row):
        self.row = row

    @property
    def rows(self):
        return self._rows.copy()

    @rows.setter
    def rows(self, rows):
        for row in rows:
            self.row = row
