<<<<<<< HEAD
# skill-dev-driver - 开发驾驶元技能

**版本**: 1.0.0  
**作者**: YYCLink  
**协议**: MIT License

## 概述

skill-dev-driver 是一个**元技能（Meta-Skill）**，专注于：
- 🎯 **理解项目目标** - 知道用户要做什么
- 📜 **记录项目历史** - 记住已完成和待办事项
- 💡 **积累解决方案** - 从问题中学习并复用
- 🔗 **调度领域技能** - 调用其他技能协同工作

## 核心特性

| 特性 | 说明 | Token 效率 |
|------|------|-----------|
| 轻量索引 | skill-index.json (~500 token) | ⭐⭐⭐⭐⭐ |
| 项目上下文 | current-state.md (~200 token) | ⭐⭐⭐⭐⭐ |
| 按需加载 | 仅加载匹配的技能 (~2000 token) | ⭐⭐⭐⭐⭐ |
| 技能调度 | 可调用其他 YYCLink 技能 | ⭐⭐⭐⭐ |

## 触发词

当用户输入包含以下关键词时，skill-dev-driver 会自动激活：

| 场景 | 触发词示例 | 调用的子技能 |
|------|-----------|-------------|
| 继续工作 | "继续"、"下一步"、"接着做"、"历史"、"进度"、"之前"、"昨天"、"上次" | project-memory |
| 规划架构 | "架构"、"设计"、"规划"、"路线"、"怎么做"、"如何开始" | core-driving |
| 解决问题 | "bug"、"错误"、"问题"、"解决"、"失败"、"报错"、"异常" | solution-library |
| 调用技能 | "用 XX 技能"、"调用 XX" | skill-router |

## 快速开始

### 方式一：通过 YYCLink-Skills 一键下载

```bash
# 在 YYCLink-Skills 目录双击 run.bat
# 或手动克隆
git clone https://github.com/wanddream/skill-dev-driver.git
```

### 方式二：直接在项目中使用

```bash
# 在你的项目目录
mkdir skills
cd skills
git clone https://github.com/wanddream/skill-dev-driver.git
```

### 方式三：在编译器中导入

**CodeBuddy/Qoder**：
1. 设置 → 技能 → 导入 Skill
2. 选择 `skill-dev-driver/SKILL.md`
3. 完成！

**Cline/Cursor**：
1. 项目里放 `skills/skill-dev-driver/`
2. 使用时说："使用 skill-dev-driver 技能"

## 目录结构

```
skill-dev-driver/
├── SKILL.md                    # 核心技能文件（入口）
├── README.md                   # 使用说明
├── skill-index.json            # 技能索引配置（Token 优化）
├── skills/                     # 子技能目录
│   ├── core-driving/           # 核心驾驶 - 理解项目目标，规划开发路线
│   │   └── SKILL.md
│   ├── project-memory/         # 项目记忆 - 记录项目历史进度，支持上下文感知
│   │   └── SKILL.md
│   └── solution-library/       # 解决方案库 - 积累问题 - 解决方案对照表
│       └── SKILL.md
└── templates/                  # 上下文模板
    ├── project-goal.template.md    # 项目目标模板
    ├── current-state.template.md   # 当前状态模板
    └── solutions.template.md       # 解决方案库模板
```

## 使用示例

### 示例 1：继续之前的工作

```
用户：继续做昨天的功能

skill-dev-driver:
📖 读取项目上下文...
当前任务：实现语音识别模块
上次进度：完成了 HTTP API 通信部分
待办：添加 VAD 语音活动检测

正在加载 project-memory 技能...

好的，我们继续实现语音识别模块。上次完成了 HTTP API 通信，
今天我们来添加 VAD 语音活动检测功能...
```

### 示例 2：调用其他技能

```
用户：用小程序技能做登录功能

skill-dev-driver:
🔗 检测到需要小程序开发技能...
正在加载 skill-miniprogram-ecosystem...

已加载小程序生态开发技能。
为了设计登录功能，请告诉我：
1. 目标平台？（微信/抖音/支付宝）
2. 登录方式？（微信登录/手机号/自定义）
```

