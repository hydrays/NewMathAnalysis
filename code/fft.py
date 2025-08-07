import cv2
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False    # 正确显示负号

def fft_image_processing(image_path, cutoff_ratio=0.1):
    """
    图像傅里叶变换处理流程：
    1. 读取图像并转为灰度图
    2. 记录原始尺寸并调整到512x512
    3. 执行FFT变换
    4. 去除高频成分
    5. 执行逆FFT变换
    6. 恢复原始尺寸
    
    参数:
        image_path: 输入图像路径
        cutoff_ratio: 高频截止比例 (0-1)
    """
    # 1. 读取图像并转为灰度图
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"图像文件未找到: {image_path}")
    original_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 2. 记录原始尺寸并调整到512x512
    h, w = gray.shape
    resized = cv2.resize(gray, (512, 512), interpolation=cv2.INTER_AREA)
    
    # 3. 执行FFT变换
    f = np.fft.fft2(resized)
    fshift = np.fft.fftshift(f)
    
    # 4. 去除高频成分
    mask = np.zeros((512, 512), dtype=np.uint8)
    center_y, center_x = 256, 256
    cutoff_radius = int(256 * cutoff_ratio)
    cv2.circle(mask, (center_x, center_y), cutoff_radius, 1, -1)
    
    fshift_filtered = fshift * mask
    
    # 5. 执行逆FFT变换
    f_ishift = np.fft.ifftshift(fshift_filtered)
    img_back = np.fft.ifft2(f_ishift)
    processed = np.abs(img_back).clip(0, 255).astype(np.uint8)
    
    # 6. 恢复原始尺寸
    restored = cv2.resize(processed, (w, h), interpolation=cv2.INTER_CUBIC)
    
    # 可视化结果
    plt.figure(figsize=(15, 10))
    
    plt.subplot(221), plt.imshow(gray, cmap='gray'), plt.title('原始图像')
    plt.subplot(222), plt.imshow(resized, cmap='gray'), plt.title('512x512 灰度图')
    
    # 频谱可视化 (对数缩放)
    magnitude_spectrum = 20 * np.log(np.abs(fshift) + 1)
    plt.subplot(223), plt.imshow(magnitude_spectrum, cmap='gray')
    plt.title('原始频谱'), plt.colorbar()
    
    filtered_spectrum = 20 * np.log(np.abs(fshift_filtered) + 1)
    plt.subplot(224), plt.imshow(filtered_spectrum, cmap='gray')
    plt.title('滤波后频谱'), plt.colorbar()
    
    plt.tight_layout()
    plt.show()
    
    # 显示处理结果
    plt.figure(figsize=(12, 6))
    plt.subplot(122), plt.imshow(restored, cmap='gray'), plt.title('恢复尺寸后图像')
    
    # 原始图像与处理后图像对比
    plt.subplot(121)
    plt.imshow(gray, cmap='gray')
    # plt.imshow(restored, cmap='jet', alpha=0.4)
    plt.title('原始图像')
    
    plt.tight_layout()
    plt.show()
    
    return restored

# 使用示例
if __name__ == "__main__":
    processed_image = fft_image_processing('media/img/greek.png', cutoff_ratio=0.5)
    
    # 保存结果
    cv2.imwrite('processed_image.jpg', processed_image)