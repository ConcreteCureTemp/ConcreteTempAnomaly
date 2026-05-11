# Concrete Curing Temperature Synthetic Dataset

[English](#english) | [中文](#中文)

<div id="english"></div>

## English

A parameter-driven synthetic time-series dataset for concrete curing temperature. All data is algorithmically simulated and artificially generated, not real-scene measured data, with full simulation code and labeled collective anomalies for time series anomaly detection research.

### 🌟 Features

- **Fully Synthetic**: All temperature data is algorithmically generated based on concrete curing physics models
- **Parameter-Driven**: Configurable parameters allow generation of diverse curing scenarios
- **Labeled Anomalies**: Includes various types of time series anomalies with ground truth labels
- **Research-Ready**: Designed specifically for time series anomaly detection algorithm development and evaluation
- **Open Source**: Complete simulation code provided for transparency and reproducibility

### 📊 Dataset Overview

This dataset simulates concrete curing temperature profiles under various conditions:

- **Normal Curing**: Standard temperature progression following concrete hydration kinetics
- **Anomalous Patterns**: Systematic anomalies including:
  - Temperature spikes (equipment malfunctions)
  - Cooling interruptions (environmental disturbances)
  - Sensor drift (measurement errors)
  - Collective anomalies (multiple correlated sensors)

### 🚀 Quick Start

```bash
# Clone the repository
git clone <your-repo-url>
cd concrete-curing-synthetic-dataset

# Install dependencies
pip install -r requirements.txt

# Generate synthetic dataset
python src/generators/main_generator.py --config config/default_config.json

# Visualize sample data
python src/visualization/plot_samples.py --data data/temperature_data.csv
```

### 📁 Project Structure

```
├── config/                 # Configuration files for dataset generation
├── data/                   # Generated synthetic datasets
│   ├── temperature_data.csv     # Main temperature time series
│   └── anomalies.csv           # Anomaly labels and metadata
├── docs/                   # Documentation and metadata
├── src/                    # Source code
│   ├── generators/         # Data generation algorithms
│   ├── utils/              # Utility functions
│   └── visualization/      # Data visualization tools
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

### 📈 Data Format

**temperature_data.csv**:
| timestamp | sensor_1 | sensor_2 | ... | sensor_n |
|-----------|----------|----------|-----|----------|
| 2023-01-01 00:00:00 | 20.5 | 20.3 | ... | 20.7 |

**anomalies.csv**:
| timestamp | sensor_id | anomaly_type | severity | description |
|-----------|-----------|--------------|----------|-------------|
| 2023-01-02 12:30:00 | sensor_3 | spike | high | Equipment malfunction |

### 🔬 Research Applications

- Time series anomaly detection algorithm development
- Concrete curing process modeling
- Sensor network fault detection
- Machine learning model training and validation

### 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div id="中文"></div>

## 中文

一个参数驱动的混凝土固化温度时间序列合成数据集。所有数据都是通过算法模拟和人工生成的，不是真实场景测量数据，包含完整的模拟代码和标注的集体异常，用于时间序列异常检测研究。

### 🌟 特点

- **完全合成**：所有温度数据基于混凝土固化物理模型算法生成
- **参数驱动**：可配置参数允许生成多样化的固化场景
- **标注异常**：包含各种类型的时序异常及真实标签
- **研究就绪**：专为时序异常检测算法开发和评估设计
- **开源透明**：提供完整模拟代码，确保透明性和可重现性

### 📊 数据集概述

该数据集模拟了各种条件下的混凝土固化温度曲线：

- **正常固化**：遵循混凝土水化动力学的标准温度进程
- **异常模式**：系统性异常包括：
  - 温度峰值（设备故障）
  - 冷却中断（环境干扰）
  - 传感器漂移（测量误差）
  - 集体异常（多个相关传感器）

### 🚀 快速开始

```bash
# 克隆仓库
git clone <你的仓库地址>
cd concrete-curing-synthetic-dataset

# 安装依赖
pip install -r requirements.txt

# 生成合成数据集
python src/generators/main_generator.py --config config/default_config.json

# 可视化样本数据
python src/visualization/plot_samples.py --data data/temperature_data.csv
```

### 📁 项目结构

```
├── config/                 # 数据集生成配置文件
├── data/                   # 生成的合成数据集
│   ├── temperature_data.csv     # 主要温度时间序列
│   └── anomalies.csv           # 异常标签和元数据
├── docs/                   # 文档和元数据
├── src/                    # 源代码
│   ├── generators/         # 数据生成算法
│   ├── utils/              # 工具函数
│   └── visualization/      # 数据可视化工具
├── requirements.txt        # Python依赖
└── README.md              # 本文件
```

### 📈 数据格式

**temperature_data.csv**:
| 时间戳 | 传感器1 | 传感器2 | ... | 传感器n |
|-----------|----------|----------|-----|----------|
| 2023-01-01 00:00:00 | 20.5 | 20.3 | ... | 20.7 |

**anomalies.csv**:
| 时间戳 | 传感器ID | 异常类型 | 严重程度 | 描述 |
|-----------|-----------|--------------|----------|-------------|
| 2023-01-02 12:30:00 | sensor_3 | spike | high | 设备故障 |

### 🔬 研究应用

- 时序异常检测算法开发
- 混凝土固化过程建模
- 传感器网络故障检测
- 机器学习模型训练和验证


### 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件。
