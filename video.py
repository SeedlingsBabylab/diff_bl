import pandas as pd
import sys


def diff(old, new):

    mismatch = pd.DataFrame(columns = old.columns)
    not_found = pd.DataFrame(columns = list(old.columns.values) + ["new_deleted"])

    for i, x in old.iterrows():
        match = new.query("(basic_level == \"{}\") & (onset == {})".format(
                          x.basic_level, x.onset))
        if match.shape[0] == 0:
            x['new_deleted'] = "deleted"
            not_found = not_found.append(x)
        elif match.shape[0] == 1:
            res = match.values.squeeze() == x.values.squeeze()
            if not all(b == True for b in res[1:]):
                mismatch = mismatch.append(match)
        else:
            print "multiple matches: {} - {}".format(x['labeled_object.object'], x.onset)

    for i, x in new.iterrows():
        match = old.query("(basic_level == \"{}\") & (onset == {})".format(
            x.basic_level, x.onset))
        if match.shape[0] == 0:
            x['new_deleted'] = "new"
            not_found = not_found.append(x)

    return mismatch, not_found


if __name__ == "__main__":

    old = pd.read_csv(sys.argv[1])
    new = pd.read_csv(sys.argv[2])

    old = old.rename(index=str, columns = {"labeled_object.ordinal": "ordinal", "labeled_object.basic_level": "basic_level", "labeled_object.onset": "onset"})
    new = new.rename(index=str, columns={"labeled_object.ordinal": "ordinal", "labeled_object.basic_level": "basic_level",
                                   "labeled_object.onset": "onset"})

    old = old.sort_values(by='ordinal')
    new = new.sort_values(by='ordinal')


    mismatch, not_found = diff(old, new)

    mismatch.to_csv("mismatch_video.csv", index=False)
    not_found.to_csv("not_found_video.csv", index=False)