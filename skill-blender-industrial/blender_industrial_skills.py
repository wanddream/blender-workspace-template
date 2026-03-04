# -*- coding: utf-8 -*-
"""
Blender 工业产品建模技能库
================================================
用于工业产品设计的 Blender 建模技能集合
通过 MCP 服务器与 Blender 通信，执行参数化建模任务
"""

import json

# ============================================================
# 技能 1: 基础几何体创建
# ============================================================

def create_cylinder(name, diameter, height, location=(0, 0, 0)):
    """
    创建圆柱体 - 用于轴、孔、容器等
    
    参数:
        name: 物体名称
        diameter: 直径 (mm)
        height: 高度 (mm)
        location: 位置 (x, y, z)
    
    返回:
        Blender Python 代码字符串
    """
    radius = diameter / 2
    code = f'''
import bpy
# 创建圆柱体
bpy.ops.mesh.primitive_cylinder_add(
    radius={radius},
    depth={height},
    location={location}
)
# 重命名
obj = bpy.context.active_object
obj.name = "{name}"
print(f"✓ 创建圆柱体：{{name}} (Φ{diameter}x{height}mm)")
'''
    return code

def create_cube(name, width, depth, height, location=(0, 0, 0)):
    """
    创建立方体 - 用于外壳、基座等
    
    参数:
        name: 物体名称
        width: 宽度 (mm)
        depth: 深度 (mm)
        height: 高度 (mm)
        location: 位置 (x, y, z)
    """
    code = f'''
import bpy
# 创建立方体
bpy.ops.mesh.primitive_cube_add(
    size=1,
    location={location}
)
obj = bpy.context.active_object
obj.name = "{name}"
# 缩放尺寸
obj.scale = ({width/2}, {depth/2}, {height/2})
bpy.ops.object.transform_apply(scale=True)
print(f"✓ 创建立方体：{{name}} ({width}x{depth}x{height}mm)")
'''
    return code

def create_torus(name, major_radius, minor_radius, location=(0, 0, 0)):
    """
    创建圆环 - 用于密封圈、O 型环等
    
    参数:
        name: 物体名称
        major_radius: 主半径 (环中心到管中心)
        minor_radius: 次半径 (管的半径)
    """
    code = f'''
import bpy
bpy.ops.mesh.primitive_torus_add(
    major_radius={major_radius},
    minor_radius={minor_radius},
    location={location}
)
obj = bpy.context.active_object
obj.name = "{name}"
print(f"✓ 创建圆环：{{name}}")
'''
    return code

def create_cone(name, bottom_diameter, top_diameter, height, location=(0, 0, 0)):
    """
    创建圆锥台 - 用于漏斗、导向件等
    """
    bottom_radius = bottom_diameter / 2
    top_radius = top_diameter / 2
    code = f'''
import bpy
bpy.ops.mesh.primitive_cone_add(
    vertices=32,
    radius1={bottom_radius},
    radius2={top_radius},
    depth={height},
    location={location}
)
obj = bpy.context.active_object
obj.name = "{name}"
print(f"✓ 创建圆锥台：{{name}}")
'''
    return code

# ============================================================
# 技能 2: 布尔运算
# ============================================================

def boolean_difference(target_name, tool_name):
    """
    布尔差集 - 用于开孔、切槽等
    
    参数:
        target_name: 目标物体名称
        tool_name: 工具物体名称 (将被减去)
    """
    code = f'''
import bpy

# 获取目标物体
target = bpy.data.objects.get("{target_name}")
tool = bpy.data.objects.get("{tool_name}")

if target and tool:
    # 添加布尔修改器
    modifier = target.modifiers.new(name="Boolean_Diff", type='BOOLEAN')
    modifier.operation = 'DIFFERENCE'
    modifier.object = tool
    
    # 应用修改器
    bpy.context.view_layer.objects.active = target
    bpy.ops.object.modifier_apply(modifier=modifier.name)
    
    # 删除工具物体
    bpy.data.objects.remove(tool)
    print(f"✓ 布尔差集完成：{{target_name}} - {{tool_name}}")
else:
    print(f"❌ 物体未找到")
'''
    return code

