# Lgorithm
>L-point+algorithm for recommendation system (롯데 멤버스 빅데이터 경진대회 : 220620~0812)  
딥러닝 기반 협업필터링, 추천 알고리즘을 활용한 상품 추천 시스템을 pyqt5로 구현

## 🍁 Description

### Recommendation idea 💡
- 구매 경험이 많은 고객은 고객 개인의 경험을 기반으로 추천, 구매 경험이 없거나 적은 고객은 비슷한 고객의 구매 경험+ 본인의 경험을 기반으로 추천
- 사례를 극단적으로 분리하지 않고, 구매 경험에 따라 5개의 Case로 나누어, 추천 알고리즘의 비율을 조정한다  
  즉, N개의 상품을 추천할 때 각 추천알고리즘을 통해 추천할 상품 갯수를 조정

### Recommendation algorithms 
- Apriori(장바구니 알고리즘)
