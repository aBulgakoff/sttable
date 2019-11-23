import pytest

import sttable.parser


@pytest.fixture()
def tf():
    def table_builder(*args, **kwargs):
        return sttable.parser.parse_str_table(*args, **kwargs)

    return table_builder
