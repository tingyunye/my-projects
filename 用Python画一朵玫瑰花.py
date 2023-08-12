#!/usr/bin/env python
# coding: utf-8

# https://mp.weixin.qq.com/s/5yLRm-LUdauhGr7vzj3W1Q

# In[1]:


from matplotlib import cm
from matplotlib.font_manager import FontProperties


# In[2]:


#声明文字窗口大小
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=25)


# In[3]:


#对使用到的整体库文件包进行导入
import matplotlib.pyplot as plt
import numpy as np


# In[9]:


#定义输出图像为3D状态输出：
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure('3D Scatter')
ax = fig.gca(projection='3d')


# In[10]:


#构建玫瑰花图像函数
[x, t] = np.meshgrid(np.array(range(25)) / 24.0, np.arange(0, 575.5, 0.5) / 575 * 17 * np.pi - 2 * np.pi)
p = np.pi / 2 * np.exp(-t / (8 * np.pi))
u = 1 - (1 - np.mod(3.6 * t, 2 * np.pi) / np.pi) ** 4 / 2
y = 2 * (x ** 2 - x) ** 2 * np.sin(p)
r = u * (x * np.sin(p) + y * np.cos(p))


# In[11]:


#对曲线进行平面的函数拟合
surf = ax.plot_surface(r * np.cos(t), r * np.sin(t), u * (x * np.cos(p) - y * np.sin(p)),                        rstride=1, cstride=1, cmap=cm.gist_heat, linewidth=0, antialiased=True)


# In[12]:


#设置标题以及格式
plt.title(u'祝各位女神节快乐！', fontproperties=font, color='blue', verticalalignment='bottom',
          bbox=dict(facecolor='y', edgecolor='blue', alpha=0.1))
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
plt.show()


# In[ ]:




