import numpy as np
from numpy.linalg import svd

ratings = np.array([
    [5,3,0,1],
    [4,0,0,1],
    [1,1,0,5],
    [0,0,5,4],
    [0,2,4,0]
])
# Perform Singular Value Decomposition
U, sigma, Vt = svd(ratings, full_matrices=False)

# Reconstruct the matrix
sigma = np.diag(sigma)
reconstructed_ratings = np.dot(np.dot(U, sigma), Vt)

# Replace the original zeros with the predicted ratings
predicted_ratings = np.where(ratings == 0, reconstructed_ratings, ratings)

print("Original Ratings Matrix:")
print(ratings)
print("\nPredicted Ratings Matrix:")
print(predicted_ratings)