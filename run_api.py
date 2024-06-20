# Import FastAPI and pandas
from fastapi import FastAPI
import pandas as pd

app = FastAPI() # Initialize FastAPI app

# Define endpoint to read data from CSV file

@app.get("/data")
def read_data():
    df = pd.read_csv('./output/products.csv')
    df = df.where(pd.notnull(df), None)     # Replace NaN with None
    return df.to_dict(orient='records')

if __name__ == "__main__": # Run FastAPI app using Uvicorn
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)