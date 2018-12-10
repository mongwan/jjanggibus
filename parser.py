import re
from urllib import request
import xml.etree.ElementTree as ET


def parse(route_id=100100185, function='getBusPos'):
    key = open('secretKey', 'r').readline()  # github 업로드를 위해 시크릿키 파일을 분리했습니다.
    # 국민대학교 정류장 고유번호 : 08110

    if function == 'getLowBusPos':  # plainNo
        url = 'http://ws.bus.go.kr/api/rest/buspos/getLowBusPosByRtid?'
    elif function == 'getBusPos':
        url = 'http://ws.bus.go.kr/api/rest/buspos/getBusPosByRtid?'
    elif function == 'getAll':
        url = 'http://ws.bus.go.kr/api/rest/arrive/getArrInfoByRouteAll?'
    else:
        url = ''
    param = "ServiceKey=" + key + "&busRouteId=" + str(route_id)

    with request.urlopen(url + param) as req:
        response_body = req.read().decode('utf-8')
        root = ET.fromstring(response_body)

        # f = open('sampleDb.db', 'w')
        # f.write(response_body)
        # f.close() 추후 DB 입출력을 위해 임시 주석처리

    for item in root[2]:  # root[2]는 <msgBody>를 의미
        yield item  # i는 itemList, 각 itemList 에서 stNm 값 가져오기


if __name__ == "__main__":
    bus_list = [(re.findall(r"\d+", i.findtext('plainNo'))[1], i.findtext('gpsX'), i.findtext('gpsY')) for i in parse()]

    for i in bus_list:
        print(i)
