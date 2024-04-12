# from flask import Flask, render_template
# import pandas as pd
# from pytrends.request import TrendReq
# import matplotlib.pyplot as plt
# from io import BytesIO
# import base64

# app = Flask(__name__)

# def get_trends_data():
#     trends = TrendReq()
#     trends.build_payload(kw_list=["DATA SCIENCE"])
#     data = trends.interest_by_region()
#     data = data.sort_values(by="DATA SCIENCE", ascending=False)
#     data = data.head(10)
#     return data

# def plot_trends(data):
#     plt.figure(figsize=(15, 12))
#     data.reset_index().plot(x="geoName", y="DATA SCIENCE", kind="bar")
#     plt.style.use('fivethirtyeight')
#     plt.tight_layout()
#     img = BytesIO()
#     plt.savefig(img, format='png')
#     img.seek(0)
#     graph_url = base64.b64encode(img.getvalue()).decode()
#     plt.close()
#     return 'data:image/png;base64,{}'.format(graph_url)

# @app.route('/')
# def index():
#     data = get_trends_data()
#     plot = plot_trends(data)
#     return render_template('index.html', plot=plot)

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request
import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

def get_trends_data(keyword):
    trends = TrendReq()
    trends.build_payload(kw_list=[keyword])
    data = trends.interest_by_region()
    data = data.sort_values(by=keyword, ascending=False)
    data = data.head(10)
    return data

def plot_trends(data, keyword):
    plt.figure(figsize=(15, 12))
    data.reset_index().plot(x="geoName", y=keyword, kind="bar")
    plt.style.use('fivethirtyeight')
    plt.tight_layout()
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return 'data:image/png;base64,{}'.format(graph_url)

@app.route('/', methods=['GET', 'POST'])
def index():
    keyword = None
    plot = None
    if request.method == 'POST':
        keyword = request.form['keyword']
        if keyword:
            data = get_trends_data(keyword)
            plot = plot_trends(data, keyword)
    return render_template('index.html', plot=plot, keyword=keyword)

if __name__ == '__main__':
    app.run(debug=True)

