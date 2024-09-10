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

def knn_api(l, w, n=5, url="http://localhost:8002/fish"):
    headers = {
        'accept': 'application/json',
    }
    
    params = {
        'length': l,
        'weight': w,
        'neighbors': n,
    }

    response = requests.get(url, params=params, headers=headers)
    j = response.json()
    r = j.get("prediction")
    #print(response)
    #print(j)
    #print(r)
    
    return r


def predict():
    length = float(input("물고기의 길이를 입력하세요: "))

    ## weight 예측 선형회귀 API 호출
    weight = lr_api(length)

    ## 물고기 분류 API 호출
    fish_class = knn_api(length, weight)

    print(f"길이:{length}의 물고기는 {weight}무게로 예측되며 종류는 {fish_class}입니다")

    
