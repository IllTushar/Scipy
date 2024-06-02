from scipy.cluster.vq import kmeans2
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    K = 3
    a = np.random.multivariate_normal([0, 6], [[2, 1], [1, 1.5]], size=200)
    b = np.random.multivariate_normal([2, 0], [[1, -1], [-1, 3]], size=200)
    c = np.random.multivariate_normal([6, 4], [[5, 0], [0, 1.2]], size=200)
    z = np.concatenate((a, b, c))

    centroids, labels = kmeans2(z, K, minit='points')
    Cluster_1 = z[labels == 0]
    Cluster_2 = z[labels == 1]
    Cluster_3 = z[labels == 2]
    plt.scatter(Cluster_1[:, 0], Cluster_1[:, 1], label='Cluster_1')
    plt.scatter(Cluster_2[:, 0], Cluster_2[:, 1],  label='Cluster_2')
    plt.scatter(Cluster_3[:, 0], Cluster_3[:, 1],  label='Cluster_3')
    plt.show()
