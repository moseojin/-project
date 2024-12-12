from flask import Flask, render_template, request, jsonify
import requests

# Flask 애플리케이션 객체 생성
map = Flask(__name__)

# Kakao API 설정
KAKAO_API_KEY = "454f6c86927d93060303d47ccb6e2010"
KAKAO_GEOCODE_URL = "https://dapi.kakao.com/v2/local/search/address.json"

# 위치 데이터를 저장할 리스트
locations = []

# 홈 페이지 라우트
@map.route('/')
def home():
    return render_template('index.html')

# 지도 페이지 라우트
@map.route('/map')
def map_view():
    return render_template('map.html', locations=locations)

# 위치 추가 라우트
@map.route('/add_location', methods=['POST'])
def add_location():
    name = request.form.get('name')
    address = request.form.get('address')

    if not name or not address:
        return jsonify({'success': False, 'message': '이름과 주소를 입력해 주세요.'})

    try:
        # Kakao API로 주소를 좌표로 변환
        headers = {"Authorization": f"KakaoAK {KAKAO_API_KEY}"}
        params = {"query": address}
        response = requests.get(KAKAO_GEOCODE_URL, headers=headers, params=params, timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            if data['documents']:
                coords = data['documents'][0]
                latitude = coords['y']
                longitude = coords['x']

                # 데이터 저장
                locations.append({'name': name, 'address': address, 'latitude': latitude, 'longitude': longitude})
                return jsonify({'success': True, 'locations': locations})
            else:
                return jsonify({'success': False, 'message': '주소에 해당하는 좌표를 찾을 수 없습니다.'})
        else:
            return jsonify({'success': False, 'message': f'API 요청 실패: {response.status_code}'})

    except requests.exceptions.RequestException as e:
        return jsonify({'success': False, 'message': f'요청 처리 중 오류 발생: {str(e)}'})

# 위치 삭제 라우트
@map.route('/delete_location', methods=['POST'])
def delete_location():
    index = request.form.get('index', type=int)
    if index is not None and 0 <= index < len(locations):
        locations.pop(index)
        return jsonify({'success': True, 'locations': locations})
    return jsonify({'success': False, 'message': '잘못된 인덱스입니다.'})