def boolean_union(target_name, tool_name):
    """
    布尔并集 - 用于合并物体
    """
    code = f'''
import bpy

target = bpy.data.objects.get("{target_name}")
tool = bpy.data.objects.get("{tool_name}")

if target and tool:
    modifier = target.modifiers.new(name="Boolean_Union", type='BOOLEAN')
    modifier.operation = 'UNION'
    modifier.object = tool
    
    bpy.context.view_layer.objects.active = target
    bpy.ops.object.modifier_apply(modifier=modifier.name)
    
    bpy.data.objects.remove(tool)
    print(f"✓ 布尔并集完成：{{target_name}} + {{tool_name}}")
'''
    return code

# ============================================================
# 技能 3: 倒角/圆角
# ============================================================

def add_fillet(name, edge_indices=None, radius=1.0):
    """
    添加圆角
    
    参数:
        name: 物体名称
        edge_indices: 要倒角的边索引列表 (None 表示所有边)
        radius: 圆角半径
    """
    code = f'''
import bpy

obj = bpy.data.objects.get("{name}")
if obj:
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='DESELECT')
    
    # 选择指定的边
    bpy.ops.object.mode_set(mode='OBJECT')
    modifier = obj.modifiers.new(name="Fillet", type='BEVEL')
    modifier.width = {radius}
    modifier.limit_method = 'ANGLE'
    
    bpy.ops.object.mode_set(mode='EDIT')
    print(f"✓ 添加圆角：{{name}} (R{radius})")
'''
    return code

def add_chamfer(name, distance=1.0, angle=45.0):
    """
    添加倒角 (斜角)
    """
    code = f'''
import bpy

obj = bpy.data.objects.get("{name}")
if obj:
    modifier = obj.modifiers.new(name="Chamfer", type='BEVEL')
    modifier.width = {distance}
    modifier.angle = math.radians({angle})
    print(f"✓ 添加倒角：{{name}} (C{distance})")
'''
    return code

# ============================================================
# 技能 4: 阵列/复制
# ============================================================

def circular_pattern(name, count, axis='Z', angle=360.0):
    """
    圆周阵列
    
    参数:
        name: 要阵列的物体名称
        count: 阵列数量
        axis: 旋转轴 ('X', 'Y', 'Z')
        angle: 阵列角度
    """
    code = f'''
import bpy
import math

source = bpy.data.objects.get("{name}")
if source:
    for i in range(1, {count}):
        new_obj = source.copy()
        new_obj.data = source.data.copy()
        new_obj.name = f"{name}_array_{i}"
        bpy.context.collection.objects.link(new_obj)
        
        # 计算旋转角度
        angle_rad = math.radians({angle} / {count} * i)
        
        # 绕轴旋转
        if '{axis}' == 'Z':
            new_obj.rotation_euler[2] = angle_rad
        elif '{axis}' == 'Y':
            new_obj.rotation_euler[1] = angle_rad
        else:
            new_obj.rotation_euler[0] = angle_rad
    
    print(f"✓ 圆周阵列完成：{{name}} x {count}")
'''
    return code

def linear_pattern(name, direction, count, spacing):
    """
    线性阵列
    
    参数:
        name: 要阵列的物体名称
        direction: 方向 ('X', 'Y', 'Z')
        count: 阵列数量
        spacing: 间距 (mm)
    """
    code = f'''
import bpy

source = bpy.data.objects.get("{name}")
if source:
    for i in range(1, {count}):
        new_obj = source.copy()
        new_obj.data = source.data.copy()
        new_obj.name = f"{name}_linear_{i}"
        bpy.context.collection.objects.link(new_obj)
        
        # 计算偏移
        offset = {spacing} * i
        if '{direction}' == 'X':
            new_obj.location[0] += offset
        elif '{direction}' == 'Y':
            new_obj.location[1] += offset
        else:
            new_obj.location[2] += offset
    
    print(f"✓ 线性阵列完成：{{name}} x {count}")
'''
    return code

