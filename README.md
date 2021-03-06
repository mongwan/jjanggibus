# 짱기버스 넘무 좋아
"짱기버스 넘무 좋아"는 전기버스를 좋아하는 개발자가 개발하는 웹 기반 전기버스 위치 추적 서비스입니다.
2018년 11월 15일, 국민대학교 앞에 위치한 버스회사인 도원교통에서 수도권 최초로 1711번 버스에 전기버스를 도입했습니다.
하지만, 아직 모든 버스가 전기버스로 대차된 것은 아니고, 4대 정도의 전기버스만 운행되고 있습니다.
전기버스를 좋아하는 개발자가 등하교길에 이왕이면 전기버스를 타고 싶은 생각에 개발을 시작했습니다.

*data.go.kr에서 secretKey를 발급받아야 API를 이용할 수 있습니다!*

## 요구사항 명세
### 기능적 요구 사항
짱기버스 넘무 좋아의 웹사이트로 접속하면 아래와 같은 기능을 확인 할 수 있어야 합니다.
- 사용자는 다음 전기버스가 오기로 예상되는 시간을 확인할 수 있어야 합니다.
    - 전기버스가 규칙적으로 차고지에서 시발한다고 가정하고, 전기버스 간의 배차간격을 고려하여
    예상되는 다음 전기버스 출차 시간과 현재 시간의 차를 표시합니다.
    - 여기에 표시된 시간은 실시간으로 새로고침이 되어야합니다.
    - 서버의 예상 상황과 다르게, 전기버스가 시발하지 않았다면 그 상황을 사용자에게 표시해야 합니다.

- 사용자는 지도 상에서 전기버스의 위치를 확인할 수 있어야 합니다.
    - 지도 위에 1711의 전체 버스 위치 및 운행 경로를 표시하며, 전기버스는 특별한 아이콘으로
    표시하여 사용자가 전기버스의 위치를 쉽게 파악할 수 있도록 합니다.
    - 전기버스의 위치만 따로 파악할 수 있는 기능이 구현되어야 합니다.

- 사용자는 서버 내의 웹페이지에서 짱 좋은 전기버스를 홍보하는 컨텐츠를 볼 수 있어야 합니다.
    - 전기버스를 더 많은 사람들이 타보았으면 하는 개발자의 마음을 담아, 사이트 내에 전기버스를
    홍보하는 유튜브 영상 등을 임베드합니다. 
    
- 타 버스가 전기버스를 도입할 때를 대비하여, 다른 버스에도 유연하게 적용할 수 있게끔 재사용성을
보장해야 합니다.

### 인터페이스 요구 사항
- 짱기버스 넘무 좋아는 모바일, 데스크탑 등 웹을 표시할 수 있는 어느 환경에서도 사용 가능하게 개발되어야 합니다.
- 각 기능을 전환할 때 미려한 효과를 통해 사용자가 시각적 만족을 얻을 수 있어야 합니다.

### 비기능적 요구 사항
- 개발은 Python으로 진행되어야 합니다. 서버를 구현하기 위한 프레임워크는 Flask를 이용합니다.

## 소프트웨어 구조 설계

코드는 app.py, parser.py, templates/index.html로 이루어져 있습니다.
- Flask로 개발되어있고, 서버를 담당하는 app.py
- openAPI를 활용하여 실제로 데이터를 받아오는 메소드가 포함되어 있는 parser.py
- 웹 브라우저에 표시할 화면이 구현되어 있는 templates/index.html

우선 서버가 app.py에서 구동되면, parser.py의 parse 메소드를 호출합니다. parse 메소드는 인자에 따라 적절한 값을
openAPI에 요청하고, 그 값을 다시 적절하게 변환하여 app.py의 list로 전달합니다. 그 후 전달 받은 값을 바탕으로
flask에서 제공하는 메소드인 render_template를 통해 templates 폴더의 index를 호출하여 화면을 구현하게끔합니다.
사용자가 URL로 접속하면, render_template가 실행되어 화면을 구현합니다.

## 구현 설계

### app.py
- electric_bus_list : 전기버스인 버스의 차량 번호 목록입니다. 튜플로 구현됩니다.
- bus_list : parse()에서 받아온 차량번호 값, 좌표값을 [차량번호, X좌표, Y좌표] 순대로 리스트화합니다.

### parser.py
- key : data.go.kr에서 받은 비밀 키입니다. github업로드를 위해 별도 파일로 분리했습니다.
- url : REST API를 활용하기 위한 URL입니다. 기능에 따라 URL이 다르므로 각 기능에 따른 url이 mapping되어야 합니다.
- param : REST API를 활용하기 위한 파라미터입니다. 요청 파라미터는 동일한 것만 사용하므로, 따로 변수로 만듭니다.
- response_body : API에서 받아온 RAW한 xml body입니다.
- root : python에서 제공하는 xml 라이브러리인 elementtree를 사용하여 구현한 xml의 가장 상위를 가리키는 변수입니다.

### templates/index.py
Daum API를 사용했고, 그 API와 관련된 내용은 생략합니다.
- item : app.py에서 전달받은 bus_list의 개별 항목입니다. [차량번호, X좌표, Y좌표]순입니다.
- loop.index : flask의 template engine인 jinja에서 제공하는 변수로, 현재 루프 정도를 1부터 나타냅니다.

## 유닛 테스트
![img](https://i.imgur.com/N1itdUA.jpg)
parse.py의 기능만을 테스트했습니다. 차량번호와 좌표가 적절히 return 되는것을 확인 할 수 있습니다.

## 통합 테스트
[bus.noryangj.in](http://bus.noryangj.in)에서 지금 확인할 수 있습니다.