# GET request using curl
# curl https://reqbin.com/echo

# curl https://reqbin.com/echo \
#    -H "Cache-Control: must-revalidate" \
#    -H "Pragma: no-cache" \
#    -H "Expires: 0"

# getting only HTTP headers using curl
# curl -I https://reqbin.com/echo
# curl -I http://localhost:8000

# getting JSON using cURL
# curl https://reqbin.com/echo/get/json \
#    -H "Accept: application/json"

# HTTP/2
# curl -I https://algorithmshub.uz

# cURL GET reques with cookies
# curl https://reqbin.com/echo \
#    -b "session=eJwlzj0wMQG7eO4Q"

# curl transfer rate limit
# curl https://reqbin.com/echo \
    # --limit-rate 1K

# curl  follow redirects
# curl -L https://reqbin.com/echo

# posting JSON using curl
# curl -X POST https://algorithmshub.uz/api/v1/login/ \
#    -H 'Content-Type: application/json' \
#    -d '{"login":"ali","password":"aliai2005"}'

# curl post json file
# curl -X POST https://reqbin.com/echo/post/json -d @filename

# curl request with Bearer Token
# curl https://reqbin.com/echo/get/json \
#    -H "Accept: application/json" \
#    -H "Authorization: Bearer {token}"

# print request headers using curl
# curl -v  https://algorithmshub.uz


curl -X GET "http://localhost:8000/query?q=a"
