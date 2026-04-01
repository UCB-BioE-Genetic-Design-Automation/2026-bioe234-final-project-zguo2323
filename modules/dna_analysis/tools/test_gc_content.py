import pytest
from modules.dna_analysis.tools.gc_content import GcContent, gc_content


class TestGcContent:
    def setup_method(self):
        self.tool = GcContent()
        self.tool.initiate()

    def test_balanced_sequence(self):
        assert self.tool.run("ATGCATGC") == 0.5

    def test_all_gc(self):
        assert self.tool.run("GGCC") == 1.0

    def test_no_gc(self):
        assert self.tool.run("AAAA") == 0.0

    def test_single_g(self):
        assert self.tool.run("G") == 1.0

    def test_single_a(self):
        assert self.tool.run("A") == 0.0

    def test_lowercase_input(self):
        assert self.tool.run("atgc") == 0.5

    def test_empty_sequence(self):
        assert self.tool.run("") == 0.0


class TestGcContentAlias:
    def test_alias_works(self):
        assert gc_content("ATGCATGC") == 0.5

    def test_alias_empty(self):
        assert gc_content("") == 0.0
