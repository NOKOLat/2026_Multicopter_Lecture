import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# ===============================
# 円弧＋矢印を描く関数
# ===============================

def draw_rotation_arc(ax, axis='x', radius=0.6, angle=np.pi/2, color=None, label=None):

    t = np.linspace(0, angle, 100)

    if axis == 'x':
        x = np.zeros_like(t)
        y = radius * np.cos(t)
        z = radius * np.sin(t)
        arrow_dir = np.array([0, -np.sin(angle), np.cos(angle)])

    elif axis == 'y':
        x = radius * np.cos(t)
        y = np.zeros_like(t)
        z = radius * np.sin(t)
        arrow_dir = np.array([-np.sin(angle), 0, np.cos(angle)])

    elif axis == 'z':
        x = radius * np.cos(t)
        y = radius * np.sin(t)
        z = np.zeros_like(t)
        arrow_dir = np.array([-np.sin(angle), np.cos(angle), 0])

    # 円弧
    if color is None:
        ax.plot(x, y, z)
    else:
        ax.plot(x, y, z, color=color)

    # 矢印の終点
    if color is None:
        ax.quiver(
            x[-1], y[-1], z[-1],
            arrow_dir[0]*0.2,
            arrow_dir[1]*0.2,
            arrow_dir[2]*0.2
        )
    else:
        ax.quiver(
            x[-1], y[-1], z[-1],
            arrow_dir[0]*0.2,
            arrow_dir[1]*0.2,
            arrow_dir[2]*0.2,
            color=color
        )

    # ラベルをつける
    if label is not None:
        mid = len(t) // 2
        lx, ly, lz = x[mid], y[mid], z[mid]
        ax.text(lx, ly, lz, label, color=color if color else 'k')


# ===============================
# メイン描画関数
# ===============================

def plot_axes_with_rotations(save_path="../images/axes_rotation.png"):

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # 原点
    origin = np.array([0, 0, 0])

    # 座標軸（色を付ける）
    ax.quiver(*origin, 1, 0, 0, color='r')
    ax.quiver(*origin, 0, 1, 0, color='g')
    ax.quiver(*origin, 0, 0, 1, color='b')

    # ラベル
    ax.text(1.1, 0, 0, "X", color='r')
    ax.text(0, 1.1, 0, "Y", color='g')
    ax.text(0, 0, 1.1, "Z", color='b')

    # 回転円弧（対応する色とラベルを渡す）
    draw_rotation_arc(ax, 'x', color='r', label='roll (X)')
    draw_rotation_arc(ax, 'y', color='g', label='pitch (Y)')
    draw_rotation_arc(ax, 'z', color='b', label='yaw (Z)')

    # 表示範囲（負の領域を広げる）
    axis_limit = 1.5
    ax.set_xlim([-axis_limit, axis_limit])
    ax.set_ylim([-axis_limit, axis_limit])
    ax.set_zlim([-axis_limit, axis_limit])

    ax.set_box_aspect([1,1,1])
    ax.set_title("Right-Hand Rule Rotations")

    plt.savefig(save_path)
    plt.close()


if __name__ == "__main__":
    plot_axes_with_rotations()