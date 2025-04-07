import matplotlib
import matplotlib.pyplot as plt

def generate_doughnut_chart(data, filename="images/chart.webp"):
    """Generate and save a doughnut chart from Excel data."""
    
    if not data:
        raise ValueError("No data available for chart generation.")

    print("--------->", data)
    labels = list(data.keys())
    sizes = list(data.values())

    matplotlib.use('agg')
    fig, ax = plt.subplots(figsize=(4, 4), dpi=100)
    wedges, texts, autotexts = ax.pie(
        sizes, labels=labels, autopct="%1.1f%%", startangle=90,
        wedgeprops={"linewidth": 2, "edgecolor": "white"},
        pctdistance=0.85
    )

    for text in autotexts:
        text.set_color("white")

    ax.set_facecolor("white")
    ax.axis("equal")

    plt.savefig(filename, format="webp", pil_kwargs={"lossless": False})
    plt.close()

    return filename
