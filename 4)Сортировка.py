#!/usr/bin/env python
# coding: utf-8

# In[34]:


d = {}
with open("predators_prey.txt") as file:
    for line in file:
        k, *v = line.strip().split('eats')
        d.setdefault(k, []).append(v)

del d[""]
d
for k, v in d.items():
    if len(v) > 1:
        print ("{} eats {} and {}".format(k, ", ".join([x for xs in v[:-1] for x in xs]), *v[-1]))
    else:
        print ("{} eats {}".format(k, ", ".join([x for xs in d[k] for x in xs])))


# In[ ]:




