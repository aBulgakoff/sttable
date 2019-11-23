from typing import List, Tuple, Optional

from .table import Table


def parse_str_table(data: str, table_with_header: bool = True) -> Table:
    """
    Parser of string representation tables :returns: :py:class:`sttable.table.Table` instance
    Example of data variable:
    | header_1st_col   | header_2nd_col   |\n
    | row_1_of_1st_col | row_1_of_2nd_col |\n
    | row_2_of_1st_col | row_2_of_2nd_col |

    :param data: string representation table with header in a first line, columns divided by "|" and rows divided by EOL "\n"
    :param table_with_header: parameter which marks header/no header table

    :return :py:class:`sttable.table.Table` object

    >>> parse_str_table(f'| head |\\n| body_1 |\\n| body_2 |')
    [{'head': 'body_1'}, {'head': 'body_2'}]

    """

    table = Table()

    if table_with_header:
        unformatted_header, unformatted_body = split_str_table(data)
        table.fields = extract_values_from_row(unformatted_header)
    else:
        unformatted_body = split_str_table(data, header=False)[1]
    for line in unformatted_body:
        table.add_row(extract_values_from_row(line))
    return table


def split_str_table(data: str, header: bool = True) -> Tuple[Optional[str], List[str]]:
    """

    :param data: string representation table with rows divided by EOL "\n"
    :param header: parameter which marks header/no header table

    :return: tuple where 1st element is an optional Table Header's line and 2nd is an array with Table Body lines

    >>> split_str_table(f'| head |\\n| body_1 |\\n| body_2 |')
    ('| head |', ['| body_1 |', '| body_2 |'])

    >>> split_str_table(f'| body_1 |\\n| body_2 |', header=False)
    (None, ['| body_1 |', '| body_2 |'])

    """

    splitted_data = data.splitlines()
    return (splitted_data[0], splitted_data[1:]) if header else (None, splitted_data)


def extract_values_from_row(line: str) -> List[str]:
    """

    >>> extract_values_from_row('| head1 | head2 |')
    ['head1', 'head2']

    """

    return [value.strip() for value in line.split('|') if value]
