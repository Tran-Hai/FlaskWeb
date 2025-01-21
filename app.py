from flask import Flask, render_template
from GenerateGraph import create_pie_chart
from DataCrawler import crawl_data
from DataAnalysis import data_analysis

app = Flask(__name__)

@app.route('/')
def home():
    dataset = crawl_data()

    dataframe = data_analysis(dataset)

    fig1 = create_pie_chart(dataframe['LK đồng bộ'], "MaLinhKien.csv")
    plot_div1 = fig1.to_html(full_html=False)

    fig2 = create_pie_chart(dataframe['LK không thể tháo rời'], "MaLinhKien.csv")
    plot_div2 = fig2.to_html(full_html=False)

    fig3 = create_pie_chart(dataframe['Mã hiện tượng'], "MaHienTuong.csv")
    plot_div3 = fig3.to_html(full_html=False)

    fig4 = create_pie_chart(dataframe['Mã nguyên nhân'], "MaNguyenNhan.csv")
    plot_div4 = fig4.to_html(full_html=False)

    fig5 = create_pie_chart(dataframe['Mã nguyên nhân gốc'], "MaNguyenNhanGoc.csv")
    plot_div5 = fig5.to_html(full_html=False)

    return render_template("home.html", plot_div1 = plot_div1, plot_div2 = plot_div2, plot_div3 = plot_div3, plot_div4 = plot_div4, plot_div5 = plot_div5)

if __name__ == '__main__':
    app.run(debug=True)