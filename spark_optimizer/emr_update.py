import os

import requests

import ruamel.yaml

here = os.path.abspath(os.path.dirname(__file__))
FILE = os.path.join(here, "emr_instance.yaml")


def main():
    res = requests.get(
        "https://raw.githubusercontent.com/powdahound/ec2instances.info/master/www/instances.json" # noqa
    )

    with open(FILE) as f:
        emr = ruamel.yaml.round_trip_load(f.read())

    inst = res.json()

    for i in inst:
        if i['emr']:
            x = i['instance_type']
            emr[x] = {}
            emr[x]["gpu"] = i["GPU"]
            emr[x]["cpu"] = i["vCPU"]
            emr[x]["memory"] = i["memory"]

    with open(FILE, "r+") as f:
        ruamel.yaml.round_trip_dump(emr, f, default_flow_style=True)


if __name__ == "__main__":
    main()
