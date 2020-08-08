cocas = ['Coca cola', 'Fresca', 'Manzanita', 'Sprite', 'Yoli']
pepsis = ['Pepsi', 'Manzanita', 'Miranda', '7up', 'Toronjada']

new_list = cocas + pepsis
new_list = set(new_list)
new_list = list(new_list)

new_list.sort()

print(new_list)
