Installation:

```bash
mamba install zchunk pip
pip install rangehttpserver
```

Prepare data on the server side (get current repodata):

```bash
mkdir repodata
cd repodata
wget https://conda.anaconda.org/conda-forge/linux-64/repodata.json
zck repodata.json
```

Prepare data on the client side (create an older repodata with less packages):
```bash
python python/diff.py
mkdir download
cd download
zck repodata0.json
```

Serve the chunked (current) repodata:
```bash
cd repodata
python -m RangeHTTPServer
```

Update the old repodata:
```bash
cd download
zckdl -s repodata0.json.zck  http://127.0.0.1:8000/repodata.json.zck
```