### 示例 3：记录解决方案

```
用户：这个 bug 终于解决了！是 numpy 版本冲突

skill-dev-driver:
💡 检测到新问题解决方案！
正在记录到 solution-library...

已记录：
问题：numpy 版本冲突导致语音识别失败
解决：锁定 numpy==1.24.3

下次遇到类似问题会自动推荐这个方案。
```

## 项目上下文管理

### 初始化（首次使用）

在项目根目录创建 `.yyclink/context/` 目录：

```bash
mkdir -p .yyclink/context
```

创建项目目标文件：

```bash
.yyclink/
└── context/
    ├── project-goal.md      # 项目目标（用户填写）
    └── current-state.md     # 当前状态（AI 更新）
```

### 项目目标模板

```markdown
# 项目目标

## 项目名称
[填写项目名称]

## 项目描述
[用一句话描述项目是做什么的]

## 核心功能
1. [功能 1]
2. [功能 2]
3. [功能 3]

## 技术栈
- 前端：
- 后端：
- 数据库：

## 目标用户
[描述目标用户群体]
```

### 当前状态模板

```markdown
# 当前状态

## 当前任务
[当前正在进行的任务]

## 完成进度
- [x] 已完成的功能
- [ ] 待办事项

## 最近修改
- [日期] 修改内容

## 遇到的问题
- 问题描述 → 解决方案
```

### 如何让 AI 自动更新

完成任务后，告诉 AI：
```
更新 current-state.md，记录今天完成了 XXX
```

或者：
```
记录到项目历史：实现了 XX 功能，遇到了 XX 问题已解决
```

## 与其他技能的配合

skill-dev-driver 可以与其他 YYCLink 技能配合使用：

| 场景 | 配合的技能 | 调用方式 |
|------|-----------|---------|
| 小程序开发 | skill-miniprogram-ecosystem | 自动调度 |
| 论文写作 | skill-thesis-writer | 自动调度 |
| 产品评审 | skill-product-manager | 自动调度 |
| Web 开发 | skill-web-dev | 自动调度 |

### 技能调度机制

当用户说"用 XX 技能"或检测到相关领域关键词时，skill-dev-driver 会：
1. 自动识别需要的技能
2. 读取目标技能的 SKILL.md
3. 按照目标技能的指令执行
4. 完成任务后返回 skill-dev-driver 继续上下文管理

## 常见问题

### Q: skill-dev-driver 和其他技能有什么区别？

**A**: skill-dev-driver 是**元技能（Meta-Skill）**，它本身不专注于某个具体领域，而是：
- 管理项目上下文（目标、历史、解决方案）
- 调度其他领域技能（小程序、论文、产品等）
- 让你在任何项目中都能"继续之前的工作"

### Q: 必须使用 .yyclink/context/目录吗？

**A**: 这是推荐的目录结构，但你可以自定义。关键是：
- skill-dev-driver 需要知道项目目标和当前状态
- 目录位置可以在 SKILL.md 中配置

### Q: 如何在多个项目中使用？

**A**: skill-dev-driver 是**项目级**的技能：
- 每个项目有自己的 `.yyclink/context/` 目录
- 在每个项目中单独初始化即可
- 项目之间的上下文互不干扰

### Q: 如何备份项目上下文？

**A**: 建议将 `.yyclink/context/` 纳入你的项目版本控制：
```bash
git add .yyclink/context/
git commit -m "记录项目状态"
```

### Q: Token 用量会不会很高？

**A**: skill-dev-driver 采用轻量索引设计：
- 基础用量：~700 token（索引 + 当前状态）
- 按需加载：~2000 token/子技能
- 单次对话总计：~2700-4700 token

## 更新日志

### v1.0.0 (2026-03-01)
- 初始版本
- 核心驾驶、项目记忆、解决方案库三个子技能
- 支持技能调度机制
- 支持项目上下文管理
- Token 优化设计

