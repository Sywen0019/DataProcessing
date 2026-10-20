# Python_Data_Processing

Python 数据处理课程资料与练习，使用 Python 3.12 和 Jupyter Notebook。

## 目录

| 路径 | 内容 |
| --- | --- |
| `EXP01/EXP01.pdf` | 实验一任务说明，保留原始文件 |
| `HW01/HW01.pdf` | 作业一任务说明，保留原始文件 |
| `AGENTS.md` | 仓库维护、编码与验证约定 |

每项任务的 Notebook、辅助模块和生成数据均放在对应目录内，仓库包含：

- `EXP01/20244081107_罗文希_exp01.ipynb`：基本运算、函数与递归、容器与统计、文件与异常、类与对象复制。
- `EXP01/student_utils.py`：学生成绩记录解析函数。
- `EXP01/exp01_data/`：实验生成的文本、统计报告和 pickle 数据。
- `HW01/20244081107_罗文希_hw01.ipynb`：最大公约数、欧拉数近似和整数幂判断等练习。
- `EXP02/20244081107_罗文希_exp02.ipynb`：NumPy 数组与抽样、SciPy 数值计算、Matplotlib 绘图、pandas 分组统计、协方差与相关系数。
- `HW02/20244081107_罗文希_hw02.ipynb`：字符串与列表处理、元组向量与矩阵运算，以及 Vector 类的比较、内积和乘法。
- `environment.yml`：共享的 ALICE 环境配置。

EXP02 和 HW02 已补全代码，并在 ALICE 中从头顺序执行，分别包含 24 和 11 个代码单元格，运行输出已保留。EXP02 的三张图表直接内嵌显示；HW02 的矩阵乘法采用行向量乘矩阵的约定。

## 开发环境

本机复用 Conda 环境 `ALICE`，路径为 `Z:\Anaconda\anaconda\envs\ALICE`，不要自动删除或重建。环境目录应放在仓库之外。

在仓库根目录打开 PowerShell，执行：

```powershell
conda activate ALICE
python -c "import os, sys; print(sys.executable); print(os.environ.get('CONDA_DEFAULT_ENV'))"
python -m pip check
Set-Location EXP01  # 按任务改为 HW01、EXP02 或 HW02
python -m jupyter lab
```

确认解释器指向 ALICE，且环境名称为 `ALICE`；如不一致，先检查环境激活状态。在 Jupyter 或 VS Code 中选择 `Python (ALICE)` 内核。若尚未注册内核，在已激活的环境中执行：

```powershell
python -m ipykernel install --user --name alice --display-name "Python (ALICE)"
```

在其他机器上，克隆仓库后从根目录运行 `conda env create -f environment.yml`、`conda activate ALICE` 并注册内核。若已有 ALICE 环境，先检查并复用它。

实验二使用 NumPy、SciPy、Matplotlib 和 pandas，已在 `environment.yml` 的 pip 依赖中记录验证版本。已有 ALICE 环境缺少这些包时，可在激活环境后执行 `python -m pip install numpy==2.5.4 scipy==1.18.1 matplotlib==3.11.2 pandas==3.0.6`，再运行 `python -m pip check`。实验二数据均在内存中处理，不生成数据或图片文件；图表使用英文标题和标签，无需额外配置中文字体。

## 运行与提交

1. 打开对应任务的 Notebook，按 Markdown 单元格中的要求完成练习。
2. 将 Notebook 工作目录设为任务目录，使辅助模块导入和数据相对路径正确。
3. 提交前重启内核并按顺序运行全部单元格，检查预期结果、边界输入、异常处理和生成文件。
4. 按 `<student_id>_<name>_expNN.ipynb` 或 `<student_id>_<name>_hwNN.ipynb` 命名，其中 `NN` 为两位任务编号；保留原有 Markdown 任务描述，在对应代码单元格中完成要求。

目前没有独立测试目录、自动化测试框架或构建流程。代码采用四空格缩进，文本文件使用 UTF-8；提交前检查 Git 差异，避免纳入环境目录、缓存、检查点和敏感信息。详细协作规范见 [AGENTS.md](AGENTS.md)。
