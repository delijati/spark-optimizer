import os

import requests
import collections

import ruamel.yaml

here = os.path.abspath(os.path.dirname(__file__))
FILE = os.path.join(here, "emr_instance.yaml")


def main():
    res = requests.get(
        "https://raw.githubusercontent.com/powdahound/ec2instances.info/master/www/instances.json" # noqa
    )

    emr = {}
    if os.path.exists(FILE):
        with open(FILE) as f:
            emr = ruamel.yaml.safe_load(f.read())

    inst = res.json()

    for i in inst:
        if i['emr']:
            x = i['instance_type']
            emr[x] = {}
            emr[x]["gpu"] = i["GPU"]
            emr[x]["cpu"] = i["vCPU"]
            emr[x]["memory"] = i["memory"]
            pricing = {}
            for k in i["pricing"]:
                pricing[k] = i["pricing"][k].get('emr')
            emr[x]["pricing"] = pricing

    with open(FILE, "w+") as f:
        ruamel.yaml.dump(collections.OrderedDict(sorted(emr.items())), f,
                         default_flow_style=False)


if __name__ == "__main__":
    main()
