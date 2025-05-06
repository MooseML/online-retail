import nbformat

notebook_path = "clustering_holiday_shoppers.ipynb"

with open(notebook_path, "r", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=nbformat.NO_CONVERT)

# remove broken widget metadata
if "widgets" in nb.metadata:
    del nb.metadata["widgets"]

with open(notebook_path, "w", encoding="utf-8") as f:
    nbformat.write(nb, f)

print(f"Cleaned widget metadata from: {notebook_path}")
