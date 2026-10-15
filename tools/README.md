# Site generator

Run from the repo root:

    python3 tools/pages.py      # English pages in public/
    python3 tools/build_lang.py # Dutch and Spanish pages in public/nl/ and public/es/

After changing English text, run `python3 tools/extract.py`: it lists strings with no Dutch or Spanish yet. Add each one to `tools/nl.json` and `tools/es.json`, then run both scripts again.
