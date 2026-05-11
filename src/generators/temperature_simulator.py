import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import gridspec
import os
import sys

# 添加项目根目录到Python路径
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, project_root)

from pandas.plotting import register_matplotlib_converters

# 注册日期转换器以兼容 Pandas 与 Matplotlib
register_matplotlib_converters()

# 设置随机种子以确保结果可复现
np.random.seed(2025)


def convert_date_single(x):
    """将单个 Unix 时间戳转换为 datetime 对象"""
    return datetime.fromtimestamp(x)


def convert_date(timelist):
    """将 Unix 时间戳列表转换为 datetime 对象列表"""
    return [datetime.fromtimestamp(x) for x in timelist]


def plot(dfs, anomalies=[]):
    """
    绘制带异常区域标记的时间序列图。

    参数:
        dfs: DataFrame 或 DataFrame 列表，包含 'timestamp' 和 'value' 列
        anomalies: 异常区间列表，每个元素为包含 'start' 和 'end'（Unix 时间戳）的 DataFrame
    """
    if isinstance(dfs, pd.DataFrame):
        dfs = [dfs]
    if not isinstance(anomalies, list):
        anomalies = [anomalies]

    df = dfs[0]
    time = convert_date(df['timestamp'])
    months = mdates.MonthLocator()
    days = mdates.DayLocator()
    month_fmt = mdates.DateFormatter('%m-%d')

    fig = plt.figure(figsize=(30, 6))
    ax = fig.add_subplot(111)

    for df in dfs:
        plt.plot(time, df['value'].to_numpy())

    colors = ['red'] + ['green'] * (len(anomalies) - 1)
    for i, anomaly in enumerate(anomalies):
        if not isinstance(anomaly, list):
            anomaly = list(anomaly[['start', 'end']].itertuples(index=False))
        for _, anom in enumerate(anomaly):
            t1 = convert_date_single(anom[0])
            t2 = convert_date_single(anom[1])
            plt.axvspan(t1, t2, color=colors[i], alpha=0.2)

    plt.title('Concrete Curing Temperature Monitoring (with Anomalies)')
    plt.ylabel('Temperature (℃)')
    plt.xlabel('Time')
    plt.xticks(size=26)
    plt.yticks(size=26)
    plt.xlim([time[0], time[-1]])

    ax.xaxis.set_major_locator(months)
    ax.xaxis.set_major_formatter(month_fmt)
    ax.xaxis.set_minor_locator(days)

    plt.show()


def plot_rws(X, window=100, k=5, lim=1000):
    """
    绘制滚动窗口子序列（用于可视化局部模式）
    """
    shift = 75
    X = X[window:]
    t = range(len(X))
    colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

    num_figs = int(np.ceil(k / 5)) + 1
    fig = plt.figure(figsize=(15, num_figs * 2))

    j = 0
    ax = fig.add_subplot(num_figs, 5, j + 1)
    idx = t[j: window + j]
    ax.plot(idx, X[j], lw=2, color=colors[j])
    plt.title("Window %d" % j, size=16)
    plt.ylim([-1, 1])

    j = 1
    ax = fig.add_subplot(num_figs, 5, j + 1)
    idx = t[j: window + j]
    ax.plot(idx, X[j], lw=2, color=colors[j])
    ax.set_yticklabels([])
    plt.title("Window %d" % j, size=16)
    plt.ylim([-1, 1])

    for i in range(2, k):
        j = i * shift
        idx = t[j: window + j]
        ax = fig.add_subplot(num_figs, 5, i + 1)
        ax.plot(idx, X[j], lw=2, color=colors[i + 1])
        ax.set_yticklabels([])
        plt.title("Window %d" % j, size=16)
        plt.ylim([-1, 1])

    plt.tight_layout()
    plt.show()


# 定义时间范围：2024-11-30 至 2025-11-30
start_date = datetime(2024, 11, 30)
end_date = datetime(2025, 11, 30)
timestamps = pd.date_range(start=start_date, end=end_date, freq='h')  # 每小时一个点


def generate_natural_temperature(dates):
    """
    生成符合自然规律的混凝土养护温度（含季节性与日内波动）
    """
    day_of_year = dates.dayofyear
    base_temp = 15

    # 季节性变化（主周期 + 次周期）
    seasonal_variation = (
        6 * np.sin(2 * np.pi * (day_of_year - 125) / 365) +
        1 * np.sin(4 * np.pi * (day_of_year - 125) / 365)
    )

    # 日内变化（6点开始升温）
    hour_of_day = dates.hour
    daily_variation = 3 * np.sin(3 * np.pi * (hour_of_day - 6) / 24)

    return base_temp + seasonal_variation + daily_variation


