import pytest

from parser import parse_str_table


@pytest.fixture()
def tf():
    def table_builder(table):
        return parse_str_table(table)

    return table_builder
