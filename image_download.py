from simple_image_download import simple_image_download as simp
response = simp.simple_image_download

keyword = ['Handgun', 'Person with handgun']

# downloading 100 images for every keys

for key in keyword:
    response().download(key, 100)


