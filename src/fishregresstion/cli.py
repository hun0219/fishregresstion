import requests
import json

def lr_api(l, url="http://localhost:8001/lr_fish"):
    headers = {
        'accept': 'application/json',
    }

    params = {
        'length': l,
        #'weight': w,
    }

    response = requests.get(url, params=params, headers=headers)
    j = response.json()
    r = j.get("weight")

    return r

def knn_api(l, w, n_neighbors, url="http://localhost:8002/lr_fish"):
    headers = {
        'accept': 'application/json',
    }
    
    params = {
        'length': l,
        'weight': w,
        'n_neighbors': '5'
    }

    response = requests.get(url, params=params, headers=headers)
    j = response.json()
    r = j.get("prediction")

    return r


def predict():
    length = float(input("물고기의 무게를 입력하세요: "))

    ## weight 예측 선형회귀 API 호출
    weight = lr_api(length)

    ## 물고기 분류 API 호출
    fish_class = knn_api(length, weight)

    print(f"length:{length} 물고기는 weight:{weight}으로 예측되며 종류는 {fish_class}입니다")

    
