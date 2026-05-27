import json
import os

floors = ["7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19"]

quantity = ["Below 20%", "20%","40%","60%","80%","100%"]

def initialize_json():
    initial_data = {
        "7": {
            "inventory": {}
            },
        "8": {
            "inventory": {}
            },
        "9": {
            "inventory": {}
            },
        "10": {
            "inventory": {}
            },
        "11": {
            "inventory": {}
            },       
        "12": {
            "inventory": {}
            },
        "13": {
            "inventory": {}
            },
        "14": {
            "inventory": {}
            },
        "15": {
            "inventory": {}
            },
        "16": {
            "inventory": {}
            },
        "17": {
            "inventory": {}
            },
        "18": {
            "inventory": {}
            },
        "19": {
            "inventory": {}
            },                     
    }
    return initial_data



def add_item(newItem, items, filename="stock.json"):
    with open(filename, "r+") as file:
        file_data = json.load(file)
        for i in file_data:
            file_data[i]["inventory"].update(
                {f"{newItem}": {
                    "Update Time": "",
                    "Quantity": ""
                    }
                }
            )
        file.seek(0)
        file.truncate()
        json.dump(file_data, file, indent=4)


