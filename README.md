# papagoKoRTT
papago를 이용한 한국어 Round-Trip-Translation REST API 입니다.
## Quick start
- `$ pip install -r requirement.txt`
- `/utils/` 폴더 안에 자신의 `OS`에 맞는 `chromedriver` 설치
   - `chrome` 버전 확인: `url`에 `chrome://version/`
   - 버전에 맞는 `chromedriver` 다운로드
   - 다운로드 링크: https://chromedriver.chromium.org/downloads
- `$ uvicorn main:app --reload`