# 生成两条独立但相似的温度序列（df 用于训练，da 用于测试+注入异常）
temperature1 = generate_natural_temperature(timestamps) + np.random.normal(0, 0.25, len(timestamps))
temperature2 = generate_natural_temperature(timestamps) + np.random.normal(0, 0.25, len(timestamps))

df = pd.DataFrame({'timestamp': timestamps, 'value': temperature1})
da = pd.DataFrame({'timestamp': timestamps, 'value': temperature2})

# 注入集体异常（Collective Anomalies）
num_points = len(da)
remaining_anomalies = int(0.02 * num_points)  # 总异常点数占比 2%
known_anomalies = []

while remaining_anomalies > 0:
    duration = np.random.randint(24, 72)  # 异常持续 1~3 天
    if duration > remaining_anomalies:
        duration = remaining_anomalies

    start_idx = np.random.randint(0, num_points - duration)
    end_idx = start_idx + duration

    anomaly_type = np.random.choice(['high', 'low'])
    anomaly_magnitude = np.random.uniform(8, 12)

    if anomaly_type == 'high':
        da.loc[start_idx:end_idx, 'value'] += anomaly_magnitude
    else:
        da.loc[start_idx:end_idx, 'value'] -= anomaly_magnitude

    known_anomalies.append({
        'start': da.iloc[start_idx]['timestamp'].timestamp(),
        'end': da.iloc[end_idx]['timestamp'].timestamp(),
        'type': f'collective_{anomaly_type}'
    })

    remaining_anomalies -= duration

# 整理已知异常记录
known_anomalies_df = pd.DataFrame(known_anomalies).sort_values('start').reset_index(drop=True)

# 转换时间戳为秒级整数（Orion 要求）
da['timestamp'] = da['timestamp'].astype(np.int64) // 10 ** 9
df['timestamp'] = df['timestamp'].astype(np.int64) // 10 ** 9
known_anomalies_df['start'] = known_anomalies_df['start'].astype(int)
known_anomalies_df['end'] = known_anomalies_df['end'].astype(int)

print("Temperature dataset sample:")
print(da.head())
print("\nKnown anomalies sample:")
print(known_anomalies_df.head())

# ===================== 保存数据到 CSV =====================
# 确保数据目录存在
os.makedirs("../../data", exist_ok=True)

da.to_csv("../../data/temperature_data.csv", index=False, encoding="utf-8-sig")
known_anomalies_df.to_csv("../../data/anomalies.csv", index=False, encoding="utf-8-sig")
print("\n✅ 数据已保存：data/temperature_data.csv + data/anomalies.csv")

# 数据可视化（三联图）
plt.style.use('seaborn-v0_8')
plt.figure(figsize=(15, 12))

# 添加 datetime 列用于绘图
da['datetime'] = pd.to_datetime(da['timestamp'], unit='s')

# (1) 全年温度趋势
plt.subplot(3, 1, 1)
plt.plot(da['datetime'].values, da['value'].values, color='blue', alpha=0.7)
plt.title('Hourly Temperature Time Series (2025)')
plt.ylabel('Temperature (℃)')
plt.grid(True, alpha=0.3)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())

# (2) 一周详细视图（2025年6月第一周）
sample_week = da[(da['datetime'] >= '2025-06-01') & (da['datetime'] < '2025-06-08')]
plt.subplot(3, 1, 2)
plt.plot(sample_week['datetime'].values, sample_week['value'].values, color='green')
plt.title('Detailed View: One Week in June')
plt.ylabel('Temperature (℃)')
plt.grid(True, alpha=0.3)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%a %H:%M'))

# (3) 异常区域高亮
plt.subplot(3, 1, 3)
plt.plot(da['datetime'].values, da['value'].values, color='blue', alpha=0.3, label='Normal')
for _, row in known_anomalies_df.iterrows():
    if row['type'].startswith('collective'):
        start = pd.to_datetime(row['start'], unit='s')
        end = pd.to_datetime(row['end'], unit='s')
        anomaly_data = da[(da['datetime'] >= start) & (da['datetime'] <= end)]
        color = 'orange' if 'high' in row['type'] else 'purple'
        plt.plot(anomaly_data['datetime'].values, anomaly_data['value'].values,
                 color=color, linewidth=2, label=f'Collective {row["type"].split("_")[1]}')

plt.title('Anomaly Detection')
plt.ylabel('Temperature (℃)')
plt.grid(True, alpha=0.3)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b'))

# 去重图例
handles, labels = plt.gca().get_legend_handles_labels()
by_label = dict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys())

plt.tight_layout()
plt.show()

# 调用自定义 plot 函数绘制带异常阴影的图
plot(da, known_anomalies_df)


def main():
    """主函数，用于命令行执行"""
    print("开始生成混凝土养护温度模拟数据...")
    print("数据已保存到 data/temperature_data.csv 和 data/anomalies.csv")
    print("可视化图表已显示")


if __name__ == "__main__":
    main()