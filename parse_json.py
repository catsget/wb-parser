import requests

url = "https://www.wildberries.ru/__internal/u-card/cards/v4/detail"

cookies = {
    "_wbauid": "977362291765809789",
    "_cp": "1",
    "x_wbaas_token": "1.1000.33bec95fa8954b9aa4f12440920f8207.MHw4MC45Mi4yNS4yMzR8TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NDsgcnY6MTQ3LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvMTQ3LjB8MTc3MTYxMTU3NnxyZXVzYWJsZXwyfGV5Sm9ZWE5vSWpvaUluMD18MHwzfDE3NzEwMDY3NzZ8MQ==.MEQCIBLiwzTO8PU413C5mRYeV1cdbkbkPsxwc8k2G0dfztC7AiBLizl44h/iJGiCrdcYD9IhIY2roByymYjuLeKRhB83EQ==",
    "wbx-validation-key": "d16d5c3b-5543-470f-899d-7f5b0676a35d",
    "routeb": "1770989211.472.1973.514412|fc3b37d75a18d923fd0e9c7589719997",
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:147.0) Gecko/20100101 Firefox/147.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    "Connection": "keep-alive",
    # 'Cookie': '_wbauid=977362291765809789; _cp=1; x_wbaas_token=1.1000.33bec95fa8954b9aa4f12440920f8207.MHw4MC45Mi4yNS4yMzR8TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NDsgcnY6MTQ3LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvMTQ3LjB8MTc3MTYxMTU3NnxyZXVzYWJsZXwyfGV5Sm9ZWE5vSWpvaUluMD18MHwzfDE3NzEwMDY3NzZ8MQ==.MEQCIBLiwzTO8PU413C5mRYeV1cdbkbkPsxwc8k2G0dfztC7AiBLizl44h/iJGiCrdcYD9IhIY2roByymYjuLeKRhB83EQ==; wbx-validation-key=d16d5c3b-5543-470f-899d-7f5b0676a35d; routeb=1770989211.472.1973.514412|fc3b37d75a18d923fd0e9c7589719997',
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Priority": "u=0, i",
}

params = {
    "appType": "1",
    "curr": "rub",
    "dest": "-1257786",
    "spp": "30",
    "hide_vflags": "4294967296",
    "ab_testing": "false",
    "lang": "ru",
}


def parse_wb_sync(nm: int):
    params["nm"] = nm
    response = requests.get(
        f"https://www.wildberries.ru/__internal/u-card/cards/v4/detail?appType=1&curr=rub&dest=-1257786&spp=30&hide_vflags=4294967296&ab_testing=false&lang=ru&nm={nm}",
        cookies=cookies,
        headers=headers,
    )

    with open("result.json", "w", encoding="utf-8") as file:
        file.write(response.text)

    return response.json()
