import pandas as pd
import numpy as np

scores = pd.read_csv('../data/the-nature-conservancy-fisheries-monitoring_public_leaderboard.csv')

sorted = scores.groupby('TeamName')['Score'].min().sort_values()

for percentile in np.arange(101)/100.:
    print percentile, sorted.quantile(percentile)