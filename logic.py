import json
import streamlit as st
import os

floors = ["7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19"]
quantity = [0, 20, 40, 60, 80, 100]

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

def add_item(newItem, filename="stock.json"):
    with open(filename, "r+") as file:
        file_data = json.load(file)
        if not newItem.strip():
            st.error("Please input an item")           
        else:
            for i in file_data:
                file_data[i]["inventory"].update(
                    {f"{newItem}": {
                        "Update Time": "",
                        "Stock Level": ""
                        }
                    }
                )
            st.success(f"{newItem} was added sucessfully.")
            file.seek(0)
            file.truncate()
            json.dump(file_data, file, indent=4)
    
def remove_item(removeItem, filename="stock.json"):
    with open(filename, "r+") as file:
        file_data = json.load(file)
        if not removeItem.strip():
            st.error("Please input an item")  
        elif removeItem in file_data["7"]["inventory"]:
            for i in file_data:
                file_data[i]["inventory"].pop(removeItem, None)
            st.success(f"{removeItem} was deleted sucessfully.")
        else:
            st.error(f"There is no {removeItem}. ")
        file.seek(0)
        file.truncate()
        json.dump(file_data, file, indent=4 )

def update_stock(floor, item, stockLevel, time, filename="stock.json"):
    with open(filename, "r+") as file:
        file_data = json.load(file)
        file_data[floor]["inventory"].update(
            {f"{item}": {
                "Update Time": f"{time}",
                "Stock Level": f"{stockLevel}"
                }                 
            }
        )
        file.seek(0)
        file.truncate()
        json.dump(file_data, file, indent=4 )
        st.success(f"{stockLevel} of {item} on {floor}/F was updated on {time}")
