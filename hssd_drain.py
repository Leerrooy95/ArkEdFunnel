import plotly.graph_objects as go

# This makes the clean Sankey diagram showing exactly where the $161K went
fig = go.Figure(go.Sankey(
    arrangement='snap',
    node = dict(
        pad=25,
        thickness=30,
        line=dict(color="black", width=1),
        label=[
            "Hot Springs School District<br>State Foundation Funding<br>(2024-25 • 82% poverty)",
            "49 Students Exit via EFA",
            "St. John's Catholic School<br>Hot Springs<br>38 students → $131,334",
            "Calvary Christian Academy<br>Hot Springs<br>11 students → $29,812",
            "Direct Loss to HSSD<br>$161,146",
            "Amplified Budget Hole<br>(fixed costs + desegregation hit)<br>≈ $240K–$320K"
        ],
        color=["#2166ac", "#fdae6b", "#1b9e77", "#1b9e77", "#b2182b", "#67000d"]
    ),
    link = dict(
        source = [0, 1, 1, 0],
        target = [1, 2, 3, 4],
        value  = [161146, 131334, 29812, 161146],
        color = ["#fdae6b55", "#1b9e7788", "#1b9e7788", "#b2182b99"]
    )
))

fig.update_layout(
    title_text="<b>Arkansas LEARNS Act in Action (2024-25)<br>Hot Springs School District → Two Religious Private Schools<br>$161,146 real dollars diverted over 49 kids</b>",
    font_size=15,
    height=750,
    paper_bgcolor="white"
)

fig.write_image("hssd_efa_drain_exact.png")  # saves the PNG file
fig.show()  # shows it in your browser when you run the script
print("Graphic saved as hssd_efa_drain_exact.png — ready to post")
