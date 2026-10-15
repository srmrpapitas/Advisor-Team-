# Site generator

Run from the repo root:

    python3 tools/pages.py      # English pages in public/
    python3 tools/build_nl.py   # Dutch pages in public/nl/ (from nl_list.py)

After changing English text, run `python3 tools/extract.py`: it lists strings with no Dutch yet. Add each one to `tools/nl.json`, then run both scripts again.
