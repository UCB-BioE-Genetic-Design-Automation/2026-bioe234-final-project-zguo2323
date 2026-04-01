class NucleotideFrequency:
    """
    Description:
        Counts the occurrences of each nucleotide (A, T, G, C) in a DNA sequence.

    Input:
        seq (str): DNA sequence (resource name or raw string).

    Output:
        dict: Dictionary with keys 'A', 'T', 'G', 'C' and their counts as values.

    Tests:
        - Case:
            Input: seq="ATGC"
            Expected Output: {"A": 1, "T": 1, "G": 1, "C": 1}
            Description: One of each nucleotide.
        - Case:
            Input: seq="AAATTTGGGCCC"
            Expected Output: {"A": 3, "T": 3, "G": 3, "C": 3}
            Description: Equal counts of all nucleotides.
        - Case:
            Input: seq="AAAA"
            Expected Output: {"A": 4, "T": 0, "G": 0, "C": 0}
            Description: Only A bases present.
        - Case:
            Input: seq=""
            Expected Output: {"A": 0, "T": 0, "G": 0, "C": 0}
            Description: Edge case — empty sequence returns all zeros.
    """

    def initiate(self) -> None:
        pass

    def run(self, seq: str) -> dict:
        """Return counts of A, T, G, C in the sequence."""
        seq = seq.upper()
        return {
            "A": seq.count("A"),
            "T": seq.count("T"),
            "G": seq.count("G"),
            "C": seq.count("C"),
        }


_instance = NucleotideFrequency()
_instance.initiate()
nucleotide_frequency = _instance.run
