import numpy as np

scores = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9],
                   [10,11,12],
                   [13,14,15]])
score_mean = scores.mean(axis = 0)    # can ignore (axis = )
scores_centered = scores - score_mean
print(scores_centered)
print(scores_centered.mean(0))