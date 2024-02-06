import requests as req
import json
import jsonlines
import pandas as pd

if __name__ == "__main__":
    with jsonlines.open("../data/summary-stats-items-2.jsonl") as reader:
        data = [obj for obj in reader]
    df = pd.DataFrame(data)
    datasets_dois = list(set(df.dataset_persistent_id.tolist()))

    for doi in datasets_dois:
        subject_list = []

        query = f'https://dataverse.harvard.edu/api/search?q="${doi}"&show_facets=true'
        res = req.get(query)
        res_dict = json.loads(res.text)

        try:
            subs = res_dict["data"]["facets"][0]["subject_ss"]["labels"]
            for s in subs:
                for key in s.keys():
                    subject_list.append(key)
        except KeyError:
            subs = "NA"

        with jsonlines.open("doi_field_map.jsonl", "a") as writer:
            writer.write({doi: subject_list})

    # frequency_dict = {}

    # for string in subject_list:
    #     if string in frequency_dict:
    #         frequency_dict[string] += 1
    #     else:
    #         frequency_dict[string] = 1

    # with open("dataverse_subject_frequency.json", "w") as file:
    #     # Use json.dump to write the dictionary to the file
    #     json.dump(frequency_dict, file)
