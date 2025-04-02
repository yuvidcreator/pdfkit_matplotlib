import pdfkit
import os

def generate_pdf(data, chart_path, output_file):
    """Generate PDF from data and include doughnut chart"""
    
    # Ensure file paths are absolute
    chart_abs_path = os.path.abspath(chart_path)
    background_abs_path = os.path.abspath("static/background.webp")

    # background: url("file://{background_abs_path}")

    print(chart_path)

    html_content = f"""
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; background: url("file://{background_abs_path}") no-repeat center center; background-size: cover; }}
            .container {{ width: 80%; margin: auto; text-align: center; }}
            img {{ max-width: 400px; display: block; margin: 20px auto; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Excel Data Report</h1>
            <table border="1" style="width: 100%; text-align: center;">
                <tr><th>Category</th><th>Value</th></tr>
                {"".join(f"<tr><td>{k}</td><td>{v}</td></tr>" for k, v in data.items())}
            </table>
            <h2>Analysis Chart</h2>
            <img src="url("file://{chart_abs_path}")" alt="Doughnut Chart"/>
        </div>
    </body>
    </html>
    """

    options = {
        "quiet": "",
        "enable-local-file-access": "",  # ✅ Allows local file access
        "page-size": "A4",
        'encoding': 'UTF-8',
        "dpi": 300
    }

    pdfkit.from_string(html_content, output_file, options=options)
