import pytest

"""
Input:
| header_1st_col   | header_2nd_col   | header_3rd_col   |
| row_1_of_1st_col | row_1_of_2nd_col | row_1_of_3rd_col |
| row_2_of_1st_col | row_2_of_2nd_col | row_2_of_3rd_col |
"""

header = '| header_1st_col | header_2nd_col | header_3rd_col |'
body_row1 = '| row_1_of_1st_col | row_1_of_2nd_col | row_1_of_3rd_col |'
body_row2 = '| row_2_of_1st_col | row_2_of_2nd_col | row_2_of_3rd_col |'

source_table = f'{header}\n{body_row1}\n{body_row2}'

exp_parsed_header = ['header_1st_col', 'header_2nd_col', 'header_3rd_col']
exp_body = [body_row1, body_row2]
exp_parsed_obj = {'header_1st_col': ['row_1_of_1st_col', 'row_2_of_1st_col'],
                  'header_2nd_col': ['row_1_of_2nd_col', 'row_2_of_2nd_col'],
                  'header_3rd_col': ['row_1_of_3rd_col', 'row_2_of_3rd_col']}

exp_col_0 = ['row_1_of_1st_col', 'row_2_of_1st_col']
exp_col_1 = ['row_1_of_2nd_col', 'row_2_of_2nd_col']
exp_col_2 = ['row_1_of_3rd_col', 'row_2_of_3rd_col']
exp_cols = [exp_col_0, exp_col_1, exp_col_2]
exp_get_col = [(0, exp_col_0), (1, exp_col_1), (2, exp_col_2)]
exp_col_negative_index = (-1, 3, 4)

exp_row_0 = ['row_1_of_1st_col', 'row_1_of_2nd_col', 'row_1_of_3rd_col']
exp_row_1 = ['row_2_of_1st_col', 'row_2_of_2nd_col', 'row_2_of_3rd_col']
exp_rows = [exp_row_0, exp_row_1]
exp_get_row = [(0, exp_row_0), (1, exp_row_1)]
exp_row_negative_index = (-1, 2, 3)


def test_fields_extracted(tf):
    header_fields = tf(source_table).fields
    assert header_fields == exp_parsed_header, \
        F'Not all fields match. Found {len(header_fields)} field(s) when expected {len(exp_parsed_header)}'


def test_container_property(tf):
    assert tf(source_table).container == exp_parsed_obj, f'Objects do not match.'


@pytest.mark.parametrize('index, expected_column', exp_get_col)
def test_get_column(tf, index, expected_column):
    assert tf(source_table).column(index) == expected_column


@pytest.mark.parametrize('index', exp_col_negative_index)
def test_try_get_nonexistent_column(tf, index):
    with pytest.raises(ValueError):
        tf(source_table).column(index)


@pytest.mark.parametrize('index, expected_row', exp_get_row)
def test_get_row(tf, index, expected_row):
    assert tf(source_table).row(index) == expected_row


@pytest.mark.parametrize('index', exp_row_negative_index)
def test_get_nonexistent_row(tf, index):
    with pytest.raises(ValueError):
        tf(source_table).row(index)


def test_get_all_rows(tf):
    assert tf(source_table).rows == exp_rows, 'Rows do not match.'


def test_get_all_columns(tf):
    assert tf(source_table).columns == exp_cols, 'Columns do not match.'
