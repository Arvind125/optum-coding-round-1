import json

deleteHighlightedKey = ["tp_status",
                        "abbr_def",
                        "dep_negation",
                        "family_negation",
                        "is_provider",
                        "negation",
                        "el_negation",
                        "exact_match",
                        "nc_scores",
                        "c_scores",
                        "context_negation",
                        "assertion",
                        "dxcat3",
                        "h_page",
                        "w_page"
                        ]


def lowercase_key(dict):

    d1 = {}
    for key in dict:
        d1[key.lower()] = dict[key]
    return d1


def replace_with_(dict):
    d1 = {}
    for key in dict:
        new_key = key.replace(" ", "_")
        d1[new_key] = dict[key]
    return d1


def removeMainKeys(dict):
    d1 = {}
    for key in dict:
        if key == "NLP_VERSION" or key == "NPI" or key == "hw_pages":
            pass
        else:
            d1[key] = dict[key]
    return d1


def removeNested(dict):
    d1 = {}
    k = "entities_with_highlights"

    for key in dict:
        if key != k:
            d1[key] = dict[key]
        else:
            nestedList = dict[k]
            valueList = []

            for nestedDict in nestedList:
                d2 = {}
                for nestedKey in nestedDict:
                    if nestedKey not in deleteHighlightedKey:
                        d2[nestedKey] = nestedDict[nestedKey]
                valueList.append(d2)

            d1[k] = valueList

    return d1


def cleanUp():
    jsonfile = open('data.json')

    jsonData = json.load(jsonfile)

    jsonData = removeMainKeys(jsonData)
    jsonData = lowercase_key(jsonData)
    jsonData = replace_with_(jsonData)
    jsonData = removeNested(jsonData)
    return jsonData


jsonData = cleanUp()
print(jsonData)

# write in output json file
with open("output.json", "w") as outfile:
    json.dump(jsonData, outfile)
