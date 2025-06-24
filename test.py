import polars as pl

df = pl.DataFrame({
    "A": ["cat", "dog", "cat", None, "cat"],
    "B": ["red", "blue", "blue", "red", "red"],
    "C": [1, 2, 2, 2, 3]
})

for col in df.columns:
    mode = df.select(pl.col(col).drop_nulls().mode()).item()
    print(f"{col}: {mode}")