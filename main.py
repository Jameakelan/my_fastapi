from fastapi import FastAPI
import joblib

app = FastAPI()

model = joblib.load("./MLModels/svdpp_model.pkl")

@app.get("/")
async def rating_predict(uid, iid):

    """
    http:host/?uid=U0001&iid=M0001
    `uid` = User ID
    `iid` = Item ID

    """

    p_value = model.predict(uid, iid)

    return {"p_value" : p_value[3]}