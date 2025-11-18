import plotly.graph_objects as go

fig = go.Figure(data=[go.Sankey(
    arrangement = "snap",
    node = dict(
        pad = 30,
        thickness = 40,
        line = dict(color = "black", width = 1),
        label = [
            "Hot Springs School District<br>State Foundation Funding<br>(2024-25 • 82% poverty district)",
            "49 EFA Students Leave",
            "St. John Catholic School (Hot Springs)<br>38 students • $131,334",
            "Calvary Christian Academy (Hot Springs)<br>11 students • $29,812",
            "Direct Public Funding Loss<br>$161,146",
            "Amplified Budget Damage<br>(fixed costs, desegregation payments, etc.)<br>estimated $240K–$320K total hole"
        ],
        color = [
            "#2c7bb6",   # HSSD (blue)
            "#fdae61",   # leaving students (orange)
            "#1b9e77",   # St. John (green)
            "#1b9e77",   # Calvary (green)
            "#d7191c",   # direct loss (red)
            "#7f0000"    # amplified damage (dark red)
        ]
    ),
    link = dict(
        source = [0, 1, 1, 0, 0],  # from HSSD → students → schools, and HSSD → losses
        target = [1, 2, 3, 4, 5],
        value  = [161146, 131334, 29812, 161146, 120000],  # last one is illustrative midpoint of extra damage
        label  = ["Students exit", "$131,334", "$29,812", "Direct loss", "~$120K extra damage (est.)"],
        color = ["#fdae6188", "#1b9e7788", "#1b9e7788", "#d7191c99", "#7f000088"]
    ))])

fig.update_layout(
    title_text="<b>Arkansas Education Freedom Accounts (2024-25)<br>Hot Springs School District → Religious Private Schools<br>Direct public funding diverted: $161,146 over 49 students</b>",
    font_size=14,
    height=700
)

fig.show()  # or fig.write_html("hssd_efa_drain.html") to save
