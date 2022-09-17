import webbrowser

# HTML 수정 함수
def write(name, desc):
  Element(name).element.innerText = desc

# 하단 버튼 링크 연결 함수
def button(*args):
  link = "https://www.naver.com/" # https:// 꼭 붙여야 연결됩니다!
  webbrowser.open(link)

# 배경 색깔 설정 함수
def background(color):
  for i in range(0, 2):
    write("g" + str(i), color[i])

def information(info):
  key = list(info.keys())
  for i in range(0, 4):
    write("a" + str(i), key[i])
    write("b" + str(i), info[key[i]])

# 배경 색깔 설정
colors = ["green", "black"]
background(colors)

# 이름과 설명, 버튼에 들어갈 글 설정
write("name", "노영재")
write("description", "내가 좋아하는 4가지")
write("button", "네이버")

# 상세설명에 들어갈 제목과 글 설정
informations = {
  "좋아하는 음식": "콩나물,라면",
  "좋아하는 체육": "배드민턴,피구",
  "좋아하는 게임": "발로란트,얼불춤 등",
  "좋아하는 영화": "명량,레디 플레이어 원"
}
information(informations)
