import pytest

from sttable.parser import parse_str_table


@pytest.fixture()
def tf():
    def table_builder(*args, **kwargs):
        return parse_str_table(*args, **kwargs)

    return table_builder
