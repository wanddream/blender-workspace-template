---
name: skill-blender-industrial
description: Blender 工业产品建模技能 - 通过 MCP 服务器与 Blender 通信，执行参数化建模任务。当用户需要创建 3D 模型、工业产品设计、容器/盖子建模、布尔运算、倒角圆角、阵列等操作时使用此技能。
triggerKeywords: ["blender", "建模", "3D", "容器", "盖子", "圆柱", "圆锥", "布尔", "倒角", "圆角", "阵列", "螺纹", "唇口", "加强筋", "材质", "导出", "STL", "OBJ"]
author: YYCLink
version: 1.0.0
dependencies: ["skill-dev-driver"]
---

# skill-blender-industrial - Blender 工业产品建模技能

## 核心定位

skill-blender-industrial 是一个**领域技能（Domain Skill）**，专注于：
- 🎯 **参数化建模** - 通过参数驱动创建 3D 模型
- 📐 **工业产品设计** - 容器、盖子、密封件等工业产品
- 🔧 **MCP 通信桥梁** - 作为 AI 与 Blender 之间的通信桥梁
- 🏭 **特征建模** - 布尔运算、倒角、圆角、阵列等工业特征

## 依赖关系

此技能依赖以下组件：
- **skill-dev-driver** - 元技能，负责任务调度和上下文管理
- **Blender** - 3D 建模软件（推荐 4.2 LTS 或 4.5 LTS）
- **BlenderMCP** - MCP 服务器，用于 AI 与 Blender 通信

## 触发条件

以下场景应自动激活此技能：

| 场景类型 | 触发词示例 | 调用的技能函数 |
|---------|-----------|---------------|
| 创建基础几何体 | "圆柱"、"立方体"、"圆环"、"圆锥" | create_cylinder, create_cube, create_torus, create_cone |
| 布尔运算 | "开孔"、"切槽"、"合并"、"减去" | boolean_difference, boolean_union |
| 倒角圆角 | "倒角"、"圆角"、"R 角" | add_fillet, add_chamfer |
| 阵列操作 | "阵列"、"复制"、"均布" | circular_pattern, linear_pattern |
| 工业特征 | "唇口"、"螺纹"、"加强筋" | create_lip_groove, create_thread, create_rib |
| 材质应用 | "材质"、"颜色"、"塑料"、"金属" | apply_material |
| 完整产品 | "容器"、"盖子"、"罐子" | create_container_body, create_lid_assembly |
| 导出文件 | "导出"、"STL"、"OBJ"、"3D 打印" | export_obj, export_stl |

## 技能库函数

### 基础几何体（4 个）

```python
create_cylinder(name, diameter, height, location)
    # 创建圆柱体 - 用于轴、孔、容器等
    
create_cube(name, width, depth, height, location)
    # 创建立方体 - 用于外壳、基座等
    
create_torus(name, major_radius, minor_radius, location)
    # 创建圆环 - 用于密封圈、O 型环等
    
create_cone(name, bottom_diameter, top_diameter, height, location)
    # 创建圆锥台 - 用于漏斗、导向件等
```

### 布尔运算（2 个）

```python
boolean_difference(target_name, tool_name)
    # 布尔差集 - 用于开孔、切槽等
    
boolean_union(target_name, tool_name)
    # 布尔并集 - 用于合并物体
```

### 倒角/圆角（2 个）

```python
add_fillet(name, edge_indices, radius)
    # 添加圆角
    
add_chamfer(name, distance, angle)
    # 添加倒角 (斜角)
```

### 阵列（2 个）

```python
circular_pattern(name, count, axis, angle)
    # 圆周阵列
    
linear_pattern(name, direction, count, spacing)
    # 线性阵列
```

### 工业特征（3 个）

```python
create_lip_groove(diameter, lip_width, groove_depth)
    # 创建密封唇口和沟槽 - 用于盖子、容器等
    
create_thread(diameter, pitch, length, is_external)
    # 创建螺纹 - 用于螺丝、瓶盖等
    
create_rib(name, length, width, height, location)
    # 创建加强筋 - 用于增加结构强度
```

### 材质应用（1 个）

```python
apply_material(name, material_type, color)
    # 应用材质 (plastic/metal/rubber/glass)
```

### 完整产品（2 个）

```python
create_lid_assembly(bucket_diameter, overhang, thickness)
    # 创建盖子组件 - 工业容器盖参数化建模
    
create_container_body(diameter, height, wall_thickness)
    # 创建容器主体 - 带内部空腔的容器
```

### 场景管理（3 个）

```python
clear_scene()
    # 清空场景
    
export_obj(filepath)
    # 导出为 OBJ 格式
    
export_stl(filepath)
    # 导出为 STL 格式 (3D 打印)
```

