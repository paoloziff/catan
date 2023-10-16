from scipy.stats import chisquare


def expected_frequencies(n):
    probs = [1/36, 2/36, 3/36, 4/36, 5/36, 6/36, 5/36, 4/36, 3/36, 2/36, 1/36]
    return [p * n for p in probs]


def observed_frequencies(outcomes):
    freq = [0]*11
    for outcome in outcomes:
        if 2 <= outcome <= 12:
            freq[outcome - 2] += 1
    return freq


def get_p_value(outcomes):
    n = len(outcomes)
    observed = observed_frequencies(outcomes)
    expected = expected_frequencies(n)
    chi2, p = chisquare(observed, expected)
    return p
