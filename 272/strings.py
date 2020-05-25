from typing import List, Set


def _extract_words(sentence: List[str]) -> Set[str]:
    return set(s.lower() for s in sentence)


def common_words(sentence1: List[str], sentence2: List[str]) -> List[str]:
    """
    Input:  Two sentences - each is a  list of words in case insensitive ways.
    Output: those common words appearing in both sentences. Capital and lowercase 
            words are treated as the same word. 

            If there are duplicate words in the results, just choose one word. 
            Returned words should be sorted by word's length.
    """
    return sorted(_extract_words(sentence1) & _extract_words(sentence2),
                  key=len)
