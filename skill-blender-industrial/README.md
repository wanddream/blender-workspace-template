# skill-blender-industrial - Blender 工业产品建模技能

> 🎯 **通过自然语言对话创建 3D 模型** - 专为工业产品设计打造的 Blender 参数化建模技能

![Blender MCP Workflow](images/blender-mcp-workflow.png)

---

## 📋 快速概览

| 项目 | 说明 |
|------|------|
| **技能名称** | skill-blender-industrial |
| **技能类型** | 领域技能（Domain Skill） |
| **依赖技能** | [skill-dev-driver](../skill-dev-driver)（元技能） |
| **依赖软件** | Blender 4.2+ / 4.5 LTS, Python 3.10+, BlenderMCP |
| **技能文件** | [SKILL.md](SKILL.md) - AI 读取的核心指令文件 |
| **代码文件** | [blender_industrial_skills.py](blender_industrial_skills.py) - 技能库实现 |
| **教程文档** | [TUTORIAL.md](TUTORIAL.md) - 完整环境搭建教程 |

---

## ⚠️ 重要说明

**这个技能不是独立运行的！**

### 与 skill-dev-driver 的关系

```
┌─────────────────────────────────────────────────────────────┐
│                     用户自然语言指令                          │
│                  "创建一个蛋白粉罐子"                          │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│  skill-dev-driver (元技能)                                   │
│  1. 理解用户意图                                             │
│  2. 检测需要 Blender 建模技能                                  │
│  3. 调度加载 skill-blender-industrial                        │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│  skill-blender-industrial (领域技能)                         │
│  1. 从技能库选择合适技能函数                                   │
│  2. 生成 Blender Python 代码                                    │
│  3. 通过 MCP 发送到 Blender                                     │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│  MCP 服务器 (blender-mcp)                                    │
│  将 Python 代码发送到 Blender                                   │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│  Blender (运行 addon.py)                                    │
│  执行 Python 代码，创建 3D 模型                                   │
└─────────────────────────────────────────────────────────────┘
```

### 技能库的作用

`blender_industrial_skills.py` 是一个**代码生成器**：

- ❌ **不是**：直接运行它来创建模型
- ✅ **而是**：它生成 Blender Python 代码，通过 MCP 发送给 Blender 执行

---

## 🚀 快速开始

### 步骤 1: 下载技能

```bash
# 方式 1: 使用一键下载脚本（推荐）
# Windows 用户直接双击 run.bat

# 方式 2: 手动克隆
git clone https://github.com/wanddream/skill-blender-industrial.git
```

### 步骤 2: 安装依赖

```bash
# 1. 安装 Blender
# 下载地址：https://www.blender.org/download/
# 推荐版本：4.5 LTS 或 4.2 LTS

# 2. 安装 Python 3.10+
# 下载地址：https://www.python.org/downloads/

# 3. 安装 BlenderMCP 服务器
uvx blender-mcp
```

### 步骤 3: 配置 MCP

在 AI 编辑器（Claude/Windsurf/Cursor）的 MCP 配置中添加：

```json
{
  "mcpServers": {
    "blender": {
      "command": "uvx",
      "args": ["blender-mcp"]
    }
  }
}
```

### 步骤 4: 导入技能到 CodeBuddy

1. 打开 CodeBuddy → 设置 → 技能 → 导入 Skill
2. 选择 `skill-blender-industrial/SKILL.md`
3. 选择「用户 Skill」类型
4. 开启技能开关

### 步骤 5: 开始使用

```
你：创建一个蛋白粉罐子，直径 110mm，高 150mm

AI: [自动调用 skill-blender-industrial 技能]
    [生成 Blender Python 代码]
    [通过 MCP 发送到 Blender]
    
✓ 容器主体创建完成！
```

---

## 📦 技能列表 (19 个)

### 基础几何体（4 个）

| 技能名 | 功能 | 参数示例 |
|--------|------|----------|
| `create_cylinder` | 创建圆柱体 | 直径、高度 |
| `create_cube` | 创建立方体 | 长、宽、高 |
| `create_torus` | 创建圆环 | 主半径、次半径 |
| `create_cone` | 创建圆锥台 | 上半径、下半径、高度 |

### 布尔运算（2 个）

| 技能名 | 功能 |
|--------|------|
| `boolean_difference` | 差集（开孔/切槽） |
| `boolean_union` | 并集（合并物体） |

### 倒角/圆角（2 个）

| 技能名 | 功能 |
|--------|------|
| `add_fillet` | 添加圆角 |
| `add_chamfer` | 添加倒角 |

### 阵列（2 个）

| 技能名 | 功能 |
|--------|------|
| `circular_pattern` | 圆周阵列 |
| `linear_pattern` | 线性阵列 |

### 工业特征（3 个）

| 技能名 | 功能 |
|--------|------|
| `create_lip_groove` | 创建密封唇口 |
| `create_thread` | 创建螺纹 |
| `create_rib` | 创建加强筋 |

### 材质（1 个）

| 技能名 | 功能 |
|--------|------|
| `apply_material` | 应用材质 (plastic/metal/rubber/glass) |

### 完整产品（2 个）

| 技能名 | 功能 |
|--------|------|
| `create_lid_assembly` | 创建容器盖组件 |
| `create_container_body` | 创建容器主体 |

