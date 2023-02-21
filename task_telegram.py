results = {'vk' : {'revenue': 103, 'cost': 98},
           'yandex' : {'revenue':179, 'cost':153},
           'ok' : {'revenue': 103, 'cost': 110},
           'adwords' : {'revenue': 35, 'cost': 34},
           'twitter' : {'revenue': 11, 'cost': 24},}
for k, v in results.items():
    v["ROI"] = round((v['revenue']/v['cost'] - 1) * 100, 2)
print(dict(sorted(results.items())))




