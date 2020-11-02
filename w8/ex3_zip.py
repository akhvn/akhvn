my_zip=lambda *it:[tuple(i[j]for i in it)for j in range(min(map(len,it)))]
