import requests as req
import jsonlines
import json
import time

if __name__ == "__main__":
    filename = "/summary-stats-items-2.jsonl"

    formats = ["nc", "gml", "gpx", "hdf", "hdf5", "shp", "geojson", "gdb"]

    res_list = []
    for format in formats:
        condition = True
        start = 0
        per_page = 1000

        while condition:
            query = f"https://dataverse.harvard.edu/api/search?q=(*.{format}%20AND%20isHarvested%3Afalse)&type=file"
            query = query + "&start=" + str(start)
            query = query + "&per_page=" + str(per_page)
            print(query)
            print("Looking at files from page " + str(start))
            res = req.get(query)

            res_dict = json.loads(res.text)
            total = res_dict["data"]["total_count"]
            writer = open(filename, "a")

            for item in res_dict["data"]["items"]:
                result = {}
                result["file_id"] = item["file_id"] if "file_id" in item else ""
                result["name"] = item["name"] if "name" in item else ""
                result["file_id"] = item["file_id"] if "file_id" in item else ""
                result["published_at"] = (
                    item["published_at"] if "published_at" in item else ""
                )
                result["size_in_bytes"] = (
                    item["size_in_bytes"] if "size_in_bytes" in item else ""
                )
                result["dataset_name"] = (
                    item["dataset_name"] if "dataset_name" in item else ""
                )
                result["dataset_id"] = (
                    item["dataset_id"] if "dataset_id" in item else ""
                )
                result["dataset_persistent_id"] = (
                    item["dataset_persistent_id"]
                    if "dataset_persistent_id" in item
                    else ""
                )
                result["description"] = (
                    item["description"] if "description" in item else ""
                )
                res_list.append(result)

            start = start + per_page

            condition = True if start < total else False
            time.sleep(0.5)

    with jsonlines.open(filename, "w") as writer:
        writer.write_all(res_list)
