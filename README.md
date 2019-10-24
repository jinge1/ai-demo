# ai-demo

## 插件

    - python

## pip 超时解决办法

- 更改安装源到国内镜像(package 为包名)

  `pip install package -i https://mirrors.aliyun.com/pypi/simple/`

- 永久更改源到国内的源(推荐)

  `pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/`

## pip install

- pylint

- jupyter

## 虚拟环境(pipenv)

### pipenv 基本操作

1. 进入项目目录

2. 安装虚拟环境
   `pipenv install`

3. 进入隔离的虚拟环境
   `pipenv shell`

### vscode 切换 pipenv 到虚拟环境

1. 查看 pipenv 虚拟环境路径
   `pipenv --venv`

2. 添加虚拟环境路径
   在 settings.json 的最后一行添加虚拟路径"python.venvPath": "1 中路径"

3. 重启 vscode

### 切换 pipenv 到虚拟环境

    点击打开项目python文件，左下角状态栏中，选择配置的虚拟环境即可

## 大纲

[Python 绘图，我只用 Matplotlib](https://www.jianshu.com/p/78ba36dddad8)

[机器学习的常用算法](https://www.jianshu.com/p/f2824467c780)
组织结构
包
模块
类
函数、变量
