import json
from bs4 import BeautifulSoup

# Name of the XML file to parse — replace with your own XML if needed
xml_file = "Arsenal.xml"

# Read the XML content
with open(xml_file) as f:
    file = f.read()

# Parse the XML using BeautifulSoup
xml_parser = BeautifulSoup(file, "xml")

# Prepare the final JSON structure
parsed_data = {"methods": []}

# Find all method-like tags — adjust these if your XML uses different tag names
method_tags = xml_parser.find_all(["abstract_method", "method", "function"])

for method in method_tags:
    method_info = {}
    method_info["name"] = method.get("name", "unknown")

    # Extract access modifier if it exists
    access_tag = method.find("access")
    if access_tag:
        method_info["access"] = access_tag.text.strip()

    # Extract parameters if they exist
    params_tag = method.find("parameters")
    params_list = []
    if params_tag:
        for arg in params_tag.find_all("argument"):
            param_info = {
                "name": arg.text.strip(),
                "type": arg.get("type", "unknown")
            }
            params_list.append(param_info)
    method_info["parameters"] = params_list

    # Extract return type if it exists
    return_tag = method.find("return")
    if return_tag:
        method_info["return"] = return_tag.text.strip()

    # Extract exceptions (throws) if they exist
    throws_tag = method.find("throws")
    throws_list = []
    if throws_tag:
        for exc in throws_tag.find_all("exception"):
            throws_list.append(exc.text.strip())
    method_info["throws"] = throws_list

    # Add this method’s info to the final JSON
    parsed_data["methods"].append(method_info)

# Convert the data to JSON and print
json_output = json.dumps(parsed_data, indent=2)
print(json_output)