## 工作原理

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

## 与 skill-dev-driver 的配合

skill-blender-industrial 是领域技能，需要与元技能 skill-dev-driver 配合使用：

### 技能调度流程

```
用户：创建一个蛋白粉罐子

skill-dev-driver:
📖 读取项目上下文...
🔗 检测到需要 Blender 建模技能...
正在加载 skill-blender-industrial...

skill-blender-industrial:
已加载 Blender 工业产品建模技能。
我将帮您创建蛋白粉罐子模型。

请问：
1. 罐子直径是多少？(默认 110mm)
2. 罐子高度是多少？(默认 150mm)
3. 是否需要盖子？
```

### 跨技能协作

```yaml
技能路由表:
  - 关键词：["blender", "建模", "3D", "容器", "盖子"]
    目标技能：skill-blender-industrial
    路径：../skill-blender-industrial/SKILL.md
```

## 环境配置

### 前置要求

1. **Blender** - 推荐 4.2 LTS 或 4.5 LTS
2. **Python 3.10+** - 用于运行 MCP 服务器
3. **BlenderMCP** - MCP 服务器

### 安装步骤

```bash
# 1. 安装 Blender
# 下载地址：https://www.blender.org/download/

# 2. 安装 Python 3.10+
# 下载地址：https://www.python.org/downloads/

# 3. 安装 BlenderMCP 服务器
uvx blender-mcp

# 4. 在 Blender 中安装 addon.py 插件
# Edit > Preferences > Add-ons > Install > 选择 addon.py
```

### MCP 配置

在 AI 编辑器的 MCP 配置文件中添加：

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

## 使用示例

### 示例 1：创建简单圆柱体

```
用户：创建一个直径 50mm、高 100mm 的圆柱体

skill-blender-industrial:
🔧 调用技能：create_cylinder
   - 直径：50mm
   - 高度：100mm

正在生成 Blender Python 代码...
通过 MCP 发送到 Blender...

✓ 创建圆柱体完成！
```

### 示例 2：创建带盖容器

```
用户：创建一个密封容器，主体直径 110mm，高 150mm，配上盖子

skill-blender-industrial:
🔧 调用技能：create_container_body
   - 直径：110mm
   - 高度：150mm
   - 壁厚：2.5mm

🔧 调用技能：create_lid_assembly
   - 桶口直径：110mm
   - 外延：12mm
   - 厚度：3mm

✓ 容器主体和盖子创建完成！
```

### 示例 3：创建阵列孔

```
用户：在圆柱顶部创建 6 个均布的螺丝孔

skill-blender-industrial:
🔧 调用技能：circular_pattern
   - 数量：6
   - 轴：Z 轴
   - 角度：360 度

🔧 调用技能：boolean_difference
   - 目标物体：圆柱体
   - 工具物体：螺丝孔

✓ 阵列孔创建完成！
```

## Token 优化策略

### 轻量索引

技能库文件 `blender_industrial_skills.py` 约 500 行代码，AI 读取时可按需加载：

| 阶段 | Token 用量 | 说明 |
|------|-----------|------|
| 初始 context | ~500 | SKILL.md |
| 技能函数加载 | ~2000 | 按需加载相关函数 |
| 总计 | ~2500 | 取决于加载函数数 |

### 按需加载

```python
# 只加载需要的技能函数
if "容器" in user_input:
    load_skill("create_container_body")
if "盖子" in user_input:
    load_skill("create_lid_assembly")
```

## 特殊场景处理

### MCP 连接失败

```
如果 MCP 连接失败：

skill-blender-industrial:
⚠️ 无法连接到 Blender MCP 服务器。

请检查：
1. Blender 是否已启动
2. BlenderMCP 插件是否已启用
3. 是否已点击 "Start MCP Server"
4. AI 编辑器的 MCP 配置是否正确

需要我帮您检查配置吗？
```

### Blender 未安装

```
如果检测到 Blender 未安装：

skill-blender-industrial:
⚠️ 未检测到 Blender 安装。

请下载并安装 Blender：
- 推荐版本：4.5 LTS 或 4.2 LTS
- 下载地址：https://www.blender.org/download/

安装完成后，请告诉我，我将继续帮您创建模型。
```

## 成功指标

用户的以下行为表示 skill-blender-industrial 工作正常：
- 能够通过自然语言描述创建 3D 模型
- 能够正确调用 MCP 服务器与 Blender 通信
- 能够在 Blender 中看到创建的模型
- 能够导出 STL/OBJ 文件用于 3D 打印

---

**版本**: 1.0.0  
**作者**: YYCLink  
**GitHub**: https://github.com/wanddream/skill-blender-industrial  
**依赖**: skill-dev-driver, Blender, BlenderMCP
