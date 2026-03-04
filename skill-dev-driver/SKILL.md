---
name: skill-dev-driver
description: 开发驾驶元技能 - 记住项目目标、历史和解决方案，并可调度其他领域技能。当用户需要理解/规划项目架构和开发路线、继续之前的工作（上下文感知）、查找历史解决方案或记录新问题、调用特定领域技能（小程序/论文/产品等）时使用此 Skill。
triggerKeywords: ["继续", "下一步", "历史", "进度", "之前", "昨天", "上次", "架构", "设计", "规划", "路线", "怎么做", "如何开始", "错误", "bug", "问题", "失败", "报错", "异常", "解决"]
author: YYCLink
version: 1.0.0
dependencies: []
---

# skill-dev-driver - 开发驾驶元技能

## 核心定位

skill-dev-driver 是一个**元技能（Meta-Skill）**，专注于：
- 🎯 **理解项目目标** - 知道用户要做什么
- 📜 **记录项目历史** - 记住已完成和待办事项  
- 💡 **积累解决方案** - 从问题中学习并复用
- 🔗 **调度领域技能** - 调用其他技能协同工作

## 触发条件

以下场景应自动激活此技能：

| 场景类型 | 触发词示例 | 调用的子技能 |
|---------|-----------|-------------|
| 继续工作 | "继续"、"下一步"、"接着做" | project-memory |
| 规划架构 | "架构"、"设计"、"规划"、"路线" | core-driving |
| 解决问题 | "bug"、"错误"、"问题"、"解决" | solution-library |
| 调用技能 | "用 XX 技能"、"调用 XX" | skill-router |

## 项目上下文管理

### 上下文路径

```
项目根目录/.yyclink/context/
├── project-goal.md      # 项目目标（用户填写）
└── current-state.md     # 当前状态（AI 更新）
```

### 读取上下文

每次对话开始时自动执行：
```
读取文件：.yyclink/context/current-state.md
读取文件：.yyclink/context/project-goal.md（如果存在）
```

### 更新上下文

完成任务后，必须更新 `current-state.md`：
```markdown
## 当前任务
[任务描述]

## 完成进度
- [x] 已完成的功能
- [ ] 待办事项

## 最近修改
- [日期] 修改内容

## 遇到的问题
- 问题描述 → 解决方案
```

## 子技能系统

### 1. 核心驾驶 (core-driving)

**触发词**: "架构"、"设计"、"规划"、"路线"、"怎么做"、"如何开始"

**职责**:
- 理解项目目标
- 规划开发路线
- 提供技术选型建议
- 在不同编译器中适配操作方式

**工作流程**:
```
1. 读取 project-goal.md 了解项目目标
2. 分析当前任务
3. 提供技术方案和路线图
4. 更新 current-state.md
```

### 2. 项目记忆 (project-memory)

**触发词**: "继续"、"下一步"、"历史"、"进度"、"之前"、"昨天"、"上次"

**职责**:
- 记录项目状态
- 支持上下文感知的任务继续
- 追踪待办事项

**工作流程**:
```
1. 读取 current-state.md 了解当前进度
2. 识别"继续"的具体内容
3. 从上次的断点继续
4. 更新 current-state.md
```

### 3. 解决方案库 (solution-library)

**触发词**: "错误"、"bug"、"问题"、"失败"、"报错"、"异常"、"解决"

**职责**:
- 积累项目中的问题 - 解决方案对照表
- 遇到相似问题时自动推荐
- 记录新的解决方案

**工作流程**:
```
1. 检测问题类型
2. 查询历史解决方案
3. 如有匹配则推荐
4. 解决新问题则记录
```

## 跨技能调度

### 调度机制

skill-dev-driver 可调用其他 YYCLink 技能：

```yaml
技能路由表:
  - 关键词：["小程序", "微信", "抖音", "支付宝"]
    目标技能：skill-miniprogram-ecosystem
    路径：../skill-miniprogram-ecosystem/SKILL.md
    
  - 关键词：["论文", "学术", "写作", "文献"]
    目标技能：skill-thesis-writer
    路径：../skill-thesis-writer/SKILL.md
    
  - 关键词：["产品", "评审", "需求", "功能"]
    目标技能：skill-product-manager
    路径：../skill-product-manager/SKILL.md
    
  - 关键词：["web", "前端", "后端", "React", "Vue"]
    目标技能：skill-web-dev
    路径：../skill-web-dev/SKILL.md
```

### 调用方式

