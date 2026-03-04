# Blender + MCP AI 建模环境搭建完整教程

> 本教程将指导您从零开始搭建 Blender + MCP 服务器的 AI 建模环境，让您能够通过自然语言对话创建 3D 模型。

![Blender MCP Tutorial](images/blender-mcp-tutorial.png)

---

## 📋 目录

1. [简介](#简介)
2. [Blender 安装与汉化](#blender-安装与汉化)
3. [BlenderMCP 服务器安装](#blendermcp-服务器安装)
4. [使用技能库](#使用技能库)
5. [常见问题](#常见问题)

---

## 简介

### 什么是 Blender？

Blender 是一款免费开源的 3D 创作软件，支持建模、雕刻、绑定、动画、渲染、合成等完整的 3D 制作流程。本教程中，我们将使用 Blender 进行工业产品的参数化建模。

### 什么是 MCP？

MCP（Model Context Protocol）是一种协议，允许 AI 编辑器（如 Claude）与本地应用程序（如 Blender）进行通信。通过 MCP，AI 可以控制 Blender 执行建模操作。

### 工作原理

```
┌─────────────────────────────────────────────────────────────┐
│  用户自然语言指令                                            │
│  "创建一个直径 110mm 的容器"                                  │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│  AI (Claude)                                                 │
│  1. 理解用户意图                                             │
│  2. 从技能库选择合适技能                                     │
│  3. 调用技能函数生成 Blender Python 代码                      │
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

---

## Blender 安装与汉化

### 步骤 1：下载 Blender

#### 推荐版本

- **Blender 4.5 LTS** - 最新长期支持版（推荐）
- **Blender 4.2 LTS** - 稳定的长期支持版

#### 下载地址

**中文社区下载站**（推荐，下载速度快）：
- 主页：https://www.blendercn.org/downloadme
- 提供阿里云、清华大学等国内镜像源

**各版本特点**：

| 版本 | 支持期限 | 说明 |
|------|----------|------|
| 4.5 LTS | 2026 年 7 月 | 最新 LTS 版本，功能最新 |
| 4.2 LTS | 2026 年 7 月 | 稳定版本，兼容性好 |

#### 下载步骤

1. 访问 https://www.blendercn.org/downloadme

![Blender 下载页面](images/blender-download.png)

2. 选择适合的版本（推荐 4.5 LTS 或 4.2 LTS）
3. 选择下载源：
   - 官方下载地址
   - 阿里云下载地址（推荐）
   - 清华大学下载地址（推荐）
4. 下载 Windows 版本（.zip 或 .msi）

### 步骤 2：安装 Blender

#### Windows 安装

1. **解压/运行安装程序**
   - 如果下载的是 `.zip` 文件，解压到任意目录（如 `C:\Program Files\Blender Foundation\Blender 4.5\`）
   - 如果下载的是 `.msi` 文件，双击运行并按提示安装

2. **创建快捷方式**（可选）
   - 右键点击 `blender.exe` → 发送到 → 桌面快捷方式

3. **启动 Blender**
   - 双击 `blender.exe` 或桌面快捷方式启动

### 步骤 3：汉化设置

Blender 内置中文语言包，无需额外下载汉化包即可启用中文界面。

![Blender 汉化设置](images/blender-hanhua.png)

#### 方法一：在 Blender 中设置（推荐）

1. 打开 Blender
2. 点击顶部菜单栏的 **Edit**（编辑）
3. 选择 **Preferences**（偏好设置）
4. 在左侧选择 **Interface**（界面）
5. 找到 **Translation**（翻译）部分
6. 勾选 **Language** 下拉框，选择 **简体中文**
7. 在 **Translation** 下方勾选：
   - ✅ **Tooltips**（工具提示）- 鼠标悬停时显示中文帮助
   - ⬜ **New Data**（新建数据）- 不建议勾选，可能导致命名问题
   - ⬜ **Interface**（界面）- 可选，勾选后界面完全汉化

#### 设置建议

```
推荐配置：
├── Language: 简体中文 ✅
├── Tooltips: ✅ (鼠标悬停帮助显示中文)
├── New Data: ⬜ (新建物体保持英文名，避免问题)
└── Interface: ⬜ (菜单保持英文，方便学习)
```

#### 方法二：使用一键切换插件

Blender 中文社区提供了一键中英切换插件：

- **Blender 4.x 版本**：下载 `0.0.3_新建物体不翻译`
- **Blender 3.x 版本**：下载 `0.0.2_新建物体不翻译`

插件安装方法：
1. 在 Blender 中打开 **Edit > Preferences > Add-ons**
2. 点击 **Install...** 按钮
3. 选择下载的插件 `.py` 文件
4. 勾选启用插件

---

## BlenderMCP 服务器安装

### 前置要求

在开始之前，请确保您已满足以下条件：

- ✅ **已安装 Blender**（见上文）
- ✅ **Python 3.10 或更高版本**
  - 检查版本：在命令行输入 `python --version`
  - 下载安装：https://www.python.org/downloads/
  - ⚠️ 安装时勾选 "Add Python to PATH"

- ✅ **Anthropic 官方账号**（使用 Claude 时需要）
  - 或使用支持 MCP 的编辑器：Windsurf、Cursor、VSCode

### 步骤 1：安装 MCP 服务器

打开命令提示符（CMD）或 PowerShell，运行以下命令：

```bash
uvx blender-mcp
```

> 💡 **提示**：如果是首次使用，系统会自动安装 `uv` 工具。Mac 用户可能需要先运行 `brew install uv`。

### 步骤 2：配置 Claude 编辑器

#### 在 Claude Desktop 中配置

1. 打开 Claude App
2. 点击 **Claude > Settings**（设置）
3. 选择 **Developer**（开发者）
4. 点击 **Edit Config**（编辑配置）
5. 在配置文件中添加以下内容：

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

6. 保存配置文件

#### 在其他编辑器中配置

- **Windsurf**、**Cursor**、**VSCode** 的配置方式类似
- 在相应编辑器的 MCP 配置中添加上述配置

### 步骤 3：安装 Blender 插件

MCP 服务器需要在 Blender 中安装对应的插件才能通信。

1. **获取插件文件**
   - MCP 服务器安装后，会提供 `addon.py` 文件
   - 通常位于 MCP 安装目录中

2. **在 Blender 中安装插件**
   - 打开 Blender
   - 点击 **Edit > Preferences > Add-ons**（编辑 > 偏好设置 > 插件）
   - 点击 **Install...**（安装）按钮
   - 浏览并选择 `addon.py` 文件
   - 勾选启用的插件

3. **确认插件已启用**
   - 在插件列表中搜索 "MCP" 或 "BlenderMCP"
   - 确保插件已勾选启用

### 步骤 4：启动 MCP 服务

1. **在 Blender 中启动服务**
   - 打开 Blender
   - 在 3D 窗口右侧或顶部找到 **MCP Blender** 标签页
   - 点击 **Start MCP Server** 按钮

2. **验证连接**
   - 打开您的 AI 编辑器（Claude/Windsurf/Cursor 等）
   - 在编辑器右侧应该能看到新增的 9 个工具按钮
   - 这些工具用于调用 Blender 服务

---

## 使用技能库

### 技能库文件

`blender_industrial_skills.py` 是一个代码生成器，包含 19 个工业建模技能函数。

### 技能列表

#### 基础几何体（4 个）

| 技能名 | 功能 | 参数示例 |
|--------|------|----------|
| `create_cylinder` | 创建圆柱体 | 直径、高度 |
| `create_cube` | 创建立方体 | 长、宽、高 |
| `create_torus` | 创建圆环 | 主半径、次半径 |
| `create_cone` | 创建圆锥台 | 上半径、下半径、高度 |

#### 布尔运算（2 个）

| 技能名 | 功能 |
|--------|------|
| `boolean_difference` | 差集（开孔/切槽） |
| `boolean_union` | 并集（合并物体） |

#### 倒角/圆角（2 个）

| 技能名 | 功能 |
|--------|------|
| `add_fillet` | 添加圆角 |
| `add_chamfer` | 添加倒角 |

#### 阵列（2 个）

| 技能名 | 功能 |
|--------|------|
| `circular_pattern` | 圆周阵列 |
| `linear_pattern` | 线性阵列 |

#### 工业特征（3 个）

| 技能名 | 功能 |
|--------|------|
| `create_lip_groove` | 创建密封唇口 |
| `create_thread` | 创建螺纹 |
| `create_rib` | 创建加强筋 |

#### 材质（1 个）

| 技能名 | 功能 |
|--------|------|
| `apply_material` | 应用材质 |

#### 完整产品（2 个）

| 技能名 | 功能 |
|--------|------|
| `create_lid_assembly` | 创建容器盖组件 |
| `create_container_body` | 创建容器主体 |

#### 场景管理（3 个）

| 技能名 | 功能 |
|--------|------|
| `clear_scene` | 清空场景 |
| `export_obj` | 导出 OBJ 格式 |
| `export_stl` | 导出 STL 格式 |

### 使用方式

#### 方式一：自然语言对话（推荐）

直接与 AI 对话，描述您想要的模型：

```
你：创建一个蛋白粉罐子，直径 110mm，高 150mm，壁厚 2.5mm

AI: [内部调用 create_container_body 技能，生成代码，通过 MCP 发送到 Blender]
```

#### 方式二：查看技能代码

如果您想了解技能如何工作，可以查看 `blender_industrial_skills.py` 文件，了解每个技能生成的 Blender Python 代码。

### 使用示例

#### 示例 1：创建简单圆柱体

```
你：创建一个直径 50mm、高 100mm 的圆柱体

AI 内部执行：
- 调用 create_cylinder(diameter=50, height=100)
- 生成 Blender Python 代码
- 通过 MCP 发送到 Blender 执行
```

#### 示例 2：创建带盖容器

```
你：创建一个密封容器，主体直径 110mm，高 150mm，配上盖子

AI 内部执行：
- 调用 create_container_body(...) 创建主体
- 调用 create_lid_assembly(...) 创建盖子
- 通过 MCP 依次执行
```

#### 示例 3：添加阵列孔

```
你：在圆柱顶部创建 6 个均布的螺丝孔

AI 内部执行：
- 创建孔的圆柱体
- 调用 circular_pattern(...) 进行圆周阵列
- 调用 boolean_difference(...) 进行布尔差集运算
```

---

## 常见问题

### Q1: 我能直接运行 blender_industrial_skills.py 吗？

**A**: 可以运行，但只会打印技能代码示例，不会创建实际模型。模型需要在 Blender 中执行生成的代码。

### Q2: 我需要安装什么？

**A**: 需要安装以下内容：
1. **Blender** - 运行 3D 建模
2. **BlenderMCP addon** - 在 Blender 中安装
3. **MCP 服务器配置** - 在 AI 编辑器中配置

### Q3: 如何添加新技能？

**A**: 在 `blender_industrial_skills.py` 文件中：
1. 添加新的技能函数
2. 在 `SKILL_REGISTRY` 中注册新技能

### Q4: MCP 连接失败怎么办？

**A**: 检查以下几点：
1. 确保 Blender 已启动并运行
2. 确保 MCP 插件在 Blender 中已启用
3. 确保在 Blender 中点击了 "Start MCP Server"
4. 检查 AI 编辑器的 MCP 配置是否正确
5. 尝试重启 Blender 和 AI 编辑器

### Q5: 汉化后有些菜单还是英文？

**A**: 这是正常现象。Blender 的翻译是逐步完善的：
- 主菜单和常用功能已翻译
- 部分专业术语可能仍显示英文
- 建议保持界面英文，只开启 Tooltips 中文提示

### Q6: 下载的模型尺寸不对怎么办？

**A**: 检查 Blender 的单位设置：
1. 在右侧属性面板找到 **Scene Properties**（场景属性）
2. 在 **Units**（单位）中设置为 **Metric**（公制）
3. 确保 **Length**（长度）单位为 **Meters**（米）或 **Millimeters**（毫米）

---

## 附录

### 相关资源链接

- **Blender 中文社区**：https://www.blendercn.org/
- **Blender 官方下载**：https://www.blender.org/download/
- **BlenderMCP 项目**：https://github.com/ahujasid/blender-mcp
- **BlenderMCP 官网**：https://blender-mcp.com/

### 版本信息

| 组件 | 推荐版本 |
|------|----------|
| Blender | 4.5 LTS / 4.2 LTS |
| Python | 3.10+ |
| BlenderMCP | 最新版 |

---

**教程版本**：v1.0  
**更新日期**：2026-03-03
