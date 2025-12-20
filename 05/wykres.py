import matplotlib.pyplot as plt


metody_szyfrowania = ["aes128-ctr", "aes128-cbc", "aes192-cbc"]


pliki = ["c_file.c", "500MB.bin", "200MB.avi"]


wyniki = {
    "aes128-ctr": [0, 47, 18],
    "aes128-cbc": [0, 47, 18],
    "aes192-cbc": [0, 47, 18],
    }


wyniki_kompresji = {
    "aes128-ctr": [0, 45, 17],
    "aes128-cbc": [0, 45, 17],
    "aes192-cbc": [0, 45, 17],
    }

x = range(len(pliki))
plt.figure(figsize=(12, 6))
bar_width = 0.35
plt.bar([i - bar_width/2 for i in x], [wyniki[metoda][i] for metoda in metody_szyfrowania for i in range(len(pliki)) if metoda == metody_szyfrowania[0]], width=bar_width, label='Szyfrowanie', color='b')
plt.bar([i + bar_width/2 for i in x], [wyniki_kompresji[metoda][i] for metoda in metody_szyfrowania for i in range(len(pliki)) if metoda == metody_szyfrowania[0]], width=bar_width, label='Kompresja + Szyfrowanie', color='r')
plt.xticks(x, pliki)
plt.xlabel('Pliki')
plt.ylabel('Czas (sekundy)')
plt.title('Porównanie czasów szyfrowania i kompresji + szyfrowania')
plt.legend()
plt.tight_layout()
plt.savefig('porownanie_szyfrowania_kompresji.png')
plt.show()