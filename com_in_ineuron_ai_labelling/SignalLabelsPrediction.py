from spectralcluster import SpectralClusterer
from kneed import KneeLocator
from sklearn.cluster import KMeans

def signalLabelPrediction(cont_embeds):
    # Finding optimum clusters c
    wcss = []
    r = range(1, 15)
    for k in r:
        km = KMeans(n_clusters=k)
        km = km.fit(cont_embeds)
        wcss.append(km.inertia_)
    kn = KneeLocator(list(r), wcss, S=1.0, curve='convex', direction='decreasing')
    c=kn.knee

    # Passing the clusters to get the labels
    clusterer = SpectralClusterer(
        min_clusters=c,
        max_clusters=100,
        p_percentile=0.90,
        gaussian_blur_sigma=1)

    labels = clusterer.predict(cont_embeds)
    return(labels)