### 场景管理（3 个）

| 技能名 | 功能 |
|--------|------|
| `clear_scene` | 清空场景 |
| `export_obj` | 导出 OBJ 格式 |
| `export_stl` | 导出 STL 格式 (3D 打印) |

---

## 💡 使用示例

### 示例 1：创建简单圆柱体

```
你：创建一个直径 50mm、高 100mm 的圆柱体

AI 内部执行：
- 调用 create_cylinder(diameter=50, height=100)
- 生成 Blender Python 代码
- 通过 MCP 发送到 Blender 执行
```

### 示例 2：创建带盖容器

```
你：创建一个密封容器，主体直径 110mm，高 150mm，配上盖子

AI 内部执行：
- 调用 create_container_body(diameter=110, height=150, wall_thickness=2.5)
- 调用 create_lid_assembly(bucket_diameter=110, overhang=12, thickness=3)
- 通过 MCP 依次执行
```

### 示例 3：添加阵列孔

```
你：在圆柱顶部创建 6 个均布的螺丝孔

AI 内部执行：
- 创建孔的圆柱体
- 调用 circular_pattern(count=6, axis='Z', angle=360)
- 调用 boolean_difference() 进行布尔差集运算
```

### 示例 4：导出 3D 打印文件

```
你：把模型导出为 STL 文件

AI 内部执行：
- 调用 export_stl(filepath="C:/models/part.stl")
- 通过 MCP 发送到 Blender 执行
```

---

## 🔧 文件结构

```
skill-blender-industrial/
├── README.md                    # 本文档
├── SKILL.md                     # 核心技能文件（AI 读取）
├── TUTORIAL.md                  # 完整环境搭建教程
├── blender_industrial_skills.py # 技能库模块（代码生成器）
└── images/                      # 文档图片（待添加）
```

---

## 📚 相关文档

| 文档 | 说明 |
|------|------|
| [SKILL.md](SKILL.md) | AI 读取的核心技能指令文件 |
| [TUTORIAL.md](TUTORIAL.md) | Blender + MCP 环境搭建完整教程 |
| [blender_industrial_skills.py](blender_industrial_skills.py) | 技能库源代码 |

---

## 🤝 与 skill-dev-driver 的配合

### 技能调度

skill-blender-industrial 是领域技能，需要与元技能 [skill-dev-driver](../skill-dev-driver) 配合使用：

```yaml
# skill-dev-driver 中的技能路由配置
技能路由表:
  - 关键词：["blender", "建模", "3D", "容器", "盖子"]
    目标技能：skill-blender-industrial
    路径：../skill-blender-industrial/SKILL.md
```

### 协作流程

```
用户：继续做昨天的容器模型

skill-dev-driver:
📖 读取项目上下文...
当前任务：创建蛋白粉罐子模型
上次进度：完成了容器主体
待办：添加盖子和密封唇口

🔗 检测到需要 Blender 建模技能...
正在加载 skill-blender-industrial...

skill-blender-industrial:
已加载 Blender 工业产品建模技能。
我们继续创建盖子组件...
```

---

## ❓ 常见问题

### Q: 我能直接运行 blender_industrial_skills.py 吗？

**A**: 可以运行，但只会打印技能代码示例，不会创建实际模型。模型需要在 Blender 中执行生成的代码。

### Q: 我需要安装什么？

**A**: 
1. **Blender**（运行 3D 建模）
2. **BlenderMCP addon**（在 Blender 中）
3. **MCP 服务器配置**（在 AI 编辑器中）
4. **skill-dev-driver**（元技能，用于技能调度）

### Q: 如何添加新技能？

**A**: 在 `blender_industrial_skills.py` 中：
1. 添加新的技能函数
2. 在 `SKILL_REGISTRY` 中注册新技能
3. 在 `SKILL.md` 中更新技能列表

### Q: MCP 连接失败怎么办？

**A**: 检查以下几点：
1. 确保 Blender 已启动并运行
2. 确保 MCP 插件在 Blender 中已启用
3. 确保在 Blender 中点击了 "Start MCP Server"
4. 检查 AI 编辑器的 MCP 配置是否正确
5. 尝试重启 Blender 和 AI 编辑器

### Q: 这个技能和其他 YYCLink 技能有什么关系？

**A**: 
- **skill-dev-driver** 是元技能，负责任务调度和上下文管理
- **skill-blender-industrial** 是领域技能，专注 Blender 建模
- 元技能可以调度多个领域技能协同工作

---

## 🔗 相关资源

| 资源 | 链接 |
|------|------|
| **技能仓库** | https://github.com/wanddream/skill-blender-industrial |
| **元技能仓库** | https://github.com/wanddream/skill-dev-driver |
| **Blender 官网** | https://www.blender.org/download/ |
| **Blender 中文社区** | https://www.blendercn.org/ |
| **BlenderMCP 项目** | https://github.com/ahujasid/blender-mcp |

---

## 📝 更新日志

| 版本 | 日期 | 更新内容 |
|------|------|----------|
| v1.0 | 2026-03-03 | 初始版本，包含 19 个基础技能 |

---

**作者**: YYCLink  
**协议**: MIT License  
**依赖**: skill-dev-driver, Blender, BlenderMCP
