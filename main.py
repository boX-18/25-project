import pandas as pd
import folium

# 1. 엑셀 파일 불러오기
df = pd.read_excel("GS25 점포정보_Sample.xlsx")

# 2. 서울시 지점만 필터링
df_seoul = df[df["주소"].str.startswith("서울")].copy()

# 3. 지도 중심 좌표 설정 (서울시청 기준)
seoul_center = [37.5665, 126.9780]
m = folium.Map(location=seoul_center, zoom_start=11)

# 4. 지도에 마커 추가
for _, row in df_seoul.iterrows():
    folium.Marker(
        location=[row["y좌표"], row["x좌표"]],
        popup=row["주소"],
        icon=folium.Icon(color="blue", icon="shopping-cart", prefix="fa")
    ).add_to(m)

# 5. HTML로 저장
m.save("gs25_seoul_map.html")
print("지도가 gs25_seoul_map.html 로 저장되었습니다.")
