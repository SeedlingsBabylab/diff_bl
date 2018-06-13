# diff_bl

check if a new basic level csv is different from the old one


```
$ python video.py old.csv new.csv
```

will produce 2 csv's. one is called ```mismatch.csv```, the other ```not_found.csv```

```mismatch.csv``` lists those entries that match between old vs. new, but one of the codes is different

```not_found.csv``` lists those entries that either exists in the new.csv but not in the old.csv (```new_delete``` column will equal "new"), or viceverse (```new_delete``` column will equal "delete")

#### how do we determine a "match"?

if your word + timestamp onset are equal


