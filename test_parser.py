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

exp_col_1 = ['row_1_of_1st_col', 'row_2_of_1st_col']
exp_col_2 = ['row_1_of_2nd_col', 'row_2_of_2nd_col']
exp_col_3 = ['row_1_of_3rd_col', 'row_2_of_3rd_col']
exp_cols = [exp_col_1, exp_col_2, exp_col_3]
exp_get_col = [(1, exp_col_1), (2, exp_col_2), (3, exp_col_3)]
exp_col_negative_index = (-1, 0, 4)

exp_row_1 = ['row_1_of_1st_col', 'row_1_of_2nd_col', 'row_1_of_3rd_col']
exp_row_2 = ['row_2_of_1st_col', 'row_2_of_2nd_col', 'row_2_of_3rd_col']
exp_rows = [exp_row_1, exp_row_2]
exp_get_row = [(1, exp_row_1), (2, exp_row_2)]
exp_row_negative_index = (-1, 0, 3)


def test_fields_extracted(tf):
    tf.table = source_table
    header_fields = tf.fields
    assert header_fields == exp_parsed_header, \
        F'Not all fields match. Found {len(header_fields)} field(s) when expected {len(exp_parsed_header)}'


def test_body_extracted(tf):
    tf.table = source_table
    assert tf.body == exp_body, 'Body does not match'


def test_container_property(tf):
    tf.table = source_table
    assert tf.container == exp_parsed_obj, f'Objects do not match.'


@pytest.mark.parametrize('index, expected_column', exp_get_col)
def test_get_column(tf, index, expected_column):
    tf.table = source_table
    assert tf.column(index) == expected_column


@pytest.mark.parametrize('index', exp_col_negative_index)
def test_try_get_nonexistent_column(tf, index):
    tf.table = source_table
    with pytest.raises(ValueError):
        tf.column(index)


@pytest.mark.parametrize('index, expected_row', exp_get_row)
def test_get_row(tf, index, expected_row):
    tf.table = source_table
    assert tf.row(index) == expected_row


@pytest.mark.parametrize('index', exp_row_negative_index)
def test_get_nonexistent_row(tf, index):
    tf.table = source_table
    with pytest.raises(ValueError):
        tf.row(index)


def test_get_all_rows(tf):
    tf.table = source_table
    assert tf.rows == exp_rows, 'Rows do not match.'


def test_get_all_columns(tf):
    tf.table = source_table
    assert tf.columns == exp_cols, 'Columns do not match.'
