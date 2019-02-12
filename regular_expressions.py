#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re


# In[8]:


example = re.match(r'AI', 'AI SATURDAY ABUJA AI')
print(result.group(0))


# In[9]:


example = re.findall('AI', 'AI SATURDAY ABUJA AI')
print(example)


# In[10]:


example = re.split(r'A', 'SATURDAY')
print(example)


# In[11]:


result = re.split(r'A', 'SATURDAY', maxsplit=1)
print(result)


# In[12]:


result = re.sub(r'ABUJA', 'NIGERIA', 'AI SATURDAY IS THE LARGEST COMMUNITY IN ABUJA')
print(result)


# In[15]:


pat = re.compile('AI')
example = pat.findall('AI SATURDAY ABUJA AI')
print(example)


# In[16]:


#Trying the compile code on a single line
result = re.compile('AI').findall('AI SATURDAY ABUJA AI')
print(result)
#WOW!!! It worked


# In[18]:


result2 = pat.findall('AI SATURDAY ABUJA')
print(result2)


# In[20]:


example = re.findall(r'.','AI SATURDAY ABUJA AI')
print(example)


# In[21]:


example = re.findall(r'\w','AI SATURDAY ABUJA AI')
print(example)


# In[22]:


example = re.findall(r'\w*','AI SATURDAY ABUJA AI')
print(example)


# In[23]:


example = re.findall(r'\w+','AI SATURDAY ABUJA AI')
print(example)


# In[25]:


example = re.findall(r'^\w+','AI SATURDAY ABUJA AI')
print(example)


# In[27]:


example = re.findall(r'\w+$','AI SATURDAY ABUJA')
print(example)


# In[28]:


example = re.findall(r'\w+$','AI SATURDAY ABUJA')
print(example)


# In[29]:


example = re.findall(r'\w\w','AI SATURDAY ABUJA')
print(example)


# In[33]:


example = re.findall(r'\b\w.','AI SATURDAY ABUJA')
print(example)


# In[34]:


line = 'asdf fjdk;afed,fjek,asdf,foo'
example = re.split(r'[;,\s]', line)
print(example)


# In[38]:


example = re.sub(r'[;,\s]',' ', line)
print(example)


# In[43]:


result=re.findall(r'\d{2}-\d{2}-\d{4}','Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009')
print(result)


# In[ ]:




