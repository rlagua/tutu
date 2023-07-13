import plotly.graph_objects as go


class Draw3D:
    def __init__(self) -> None:
        # 创建3D折线图
        self.fig = go.Figure()

    def add_lines(self, lines):
        keys = lines.keys()
        xyz = ["var.group[0].here[0]",
               "var.group[0].here[1]", "var.group[0].here[2]"]
        i = 0
        for item in xyz:
            if not item in keys:
                print("无犯规点")
            else:
                i += 1
        if i == 3:
            self.fig.add_trace(go.Scatter3d(
                x=lines[xyz[0]],
                y=lines[xyz[1]],
                z=lines[xyz[2]],
                mode='lines',
                name="here"
            ))

        xyz2 = ["var.group[0].setpoint[0]",
                "var.group[0].setpoint[1]", "var.group[0].setpoint[2]"]
        keys = lines.keys()
        i = 0
        for item in xyz2:
            if not item in keys:
                print("无setpoint")
                print(item)
            else:
                i += 1
        if i == 3:
            self.fig.add_trace(go.Scatter3d(
                x=lines[xyz2[0]],
                y=lines[xyz2[1]],
                z=lines[xyz2[2]],
                mode='lines',
                name="setpoint"
            ))

    def set_range(self):
        self.fig.update_layout(scene=dict(
            xaxis_range=[-1500, 1500],
            yaxis_range=[-1500, 1500],
            zaxis_range=[-1500, 1500]
        ))

    def show(self):
        self.set_range()
        self.fig.show()

    def save(self):
        self.fig.to_html("1111111")
