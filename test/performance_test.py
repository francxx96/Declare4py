import sys
sys.path.append("..")
import os
from src.api.declare4py import Declare4Py
import time

log_path = os.path.join("..", "test", "Sepsis Cases.xes.gz")
model_path = os.path.join("..", "test", "test_models", "model1.decl")
d4py = Declare4Py()
d4py.parse_xes_log(log_path)
test = "query"

start = time.time()
if test == "checking":
    d4py.parse_decl_model(model_path)
    d4py.conformance_checking(consider_vacuity=True)
elif test == "discovery":
    d4py.compute_frequent_itemsets(min_support=0.8, len_itemset=2)
    d4py.discovery(consider_vacuity=True, max_declare_cardinality=2)
elif test == "query":
    res = d4py.query_checking(template_str='Response', activation='CRP', consider_vacuity=False, min_support=0.2, return_first=False)
else:
    pass
end = time.time()
print(f"{end - start}")