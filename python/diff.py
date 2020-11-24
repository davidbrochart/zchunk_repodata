import json


with open('repodata/repodata.json') as f:
    repodata = json.load(f)

last_package = list(repodata['packages'].keys())[-1]
del repodata['packages'][last_package]

with open('download/repodata0.json', 'w') as f:
    json.dump(repodata, f, indent=2)
