# AI 开发工作流

个人 AI 开发全流程工作流模板。

## 工具链

| 工具 | 用途 | 状态 |
|------|------|------|
| **GitHub** | 代码版本管理 | 已配置 |
| **DVC** | 数据/模型版本控制 | 已安装 |
| **W&B** | 实验跟踪 | 已安装 |
| **Obsidian** | 知识管理/笔记 | 已安装 |
| **GitHub Projects** | 任务看板 | 网页端 |

## 项目结构

```
ai-dev-workflow/
├── src/              # 源代码
├── data/             # 数据集（DVC 管理）
├── models/           # 模型文件（DVC 管理）
├── configs/          # 配置文件
├── experiments/      # 实验记录
├── scripts/          # 工具脚本
├── notebooks/        # Jupyter notebooks
├── docs/             # 文档
├── dvc.yaml          # DVC 流水线定义
└── README.md         # 本文件
```

## 快速开始

### 1. 克隆项目

```bash
git clone git@github.com-443:sean17782-ai/ai-dev-workflow.git
cd ai-dev-workflow
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 配置 W&B

```bash
wandb login
# 输入 API Key: https://wandb.ai/authorize
```

### 4. 拉取数据

```bash
dvc pull
```

### 5. 运行实验

```bash
python src/train.py --config configs/experiment.yaml
```

## 使用流程

### 日常开发循环

```
1. GitHub Projects 创建任务
        ↓
2. 编写代码 / 修改配置
        ↓
3. 本地运行实验 → W&B 自动记录
        ↓
4. 提交代码 → git push
        ↓
5. 提交数据/模型变更 → dvc push
        ↓
6. Obsidian 记录实验笔记
        ↓
7. 回到步骤 1
```

### DVC 数据管理

```bash
# 添加数据文件到 DVC 跟踪
dvc add data/train.csv

# 推送到远程存储
dvc push

# 拉取数据
dvc pull

# 查看数据版本状态
dvc status
```

### W&B 实验跟踪

```python
import wandb

# 初始化实验
wandb.init(project="my-project", name="experiment-001")

# 记录配置
wandb.config.update({
    "learning_rate": 0.001,
    "batch_size": 32,
    "epochs": 10
})

# 记录指标
for epoch in range(10):
    loss = train_one_epoch()
    wandb.log({"loss": loss, "epoch": epoch})

# 记录模型
wandb.save("models/model.pt")

# 结束实验
wandb.finish()
```

### Obsidian 笔记结构

```
docs/
├── papers/          # 论文阅读笔记
├── experiments/     # 实验总结
├── ideas/           # 想法/灵感
├── snippets/        # 代码片段
└── daily/           # 每日记录
```

## 配置文件

### requirements.txt

```
torch>=2.0
transformers>=4.30
wandb>=0.15
dvc>=3.0
```

### dvc.yaml（示例）

```yaml
stages:
  prepare:
    cmd: python src/prepare.py
    deps:
      - src/prepare.py
      - data/raw
    outs:
      - data/processed:
          cache: true

  train:
    cmd: python src/train.py
    deps:
      - src/train.py
      - data/processed
    outs:
      - models/model.pt:
          cache: true
```

## 常见问题

**Q: 数据文件太大，Git 推送失败？**
A: 用 DVC 管理大文件，Git 只跟踪 `.dvc` 元数据文件。

**Q: 如何复现之前的实验？**
A: 通过 W&B 的 run ID 找到对应参数，配合 DVC 的数据版本号。

**Q: 如何备份？**
A: Git 推送到 GitHub，DVC 推送到远程存储（S3/GDrive/SSH）。
