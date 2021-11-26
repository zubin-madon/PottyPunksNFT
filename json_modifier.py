import json

for i in range(10001):
"""This is for 10k json files. Replace 10001 with whatever number of jsons you have plus one. 
If your json files go from 1 to 10k (normally for ETH) instead of 0 to 10K (normally for solana), replace range(10001) with range(1,10001)"""

    a_file = open(f"PATH_FOLDER_NAME/{i}.json", "r")
    json_object = json.load(a_file)
    a_file.close()
    new_data = {"trait_type":"Number", "value":f"{i}"}
    json_object['attributes'].append(new_data)
    a_file = open(f"PATH_FOLDER_NAME/{i}.json", "w")
    json.dump(json_object, a_file)
    a_file.close()
