from typing import List

def sortScores(unsorted_scores: List[int], highest_possible: int) -> List[int]: 
    score_counts = [0] * (highest_possible+1)
    for score in unsorted_scores:
        score_counts[score] += 1

    sorted_scores = []
    for score_val in range(highest_possible,-1,-1):
        if score_counts[score_val] != 0:
            for _ in range(0, score_counts[score_val]):
                sorted_scores.append(score_val)
    return sorted_scores


unsorted = [37,89,41,65,91,53]
print(sortScores(unsorted, 100))