**方式 1：读取并执行**
```
读取文件：{技能路径}/SKILL.md
按照技能指令执行
```

**方式 2：委托执行**
```
告诉用户：正在调用 XX 技能...
加载目标技能
将任务委托给目标技能
```

## 使用流程

### 第一步：初始化（首次使用）

在项目根目录创建 `.yyclink/context/` 目录：

```bash
mkdir -p .yyclink/context
```

创建 `project-goal.md`：
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

创建 `current-state.md`：
```markdown
# 当前状态

## 当前任务
[首次使用为空]

## 完成进度
- [ ] 待办事项

## 最近修改
- [日期] 初始化项目上下文

## 解决方案库
[首次使用为空]
```

### 第二步：日常使用

**对话开始时**：
```
1. 自动读取 .yyclink/context/current-state.md
2. 自动读取 .yyclink/context/project-goal.md
3. 分析用户输入，匹配触发词
4. 加载对应的子技能
```

**执行任务**：
```
1. 执行子技能逻辑
2. 如需调用其他技能，执行跨技能调度
3. 记录解决方案（如有新问题）
```

**任务结束时**：
```
1. 更新 current-state.md
2. 记录完成进度
3. 记录新的解决方案
```

## Token 优化策略

### 轻量索引

```json
// skill-index.json (~500 token)
{
  "name": "skill-dev-driver",
  "version": "1.0.0",
  "skills": [
    {
      "id": "core-driving",
      "name": "核心驾驶",
      "description": "理解项目目标，规划开发路线",
      "triggerKeywords": ["架构", "设计", "规划", "路线"]
    },
    {
      "id": "project-memory",
      "name": "项目记忆",
      "description": "记录项目历史进度，支持上下文感知",
      "triggerKeywords": ["继续", "下一步", "历史", "进度"]
    },
    {
      "id": "solution-library",
      "name": "解决方案库",
      "description": "积累问题 - 解决方案对照表",
      "triggerKeywords": ["错误", "bug", "问题", "解决"]
    }
  ]
}
```

### 按需加载

| 阶段 | Token 用量 | 说明 |
|------|-----------|------|
| 初始 context | ~700 | index + current-state |
| 子技能加载 | ~2000 | 每个子技能 |
| 外部技能加载 | ~2000 | 每个外部技能 |
| **单次对话总计** | **~2700-4700** | 取决于加载技能数 |

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

## 与其他技能的配合

| 场景 | 配合的技能 | 调用方式 |
|------|-----------|---------|
| 小程序开发 | skill-miniprogram-ecosystem | 读取并执行 |
| 论文写作 | skill-thesis-writer | 读取并执行 |
| 产品评审 | skill-product-manager | 读取并执行 |
| Web 开发 | skill-web-dev | 读取并执行 |

## 记忆系统

### 自动检索

每次对话开始前，自动执行：
1. 读取 `.yyclink/context/project-goal.md`
2. 读取 `.yyclink/context/current-state.md`
3. 检索历史决策记录
4. 检索已记录的解决方案

### 信息沉淀

每次对话结束时，执行：
1. 提取关键决策点
2. 更新 `current-state.md`
3. 如有新解决方案，追加到 `solutions.md`

## 特殊场景处理

### 用户说"我不知道"

不提供标准答案，而是：
1. 提供获取答案的方法（去哪里找、问谁、怎么验证）
2. 要求用户调研后带着信息回来
3. 提供调研框架模板

### 上下文不存在

```
如果 `.yyclink/context/` 目录不存在：

skill-dev-driver:
📁 检测到这是首次使用 skill-dev-driver 技能。
正在初始化项目上下文...

已创建 .yyclink/context/ 目录。
请填写 project-goal.md 中的项目信息，
这样我就能更好地理解你的项目目标了。
```

### 技能未找到

```
如果调用的技能不存在：

skill-dev-driver:
⚠️ 未找到技能：skill-xxx
可能的原因：
1. 技能未下载：运行 run.bat 下载技能
2. 路径错误：检查技能路径配置

是否需要我帮你下载这个技能？
```

## 成功指标

用户的以下行为表示 skill-dev-driver 工作正常：
- 主动提及"继续"、"下一步"等上下文感知词
- 使用技能调度功能
- 记录新的解决方案
- 说"这个之前做过"时能正确回忆

---

**版本**: 1.0.0  
**作者**: YYCLink  
**GitHub**: https://github.com/wanddream/skill-dev-driver
