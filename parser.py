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
    unformatted_header = _extract_table_header(unformatted_data)
    unformatted_body = _extract_table_body(unformatted_data)
    table_fields = _extract_values_from_row(unformatted_header)
    mapped_data = _map_all_values_to_fields(table_fields, unformatted_body)
    return mapped_data


def _map_all_values_to_fields(fields, table_body):
    container = {item: [] for item in fields}

    for line in table_body:
        line_values = _extract_values_from_row(line)

        for index in range(len(line_values)):
            container[fields[index]].append(line_values[index])
    return container


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

    def __init__(self, container):
        self._container = container
        self._table = None
        self._fields = None
        self._body = None

    @property
    def table(self):
        if self._table:
            return self._table
        else:
            raise ValueError('Table is empty.')

    @property
    def fields(self):
        if not self._fields:
            self._fields = list(self.container.keys())
        return self._fields

    @property
    def container(self):
        return self._container

    def column(self, index):
        fields_names = self.fields
        if index < 0 or index > (len(fields_names) - 1):
            raise ValueError(f'Column No.{index} does not exist. Last column is {len(fields_names) - 1}.')
        return self.container[fields_names[index]]

    @property
    def columns(self):
        aggregated_columns = []
        for index in range(len(self.fields)):
            aggregated_columns.append(self.container[self.fields[index]])
        return aggregated_columns

    def row(self, index):
        aggregated_row = []
        index_last_elem_of_first_field = len(self.container[self.fields[0]]) - 1
        if index < 0 or index > index_last_elem_of_first_field:
            raise ValueError(f'Row No.{index} does not exist. Last row is {index_last_elem_of_first_field}.')
        for value in self.container.values():
            aggregated_row.append(value[index])
        return aggregated_row

    @property
    def rows(self):
        aggregated_rows = []
        for index in range(len(self.fields) - 1):
            aggregated_rows.append(self.row(index))
        return aggregated_rows
