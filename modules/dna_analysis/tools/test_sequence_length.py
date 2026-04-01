import pytest
from modules.dna_analysis.tools.sequence_length import SequenceLength, sequence_length


class TestSequenceLength:
    def setup_method(self):
        self.tool = SequenceLength()
        self.tool.initiate()

    def test_short_sequence(self):
        assert self.tool.run("ATGC") == 4

    def test_longer_sequence(self):
        assert self.tool.run("ATGCATGCATGC") == 12

    def test_single_base(self):
        assert self.tool.run("A") == 1

    def test_empty_sequence(self):
        assert self.tool.run("") == 0

    def test_all_same_base(self):
        assert self.tool.run("GGGGG") == 5


class TestSequenceLengthAlias:
    def test_alias_works(self):
        assert sequence_length("ATGC") == 4

    def test_alias_empty(self):
        assert sequence_length("") == 0
