class GcContent:
    """
    Description:
        Computes the fraction of G and C bases in a DNA sequence.

    Input:
        seq (str): DNA sequence (resource name or raw string).

    Output:
        float: GC fraction between 0.0 and 1.0.

    Tests:
        - Case:
            Input: seq="ATGCATGC"
            Expected Output: 0.5
            Description: Balanced sequence, 50% GC.
        - Case:
            Input: seq="AAAA"
            Expected Output: 0.0
            Description: All A bases, 0% GC.
        - Case:
            Input: seq="GGGG"
            Expected Output: 1.0
            Description: All G bases, 100% GC.
        - Case:
            Input: seq=""
            Expected Output: 0.0
            Description: Edge case — empty sequence returns 0.
    """

    def initiate(self) -> None:
        pass

    def run(self, seq: str) -> float:
        """Return GC fraction between 0 and 1."""
        seq = seq.upper()
        if not seq:
            return 0.0
        gc = sum(1 for b in seq if b in "GC")
        return gc / len(seq)


_instance = GcContent()
_instance.initiate()
gc_content = _instance.run