---

## 贡献

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request
=======
# YYCLink AI Skills

YYCLink 的个人 AI Skill 集合，用于 Claude Code 等 AI 编程助手。

> 📋 **本仓库是技能索引中心**，每个技能都是独立仓库，可单独下载使用。

## 🎯 我的 Skills

| Skill | 说明 | 适用场景 | GitHub |
|-------|------|----------|--------|
| **skill-dev-driver** ⭐ | 开发驾驶元技能 - 项目上下文管理/技能调度 | 所有项目的开发驾驶 | [GitHub](https://github.com/wanddream/skill-dev-driver) |
| skill-miniprogram-ecosystem | 小程序开发生态 | 微信/抖音/支付宝小程序开发 | [GitHub](https://github.com/wanddream/skill-miniprogram-ecosystem) |
| skill-thesis-writer | 论文写作助手 | 学术论文写作 | [GitHub](https://github.com/wanddream/skill-thesis-writer) |
| skill-product-manager | 产品经理拷打 | 产品方案评审/从 0 到 1 打磨 | [GitHub](https://github.com/wanddream/skill-product-manager) |

## 🚀 快速开始

### 方式一：一键下载所有 Skills（推荐）

**Windows 用户：**

直接双击 **`run.bat`** 即可自动下载/更新所有 Skills。

> 如果双击没反应，可能是 PowerShell 执行策略限制，右键 `install.ps1` → 使用 PowerShell 运行。

**Linux/Mac:**
```bash
# 手动克隆
git clone https://github.com/wanddream/skill-miniprogram-ecosystem.git
git clone https://github.com/wanddream/skill-thesis-writer.git
```

### 方式二：手动克隆单个 Skill

```bash
# 开发驾驶（元技能）
git clone https://github.com/wanddream/skill-dev-driver.git

# 小程序开发生态
git clone https://github.com/wanddream/skill-miniprogram-ecosystem.git

# 论文写作助手
git clone https://github.com/wanddream/skill-thesis-writer.git

# 产品经理拷打
git clone https://github.com/wanddream/skill-product-manager.git
```

### 方式三：让 AI 读取远程 SKILL.md

告诉 AI：
> "读取 https://github.com/wanddream/skill-xxx/raw/main/SKILL.md"

AI 会自动获取技能指令，无需下载到本地。

## 📁 目录结构

```
YYCLink-Skills/
├── README.md              # 本文件 - 技能总览
├── install.ps1            # Windows 一键下载/更新脚本
├── run.bat                # 双击运行入口
├── .gitignore             # 忽略下载的 skill-*/ 文件夹
├── skill-dev-driver/      # 开发驾驶元技能（下载后）
├── skill-miniprogram-ecosystem/   # 小程序技能（下载后）
├── skill-thesis-writer/           # 论文技能（下载后）
└── skill-product-manager/         # 产品经理拷打（下载后）
```

## 🔄 更新所有 Skills

直接双击 **`run.bat`**，脚本会自动检测本地已存在的技能并执行 `git pull` 更新。

## ➕ 如何添加新 Skill

### 第 1 步：创建新技能仓库

1. 在 GitHub 创建新仓库，命名格式：`skill-<功能名>`
   - 例如：`skill-web-dev`、`skill-python-ml`

2. 本地创建技能结构：
```
skill-xxx/
├── SKILL.md          # 核心技能文件（必填）
├── README.md         # 技能说明文档
├── examples/         # 示例代码（可选）
└── .gitignore
```

### 第 2 步：编写 SKILL.md

`SKILL.md` 是 AI 读取的核心文件，告诉 AI 如何使用这个技能。

**⚠️ 重要：必须包含 `name` 字段**，否则 CodeBuddy 无法正确识别技能名称：

```markdown
---
name: skill-xxx
---

# Skill: 技能名称

## 描述
这个技能是做什么的...

## 触发词
当用户说以下关键词时触发此技能：
- "关键词 1"
- "关键词 2"

## 指令
当技能被触发时，AI 应该：
1. 第一步做什么
2. 第二步做什么

## 示例
用户：xxx
AI：xxx
```

> 💡 **提示**：开头的 YAML Front Matter `name: skill-xxx` 是 CodeBuddy 识别技能的关键，必须与仓库名保持一致。

### 第 3 步：添加到 install.ps1

打开 `install.ps1`，在 `$repos = @( ... )` 数组中添加新条目：

```powershell
$repos = @(
    @{
        name = "skill-miniprogram-ecosystem"
        url  = "https://github.com/wanddream/skill-miniprogram-ecosystem.git"
    },
    @{
        name = "skill-thesis-writer"
        url  = "https://github.com/wanddream/skill-thesis-writer.git"
    },
    # ====== 在这里添加新技能 ======
    @{
        name = "skill-web-dev"
        url  = "https://github.com/username/skill-web-dev.git"
    }
)
```

### 第 4 步：更新 README.md

1. 在 "我的 Skills" 表格中添加新技能：

```markdown
| skill-web-dev | Web 开发指南 | 前端/后端开发 | [GitHub](https://github.com/username/skill-web-dev) |
```

2. 更新"目录结构"部分，删除 `skills.json` 的引用

### 第 5 步：提交并推送

```bash
git add .
git commit -m "添加新技能：skill-web-dev"
git push
```

### 完整示例流程

```bash
# 1. 创建新仓库
mkdir skill-web-dev
cd skill-web-dev
git init

# 2. 创建 SKILL.md
cat > SKILL.md << 'EOF'
# Skill: Web 开发

## 描述
前端和后端开发最佳实践

## 触发词
- "web 开发"
- "前端"
- "后端"

## 指令
1. 询问用户具体需求
2. 提供技术方案
EOF

# 3. 提交到 GitHub
git add .
git commit -m "init"
git remote add origin https://github.com/username/skill-web-dev.git
git push -u origin main

# 4. 在索引仓库更新配置
cd ../YYCLink-Skills
# 编辑 install.ps1 在 $repos 数组中添加新技能
# 编辑 README.md 添加表格行

git add .
git commit -m "添加 skill-web-dev"
git push
```

## 🔧 在 CodeBuddy 中使用

### 导入方式（推荐「用户 Skill」）

打开 CodeBuddy → 设置 → 技能 → 导入 Skill

| 类型 | 适用场景 | 特点 |
|------|----------|------|
| **用户 Skill** ⭐ | 个人通用技能 | 跨项目全局可用，切换项目自动继承 |
| 项目 Skill | 项目专属规范 | 仅当前项目有效，换项目需重新导入 |

> 💡 **建议**：个人开发的技能一律作为「用户 Skill」导入，这样在任何项目中都能使用，无需重复配置。

### 使用步骤

1. **下载 Skill**：通过本仓库的 `run.bat` 一键下载所有技能
2. **导入 CodeBuddy**：设置 → 技能 → 导入 Skill → 选择下载好的 `SKILL.md` 文件
3. **选择「用户 Skill」**：确保导入时选择「用户 Skill」类型
4. **开启使用**：在技能列表中开启对应的技能开关即可

## 🤖 AI 如何使用 Skills

### 方法 1：读取本地 SKILL.md（如果已下载）
```
用户：使用小程序技能
AI：读取 skill-miniprogram-ecosystem/SKILL.md 获取指令
```

### 方法 2：读取远程 SKILL.md（无需下载）
```
用户：使用小程序技能
AI：通过 HTTP 读取远程 SKILL.md 内容
```
>>>>>>> 0408c2b798d8212b859c88ed3320b3dbafcc79a5

---

**作者**: YYCLink  
<<<<<<< HEAD
**GitHub**: https://github.com/wanddream/skill-dev-driver  
**YYCLink-Skills**: https://github.com/wanddream/YYCLink-Skills  
=======
>>>>>>> 0408c2b798d8212b859c88ed3320b3dbafcc79a5
**协议**: MIT License
