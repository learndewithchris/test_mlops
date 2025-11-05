from fastapi import FastAPI

# initialize app
app = FastAPI()

@app.get("/")
async def home():
    return {"data":"ML Model Prediction"}



# LEts create a get request endpooint

@pp.get("/features/")
def get_items():
    return {"item"}
# run app with --> uvicorn app:app --reload