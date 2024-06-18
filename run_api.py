from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/data")
def read_data():
    df = pd.read_csv('./output/products.csv')
    df = df.where(pd.notnull(df), None)     # Replace NaN with None
    return df.to_dict(orient='records')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)