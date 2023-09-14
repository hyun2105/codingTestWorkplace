import requests
#curl -X POST "https://wargame.islab.work"
response = requests.post(url = "https://wargame.islab.work/test.php?data=1234&data2=5678",
                        data = {
                            "data3" :"hello",
                            "data4" : "hi"
                        },
                        headers= {
                            "X-Auth":"r3Dwm8bSC82QgpPiR4ZQbw==",
                            "X-Level" : "dsadsa"
                        },
                        verify=False)
print(response.text)