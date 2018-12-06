from urllib import request
import xml.etree.ElementTree as ET

parse_function_mapping = {
    ""
}


def parse():
    key = open('secretKey', 'r').readline()  # github 업로드를 위해 시크릿키 파일을 분리했습니다.
    route_id = 100100185  # 1711 고유 아이디

    # 국민대학교 정류장 고유번호 : 08110

    url = 'http://ws.bus.go.kr/api/rest/arrive/getArrInfoByRouteAll?'
    param = "ServiceKey=" + key + "&busRouteId=" + str(route_id)

    with request.urlopen(url + param) as req:
        response_body = req.read().decode('utf-8')
        root = ET.fromstring(response_body)

        # f = open('sampleDb.db', 'w')
        # f.write(response_body)
        # f.close() 추후 DB 입출력을 위해 임시 주석처리

    for i in root[2]:  # root[2]는 <msgBody>를 의미
        yield i.findtext('stNm')  # i는 itemList, 각 itemList 에서 stNm 값 가져오기


if __name__ == "__main__":
    for i in parse():
        print(i)
