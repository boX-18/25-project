import pandas as pd
import folium

# 1. CSV 파일 읽기 (파일 경로 예시)
df = pd.read_csv("convenience_stores_seoul.csv")
# 컬럼: brand, latitude, longitude

# 2. 서울 지도 생성
seoul_center = [37.5665, 126.9780]
m = folium.Map(location=seoul_center, zoom_start=11)

# 3. 브랜드별 색상 지정
color_map = {
    "GS25": "blue",
    "CU": "green",
    "SevenEleven": "red"
}

# 4. 마커 추가
for _, row in df.iterrows():
    brand = row['brand']
    lat, lon = row['latitude'], row['longitude']
    folium.CircleMarker(
        location=[lat, lon],
        radius=5,
        color=color_map.get(brand, "gray"),
        fill=True,
        fill_color=color_map.get(brand, "gray"),
        popup=f"{brand}: {lat:.4f}, {lon:.4f}"
    ).add_to(m)

# 5. 지도 저장
m.save("seoul_convenience_map.html")
print("HTML 파일 생성 완료: seoul_convenience_map.html")
