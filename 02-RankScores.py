# Problem 2 - Rank Scores ( https://leetcode.com/problems/rank-scores/ )
import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    # Rank scores by dense rank method in pandas
    scores['rank'] = scores['score'].rank(ascending = False, method = 'dense')
    # Sort the table by rank in ascending order
    return scores[['score', 'rank']].sort_values(by=['rank'])