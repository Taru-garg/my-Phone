import requests
import json
import os


image_path = "/home/vip/Pictures/dog.jpg"
c_time = str(os.path.getctime(image_path))


def findtag(image_path, c_time):
    with open("t.json", "r") as read_file:
        developer = json.load(read_file)
        key = developer["image_tags"]
        for t in key:
            for x, y in t.items():
                if x == c_time and image_path == y[0]:
                    return y[1]
    return None


def api(image_path):
    api_key = "acc_4789f20196cd49d"
    api_secret = "8a15436aeb272e9e498d68db95af7fd9"
    response = requests.post(
        "https://api.imagga.com/v2/tags?limit=3",
        auth=(api_key, api_secret),
        files={"image": open(image_path, "rb")},
    )
    return response.json()


def write(jsonresponse):
    def write_json(data, filename="t.json"):
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    with open("t.json") as read_file:
        data = json.load(read_file)
        y = {
            c_time: [
                image_path,
                jsonresponse["result"]["tags"][0]["tag"]["en"]
                + " "
                + jsonresponse["result"]["tags"][1]["tag"]["en"],
            ]
        }
        data["image_tags"].append(y)
    write_json(data)


if findtag(image_path, c_time) != None:
    print(findtag(image_path, c_time))
else:
    jsonresponse = api(image_path)
    print(
        jsonresponse["result"]["tags"][0]["tag"]["en"]
        + " "
        + jsonresponse["result"]["tags"][1]["tag"]["en"]
    )
    write(jsonresponse)
