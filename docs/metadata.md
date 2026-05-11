# 混凝土养护温度模拟数据集 - 数据元说明

## 1. 主数据文件：data/temperature_data.csv

| 字段名 | 类型 | 单位 | 说明 |
|-------|------|------|------|
| timestamp | int64 | 秒 | Unix 时间戳，从 2024-11-30 至 2025-11-30，采样频率为 1 小时 |
| value | float64 | ℃ | 混凝土养护温度，含自然波动、季节变化、日内变化及人工注入异常 |

---

## 2. 异常标注文件：data/anomalies.csv

| 字段名 | 类型 | 单位 | 说明 |
|-------|------|------|------|
| start | int64 | 秒 | 异常开始时间戳 |
| end | int64 | 秒 | 异常结束时间戳 |
| type | string | - | 异常类型：collective_high / collective_low |

---

## 3. 数据说明
- 数据长度：1 年，每小时 1 条，共 8761 条记录
- 异常比例：约 2% 数据点为集体异常
- 异常类型：持续高温异常、持续低温异常
- 异常时长：随机 1～3 天
- 温度范围：正常 10～25℃，异常 ±8～12℃
- 适用场景：时间序列异常检测、混凝土养护监测、工业时序数据分析

---

## 4. 项目结构

```
.
├── src/
│   ├── generators/
│   │   └── temperature_simulator.py  # 数据生成主程序
│   ├── utils/
│   └── visualization/
├── data/
│   ├── temperature_data.csv  # 主数据文件
│   └── anomalies.csv         # 异常标注文件
├── docs/
│   └── metadata.md           # 本文档
├── results/
├── tests/
├── config/
├── requirements.txt          # Python依赖包
├── setup.py                  # 包安装配置
└── .gitignore               # Git忽略文件配置
```

---

## 5. 使用方法

### 安装依赖
```bash
pip install -r requirements.txt
```

### 运行数据生成
```bash
python src/generators/temperature_simulator.py
```

### 安装为包
```bash
pip install -e .
```

### 使用命令行工具
```bash
concrete-temp-sim
```