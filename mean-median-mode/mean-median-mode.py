from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    mean = float(sum(x)/len(x))
    x.sort()
    if len(x)%2!=0:
        median = float(x[len(x)//2])
    
    else:
        x1 = x[len(x)//2]
        x2 = x[(len(x)//2)-1]
        median = float((x1+x2)/2)
    counts = Counter(x)
    max_count = max(counts.values())
    modes = [k for k, v in counts.items() if v == max_count]
    if len(modes) == 1:
        mode = float(modes[0])
    else:
        mode = float(min(modes)) 
    return {
        "mean": mean,
        "median": median,
        "mode": mode
    }
    