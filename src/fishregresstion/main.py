from typing import Union
from fastapi import FastAPI
import pickle
from fishregresstion.model.manager import get_model_path
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/lr_fish")
def fish(length: float):
    """
    물고기의 종류 판별기

    Args:
        length (float): 물고기 길이(cm)
        weight (float): 물고기 무게(g)

    Returns:
        dict: 물고기 종류를 담은 딕셔너리
    """
    ### 모델 불러오기럼
#    with open(get_model_path(), "rb") as f:
#        fish_model = pickle.load(f)

    model_path = f"{os.path.dirname(get_model_path())}/lr_model.pkl"
    print(model_path)

    with open(model_path, "rb") as f:
        fish_model = pickle.load(f)

    weight = fish_model.predict([[length ** 2, length]])[0]

    return {
                "weight": weight
            }