# ============================================================
# 技能 5: 工业产品专用特征
# ============================================================

def create_lip_groove(diameter, lip_width=3.0, groove_depth=1.5):
    """
    创建密封唇口和沟槽 - 用于盖子、容器等
    
    参数:
        diameter: 基础直径
        lip_width: 唇口宽度
        groove_depth: 沟槽深度
    """
    outer_diameter = diameter + lip_width * 2
    groove_diameter = diameter - groove_depth * 2
    
    code = f'''
import bpy

# 创建外唇
bpy.ops.mesh.primitive_cylinder_add(
    radius={outer_diameter}/2,
    depth=2,
    location=(0, 0, 1)
)
lip = bpy.context.active_object
lip.name = "Sealing_Lip"

# 创建沟槽切除工具
bpy.ops.mesh.primitive_cylinder_add(
    radius={groove_diameter}/2,
    depth=3,
    location=(0, 0, 0.5)
)
cutter = bpy.context.active_object
cutter.name = "Groove_Cutter"

# 布尔差集创建沟槽
modifier = lip.modifiers.new(name="Groove", type='BOOLEAN')
modifier.operation = 'DIFFERENCE'
modifier.object = cutter
bpy.context.view_layer.objects.active = lip
bpy.ops.object.modifier_apply(modifier=modifier.name)
bpy.data.objects.remove(cutter)

print(f"✓ 创建密封唇口和沟槽 (Φ{diameter}mm)")
'''
    return code

def create_thread(diameter, pitch, length, is_external=True):
    """
    创建螺纹 - 用于螺丝、瓶盖等
    
    参数:
        diameter: 螺纹直径
        pitch: 螺距
        length: 螺纹长度
        is_external: True=外螺纹，False=内螺纹
    """
    code = f'''
import bpy
import math

# 创建螺旋线
vertices = int({length} / {pitch} * 32)
angle_step = math.pi * 2 / 32
radius = {diameter} / 2

verts = []
for i in range(vertices):
    angle = angle_step * i
    x = radius * math.cos(angle)
    y = radius * math.sin(angle)
    z = (i / vertices) * {length}
    verts.append((x, y, z))

# 创建螺纹路径
mesh = bpy.data.meshes.new("Thread_Path")
mesh.from_pydata(verts, [], [])
mesh.update()

obj = bpy.data.objects.new("Thread_Path", mesh)
bpy.context.collection.objects.link(obj)

print(f"✓ 创建螺纹路径 (Φ{diameter}, 螺距{pitch}, 长度{length})")
'''
    return code

def create_rib(name, length, width, height, location=(0, 0, 0)):
    """
    创建加强筋 - 用于增加结构强度
    """
    code = f'''
import bpy

# 创建加强筋
bpy.ops.mesh.primitive_cube_add(
    size=1,
    location={location}
)
obj = bpy.context.active_object
obj.name = "{name}"
obj.scale = ({width/2}, {length/2}, {height/2})
bpy.ops.object.transform_apply(scale=True)

# 添加圆角
modifier = obj.modifiers.new(name="Fillet", type='BEVEL')
modifier.width = 0.5
modifier.limit_method = 'ANGLE'

print(f"✓ 创建加强筋：{{name}} ({length}x{width}x{height}mm)")
'''
    return code

# ============================================================
# 技能 6: 材质应用
# ============================================================

