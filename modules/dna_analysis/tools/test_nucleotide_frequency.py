import pytest
from modules.dna_analysis.tools.nucleotide_frequency import NucleotideFrequency, nucleotide_frequency


class TestNucleotideFrequency:
    def setup_method(self):
        self.tool = NucleotideFrequency()
        self.tool.initiate()

    def test_one_of_each(self):
        assert self.tool.run("ATGC") == {"A": 1, "T": 1, "G": 1, "C": 1}

    def test_equal_counts(self):
        assert self.tool.run("AAATTTGGGCCC") == {"A": 3, "T": 3, "G": 3, "C": 3}

    def test_only_a(self):
        assert self.tool.run("AAAA") == {"A": 4, "T": 0, "G": 0, "C": 0}

    def test_only_gc(self):
        assert self.tool.run("GGCC") == {"A": 0, "T": 0, "G": 2, "C": 2}

    def test_lowercase_input(self):
        assert self.tool.run("atgc") == {"A": 1, "T": 1, "G": 1, "C": 1}

    def test_empty_sequence(self):
        assert self.tool.run("") == {"A": 0, "T": 0, "G": 0, "C": 0}

    def test_keys_present(self):
        result = self.tool.run("ATGC")
        assert set(result.keys()) == {"A", "T", "G", "C"}


class TestNucleotideFrequencyAlias:
    def test_alias_works(self):
        assert nucleotide_frequency("ATGC") == {"A": 1, "T": 1, "G": 1, "C": 1}

    def test_alias_empty(self):
        assert nucleotide_frequency("") == {"A": 0, "T": 0, "G": 0, "C": 0}
