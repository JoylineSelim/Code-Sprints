
   from collections import Counter

def steadyGene(gene):
    n = len(gene)
    ideal = n // 4
    count = Counter(gene)

    # Letters that appear more than ideal count
    excess = {c: max(0, count[c] - ideal) for c in "ACGT"}

    # If already steady
    if all(v == 0 for v in excess.values()):
        return 0

    min_len = n
    left = 0
    window = Counter()

    for right in range(n):
        window[gene[right]] += 1

        # Shrink window until it no longer covers the excess
        while all(window[c] >= excess[c] for c in "ACGT"):
            min_len = min(min_len, right - left + 1)
            window[gene[left]] -= 1
            left += 1

    return min_len





#  Example usage
if __name__ == '__main__':
    gene = input("Enter the gene string: ").strip()
    print(steadyGene(gene))
