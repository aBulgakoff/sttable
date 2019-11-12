import pytest

from parser import StrTableParser


@pytest.fixture()
def tf():
    def init_parser(table):
        return StrTableParser(table)

    return init_parser
