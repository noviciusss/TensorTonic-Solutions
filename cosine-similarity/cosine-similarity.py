import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    doti = np.dot(a,b)
    a1 = np.linalg.norm(a)
    b1 = np.linalg.norm(b)
    if a1 ==0 or b1==0:
        return 0.0
    ans = doti / (a1*b1)
    return float(ans)