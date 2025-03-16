form sklearn.datasets import make_clasifications
import numpy as np
x,y=make_classification(n_sample=100,n_fatures=2,n_informative=1,n_redundant=0,n_classes=2,n_clusters_per_class=1,random_state=41,hypercube=False,class_sep=10)
import matplotlib.pyplot as plt