def apply_material(name, material_type='plastic', color=None):
    """
    应用材质
    
    参数:
        name: 物体名称
        material_type: 材质类型 ('plastic', 'metal', 'rubber', 'glass')
        color: 颜色 (R, G, B) 0-1 范围
    """
    colors = {
        'white': (0.95, 0.95, 0.95),
        'black': (0.05, 0.05, 0.05),
        'gray': (0.5, 0.5, 0.5),
        'red': (0.8, 0.1, 0.1),
        'blue': (0.1, 0.1, 0.8),
        'yellow': (0.9, 0.9, 0.1),
        'orange': (0.95, 0.5, 0.1),
    }
    
    if color is None:
        color = colors.get('gray', (0.5, 0.5, 0.5))
    elif isinstance(color, str):
        color = colors.get(color, (0.5, 0.5, 0.5))
    
    code = f'''
import bpy

obj = bpy.data.objects.get("{name}")
if obj:
    # 创建材质
    mat = bpy.data.materials.new(name="{material_type}_mat")
    mat.use_nodes = True
    
    # 设置基础颜色
    bsdf = mat.node_tree.nodes["Principled BSDF"]
    bsdf.inputs["Base Color"].default_value = ({color[0]}, {color[1]}, {color[2]}, 1)
    
    # 设置材质属性
    if "{material_type}" == 'metal':
        bsdf.inputs["Metallic"].default_value = 0.9
        bsdf.inputs["Roughness"].default_value = 0.2
    elif "{material_type}" == 'rubber':
        bsdf.inputs["Roughness"].default_value = 0.8
    elif "{material_type}" == 'glass':
        bsdf.inputs["Transmission"].default_value = 1.0
        bsdf.inputs["Roughness"].default_value = 0.0
    else:  # plastic
        bsdf.inputs["Roughness"].default_value = 0.4
    
    # 应用材质
    if obj.data.materials:
        obj.data.materials[0] = mat
    else:
        obj.data.materials.append(mat)
    
    print(f"✓ 应用材质：{{name}} -> {material_type}")
'''
    return code

# ============================================================
# 技能 7: 完整产品建模
# ============================================================

def create_lid_assembly(bucket_diameter=110, overhang=12, thickness=3.0):
    """
    创建盖子组件 - 工业容器盖参数化建模
    
    参数:
        bucket_diameter: 桶口直径 (mm)
        overhang: 盖子外延 (mm)
        thickness: 盖子厚度 (mm)
    """
    lid_diameter = bucket_diameter + overhang * 2
    
    code = f'''
import bpy

# 清理场景
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# 1. 创建盖子主体
bpy.ops.mesh.primitive_cylinder_add(
    radius={lid_diameter}/2,
    depth={thickness},
    location=(0, 0, 0)
)
lid = bpy.context.active_object
lid.name = "Lid_Body"

# 2. 创建密封唇口
lip_radius = {bucket_diameter}/2
bpy.ops.mesh.primitive_torus_add(
    major_radius=lip_radius,
    minor_radius=1.5,
    location=(0, 0, -{thickness}/2)
)
seal = bpy.context.active_object
seal.name = "Sealing_Ring"

# 3. 创建勺子卡槽
bpy.ops.mesh.primitive_cylinder_add(
    radius=20,
    depth=10,
    location=(0, -30, {thickness}/2)
)
slot = bpy.context.active_object
slot.name = "Spoon_Slot"

# 布尔差集创建卡槽
modifier = lid.modifiers.new(name="Slot_Cut", type='BOOLEAN')
modifier.operation = 'DIFFERENCE'
modifier.object = slot
bpy.context.view_layer.objects.active = lid
bpy.ops.object.modifier_apply(modifier=modifier.name)
bpy.data.objects.remove(slot)

# 4. 添加圆角
modifier = lid.modifiers.new(name="Edge_Fillet", type='BEVEL')
modifier.width = 1.0
modifier.limit_method = 'ANGLE'

print(f"✓ 创建盖子组件 (Φ{lid_diameter}mm)")
'''
    return code

