import json
import csv

# generate restaurant headers and rows 
def generate_restaurant_rows(restaurants):
    header = ["id", "name", "phone_number", "address", "type", "description", "logo_photos", "cuisines"]

    rows = [header]
    for restaurant in restaurants:
        row = [
            restaurant["_id"],
            restaurant["name"],
            restaurant["phone_number"],
            restaurant["address"],
            restaurant["type"],
            restaurant["description"],
            json.dumps(restaurant["logo_photos"]),
            json.dumps(restaurant["cuisines"])
        ]
        rows.append(row)

    return rows

# generate menu items headers and rows
def generate_menu_item_rows(restaurants):
    header = ["restaurant_id", "category_name", "product_id", "name", "price", "image"]

    rows = [header]

    for restaurant in restaurants:
        for category in restaurant["menu"]:
            for item in category["items"]:
                rows.append([
                    restaurant["_id"],
                    category["category_name"],
                    item["product_id"],
                    item["name"],
                    item["price"],
                    item["image"]
                ])

    return rows

def write_csv(filename, rows):
    with open(filename, mode="w") as csv_file:
        csv_writer = csv.writer(csv_file)

        # Write the header row using the first row of the rows list
        if rows:
            header = rows[0]
            csv_writer.writerow(header)

        # Write data rows
        for row in rows[1:]:
            csv_writer.writerow(row)

def main():
    # Load JSON data from the file
    with open("data.json", "r") as json_file:
        data = json.load(json_file)

    # Generate rows for restaurants csv and write the file
    restaurant_rows = generate_restaurant_rows(data["restaurants"])
    write_csv("restaurants.csv", restaurant_rows)

    # Generate rows for menu items csv and write the file
    menu_item_rows = generate_menu_item_rows(data["restaurants"])
    write_csv("menu_items.csv", menu_item_rows)

if __name__ == "__main__":
    main()