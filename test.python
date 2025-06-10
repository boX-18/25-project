import folium

# 서울시 중심 좌표
seoul_center = [37.5665, 126.9780]

# 지도 생성
m = folium.Map(location=seoul_center, zoom_start=12)

# 편의점 위치 예시 데이터 (실제 데이터는 공공데이터 또는 크롤링 필요)
gs25_locations = [
    [37.5700, 126.9769, "GS25 종로점"],
    [37.5610, 126.9830, "GS25 명동점"],
]

cu_locations = [
    [37.5665, 126.9850, "CU 을지로점"],
    [37.5550, 126.9700, "CU 서울역점"],
]

seven_locations = [
    [37.5640, 126.9740, "세븐일레븐 시청점"],
    [37.5580, 126.9780, "세븐일레븐 충무로점"],
]

# 마커 추가 함수
def add_markers(locations, color):
    for lat, lon, name in locations:
        folium.Marker(
            location=[lat, lon],
            popup=name,
            icon=folium.Icon(color=color)
        ).add_to(m)

# 편의점 별로 마커 추가
add_markers(gs25_locations, "blue")
add_markers(cu_locations, "green")
add_markers(seven_locations, "red")

# 지도 저장
m.save("seoul_convenience_stores.html")
print("지도가 seoul_convenience_stores.html 로 저장되었습니다.")
