"""
sttable
~~~~~~~~~~~~~~~~~~

Parser of string representation tables, example:

    | header_1st_col   | header_2nd_col   |\n
    | row_1_of_1st_col | row_1_of_2nd_col |\n
    | row_2_of_1st_col | row_2_of_2nd_col |

Parsed information can be accessed by rows:

[{'header_1st_col': 'row_1_of_1st_col', 'header_2nd_col': 'row_1_of_2nd_col'},
{'header_1st_col': 'row_2_of_1st_col', 'header_2nd_col': 'row_2_of_2nd_col'}]

As well as by columns:

{'header_1st_col': ['row_1_of_1st_col', 'row_2_of_1st_col'],
header_2nd_col': ['row_1_of_2nd_col', 'row_2_of_2nd_col']}

Fields:

['header_1st_col', 'header_2nd_col', 'header_3rd_col']

"""

from .parser import (
    parse_str_table,
)
