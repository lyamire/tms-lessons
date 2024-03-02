import json

from pydantic import BaseModel
from typing import List

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    category_id: int

class Category(BaseModel):
    id: int
    name: str
    products: List[Product]

class BasePagination(BaseModel):
    count: int
    next: str | None = None
    previous: str | None = None

class PaginatedProducts(BasePagination):
    category_id: int
    results: list[Product]

class PaginatedCategories(BasePagination):
    results: list[Category]

class Database:
    _categories: List[Category] = []
    _products: List[Product] = []

    def __init__(self):
        self._load_data()

    def _load_data(self):
        with open('data_shop.json') as data_file:
            data = json.load(data_file)

            for category in data['categories']:
                new_category = Category(id=category['id'], name=category['name'], products=[])
                self._categories.append(new_category)

            for product in data['products']:
                category = next(x for x in self._categories if x.id == product['category_id'])
                new_product = Product(id=product['id'], name=product['name'], description=product['description'],
                                      price=product['price'], category_id=category.id)
                category.products.append(new_product)
                self._products.append(new_product)

    def get_categories(self):
        return self._categories

    def get_category(self, category_id: int) -> Category | None:
        for q in self._categories:
            if q.id == category_id:
                return q
        return None

    def get_products(self):
        return self._products

    def get_product(self, product_id: int) -> Product | None:
        for q in self._products:
            if q.id == product_id:
                return q
        return None

    def get_category_products(self, category_id):
        return [x for x in self._products if x.category_id == category_id]


if __name__ == "__main__":
    db = Database()
    for question in db._categories:
        print(question.dict())