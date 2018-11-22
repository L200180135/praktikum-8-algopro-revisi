## kegiatan 1

dd = {"a" : "Anisa" , "N" : "L200180135" , "A" : "Jl. Garuda II NO. 6B, Banaran, Boyolali" , "K" : "57313" , "p" : "Informatika" , "f" : "Komunikasi dan Informatika" , "ttl" : "20 Januari 2000"}
def nama () :
    "Nama :" , dd ["a"]
    return
def NIM () :
    "NIM :" , dd ["N"]
    return
def Alamat () :
    "Alamat :" , dd ["A"]
    return
def KodePos () :
    "Kode Pos :" ,  dd ["K"]
    return
def Prodi () :
    "Prodi :" , dd ["p"]
    return
def Fakultas () :
    "Fakultas :" , dd ["f"]
    return
def TanggalLahir () :
    "Tanggal Lahir :" , dd ["ttl"]
b = "Pilihan yang teredia : \n b menampilkan bantuan ini \n N menampilkan NIM \n a menampilkan Nama \n A menampilkan Alamat \n K menampilkan Kode Pos \n p menampilkan Prodi \n f menampilkan Fakultas \n ttl menampilkan Tanggal Lahir \n k untuk mengakhiri program"
print b
c = raw_input ("Masukkan pilihan anda :")
k = "Selesai"
while c != k :
    if c == "b" :
        print b ,
        c = raw_input (" \nMasukkan pilihan anda :")
    elif c == "k"  :
        print k
        break
    elif c == "a" or nama () :
        print "Nama :" , dd ["a"],
        c = raw_input (".\nMasukkan pilihan anda :" )
    elif c == "N" or NIM () :
        print "NIM :" , dd ["N"] ,
        c = raw_input (".\nMasukkan pilihan anda :")
    elif c == "A" or Alamat () :
        print "Alamat :" , dd ["A"] ,
        c = raw_input (".\nMasukkan pilihan anda :")
    elif c == "K" or KodePos () :
        print "Kode Pos :" , dd ["K"] ,
        c = raw_input (".\nMasukkan pilihan anda :")
    elif c == "p" or Prodi () :
        print "Prodi :" , dd ["p"] ,
        c = raw_input (". \nMasukkan pilihan anda :")
    elif c == "f" or Fakultas () :
        print "Fakultas :" , dd ["f"] ,
        c = raw_input (".\nMasukkan pilihan anda :")
    elif c == "ttl" or TanggalLahir () :
        print "Tanggal Lahir :" , dd ["ttl"] ,
        c = raw_input (". \nMasukkan pilihan anda :")
    else :
        print "Perintah tidak dikenal" ,
        c = raw_input (". \nMasukkan pilihan anda :")

## kegiatan 2

def konvsuhu (c = 0 , f = 0) :
    if c != 0 :
        d = ((9 * c /5) + 32)
        print "Suhu yang sudah dikonversi" , d
    elif f != 0 :
        y = ((f - 32)*5/9)
        print "Suhu yang sudah dikonversi" , y
    else :
        print "0 derajat celcius = 32 derajat farenheit"
    return
