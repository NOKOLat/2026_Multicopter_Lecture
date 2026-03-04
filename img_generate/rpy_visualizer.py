import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# ===============================
# 回転行列（ZYX: yaw → pitch → roll）
# ===============================

def rotation_matrix(roll, pitch, yaw):
    Rx = np.array([
        [1, 0, 0],
        [0, np.cos(roll), -np.sin(roll)],
        [0, np.sin(roll),  np.cos(roll)]
    ])

    Ry = np.array([
        [ np.cos(pitch), 0, np.sin(pitch)],
        [0, 1, 0],
        [-np.sin(pitch), 0, np.cos(pitch)]
    ])

    Rz = np.array([
        [np.cos(yaw), -np.sin(yaw), 0],
        [np.sin(yaw),  np.cos(yaw), 0],
        [0, 0, 1]
    ])

    return Rz @ Ry @ Rx


# ===============================
# 3D描画
# ===============================

def plot_attitude(roll, pitch, yaw, save_path="attitude.png"):

    R = rotation_matrix(roll, pitch, yaw)

    # 基準座標軸
    origin = np.array([0, 0, 0])
    axes = np.eye(3)

    # 回転後座標軸
    rotated_axes = R @ axes

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # 元の座標軸
    ax.quiver(*origin, *axes[:,0])
    ax.quiver(*origin, *axes[:,1])
    ax.quiver(*origin, *axes[:,2])

    # 回転後座標軸
    ax.quiver(*origin, *rotated_axes[:,0])
    ax.quiver(*origin, *rotated_axes[:,1])
    ax.quiver(*origin, *rotated_axes[:,2])

    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    ax.set_title("Roll / Pitch / Yaw Visualization")

    plt.savefig(save_path)
    plt.close()


# ===============================
# 実行例
# ===============================

if __name__ == "__main__":

    # 度 → ラジアン変換
    roll  = np.deg2rad(30)
    pitch = np.deg2rad(20)
    yaw   = np.deg2rad(45)

    plot_attitude(roll, pitch, yaw)