def create_container_body(diameter=110, height=150, wall_thickness=2.5):
    """
    创建容器主体 - 带内部空腔的容器
    
    参数:
        diameter: 外径 (mm)
        height: 高度 (mm)
        wall_thickness: 壁厚 (mm)
    """
    code = f'''
import bpy

# 1. 创建外圆柱
bpy.ops.mesh.primitive_cylinder_add(
    radius={diameter}/2,
    depth={height},
    location=(0, 0, {height}/2)
)
body = bpy.context.active_object
body.name = "Container_Body"

# 2. 创建内腔切除工具
bpy.ops.mesh.primitive_cylinder_add(
    radius={diameter}/2 - {wall_thickness},
    depth={height} - {wall_thickness},
    location=(0, 0, {wall_thickness} + ({height} - {wall_thickness})/2)
)
cutter = bpy.context.active_object
cutter.name = "Cavity_Cutter"

# 3. 布尔差集创建空腔
modifier = body.modifiers.new(name="Cavity", type='BOOLEAN')
modifier.operation = 'DIFFERENCE'
modifier.object = cutter
bpy.context.view_layer.objects.active = body
bpy.ops.object.modifier_apply(modifier=modifier.name)
bpy.data.objects.remove(cutter)

# 4. 添加底部圆角
modifier = body.modifiers.new(name="Bottom_Fillet", type='BEVEL')
modifier.width = 3.0
modifier.limit_method = 'ANGLE'

print(f"✓ 创建容器主体 (Φ{diameter}x{height}mm, 壁厚{wall_thickness}mm)")
'''
    return code

# ============================================================
# 技能 8: 场景管理
# ============================================================

def clear_scene():
    """
    清空场景
    """
    code = '''
import bpy
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()
print("✓ 场景已清空")
'''
    return code

def export_obj(filepath):
    """
    导出为 OBJ 格式
    """
    code = f'''
import bpy
bpy.ops.export_mesh.obj(filepath="{filepath}")
print(f"✓ 导出 OBJ: {filepath}")
'''
    return code

def export_stl(filepath):
    """
    导出为 STL 格式 (3D 打印)
    """
    code = f'''
import bpy
bpy.ops.export_mesh.stl(filepath="{filepath}")
print(f"✓ 导出 STL: {filepath}")
'''
    return code

# ============================================================
# 技能库注册表
# ============================================================

SKILL_REGISTRY = {
    # 基础几何体
    'create_cylinder': create_cylinder,
    'create_cube': create_cube,
    'create_torus': create_torus,
    'create_cone': create_cone,
    
    # 布尔运算
    'boolean_difference': boolean_difference,
    'boolean_union': boolean_union,
    
    # 倒角/圆角
    'add_fillet': add_fillet,
    'add_chamfer': add_chamfer,
    
    # 阵列
    'circular_pattern': circular_pattern,
    'linear_pattern': linear_pattern,
    
    # 工业特征
    'create_lip_groove': create_lip_groove,
    'create_thread': create_thread,
    'create_rib': create_rib,
    
    # 材质
    'apply_material': apply_material,
    
    # 完整产品
    'create_lid_assembly': create_lid_assembly,
    'create_container_body': create_container_body,
    
    # 场景管理
    'clear_scene': clear_scene,
    'export_obj': export_obj,
    'export_stl': export_stl,
}

def get_skill_names():
    """获取所有可用技能名称"""
    return list(SKILL_REGISTRY.keys())

def execute_skill(skill_name, **kwargs):
    """
    执行技能并返回 Blender Python 代码
    
    参数:
        skill_name: 技能名称
        **kwargs: 技能参数
    
    返回:
        Blender Python 代码字符串
    """
    if skill_name not in SKILL_REGISTRY:
        return f'print("❌ 技能不存在：{skill_name}")'
    
    skill_func = SKILL_REGISTRY[skill_name]
    return skill_func(**kwargs)

# ============================================================
# 主函数 - 用于测试
# ============================================================

if __name__ == "__main__":
    # 测试技能库
    print("可用技能列表:")
    for skill in get_skill_names():
        print(f"  - {skill}")
    
    print("\n" + "="*50)
    print("测试：创建盖子组件")
    print("="*50)
    
    code = create_lid_assembly(bucket_diameter=110)
    print(code)
