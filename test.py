import pandas as pd
dict_= {"a":1,"b":{"d":3,"e":5}}

#op {a:1, b.d:3, b.e:5}

# res = {}


# import pandas as pd

d = pd.json_normalize(dict_)
print(d.to_dict(orient='records')[0])
{'a': 1, 'b.d': 3, 'b.e': 5}  