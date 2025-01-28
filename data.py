import pandas as pd
import json
from content import data

df = pd.DataFrame(data)
htmldf = df.to_html(classes='table table-bordered table-striped', index=False)
