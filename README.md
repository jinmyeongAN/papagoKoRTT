# đŚ papagoKoRTT đŚ
`papago`ëĽź ě´ěŠí íęľ­ě´ `Round-Trip-Translation` `REST API` ěëë¤.
## Quick start
- `$ pip install -r requirement.txt`
- `/utils/` í´ë ěě ěě ě `OS`ě ë§ë `chromedriver` ě¤ěš
   - `chrome` ë˛ě  íě¸: `url`ě `chrome://version/`
   - ë˛ě ě ë§ë `chromedriver` ë¤ě´ëĄë
   - ë¤ě´ëĄë ë§íŹ: https://chromedriver.chromium.org/downloads
- `$ uvicorn main:app --reload`
## Example
<img width="1367" alt="ááłááłááľáŤááŁáş 2022-10-31 ááŠááŽ 6 47 47" src="https://user-images.githubusercontent.com/41921073/198979983-eb005bad-3736-4e10-914a-8b9edd27e28c.png">

## Schema
### Request
#### Request body
```JSON
{
  "sentence": {input string}
}
```
### Response
#### curl
```
curl -X 'POST' \
  'http://{host}/papago/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "sentence": {input string}
}'
```
#### Request URL
`http://{host}/papago/`

#### Response body
```JSON
{
  "sentence": {output string}
}
