
import matplotlib.pyplot as plt
import numpy as np

from sklearn import linear_model,svm,tree

# %%
# 线性回归
print(tree)

# 定义训练数据
# 定义训练数据（100个二维1-30随机离散点）
x = np.random.randint(1, 30, [100, 1])
# 根据x值创建一定范围随机离散点
y = 2 * x + np.random.randint(1, 10, [100, 1])

# Linear Model 线性模型
model = linear_model.LinearRegression()
# 训练数据
model.fit(x, y)
# 预测
result = model.predict(x)
score = model.score(x, y)
print(score)


# 标记绘图说明
plt.title("xianxianhuigui")
plt.xlabel("x")
plt.ylabel("y")

# 绘制测试数据离散点
plt.scatter(x, y)

# 绘制训练回归线
plt.plot(x, result, color="blue")

# 预测
test = [[15]]
plt.scatter(test, model.predict(test), color="yellow")
plt.show()


# %%
# 回归决策树

# # 定义训练数据
# # 定义训练数据（100个二维1-30随机离散点）
# X = [[0, 0], [2, 2]]
# y = [0.5, 2.5]
# clf = tree.DecisionTreeRegressor()
# clf = clf.fit(X, y)
# clf.predict([[1, 1]])

# # Linear Model 线性模型
# model = linear_model.LinearRegression()
# # 训练数据
# model.fit(x, y)
# # 预测
# result = model.predict(x)
# score = model.score(x, y)
# print(score)


# # 标记绘图说明
# plt.title("xianxianhuigui")
# plt.xlabel("x")
# plt.ylabel("y")

# # 绘制测试数据离散点
# plt.scatter(x, y)

# # 绘制训练回归线
# plt.plot(x, result, color="blue")

# # 预测
# test = [[15]]
# plt.scatter(test, model.predict(test), color="yellow")
# plt.show()


# %%
