class SequenceLength:
    """
    Description:
        Returns the number of bases in a DNA sequence.

    Input:
        seq (str): DNA sequence (resource name or raw string).

    Output:
        int: Length of the sequence in base pairs.

    Tests:
        - Case:
            Input: seq="ATGC"
            Expected Output: 4
            Description: Simple 4-base sequence.
        - Case:
            Input: seq="ATGCATGCATGC"
            Expected Output: 12
            Description: Longer sequence.
        - Case:
            Input: seq=""
            Expected Output: 0
            Description: Edge case — empty sequence returns 0.
    """

    def initiate(self) -> None:
        pass

    def run(self, seq: str) -> int:
        """Return the number of bases in the sequence."""
        return len(seq)


_instance = SequenceLength()
_instance.initiate()
sequence_length = _instance.run
