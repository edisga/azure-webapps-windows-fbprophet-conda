#Prohet sample code was taken from here: https://facebook.github.io/prophet/docs/quick_start.html

from flask import Flask, render_template
import pandas as pd
from fbprophet import Prophet

app = Flask(__name__)

@app.route("/")
def hello():
    df = pd.read_csv('./examples/example_wp_log_peyton_manning.csv')
    df.head()
    m = Prophet()
    m.fit(df)
    future = m.make_future_dataframe(periods=365)
    future.tail()
    forecast = m.predict(future)
    data = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
    ret = data.to_json(orient='records', date_format='iso')
    return ret

if __name__ == "__main__":
    app.run()