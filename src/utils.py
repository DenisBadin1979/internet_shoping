import json
import os


def jason_read(jon_path: str) -> dict:
    full_path = os.path.abspath(jon_path)
    with open(full_path, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data


if __name__ == "__main__":
    prod_data = jason_read("data/products.json")
    print(prod_data)
