from app.db import database, models

stores = {store["id"]: store for store in sorted(database.generate_store_db(), key=lambda d: d["id"])}
products = database.generate_product_db()
inventory = database.generate_inventory_db()

# --------- Stores ---------
def all_stores():
    return list(stores.values())

def store_by_id(store_id: int):
    return stores.get(store_id, {})

def add_store(store: models.Store):
    if not stores:
        new_id = 1
    else:
        new_id = max(stores.keys()) + 1  # Encuentra el siguiente ID disponible
    
    new_store = {
        "id": new_id,
        "name": store.name,
        "address": store.address
    }
    stores[new_id] = new_store
    return new_store

def delete_store(store_id: int):
    if store_id in stores:
        del stores[store_id]
    else:
        raise ValueError("Store not found")

# --------- Products ---------
def all_products():
    return products