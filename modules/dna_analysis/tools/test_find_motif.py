import pytest
from modules.dna_analysis.tools.find_motif import FindMotif, find_motif


class TestFindMotif:
    def setup_method(self):
        self.tool = FindMotif()
        self.tool.initiate()

    def test_motif_found_once(self):
        assert self.tool.run("ATGCATGC", "ATG") == [1, 5]

    def test_motif_found_twice(self):
        assert self.tool.run("AATGCAATG", "AATG") == [1, 6]

    def test_motif_not_found(self):
        assert self.tool.run("ATGCATGC", "TTT") == []

    def test_overlapping_matches(self):
        assert self.tool.run("AAAA", "AA") == [1, 2, 3]

    def test_motif_equals_seq(self):
        assert self.tool.run("ATGC", "ATGC") == [1]

    def test_motif_longer_than_seq(self):
        assert self.tool.run("AT", "ATGC") == []

    def test_lowercase_input(self):
        assert self.tool.run("atgcatgc", "atg") == [1, 5]

    def test_empty_motif(self):
        assert self.tool.run("ATGC", "") == []


class TestFindMotifAlias:
    def test_alias_works(self):
        assert find_motif("AATGCAATG", "AATG") == [1, 6]

    def test_alias_not_found(self):
        assert find_motif("ATGC", "TTT") == []
