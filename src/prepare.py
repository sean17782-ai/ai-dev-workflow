#!/usr/bin/env python3
"""
数据准备脚本示例
"""

import os
import json


def main():
    os.makedirs("data/processed", exist_ok=True)
    os.makedirs("models", exist_ok=True)

    # 示例：生成处理后的数据
    print("数据准备完成")

    # 记录处理信息
    info = {
        "status": "success",
        "data_dir": "data/processed"
    }
    with open("metrics.json", "w") as f:
        json.dump(info, f, indent=2)


if __name__ == "__main__":
    main()
