from sklearn.metrics import pairwise_distances_argmin

def kmeans_Lloyd(X, n_clusters, rseed=2):
    # 1. Randomly choose clusters
    rng = np.random.RandomState(rseed)
    i = rng.permutation(X.shape[0])[:n_clusters]
    centers = X[i]
    
    while True:
        # 2a. Assign labels based on closest center
        labels = pairwise_distances_argmin(X, centers)
        
        # 2b. Find new centers from means of points
        new_centers = np.array([X[labels == i].mean(0)
                                for i in range(n_clusters)])
        
        # 2c. Check for convergence
        if np.all(centers == new_centers):
            break
        centers = new_centers
    
    return centers, labels


from sklearn.cluster import KMeans
def kmeans_plus(X,n_cluster):

    kmeans = KMeans(n_cluster)
    labels = kmeans.fit_predict(X)
    centers = kmeans.cluster_centers_
    return centers, labels


    
  
    
# 알고리즘이 정상적으로 작성되었다면 수정할 필요 없음
predict_centers_Lloyd, predict_labels_Lloyd = kmeans_Lloyd(X, 10)
predict_centers_Plus, predict_labels_Plus = kmeans_plus(X, 10)
