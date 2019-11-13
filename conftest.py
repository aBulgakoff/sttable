import pytest

from parser import Table, parse_str_table


@pytest.fixture()
def tf():
    def table_builder(table):
        return Table(parse_str_table(table))

    return table_builder
