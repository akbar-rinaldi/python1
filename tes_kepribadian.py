#Header
username=input("Silahkan masukan nama anda : ").upper()
userage=int(input("Silahkan masukan umur anda : "))

print("HALO", username)
print("\n SELAMAT DATANG DI PROGRAM TEST KEPRIBADIAN")
print("\nProgram test ini berisi 11 pertanyaan yang harus anda jawab\n dengan jujur agar hasil bisa akurat")
print("Ikuti petunjuk dibawah ini untuk menjawab test ini")

#Body(pertanyaam nya)
print("\n1. Suatu saat, kamu dia ajak pergi ke restoran bersama teman mu. Apa yang kamu lakukan ?")
print("\nA.Pilih menu terbaik dan termahal \nB.Terserah yang penting enak \nC.Apapun makanan nya yang penting ngumpul bareng \nD.Minta di jelasin menu nya")
p1=input("Jawaban kamu : ")

print("\n2. Suatu saat, ketika kamu pergi keluar kota, kamu lapar dan ingin makan siang. Tempat seperti apa yang kamu pilih ?")
print("\nA.Murah dan enak \nB.Coba tempat  baru \nC.Langganan \nD.Survey dulu di internet")
p2=input("Jawaban kamu : ")

print("\n3. Apa yang kamu lakukan ketika ada janji ?")
print("\nA.Datang sebelum waktu nya \nB.Datang tepat waktu \nC.Suka telat \nD.Lupa kalau ada janji")
p3=input("Jawaban kamu : ")

print("\n4. Baju seperti apa yang menjadi kesukaa mu ?")
print("\nA.Polos/1 warna \nB.Banyak motif \nC.Berwarna cerah \nD.Formal")
p4=input("Jawaban KAMU : ")

print("\n5. Apa jenis/genre musik kesukaan mu ?")
print("\nSedih/galau:pop \n Keras:rock \n Santai:regea/ska \ Semangat: Punk")
p5=input("Jawaban kamu : ")

print("\n6. Apa yang kamu lakukan jika kamu baru saja membeli barang baru ?")
print("\nMenjaga nya sepenuh hati \n Memamerkannya \n Memanfaatkan nya secara maksimal \n Biasa saja")
p6=input("Jawaban kamu : ")

print("\n7. Mana yang termasuk hobi mu ?")
print("\nMain catur \n Menyanyi \n Olahraga \n Baca buku ")
p7=input("Jawaban kamu : ")

print("\n8. Bagaimana jika kamu akan mmegungkapkan sesuatu ke orang lain ?")
print("\nPikir matang-matang \n Sungkan \n Ceplas-ceplos \n Apa ada nya")
p8=input("Jawaban kamu : ")

print("\n9. Apa yang menjadi cita citamu-mu ?")
print("\nDosen \n Presiden \n Artis \n Penulis")
p9=input("Jawaban kamu : ")

print("\n10.Dari beberapa hal berikut, mana yang kamu takuti ?")
print("\nDimanfaatkan \n Ditolak \n Dikritik \n Keluar dari zona nyaman")
p10=input("Jawaban kamu : ")

print("\n11.Dari beberapa hal berikut, mana yanng menjadi prioritas mu ?")
print("\n Target \n Kebersamaan \n Kesempurnaan \n Hindari konflik")
p11=input("Jawaban kamu : ")

print("\n12.Jika pada suatu saat kamu berteemu musuh mu yang sdua sangat dendam padamu, dan kamu di tantang berkelahi, apa yang kamu lakukan ?")
print("\nHanya bisa berteriak \n Hajar \n Ajak damai \n Kabur")
p12=input("Jawaban kamu : ")

#Penentuan skor

if p1.lower()=="a":
    skor1=40
elif p1.lower()=="b":
    skor1=10
elif p1.lower()=="c":
    skor1=30
else:
    skor1=20

if p2.lower()=="a":
    skor2=30
elif p2.lower()=="b":
    skor2=40
elif p2.lower()=="c":
    skor2=10
else:
    skor2=20

if p3.lower()=="a":
    skor3=40
elif p3.lower()=="b":
    skor3=20
elif p3.lower()=="c":
    skor3=10
else:
    skor3=30

if p4.lower()=="a":
    skor4=40
elif p4.lower()=="b":
    skor4=10
elif p4.lower()=="c":
    skor4=30
else:
    skor4=20

if p5.lower()=="a":
    skor5=20
elif p5.lower()=="b":
    skor5=40
elif p5.lower()=="c":
    skor5=10
else:
    skor5=30

if p6.lower()=="a":
    skor6=20
elif p6.lower()=="b":
    skor6=30
elif p6.lower()=="c":
    skor6=40
else:
    skor6=10

if p7.lower()=="a":
    skor7=10
elif p7.lower()=="b":
    skor7=30
elif p7.lower()=="c":
    skor7=40
else:
    skor7=20

if p8.lower()=="a":
    skor8=20
elif p8.lower()=="b":
    skor8=10
elif p8.lower()=="c":
    skor8=30
else:
    skor8=40

if p9.lower()=="a":
    skor9=10
elif p9.lower()=="b":
    skor9=40
elif p9.lower()=="c":
    skor9=30
else:
    skor9=20

if p10.lower()=="a":
    skor10=40
elif p10.lower()=="b":
    skor10=30
elif p10.lower()=="c":
    skor10=20
else:
    skor10=10

if p11.lower()=="a":
    skor11=40
elif p11.lower()=="b":
    skor11=30
elif p11.lower()=="c":
    skor11=20
else:
    skor11=10

if p12.lower()=="a":
    skor12=30
elif p12.lower()=="b":
    skor12=40
elif p12.lower()=="c":
    skor12=10
else:
    skor12=20


skor_total=skor1+skor2+skor3+skor4+skor5+skor6+skor7+skor8+skor9+skor10+skor11+skor12

print("Skor kamu adalah", skor_total)



if skor_total <= 120 and skor_total<=200:
    print("Kamu adalah seorang Plegmatis")
elif skor_total >=210 and skor_total <=300:
    print("Kamu adalah seorang Melankolis")
elif skor_total >= 310 and skor_total <=400:
    print("Kamu adalah seorang Sanguinis")
elif skor_total >= 410 and skor_total<=480:
    print("Kamu adalah seorang Koleris")
else:
    print("Kamu adalah orang KOMUNIS")