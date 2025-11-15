import plotly.graph_objects as go

fig = go.Figure(go.Sankey(
    node = dict(
        label = ["HSSD Budget", "EFA Divert", "Private Schools", "Deseg Block"],
        color = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]
    ),
    link = dict(
        source = [0, 0, 1],
        target = [1, 2, 2],
        value = [161146, 161146, 161146 * 0.5]  # 50% blocked by deseg
    )
))

fig.update_layout(title_text="REAL: $161K Drained from HSSD (2024-25)", font_size=14)
fig.write_image("out/hssd_real_drain.png")
fig.show()
print("REAL GRAPH: out/hssd_real_drain.png")
