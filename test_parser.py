import pytest

"""
Example of Input:
| header_1st_col   | header_2nd_col   | header_3rd_col   |
| row_1_of_1st_col | row_1_of_2nd_col | row_1_of_3rd_col |
| row_2_of_1st_col | row_2_of_2nd_col | row_2_of_3rd_col |
"""

HEADER = '| header_1st_col | header_2nd_col | header_3rd_col |'
BODY_ROW1 = '| row_1_of_1st_col | row_1_of_2nd_col | row_1_of_3rd_col |'
BODY_ROW2 = '| row_2_of_1st_col | row_2_of_2nd_col | row_2_of_3rd_col |'
BODY_ROW2_MISSING_MID = '| row_2_of_1st_col |   | row_2_of_3rd_col |'
BODY_ROW2_WRONG_SIZE = '| row_2_of_1st_col | row_2_of_2nd_col |'

SOURCE_TABLE = f'{HEADER}\n{BODY_ROW1}\n{BODY_ROW2}'
SOURCE_TABLE_MISSING_REC = f'{HEADER}\n{BODY_ROW1}\n{BODY_ROW2_MISSING_MID}'
SOURCE_TABLE_WRONG_REC = f'{HEADER}\n{BODY_ROW1}\n{BODY_ROW2_WRONG_SIZE}'
SOURCE_TABLE_NO_HEADER = f'{BODY_ROW1}\n{BODY_ROW2}'

EXP_FIELDS = ['header_1st_col', 'header_2nd_col', 'header_3rd_col']
EXP_BODY = [BODY_ROW1, BODY_ROW2]

EXP_COL0 = ['row_1_of_1st_col', 'row_2_of_1st_col']
EXP_COL1 = ['row_1_of_2nd_col', 'row_2_of_2nd_col']
EXP_COL2 = ['row_1_of_3rd_col', 'row_2_of_3rd_col']

EXP_COLS = {EXP_FIELDS[0]: EXP_COL0, EXP_FIELDS[1]: EXP_COL1, EXP_FIELDS[2]: EXP_COL2}

EXP_GET_COL = [(0, EXP_COL0), (1, EXP_COL1), (2, EXP_COL2)]
EXP_NONEXISTENT_COL_INDEX = (-4, 3, 4)

EXP_ROW0 = {'header_1st_col': 'row_1_of_1st_col',
            'header_2nd_col': 'row_1_of_2nd_col',
            'header_3rd_col': 'row_1_of_3rd_col'}
EXP_ROW1 = {'header_1st_col': 'row_2_of_1st_col',
            'header_2nd_col': 'row_2_of_2nd_col',
            'header_3rd_col': 'row_2_of_3rd_col'}
EXP_ROW1_MISSING_REC = {'header_1st_col': 'row_2_of_1st_col',
                        'header_2nd_col': '',
                        'header_3rd_col': 'row_2_of_3rd_col'}
EXP_ROWS = [EXP_ROW0, EXP_ROW1]
EXP_GET_ROW = [(0, EXP_ROW0), (1, EXP_ROW1), (-1, EXP_ROW1), (-2, EXP_ROW0)]
EXP_NONEXISTENT_ROW_INDEX = (2, 3, -3)

EXP_ROW_NO_HEADER0 = {'0': 'row_1_of_1st_col',
                      '1': 'row_1_of_2nd_col',
                      '2': 'row_1_of_3rd_col'}
EXP_ROW_NO_HEADER1 = {'0': 'row_2_of_1st_col',
                      '1': 'row_2_of_2nd_col',
                      '2': 'row_2_of_3rd_col'}
EXP_ROW_NO_HEADER = [(0, EXP_ROW_NO_HEADER0), (1, EXP_ROW_NO_HEADER1),
                     (-1, EXP_ROW_NO_HEADER1), (-2, EXP_ROW_NO_HEADER0)]


def test_fields_extracted(tf):
    header_fields = tf(SOURCE_TABLE).fields
    assert header_fields == EXP_FIELDS, \
        F'Not all fields match. Found {len(header_fields)} field(s) when expected {len(EXP_FIELDS)}'


@pytest.mark.parametrize('index, expected_column', EXP_GET_COL)
def test_get_column(tf, index, expected_column):
    assert tf(SOURCE_TABLE).get_column(index) == expected_column


@pytest.mark.parametrize('index', EXP_NONEXISTENT_COL_INDEX)
def test_try_get_nonexistent_column(tf, index):
    with pytest.raises(IndexError):
        tf(SOURCE_TABLE).get_column(index)


def test_get_all_columns(tf):
    assert tf(SOURCE_TABLE).columns == EXP_COLS, 'Columns do not match.'


@pytest.mark.parametrize('index, expected_row', EXP_GET_ROW)
def test_get_row(tf, index, expected_row):
    assert tf(SOURCE_TABLE).get_row(index) == expected_row


def test_get_row_missing_rec(tf):
    assert tf(SOURCE_TABLE_MISSING_REC).get_row(1) == EXP_ROW1_MISSING_REC


def test_get_row_wrong_rec(tf):
    with pytest.raises(IndexError):
        tf(SOURCE_TABLE_WRONG_REC).get_row(1)


@pytest.mark.parametrize('index', EXP_NONEXISTENT_ROW_INDEX)
def test_get_nonexistent_row(tf, index):
    with pytest.raises(IndexError):
        tf(SOURCE_TABLE).get_row(index)


def test_get_all_rows(tf):
    assert tf(SOURCE_TABLE).rows == EXP_ROWS, 'Rows do not match.'


@pytest.mark.parametrize('index, expected_row', EXP_ROW_NO_HEADER)
def test_get_row_no_header(tf, index, expected_row):
    assert tf(SOURCE_TABLE_NO_HEADER, table_with_header=False).get_row(index) == expected_row
