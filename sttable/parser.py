from typing import List, Tuple

from .table import Table


def parse_str_table(data: str) -> Table:
    """
    Parser of string representation tables

    :param data: string representation table
    with header in a first line, columns divided by "|" and rows divided by EOL "\n"
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


def split_str_table(data: str) -> Tuple[str, List[str]]:
    """
    :param data: string representation table with rows divided by EOL "\n"
    :return: tuple where 1st element is a Table Header's line and 2nd is an array with Table Body lines

    Example:
    >>> split_str_table(f'| head |\\n| body_1 |\\n| body_2 |')
    ('| head |', ['| body_1 |', '| body_2 |'])
    """
    splitted_data = data.splitlines()
    return splitted_data[0], splitted_data[1:]


def extract_values_from_row(line: str) -> List[str]:
    """
    Example:
    >>> extract_values_from_row('| head1 | head2 |')
    ['head1', 'head2']
    """
    return [value.strip() for value in line.split('|') if value]
