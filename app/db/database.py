import json
import random
from pathlib import Path
from typing import List, Dict, Any

DATA_PATH = Path("data")

def load_json(file_name: str) -> List[Dict[str, Any]]:
    file_path = DATA_PATH / file_name
    if not file_path.exists():
        raise FileNotFoundError(f"File {file_name} not found in {DATA_PATH}")

    with file_path.open(encoding="utf-8") as stream:
        return json.load(stream)

def generate_store_db() -> List[Dict[str, Any]]:
    return load_json("stores.json")

def generate_product_db() -> List[Dict[str, Any]]:
    return load_json("products.json")

def generate_inventory_db() -> List[Dict[str, Any]]:
    stores = generate_store_db()
    products = generate_product_db()

    return [
        {
            "store_id": store["id"],
            "store_name": store["name"],
            "inventory": [
                {
                    "product_id": product["id"],
                    "product_name": product["name"],
                    "count": random.randint(1, 999)  # Ensures nonzero stock
                }
                for product in products
            ]
        }
        for store in stores
    ]