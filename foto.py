import cv2
import numpy as np
import os

# Resimlerin bulunduğu klasör
image_folder = "resimler"

# Tüm resimlerin listesi
image_files = os.listdir(image_folder)

# Benzerlik skorlarını tutan sözlük
similarity_scores = {}

for i in range(len(image_files)):
    for j in range(i+1, len(image_files)):
        img1 = cv2.imread(os.path.join(image_folder, image_files[i]), 0)
        img2 = cv2.imread(os.path.join(image_folder, image_files[j]), 0)

        # 20x20 piksel boyutuna indirgeme
        img1 = cv2.resize(img1, (20, 20))
        img2 = cv2.resize(img2, (20, 20))

        # Benzerlik skorunu hesaplama
        score = cv2.matchTemplate(img1, img2, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(score)

        # En yüksek benzerlik skorunu kaydetme
        similarity_scores[(image_files[i], image_files[j])] = max_val

# Benzerlik skorlarını büyükten küçüğe doğru sıralama
sorted_scores = sorted(similarity_scores.items(), key=lambda x: x[1], reverse=True)

# En çok benzeyen görsellerin listesini yazdırma
for pair, score in sorted_scores:
    print(f"{pair[0]} and {pair[1]}: {score*100}%")
