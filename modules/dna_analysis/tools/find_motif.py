class FindMotif:
    """
    Description:
        Find all starting positions (1-based) of a motif in a DNA sequence.

    Input:
        seq (str): DNA sequence (resource name or raw string).
        motif (str): Short DNA pattern to search for.

    Output:
        list: List of 1-based integer positions where the motif starts.
              Returns an empty list if the motif is not found.

    Tests:
        - Case:
            Input: seq="AATGCAATG", motif="AATG"
            Expected Output: [1, 6]
            Description: Motif appears twice, overlapping search.
        - Case:
            Input: seq="ATGCATGC", motif="TTT"
            Expected Output: []
            Description: Motif not present, returns empty list.
        - Case:
            Input: seq="AAAA", motif="AA"
            Expected Output: [1, 2, 3]
            Description: Overlapping matches are all reported.
        - Case:
            Input: seq="ATGC", motif=""
            Expected Output: []
            Description: Edge case — empty motif returns empty list.
    """

    def initiate(self) -> None:
        pass

    def run(self, seq: str, motif: str) -> list:
        """Return all 1-based start positions of motif in seq."""
        if not motif:
            return []
        seq = seq.upper()
        motif = motif.upper()
        positions = []
        for i in range(len(seq) - len(motif) + 1):
            if seq[i:i + len(motif)] == motif:
                positions.append(i + 1)
        return positions


_instance = FindMotif()
_instance.initiate()
find_motif = _instance.run
