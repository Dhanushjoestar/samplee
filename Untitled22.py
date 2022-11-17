#!/usr/bin/env python
# coding: utf-8

# In[1]:


from matplotlib import pyplot as plt

x=[2,4,6,8]
y=[2,4,6,8]
plt.scatter(x,y,label='skitscat',color='k')
plt.title('scatter')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.show()


# In[2]:


import matplotlib.pyplot as plt
# data to display on plots
x = [ 2, 3, 4, 5, 6, 7, 4]
y = [8, 8.5, 9, 9.5, 10, 10.5, 11]

plt.scatter(x,y,label='Values of x&y',color='r')
plt.title('Smart Band Data Report')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
# Print the chart
plt.show()


# In[5]:


from matplotlib import pyplot as plt
slices=[2,4,6,8]
activities=["walking","talking","moving","swimming"]
cols=['g','c','b','y']

plt.pie(slices,
       labels= activities,
       colors=cols,
       startangle=90,
        shadow=True,
        autopct='%1.1f%%')
plt.title('pie chart')
plt.show()


# In[6]:


from matplotlib import pyplot as plt
x = [ 25, 50, 36, 19]
y = ['Neural Network', 'Data analytics', 'Quantum Computing', 'Machine Learning']
plt.pie(x, labels=y)
plt.title("Pie Chart")
cols = ['b','c','g', 'orange']
plt.pie(x,
labels =y,
colors = cols,
startangle = 90,
shadow = True,
explode =(0.1,0,0,0),
autopct ='%1.1f%%')


# In[ ]:




