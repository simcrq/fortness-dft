"""
声子能带绘图脚本
从 band.yaml 文件读取数据并绘制声子能带图
"""
import yaml
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
from scipy.optimize import linear_sum_assignment

# 设置中文字体
rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'Arial']
rcParams['axes.unicode_minus'] = False


def read_band_yaml(filename='band.yaml'):
    """读取 band.yaml 文件"""
    with open(filename, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    return data


def extract_band_data(data, sort_bands=True):
    """
    从 yaml 数据中提取能带信息
    
    参数:
    -----
    data : dict
        从 band.yaml 读取的数据
    sort_bands : bool
        是否对能带进行排序以确保连续性（推荐True，避免能带交叉导致的尖点）
    """
    phonon = data['phonon']
    nband = len(phonon[0]['band'])  # 能带数量
    npoint = len(phonon)  # k点数量
    
    # 提取距离和频率
    distances = np.array([p['distance'] for p in phonon])
    frequencies = np.zeros((npoint, nband))
    
    for i, p in enumerate(phonon):
        for j, band in enumerate(p['band']):
            frequencies[i, j] = band['frequency']
    
    # 对能带进行排序，确保连续性
    if sort_bands:
        frequencies = sort_band_connection(frequencies)
    
    return distances, frequencies, nband


def sort_band_connection(frequencies):
    """
    对能带进行排序，确保能带的连续性
    使用左右导数相近的方法来匹配能带，确保能带平滑连接
    
    算法：
    1. 计算每个k点每条能带的左导数（与前一k点的差）
    2. 计算每个k点每条能带的右导数（与后一k点的差）
    3. 匹配时要求左右导数都相近，确保曲线平滑
    
    参数:
    -----
    frequencies : ndarray
        形状为 (npoint, nband) 的频率数组
    
    返回:
    -----
    sorted_frequencies : ndarray
        排序后的频率数组
    """
    npoint, nband = frequencies.shape
    sorted_freq = np.zeros_like(frequencies)
    sorted_freq[0, :] = np.sort(frequencies[0, :])  # 第一个k点按频率排序
    
    # 对于每个后续的k点，使用匈牙利算法找到最优匹配
    for i in range(1, npoint):
        current_bands = frequencies[i, :]
        previous_bands = sorted_freq[i-1, :]
        
        # 构建代价矩阵
        cost_matrix = np.zeros((nband, nband))
        
        for prev_idx in range(nband):
            for curr_idx in range(nband):
                # 左导数（从前一个点到当前点的斜率）
                left_slope = current_bands[curr_idx] - previous_bands[prev_idx]
                
                # 基础代价：频率差
                freq_cost = abs(left_slope)
                
                # 如果不是最后一个点，考虑右导数的连续性
                if i < npoint - 1:
                    next_bands = frequencies[i + 1, :]
                    
                    # 对于每个可能的next_bands，计算右导数
                    # 假设next点的能带顺序还未确定，考虑所有可能性中的最佳情况
                    min_derivative_cost = float('inf')
                    
                    for next_idx in range(nband):
                        # 右导数（从当前点到下一个点的斜率）
                        right_slope = next_bands[next_idx] - current_bands[curr_idx]
                        
                        # 导数连续性代价：左右斜率应该相近（曲线平滑）
                        derivative_cost = abs(left_slope - right_slope)
                        
                        if derivative_cost < min_derivative_cost:
                            min_derivative_cost = derivative_cost
                    
                    # 总代价 = 频率跳变 + 导数不连续性
                    # 权重可调：导数连续性更重要
                    cost_matrix[prev_idx, curr_idx] = freq_cost + 2.0 * min_derivative_cost
                else:
                    # 最后一个点只考虑频率差
                    cost_matrix[prev_idx, curr_idx] = freq_cost
        
        # 使用匈牙利算法求解最优分配
        row_ind, col_ind = linear_sum_assignment(cost_matrix)
        
        # 按照最优分配重新排列当前k点的能带
        for prev_idx, curr_idx in zip(row_ind, col_ind):
            sorted_freq[i, prev_idx] = current_bands[curr_idx]
    
    return sorted_freq


def get_high_symmetry_points(data):
    """获取高对称点位置和标签"""
    labels = data['labels']
    segment_nqpoint = data['segment_nqpoint']
    phonon = data['phonon']
    
    # 计算高对称点的位置
    positions = [0]  # 起始点
    point_labels = [labels[0][0]]  # 起始标签
    
    cumsum = 0
    for i, nq in enumerate(segment_nqpoint):
        cumsum += nq - 1
        positions.append(phonon[cumsum]['distance'])
        point_labels.append(labels[i][1])
    
    return positions, point_labels


def plot_bands(distances, frequencies, high_sym_pos, high_sym_labels, 
               bands_to_plot=None, color='red', linewidth=1.5, 
               figsize=(10, 6), ylim=None, title='Phonon Band Structure'):
    """
    绘制能带图
    
    参数:
    -----
    distances : array
        k点距离
    frequencies : array
        频率数据，形状为 (npoint, nband)
    high_sym_pos : list
        高对称点位置
    high_sym_labels : list
        高对称点标签
    bands_to_plot : list, optional
        要显示的能带索引列表（从0开始），None表示显示所有能带
    color : str
        能带颜色
    linewidth : float
        线宽
    figsize : tuple
        图形大小
    ylim : tuple, optional
        y轴范围 (ymin, ymax)
    title : str
        图标题
    """
    nband = frequencies.shape[1]
    
    # 如果未指定要绘制的能带，则绘制所有能带
    if bands_to_plot is None:
        bands_to_plot = list(range(nband))
    
    # 创建图形
    fig, ax = plt.subplots(figsize=figsize)
    
    # 绘制选定的能带
    for band_idx in bands_to_plot:
        if band_idx < nband:
            ax.plot(distances, frequencies[:, band_idx], 
                   color=color, linewidth=linewidth)
    
    # 添加高对称点的竖线
    for pos in high_sym_pos:
        ax.axvline(x=pos, color='gray', linestyle='--', linewidth=0.8, alpha=0.5)
    
    # 添加y=0的水平线
    ax.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
    
    # 设置x轴标签
    ax.set_xticks(high_sym_pos)
    ax.set_xticklabels(high_sym_labels)
    
    # 设置坐标轴标签
    ax.set_xlabel('Wave Vector', fontsize=12)
    ax.set_ylabel('Frequency (THz)', fontsize=12)
    ax.set_title(title, fontsize=14)
    
    # 设置x轴范围
    ax.set_xlim(distances[0], distances[-1])
    
    # 设置y轴范围
    if ylim is not None:
        ax.set_ylim(ylim)
    
    # 添加网格
    ax.grid(True, alpha=0.3, linestyle=':', linewidth=0.5)
    
    plt.tight_layout()
    
    return fig, ax


def main():
    """主函数"""
    # 读取数据
    print("正在读取 band.yaml 文件...")
    data = read_band_yaml('band.yaml')
    
    # ==================== 自定义区域 ====================
    # 是否对能带进行排序以确保连续性（避免尖点）
    # True: 能带会平滑连接（推荐）
    # False: 按 band.yaml 中的原始顺序（可能有尖点）
    sort_bands = True
    
    # 设置要显示的能带（从0开始编号）
    # None 表示显示所有能带
    # 例如: [0, 1, 2] 表示只显示前3条能带（最低的3条）
    # 例如: [3, 4, 5] 表示只显示第4、5、6条能带
    bands_to_plot = [1,2,4,5]  # 显示所有能带
    # bands_to_plot = [0, 1, 2]  # 显示前3条能带
    # bands_to_plot = [3, 4, 5]  # 只显示第4、5、6条能带
    
    # 设置y轴范围（None为自动）
    ylim = (-5, 50)  # 或者 None
    
    # 设置颜色和线宽
    color = 'red'
    linewidth = 1.5
    # ===================================================
    
    # 提取能带数据
    distances, frequencies, nband = extract_band_data(data, sort_bands=sort_bands)
    print(f"能带数量: {nband}")
    print(f"k点数量: {len(distances)}")
    print(f"能带排序: {'已启用（平滑连接）' if sort_bands else '未启用（原始顺序）'}")
    
    # 获取高对称点
    high_sym_pos, high_sym_labels = get_high_symmetry_points(data)
    print(f"高对称点: {high_sym_labels}")
    
    # 绘制能带图
    print("正在绘制能带图...")
    fig, ax = plot_bands(
        distances, frequencies, 
        high_sym_pos, high_sym_labels,
        bands_to_plot=bands_to_plot,
        color=color,
        linewidth=linewidth,
        ylim=ylim,
        title='Phonon Band Structure'
    )
    
    # 保存图片
    output_file = 'phonon_band.png'
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"图片已保存至: {output_file}")
    
    # 显示图形
    plt.show()


if __name__ == '__main__':
    main()
