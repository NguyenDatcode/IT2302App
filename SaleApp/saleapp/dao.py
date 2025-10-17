import json

def load_categories():
    with open("data/category.json" , encoding="utf-8") as f:
        return json.load(f)

def load_product():
    with open("data/product.json", encoding="utf-8") as k:
        products =json.load(k)

        return products


if __name__=="__main__":
    print(load_product())