# goruntuteknikleri
Bu kod örneği, belirli bir klasördeki tüm görseller arasındaki benzerlikleri karşılaştırır. 
Her bir görsel 20x20 piksel boyutuna indirgenir ve OpenCV'nin matchTemplate işlevi kullanılarak 
bir diğerine karşı benzerlik skoru hesaplanır. Bu skorlar, daha sonra en yüksekten en düşüğe doğru sıralanır.

Bu kodun karmaşıklığı O(n^2) olacaktır çünkü her bir resmi diğer tüm resimlerle karşılaştırır. 
Bu, resim sayısı arttıkça işlem süresinin dramatik olarak artacağı anlamına gelir. 
İyileştirmeler, k-means gibi bir kümeleme algoritması veya başka bir veri indirgeme teknolojisi kullanılarak yapılabilir.
