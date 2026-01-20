import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d.proj3d import proj_transform

class Arrow3D(FancyArrowPatch):
    """用于3D箭头的类"""
    def __init__(self, x, y, z, dx, dy, dz, *args, **kwargs):
        super().__init__((0, 0), (0, 0), *args, **kwargs)
        self._xyz = (x, y, z)
        self._dxdydz = (dx, dy, dz)

    def draw(self, renderer):
        x1, y1, z1 = self._xyz
        dx, dy, dz = self._dxdydz
        x2, y2, z2 = (x1 + dx, y1 + dy, z1 + dz)

        xs, ys, zs = proj_transform((x1, x2), (y1, y2), (z1, z2), self.axes.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        super().draw(renderer)
        
    def do_3d_projection(self, renderer=None):
        x1, y1, z1 = self._xyz
        dx, dy, dz = self._dxdydz
        x2, y2, z2 = (x1 + dx, y1 + dy, z1 + dz)

        xs, ys, zs = proj_transform((x1, x2), (y1, y2), (z1, z2), self.axes.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        
        return np.min(zs)

def plot_c3v_symmetry():
    """绘制C3v对称性示意图"""
    fig = plt.figure(figsize=(12, 5))
    
    # 左图：顶视图
    ax1 = fig.add_subplot(121)
    ax1.set_aspect('equal')
    ax1.set_title('$C_{3v}$ 对称性 - 顶视图', fontsize=14, fontweight='bold')
    
    # 绘制正三角形（分子骨架）
    angles = np.array([90, 210, 330]) * np.pi / 180
    radius = 1.0
    vertices = np.array([[radius * np.cos(a), radius * np.sin(a)] for a in angles])
    triangle = plt.Polygon(vertices, fill=False, edgecolor='black', linewidth=2)
    ax1.add_patch(triangle)
    
    # 绘制中心原子
    ax1.plot(0, 0, 'o', color='red', markersize=15, label='中心原子')
    
    # 绘制外围原子
    for i, v in enumerate(vertices):
        ax1.plot(v[0], v[1], 'o', color='blue', markersize=12)
    
    # 绘制C3旋转轴（中心点）
    ax1.plot(0, 0, 'x', color='green', markersize=15, markeredgewidth=3, label='$C_3$轴 (⊙)')
    
    # 绘制3个镜面 (σv)
    for i, angle in enumerate(angles):
        # 镜面沿着从中心穿过每个顶点的线
        x_mirror = [0, 1.5 * np.cos(angle)]
        y_mirror = [0, 1.5 * np.sin(angle)]
        ax1.plot(x_mirror, y_mirror, '--', color='purple', linewidth=2, 
                label='镜面 $\sigma_v$' if i == 0 else '')
        
        # 在镜面上标注
        label_x = 1.3 * np.cos(angle)
        label_y = 1.3 * np.sin(angle)
        ax1.text(label_x, label_y, f'$\sigma_v${i+1}', fontsize=10, color='purple', 
                ha='center', va='center', weight='bold')
    
    ax1.set_xlim(-1.8, 1.8)
    ax1.set_ylim(-1.8, 1.8)
    ax1.grid(True, alpha=0.3)
    ax1.legend(loc='upper right')
    ax1.set_xlabel('x', fontsize=11)
    ax1.set_ylabel('y', fontsize=11)
    
    # 右图：3D视图
    ax2 = fig.add_subplot(122, projection='3d')
    ax2.set_title('$C_{3v}$ 对称性 - 3D视图', fontsize=14, fontweight='bold')
    
    # 绘制三角锥形分子
    z_center = 0.8
    z_base = 0
    
    # 中心原子
    ax2.scatter([0], [0], [z_center], c='red', s=200, label='顶端原子')
    
    # 底部原子
    for v in vertices:
        ax2.scatter([v[0]], [v[1]], [z_base], c='blue', s=150)
    
    # 连接线
    for v in vertices:
        ax2.plot([0, v[0]], [0, v[1]], [z_center, z_base], 'k-', linewidth=1.5)
    
    # C3轴
    ax2.plot([0, 0], [0, 0], [-0.5, 1.2], 'g-', linewidth=3, label='$C_3$轴')
    arrow = Arrow3D(0, 0, 1.2, 0, 0, 0.3, mutation_scale=20, 
                   lw=2, arrowstyle='-|>', color='green')
    ax2.add_artist(arrow)
    
    # 绘制镜面
    for i, angle in enumerate(angles):
        x_plane = [0, 1.5 * np.cos(angle), 0]
        y_plane = [0, 1.5 * np.sin(angle), 0]
        z_plane = [-0.3, 0, 1.1]
        ax2.plot(x_plane, y_plane, z_plane, '--', color='purple', 
                linewidth=2, alpha=0.7, label='镜面 $\sigma_v$' if i == 0 else '')
    
    ax2.set_xlim(-1.5, 1.5)
    ax2.set_ylim(-1.5, 1.5)
    ax2.set_zlim(-0.5, 1.5)
    ax2.set_xlabel('x', fontsize=10)
    ax2.set_ylabel('y', fontsize=10)
    ax2.set_zlabel('z', fontsize=10)
    ax2.legend()
    
    plt.tight_layout()
    return fig

def plot_d3v_symmetry():
    """绘制D3v 对称性示意图"""
    fig = plt.figure(figsize=(12, 5))
    
    # 左图：顶视图
    ax1 = fig.add_subplot(121)
    ax1.set_aspect('equal')
    ax1.set_title('$D_{3v}$ 对称性 - 顶视图', fontsize=14, fontweight='bold')
    
    # 绘制正三角形
    angles = np.array([90, 210, 330]) * np.pi / 180
    radius = 1.0
    vertices = np.array([[radius * np.cos(a), radius * np.sin(a)] for a in angles])
    triangle = plt.Polygon(vertices, fill=False, edgecolor='black', linewidth=2)
    ax1.add_patch(triangle)
    
    # 绘制中心原子
    ax1.plot(0, 0, 'o', color='red', markersize=15, label='中心')
    
    # 绘制外围原子
    for i, v in enumerate(vertices):
        ax1.plot(v[0], v[1], 'o', color='blue', markersize=12)
    
    # C3旋转轴（中心）
    ax1.plot(0, 0, 'x', color='green', markersize=15, markeredgewidth=3, label='$C_3$轴 (⊙)')
    
    # 绘制3个σv镜面（穿过顶点）
    for i, angle in enumerate(angles):
        x_mirror = [0, 1.5 * np.cos(angle)]
        y_mirror = [0, 1.5 * np.sin(angle)]
        ax1.plot(x_mirror, y_mirror, '--', color='purple', linewidth=2,
                label='$\sigma_v$ 镜面' if i == 0 else '')
        label_x = 1.35 * np.cos(angle)
        label_y = 1.35 * np.sin(angle)
        ax1.text(label_x, label_y, f'$\sigma_v${i+1}', fontsize=10, color='purple',
                ha='center', va='center', weight='bold')
    
    # 绘制3个C2轴（穿过顶点/赤道原子）
    # 对于三角双锥，C2轴穿过赤道上的原子
    for i, angle in enumerate(angles):
        x_c2 = [0, 1.6 * np.cos(angle)]
        y_c2 = [0, 1.6 * np.sin(angle)]
        ax1.plot(x_c2, y_c2, ':', color='orange', linewidth=2.5,
                label='$C_2$轴' if i == 0 else '')
        # 标记C2轴
        label_x = 1.65 * np.cos(angle)
        label_y = 1.65 * np.sin(angle)
        ax1.plot(label_x, label_y, 's', color='orange', markersize=8)
    
    ax1.set_xlim(-1.8, 1.8)
    ax1.set_ylim(-1.8, 1.8)
    ax1.grid(True, alpha=0.3)
    ax1.legend(loc='upper right', fontsize=9)
    ax1.set_xlabel('x', fontsize=11)
    ax1.set_ylabel('y', fontsize=11)
    
    # 右图：3D视图
    ax2 = fig.add_subplot(122, projection='3d')
    ax2.set_title('$D_{3v}$ 对称性 - 3D视图', fontsize=14, fontweight='bold')
    
    # 绘制三角双锥形分子
    z_top = 1.2
    z_mid = 0
    z_bottom = -1.2
    
    # 顶端和底端原子
    ax2.scatter([0], [0], [z_top], c='green', s=200, label='轴向原子')
    ax2.scatter([0], [0], [z_bottom], c='green', s=200)
    
    # 中心原子（可选）
    ax2.scatter([0], [0], [z_mid], c='red', s=180, label='中心原子')
    
    # 赤道平面原子
    for v in vertices:
        ax2.scatter([v[0]], [v[1]], [z_mid], c='blue', s=150, label='赤道原子' if v is vertices[0] else '')
    
    # 连接线
    for v in vertices:
        ax2.plot([0, v[0]], [0, v[1]], [z_mid, z_mid], 'k-', linewidth=1.5)
        ax2.plot([0, v[0]], [0, v[1]], [z_top, z_mid], 'k-', linewidth=1.2, alpha=0.6)
        ax2.plot([0, v[0]], [0, v[1]], [z_bottom, z_mid], 'k-', linewidth=1.2, alpha=0.6)
    
    # C3主轴
    ax2.plot([0, 0], [0, 0], [-1.5, 1.5], 'g-', linewidth=3, label='$C_3$主轴')
    
    # 垂直镜面（穿过 C3 轴和赤道原子）
    for i, angle in enumerate(angles):
        x_plane = [0, 1.5 * np.cos(angle), 0]
        y_plane = [0, 1.5 * np.sin(angle), 0]
        z_plane_vert = [-1.4, 0, 1.4]
        ax2.plot(x_plane, y_plane, z_plane_vert, '--', color='purple',
                linewidth=2, alpha=0.7, label='$\sigma_v$ 镜面' if i == 0 else '')
    
    # C2轴
    for i, angle in enumerate(angles):
        x_c2 = [-1.5 * np.cos(angle), 1.5 * np.cos(angle)]
        y_c2 = [-1.5 * np.sin(angle), 1.5 * np.sin(angle)]
        z_c2 = [0, 0]
        ax2.plot(x_c2, y_c2, z_c2, ':', color='orange', linewidth=2.5,
                label='$C_2$轴' if i == 0 else '')
    
    ax2.set_xlim(-1.5, 1.5)
    ax2.set_ylim(-1.5, 1.5)
    ax2.set_zlim(-1.5, 1.5)
    ax2.set_xlabel('x', fontsize=10)
    ax2.set_ylabel('y', fontsize=10)
    ax2.set_zlabel('z', fontsize=10)
    ax2.legend(fontsize=8, loc='upper left')
    
    plt.tight_layout()
    return fig

def main():
    """主函数：生成所有对称性示意图"""
    # 设置中文字体
    plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'Arial Unicode MS']
    plt.rcParams['axes.unicode_minus'] = False
    
    # 绘制C3v对称性
    print("正在生成 C3v 对称性示意图...")
    fig1 = plot_c3v_symmetry()
    fig1.savefig('C3v_symmetry.png', dpi=300, bbox_inches='tight')
    print("C3v 对称性示意图已保存为 C3v_symmetry.png")
    
    # 绘制D3v 对称性
    print("\n正在生成 D3v 对称性示意图...")
    fig2 = plot_d3v_symmetry()
    fig2.savefig('D3v_symmetry.png', dpi=300, bbox_inches='tight')
    print("D3v 对称性示意图已保存为 D3v_symmetry.png")
    
    # 显示图形
    plt.show()
    
    print("\n对称性元素说明:")
    print("C3v 点群: C3旋转轴 + 3个σv镜面")
    print("  - 例子: NH3, CHCl3")
    print("\nD3v 点群: C3主轴 + 3个C2轴 + 3个σv镜面")
    print("  - 例子: PCl5（三角双锥），乙烷交叉式构象")

if __name__ == "__main__":
    main()
