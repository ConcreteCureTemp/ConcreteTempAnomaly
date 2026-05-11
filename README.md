# Concrete Curing Temperature Synthetic Dataset

[English](#english) | [中文](#中文)

<div id="english"></div>

## English

A parameter-driven synthetic time-series dataset for concrete curing temperature monitoring. All data is algorithmically simulated and artificially generated, not real-scene measured data, with full simulation code and labeled collective anomalies for time series anomaly detection research.

### 🌟 Features

- **Fully Synthetic**: All temperature data is algorithmically generated based on concrete curing physics models
- **Realistic Patterns**: Incorporates seasonal variations, daily cycles, and natural temperature fluctuations
- **Labeled Collective Anomalies**: Includes systematic temperature deviations with precise start/end timestamps
- **Research-Ready**: Designed specifically for time series anomaly detection algorithm development and evaluation
- **Open Source**: Complete simulation code provided for transparency and reproducibility

### 📊 Dataset Overview

This dataset simulates concrete curing temperature profiles over a one-year period (2024-11-30 to 2025-11-30) with hourly sampling:

- **Data Volume**: 8,761 hourly temperature readings
- **Anomaly Rate**: ~2% of data points contain collective anomalies
- **Anomaly Types**: 
  - Collective high temperature anomalies (duration: 1-3 days)
  - Collective low temperature anomalies (duration: 1-3 days)
- **Temperature Range**: Normal 10-25°C, anomalies ±8-12°C deviation
- **Sampling Frequency**: 1 hour intervals

### 🚀 Quick Start

```bash
# Clone the repository
cd ConcreteTempAnomaly

# Install dependencies
pip install -r requirements.txt

# Generate new synthetic dataset
python src/generators/temperature_simulator.py

# Or install as a package and use command line tool
pip install -e .
concrete-temp-sim
```

### 📁 Project Structure

```
├── src/
│   ├── generators/
│   │   └── temperature_simulator.py  # Main data generation script
│   ├── utils/
│   └── visualization/
├── data/
│   ├── temperature_data.csv  # Main temperature time series (timestamp, value)
│   └── anomalies.csv         # Anomaly labels (start, end, type)
├── docs/
│   └── metadata.md           # Detailed data documentation
├── requirements.txt          # Python dependencies
├── setup.py                  # Package installation configuration
└── README.md                # This file
```

### 📈 Data Format

**temperature_data.csv**:
| timestamp | value |
|-----------|--------|
| 1732924800 | 11.174 |
| 1732928400 | 10.401 |

- **timestamp**: Unix timestamp in seconds (hourly intervals)
- **value**: Temperature in Celsius (°C)

**anomalies.csv**:
| start | end | type |
|-------|-----|------|
| 1741680000 | 1741759200 | collective_high |
| 1754294400 | 1754449200 | collective_low |

- **start**: Anomaly start timestamp (Unix seconds)
- **end**: Anomaly end timestamp (Unix seconds)  
- **type**: Anomaly classification (collective_high or collective_low)

### ⚙️ Configuration

The temperature simulator uses the following key parameters (modifiable in source code):

- **Time Range**: November 30, 2024 to November 30, 2025
- **Sampling**: 1-hour intervals
- **Temperature Model**: Base 15°C with seasonal and daily variations
- **Anomaly Injection**: 2% of data with 1-3 day duration anomalies
- **Noise Level**: ±0.25°C random noise for realism

### 🔬 Research Applications

- Time series anomaly detection algorithm development
- Concrete curing process monitoring systems
- Industrial IoT sensor network analysis
- Machine learning model training and validation
- Collective anomaly detection research

### 🛠️ Technical Details

The simulation incorporates:
- **Seasonal Variations**: Annual temperature cycles using sinusoidal functions
- **Daily Cycles**: Hourly temperature fluctuations based on time of day
- **Natural Noise**: Gaussian noise for realistic sensor measurements
- **Collective Anomalies**: Systematic temperature deviations lasting 24-72 hours
- **Physics-Based Modeling**: Temperature patterns based on concrete hydration kinetics

### 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div id="中文"></div>

## 中文

一个参数驱动的混凝土固化温度时间序列合成数据集。所有数据都是通过算法模拟和人工生成的，不是真实场景测量数据，包含完整的模拟代码和标注的集体异常，用于时间序列异常检测研究。

### 🌟 特点

- **完全合成**：所有温度数据基于混凝土固化物理模型算法生成
- **真实模式**：包含季节变化、日周期和自然温度波动
- **标注集体异常**：包含系统性温度偏差及精确的起止时间戳
- **研究就绪**：专为时序异常检测算法开发和评估设计
- **开源透明**：提供完整模拟代码，确保透明性和可重现性

### 📊 数据集概述

该数据集模拟了为期一年的混凝土固化温度曲线（2024-11-30 至 2025-11-30），每小时采样：

- **数据量**：8,761 个每小时温度读数
- **异常率**：约2%的数据点包含集体异常
- **异常类型**：
  - 集体高温异常（持续1-3天）
  - 集体低温异常（持续1-3天）
- **温度范围**：正常10-25°C，异常±8-12°C偏差
- **采样频率**：1小时间隔

### 🚀 快速开始

```bash
# 克隆仓库
cd ConcreteTempAnomaly

# 安装依赖
pip install -r requirements.txt

# 生成新的合成数据集
python src/generators/temperature_simulator.py

# 或安装为包并使用命令行工具
pip install -e .
concrete-temp-sim
```

### 📁 项目结构

```
├── src/
│   ├── generators/
│   │   └── temperature_simulator.py  # 主要数据生成脚本
│   ├── utils/
│   └── visualization/
├── data/
│   ├── temperature_data.csv  # 主要温度时间序列 (timestamp, value)
│   └── anomalies.csv         # 异常标签 (start, end, type)
├── docs/
│   └── metadata.md           # 详细数据文档
├── requirements.txt          # Python依赖
├── setup.py                  # 包安装配置
└── README.md                # 本文件
```

### 📈 数据格式

**temperature_data.csv**:
| 时间戳 | 数值 |
|-----------|--------|
| 1732924800 | 11.174 |
| 1732928400 | 10.401 |

- **timestamp**: Unix时间戳（秒级，小时间隔）
- **value**: 温度值（摄氏度°C）

**anomalies.csv**:
| 起始时间 | 结束时间 | 类型 |
|-------|-----|------|
| 1741680000 | 1741759200 | collective_high |
| 1754294400 | 1754449200 | collective_low |

- **start**: 异常开始时间戳（Unix秒）
- **end**: 异常结束时间戳（Unix秒）
- **type**: 异常分类（collective_high或collective_low）

### ⚙️ 配置

温度模拟器使用以下关键参数（可在源代码中修改）：

- **时间范围**：2024年11月30日至2025年11月30日
- **采样间隔**：1小时
- **温度模型**：基准15°C，含季节和日变化
- **异常注入**：2%数据量，持续1-3天的异常
- **噪声水平**：±0.25°C随机噪声增加真实感

### 🔬 研究应用

- 时序异常检测算法开发
- 混凝土固化过程监控系统
- 工业物联网传感器网络分析
- 机器学习模型训练和验证
- 集体异常检测研究

### 🛠️ 技术细节

模拟包含：
- **季节变化**：使用正弦函数模拟年度温度周期
- **日周期**：基于一天中时间的每小时温度波动
- **自然噪声**：高斯噪声模拟真实传感器测量
- **集体异常**：持续24-72小时的系统性温度偏差
- **基于物理的建模**：基于混凝土水化动力学的温度模式

### 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件。
