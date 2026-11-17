# Python_Data_Processing

Python 数据处理课程练习，使用 Python 3.12 和 Jupyter Notebook。作者为罗文希，学号为 `20244081107`。

## 目录

| 目录 | 内容 |
| --- | --- |
| `EXP01/` | 基本运算、函数与递归、容器与统计、文件与异常、类与对象复制 |
| `HW01/` | 最大公约数、欧拉数近似和整数幂判断等练习 |
| `EXP02/` | NumPy 数组与抽样、SciPy 数值计算、Matplotlib 绘图和 pandas 统计 |
| `HW02/` | 字符串与列表、向量与矩阵运算、Vector 类 |
| `EXP03/` | 正则表达式匹配、分组与替换、BeautifulSoup 解析 HTML |
| `HW03/` | 半圆定律、生命游戏与 pandas 数据处理 |

Notebook 使用 `20244081107_罗文希_expXX.ipynb` 或 `20244081107_罗文希_hwXX.ipynb` 命名，放在对应任务目录中。

`EXP01/student_utils.py` 提供学生成绩记录解析函数。`EXP01/exp01_data/` 包含 `students.txt`、`report.txt` 和 `students.pkl`，用于展示文件输入输出。

EXP02 的图表直接内嵌显示，数据在内存中处理。HW02 的矩阵乘法采用行向量乘矩阵的约定。

EXP03 的 HTML 示例直接写在 Notebook 中。HW03 的输入文件为 `archive/iris.csv`。代码优先读取任务目录中的 `iris.csv`，不存在时读取归档目录中的文件。

HW03 原始 CSV 缺少种类列，并包含测量缺失值。Notebook 核对行数、索引和测量差异后，按原始顺序从 scikit-learn 的 Iris 数据补入种类标签；先完成题目指定的两行修正，再参考作者“Cleaning Dataset”部分用 `dropna()` 删除剩余缺失行。清洗后保留148行，继续计算比例特征、导出 `HW03/iris_corrected.csv`（148行、7列），并按花卉种类完成五项分组统计。

## 开发环境

使用 Python 3.12 的 Conda 环境 `ALICE`。本机环境位于 `Z:\Anaconda\anaconda\envs\ALICE`，已有环境应先检查并复用，环境目录放在仓库之外。

新机器首次配置时运行以下命令。

```powershell
conda create -n ALICE python=3.12 pip
conda activate ALICE
python -m pip install jupyterlab notebook ipykernel numpy scipy matplotlib pandas beautifulsoup4 scikit-learn
python -m ipykernel install --user --name alice --display-name "Python (ALICE)"
python -m pip check
```

上述命令安装依赖的可用版本，具体结果可能随版本变化。本地维护的 `environment.yml` 可用于记录精确版本，该文件保存在本地。

每次运行时，在仓库根目录打开 PowerShell。

```powershell
conda activate ALICE
python -c "import os, sys; print(sys.executable); print(os.environ.get('CONDA_DEFAULT_ENV'))"
python -m pip check
Set-Location EXP01  # 按任务替换目录
python -m jupyter lab
```

确认解释器指向 ALICE，且环境名称为 `ALICE`。在 Jupyter 或 VS Code 中选择 `Python (ALICE)` 内核，并将工作目录设为对应任务目录，使相对路径和辅助模块导入正确。

## GitHub 文件范围

仓库保留 README、`.gitignore`、任务 Notebook、Python 辅助模块及输入输出数据。题目 PDF、`AGENTS.md`、环境配置、缓存和编辑器设置保存在本地或由忽略规则排除。

任务目录使用 `EXPxx/` 和 `HWxx/` 格式，其中 `xx` 为两位编号。输入输出放入任务下的 `*_data/`、`data/`、`input/`、`output/`、`inputs/` 或 `outputs/` 目录。规则另允许 `HW03/archive/`，用于保存作业三原始数据，并允许提交生成的 `HW03/iris_corrected.csv`。

新增任务或数据后同步更新本页目录，并通过 `git status` 检查待提交文件。需要使用其他数据路径时，在 `.gitignore` 中添加对应规则。

## 运行与提交

1. 打开对应任务的 Notebook，按 Markdown 单元中的题目要求完成练习。
2. 从干净内核按顺序运行全部单元，检查结果、边界输入、预期异常和文件路径。
3. 保留真实执行输出，文本文件使用 UTF-8，代码使用四空格缩进。
4. 提交前检查 Git 差异，确认 Notebook 所需辅助模块及输入输出文件齐全。

目前没有独立测试目录、自动化测试框架或构建流程。Notebook 的完整执行是课程代码的主要验证方式。
