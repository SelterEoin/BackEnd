def zamien_kropke_na_przecinek(words):
    new_list = []
    for i in range(len(words)):
        words[i] = words[i].replace(".", ",",1)
        n = words[i].split(",")
        new_list.append(n[1])
    return new_list
text = ['guns.Long_gun', 'guns.Rifle', 'guns.Shotgun',
         'guns.caliber', 'guns.firearm', 'guns.guns',
         'guns.type', 'guns.5.56×45mm', 'guns.M14']
print(zamien_kropke_na_przecinek(text))