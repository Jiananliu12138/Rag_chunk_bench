# download_model.py
from huggingface_hub import snapshot_download
import os

# 设置模型名称
model_name = "BAAI/bge-large-en-v1.5"

# 设置下载路径（可选，默认缓存到 ~/.cache/huggingface/）
local_dir = "./models/bge-large-en-v1.5"

print(f"开始下载模型: {model_name}")
print(f"保存路径: {local_dir}")

try:
    # 下载完整模型
    snapshot_download(
        repo_id=model_name,
        local_dir=local_dir,
        local_dir_use_symlinks=False,  # 使用实际文件而非符号链接
        resume_download=True,           # 支持断点续传
    )
    print(f"✅ 模型下载成功！保存在: {local_dir}")
except Exception as e:
    print(f"❌ 下载失败: {e}")