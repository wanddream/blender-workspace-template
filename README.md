# Blender 工作区模板

> 专为机械零件和塑料零件建模设计的 Blender 工作区模板

## 🚀 快速开始

### 步骤 1：克隆仓库

```bash
git clone https://github.com/wanddream/blender-workspace-template.git
```

### 步骤 2：移动到目标位置

将整个 `blender-workspace-template` 文件夹移动到你希望存放的位置，例如：
- `D:\BlenderProjects\blender-workspace-template`
- `C:\Users\你的用户名\Documents\blender-workspace-template`

### 步骤 3：打开工作区

双击文件夹中的 `blender-workspace-template.code-workspace` 文件，VS Code 会自动打开。

### 步骤 4：（可选）创建桌面快捷方式

1. 在 VS Code 中，点击 **"文件"** → **"将工作区另存为..."**
2. 选择一个方便的位置，例如桌面
3. 命名为 `建模模板.code-workspace`
4. 以后双击这个快捷方式即可直接打开工作区

## 📁 工作区结构

```
blender-workspace-template/
├── blender-workspace-template.code-workspace  ← 双击打开这个文件
├── README.md                                   # 本说明文件
├── docs/
│   └── blender-prompts.md                      # Blender 建模提示词大全
├── skill-blender-industrial/                   # Blender 工业建模技能库
└── skill-dev-driver/                           # 开发驱动技能库
```

## 🛠️ 技能文件夹

### skill-blender-industrial
Blender 工业建模技能库，包含：
- 基础几何体创建
- 参数化建模
- 布尔运算
- 表面细分
- 工业零件建模技巧

### skill-dev-driver
开发驱动技能库，包含：
- 项目记忆管理
- 解决方案库
- 核心开发流程

## 📝 建模提示词

详细的建模提示词请参考 [`docs/blender-prompts.md`](docs/blender-prompts.md)

### 快速参考

**初始建模提示词模板：**
```
你是一名 Blender 智能建模助手，擅长将自然语言指令转化为精准的 Blender 操作。

【建模要求】
- 单位：米 (m)
- 精度：小数点后 3 位
- 细分等级：3

【当前任务】
创建一个 [零件名称]，尺寸：[长×宽×高/直径×高度]
```

**微调修改提示词：**
```
请修改 [物体名称]：
- 修改内容：[具体修改]
- 保持精度：[精度要求]
- 确认是否符合设计意图
```

**材质渲染提示词：**
```
为 [物体名称] 添加材质：
- 材质类型：[塑料/金属/橡胶]
- 颜色：[颜色值]
- 表面质感：[光滑/磨砂/纹理]
```

## ⚙️ VS Code 设置

本工作区已配置以下设置：

```json
{
  "editor.formatOnSave": true,
  "files.exclude": {
    "**/.git": true,
    "**/__pycache__": true,
    "**/*.pyc": true
  }
}
```

## 📌 使用建议

1. **工作区位置** - 将模板文件夹放在固定位置，不要频繁移动
2. **桌面快捷方式** - 建议创建快捷方式，方便快速打开
3. **提示词迭代** - 根据实际使用情况不断优化提示词
4. **技能库更新** - 定期从主仓库拉取最新技能

## 🔗 相关资源

- [Blender 官方文档](https://docs.blender.org/)
- [Blender 工业建模教程](https://www.blender.org/support/tutorials/)
- [建模提示词大全](docs/blender-prompts.md)
