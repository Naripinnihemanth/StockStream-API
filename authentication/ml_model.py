import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.neighbors import NearestNeighbors

from Products.models import *
from .models import historyModel


class RecommendationML:

    def __init__(self):
        self.encoder = OneHotEncoder(handle_unknown="ignore")
        self.model = NearestNeighbors(metric="euclidean")
        self.products = None
        self.X = None

    def train(self):
        products = ProductModel.objects.all()

        if not products.exists():
            return

        self.products = list(products)   # VERY IMPORTANT

        categories = [[p.category.id] for p in self.products]
        prices = [[float(p.price)] for p in self.products]

        cat_encoded = self.encoder.fit_transform(categories).toarray()
        price_array = np.array(prices)

        self.X = np.hstack([cat_encoded, price_array])

        self.model.fit(self.X)

    def recommend(self, user, k=15):

        if self.X is None or self.products is None:
            return ProductModel.objects.all().order_by("-id")[:k]

        history = (
            historyModel.objects
            .filter(auther=user)
            .order_by("-id")[:10]
        )

        if not history:
            return ProductModel.objects.all().order_by("-id")[:k]

        categories = [h.category for h in history if h.category]
        if not categories:
            return ProductModel.objects.all().order_by("-id")[:k]

        fav_category = max(set(categories), key=categories.count)

        avg_price = np.mean([float(h.price) for h in history])

        cat_encoded = self.encoder.transform([[fav_category]]).toarray()
        user_vector = np.hstack([cat_encoded, [[avg_price]]])

        # Increase search pool to ensure we still get k results
        search_k = min(len(self.products), k * 3)

        distances, indices = self.model.kneighbors(user_vector, n_neighbors=search_k)

        results = [self.products[i] for i in indices[0]]

        # DO NOT remove seen products
        # Just trim to k
        return results[:k]

