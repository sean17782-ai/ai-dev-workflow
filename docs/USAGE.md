# AI 开发工作流使用指南

## 一、首次设置（一次性）

### 1.1 安装工具

```bash
# DVC 和 W&B（通过 pipx）
pipx install dvc
pipx install wandb

# Obsidian（Arch Linux）
sudo pacman -S obsidian
```

### 1.2 配置 W&B

```bash
wandb login
# 打开 https://wandb.ai/authorize 获取 API Key
```

### 1.3 配置 DVC 远程存储（可选）

```bash
# 使用 Google Drive
dvc remote add -d storage gdrive://<folder_id>

# 或使用 S3
dvc remote add -d storage s3://mybucket/dvcstore

# 或使用 SSH
dvc remote add -d storage ssh://user@example.com/path/to/store
```

### 1.4 创建 GitHub 仓库

```bash
cd ~/ai-dev-workflow
git add .
git commit -m "Initial commit: AI dev workflow setup"
git remote add origin git@github.com-443:sean17782-ai/ai-dev-workflow.git
git push -u origin master
```

---

## 二、日常开发流程

### 2.1 开始新实验

```bash
# 1. 在 GitHub Projects 创建任务卡片
# 2. 创建新分支（可选）
git checkout -b experiment/new-idea

# 3. 修改配置
vim configs/experiment.yaml

# 4. 运行实验
python src/train.py --config configs/experiment.yaml

# 5. 查看 W&B 面板
# 自动打开 https://wandb.ai/sean17782-ai/ai-dev-workflow
```

### 2.2 数据管理

```bash
# 添加新数据集
dvc add data/my_dataset.csv
git add data/my_dataset.csv.dvc .gitignore
git commit -m "Add dataset: my_dataset.csv"

# 推送到远程
dvc push

# 拉取最新数据
dvc pull

# 查看数据版本
dvc status
```

### 2.3 模型管理

```bash
# 训练完成后，模型自动保存到 models/
# 用 DVC 跟踪模型文件
dvc add models/best_model.pt
git add models/best_model.pt.dvc
git commit -m "Add model: best_model.pt"
dvc push
```

### 2.4 实验对比

```bash
# 在 W&B 面板中：
# 1. 选择多个 run
# 2. 点击 "Compare" 查看指标对比
# 3. 导出对比表格

# 命令行查看历史
wandb sync --view
```

---

## 三、Obsidian 笔记模板

### 3.1 论文阅读笔记

```markdown
# {{title}}

**作者**: 
**期刊/会议**: 
**年份**: 
**链接**: 

## 核心思想

## 方法

## 实验结果

## 个人思考

## 相关论文

#paper #{{tag}}
```

### 3.2 实验记录

```markdown
# 实验: {{experiment_name}}

**日期**: {{date}}
**状态**: 进行中 / 完成 / 失败

## 目标

## 配置

## 结果

## 分析

## 下一步

#experiment #{{tag}}
```

### 3.3 每日记录

```markdown
# {{date}}

## 今日完成

## 遇到的问题

## 明日计划

## 灵感/想法

#daily
```

---

## 四、GitHub Projects 看板设置

### 4.1 推荐列设置

| 列名 | 用途 |
|------|------|
| Backlog | 待办事项 |
| In Progress | 进行中 |
| Review | 待审查 |
| Done | 已完成 |

### 4.2 任务卡片模板

```markdown
## 任务描述

**优先级**: 高/中/低
**预计时间**: 
**关联实验**: W&B run 链接

### 验收标准

- [ ] 标准 1
- [ ] 标准 2

### 备注

```

---

## 五、常用命令速查

### Git

```bash
git status
git add .
git commit -m "message"
git push
git pull
git log --oneline -10
```

### DVC

```bash
dvc init
dvc add <file>
dvc push
dvc pull
dvc status
dvc repro          # 运行流水线
dvc dag            # 查看流水线图
```

### W&B

```bash
wandb login
wandb init
wandb status
wandb sync <run_id>  # 同步离线 run
```

### Python

```bash
pip install -r requirements.txt
python src/train.py --config configs/experiment.yaml
python src/train.py --epochs 20 --lr 0.01  # 覆盖参数
```

---

## 六、最佳实践

### 6.1 实验命名规范

```
{model}_{dataset}_{variant}_{date}

例如:
resnet18_cifar10_baseline_20260915
vit_imagenet_finetune_20260916
```

### 6.2 提交规范

```
feat: 添加新模型
fix: 修复数据加载 bug
exp: 新实验 - 学习率搜索
docs: 更新文档
data: 更新数据集
```

### 6.3 文件组织

```
experiments/
├── 2026-09-15_baseline/
│   ├── config.yaml
│   ├── wandb_link.txt
│   └── notes.md
├── 2026-09-16_lr-search/
│   ├── config.yaml
│   ├── wandb_link.txt
│   └── notes.md
```

---

## 七、故障排除

### DVC 推送失败

```bash
# 检查远程配置
dvc remote list

# 重新配置
dvc remote modify storage gdrive_client_id <id>
dvc remote modify storage gdrive_client_secret <secret>
```

### W&B 登录失败

```bash
# 检查网络
ping api.wandb.ai

# 使用代理
export WANDB_BASE_URL=https://api.wandb.ai
wandb login
```

### 数据版本冲突

```bash
# 查看差异
dvc status

# 强制拉取
dvc checkout --force
```
