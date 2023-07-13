
import plotly.graph_objects as go
import csv

x = []
y = []
z = []
x2 = []
y2 = []
z2 = []
with open('CA-Sample-cnt40.data', 'r') as fp:
    data = csv.reader(fp)
    next(data)
    next(data)
    next(data)
    for row in data:
        num = float(row[0].split(";")[1])
        x.append(num)
        y.append(float(row[1]))
        z.append(float(row[2]))
        x2.append(float(row[3]))
        y2.append(float(row[4]))
        z2.append(float(row[5]))

print(x)
print(y)
print(z)


# 创建3D折线图
fig = go.Figure()

fig.add_trace(go.Scatter3d(
    x=x,
    y=y,
    z=z,
    mode='markers',
    name="setpoint"
))

fig.add_trace(go.Scatter3d(
    x=x2,
    y=y2,
    z=z2,
    mode='markers',
    name="here"
))
# 设置图表布局
# fig.update_layout(scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z'))
# 设置相机视角
ce = max(max(x), max(y), max(z), max(x2), max(y2), max(z2) )
print(ce)
range = [0, 1500]
fig.update_layout(scene=dict(
    xaxis_range=range,
    yaxis_range=range,
    zaxis_range=range
))
fig.show()