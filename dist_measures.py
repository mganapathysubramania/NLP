"""Calculate information-theoretic measures of distributional
similarity based on word frequencies in two texts
"""

import collections
import math


def read_words(infile):
    with open(infile) as input_text:
        return [x.strip() for x in input_text.read().split()]


def get_counts(word_list):
    return collections.Counter(word_list)


def create_prob_dist(count_dict):
    total_ct = sum(count_dict.values())
    p = {x: ct / total_ct for x, ct in count_dict.items()}
    return p


def count_smoothing(freq_dist, vocabulary, alpha=1):
    """Implement simple count-based probability smoothing.
    Given a target vocabulary and a set of observed count frequencies,
    calculate a new set of counts so that Count(x) > 0 for all words
    in the target vocabulary.  This is achieved by adding `alpha`
    to each observed count
    """
    return {w: freq_dist.get(w, 0) + alpha for w in vocabulary}


def entropy(p):
    """Calculate entropy H(p) for a probability distribution represented
    as a mapping (dictionary) from word tokens to probabilities
    """
    h = 0

    for prob in p:
        h=(h+(p[prob]*(math.log(p[prob],2)))) #calculating entropy for probability destribution p in bits
    #converting bit to nats
    h=-(h/(math.log(2.71828,2))) #value of e=2.71828
    return h


def cross_entropy(p1, p2):
    """Calculate cross-entropy H(p1, p2) for two probability distributions
    represented as a mapping (dictionary) from word tokens to
    probabilities
    """
    xh = 0

    for prob in p1:
        xh=(xh+(p1[prob]*(math.log(p2[prob],2)))) #cross entropy of two probability distributions p1 and p2 in bits
        
    #converting bit to nats
    xh=-(xh/(math.log(2.71828,2))) #value of e=2.71828 
    return xh


def kl_divergence(p1, p2):
    """Calculate Kullback-Leibler divergence D_{KL}(p1||p2) for two
    probability distributions represented as a mapping (dictionary)
    from word tokens to probabilities
    """
    kl = 0

    for prob in p1:
        kl=(kl+(p1[prob]*(math.log((p2[prob]/p1[prob]),2)))) #calculating KL divergence for 2 probabilities

    kl=-(kl/(math.log(2.71828,2)))#converting bits to nats #value of e=2.71828 

    return kl


def js_divergence(p1, p2):
    """Calculate Jensen-Shannon divergence D_{JS}(p1||p2) for two
    probability distributions represented as a mapping (dictionary)
    from word tokens to probabilities
    """
    js = 0
    pmx={}


    for prob in p1:            
        mx=(p1[prob]+p2[prob])/2
        pmx[prob]=mx
        
    klp1m=kl_divergence(p1, pmx)
    klp2m=kl_divergence(p2, pmx)
    js=(klp1m+klp2m)/2  #calculating JS divergence for 2 probabilities from DKL(p1,mx) and DKL(p2,mx)

    #js=(js/(math.log(2.71828,2))) 


    return js


if __name__ == "__main__":
    """Do not edit this code
    """
    words_a = read_words("test_a.txt")
    words_b = read_words("test_b.txt")

    ct_a = get_counts(words_a)
    ct_b = get_counts(words_b)

    vocab = set(ct_a.keys()) | set(ct_b.keys())
    ct_a = count_smoothing(ct_a, vocab)
    ct_b = count_smoothing(ct_b, vocab)

    p_a = create_prob_dist(ct_a)
    p_b = create_prob_dist(ct_b)

    h_a = entropy(p_a)
    h_b = entropy(p_b)
    xh_ab = cross_entropy(p_a, p_b)
    xh_ba = cross_entropy(p_b, p_a)
    kl_ab = kl_divergence(p_a, p_b)
    kl_ba = kl_divergence(p_b, p_a)
    js_ab = js_divergence(p_a, p_b)
    js_ba = js_divergence(p_b, p_a)

    for metric in [h_a, h_b, xh_ab, xh_ba,
                   kl_ab, kl_ba, js_ab, js_ba]:
        print("{:.3f}".format(metric))



