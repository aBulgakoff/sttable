class StrTableParser(object):
    """
    Parser of string representation tables

    Example of basic usage:
    >>> StrTableParser(table=f'| head |\\n| body_1 |\\n| body_2 |').container
    {'head': ['body_1', 'body_2']}
    """

    def __init__(self, table=None):
        self._container = {}
        self._table = None
        self._fields = None
        self._body = None

        if table:
            self.table = table

    @property
    def table(self):
        if self._table:
            return self._table
        else:
            raise ValueError('Table is empty.')

    @table.setter
    def table(self, table_in_str):
        """
        :param table_in_str: string representation table
        with header in first line, columns divided by "|" and EOL "\n"

        Example:
        | header_1st_col   | header_2nd_col   | header_3rd_col   |\n
        | row_1_of_1st_col | row_1_of_2nd_col | row_1_of_3rd_col |\n
        | row_2_of_1st_col | row_2_of_2nd_col | row_2_of_3rd_col |

        """
        self._table = table_in_str

    @staticmethod
    def _get_values_from_str(line):
        return [value.strip() for value in line.split('|') if value.strip()]

    @staticmethod
    def _extract_header_of_table(table):
        """
        >>> StrTableParser._extract_header_of_table(f'| head |\\n| body_1 |\\n| body_2 |')
        '| head |'
        """

        return table.split("\n")[0]

    @staticmethod
    def _extract_body_of_table(table):
        """
        >>> StrTableParser._extract_body_of_table(f'| head |\\n| body_1 |\\n| body_2 |')
        ['| body_1 |', '| body_2 |']
        """
        return table.split("\n")[1:]

    def _extract_fields(self):
        return self._get_values_from_str(self._extract_header_of_table(self.table))

    @property
    def fields(self):
        if not self._fields:
            self._fields = self._extract_fields()
        return self._fields

    def _map_all_values_to_fields(self):
        container = {item: [] for item in self.fields}

        for line in self.body:
            line_values = self._get_values_from_str(line)

            for index in range(len(line_values)):
                container[self.fields[index]].append(line_values[index])
        return container

    @property
    def body(self):
        if not self._body:
            self._body = self._extract_body_of_table(self.table)
        return self._body

    @property
    def container(self):
        if not self._container:
            self._container.update(self._map_all_values_to_fields())
        return self._container

    def column(self, index):
        fields_names = self.fields
        if (index - 1) < 0 or (index - 1) > (len(fields_names) - 1):
            raise ValueError(f'Column No.{index} does not exist. Amount of columns is {len(fields_names)}.')
        return self.container[fields_names[index - 1]]

    @property
    def columns(self):
        aggregated_columns = []
        for index in range(len(self.fields)):
            aggregated_columns.append(self.container[self.fields[index]])
        return aggregated_columns

    def row(self, index):
        aggregated_row = []
        if (index - 1) < 0 or (index - 1) > (len(self.body) - 1):
            raise ValueError(f'Row No.{index} does not exist. Amount of rows is {len(self.fields)}.')
        for value in self.container.values():
            aggregated_row.append(value[index - 1])
        return aggregated_row

    @property
    def rows(self):
        aggregated_rows = []
        for index in range(len(self.fields) - 1):
            aggregated_rows.append(self.row(index + 1))
        return aggregated_rows
