% Fakta olahraga
olahraga(renang).
olahraga(basket).
olahraga(lari).
olahraga(yoga).
olahraga(bersepeda).
olahraga(angkat_beban).

% Kriteria setiap olahraga
kriteria(kemampuan_berenang, renang).
kriteria(suka_air, renang).
kriteria(kemampuan_melompat, basket).
kriteria(kemampuan_lari_cepat, basket).
kriteria(daya_tahan_tinggi, lari).
kriteria(suka_lari, lari).
kriteria(fleksibilitas_tubuh, yoga).
kriteria(mencari_relaksasi, yoga).
kriteria(suka_outdoor, bersepeda).
kriteria(keseimbangan_tubuh, bersepeda).
kriteria(kekuatan_fisik, angkat_beban).
kriteria(ingin_meningkatkan_otot, angkat_beban).

% Pertanyaan untuk setiap kriteria
pertanyaan(kemampuan_berenang, "Apakah Anda bisa berenang?").
pertanyaan(suka_air, "Apakah Anda suka aktivitas di air?").
pertanyaan(kemampuan_melompat, "Apakah Anda mampu melakukan lompatan tinggi?").
pertanyaan(kemampuan_lari_cepat, "Apakah Anda mampu berlari dengan cepat?").
pertanyaan(daya_tahan_tinggi, "Apakah Anda memiliki daya tahan tubuh yang tinggi?").
pertanyaan(suka_lari, "Apakah Anda suka berlari?").
pertanyaan(fleksibilitas_tubuh, "Apakah Anda memiliki tubuh yang fleksibel?").
pertanyaan(mencari_relaksasi, "Apakah Anda ingin mencari olahraga yang menenangkan atau relaksasi?").
pertanyaan(suka_outdoor, "Apakah Anda suka beraktivitas di luar ruangan?").
pertanyaan(keseimbangan_tubuh, "Apakah Anda memiliki keseimbangan tubuh yang baik?").
pertanyaan(kekuatan_fisik, "Apakah Anda memiliki kekuatan fisik yang baik?").
pertanyaan(ingin_meningkatkan_otot, "Apakah Anda ingin meningkatkan massa otot?").

% Fakta jawaban (dari user)
:- dynamic kriteria_pos/1.
:- dynamic kriteria_neg/1.
