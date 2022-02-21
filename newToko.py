produk=[
    {
        'kategori':'pensil',
        'merk':'faber castel',
        'unit price':2000,
        'unit sold':20
    },
    {
        'kategori':'pulpen',
        'merk':'faster',
        'unit price':3000,
        'unit sold':10
    },
    {
        'kategori':'penghapus',
        'merk':'joyko',
        'unit price':5000,
        'unit sold':5
    }    
]
def upd_produk():
    for i in range(len(produk)):
        produk[i]['nama']=produk[i]['kategori']+'_'+produk[i]['merk']
        produk[i]['income']=produk[i]['unit sold']*produk[i]['unit price'] 
upd_produk()

def total_sales():
    income=0
    for i in range(len(produk)):
        income+=produk[i]['income']
    print('Total Income = ',income)

def cek_tambah(tambah_produk):
    for i in range(len(produk)):
        if(tambah_produk!=produk[i]['nama']):
            ket=True
        else:
            ket=False
            break
    return (ket)

def ada_porduk():
    if len(produk)==0:
        return False
    else:
        return True

def menu_1():
    while True:
        subMenu=input('''
+++++Data Produk+++++

1. Data seluruh produk
2. Data produk tertentu
3. Kembali ke menu utama
Silahkan pilih submenu (1-3): ''')
        if(subMenu=='1'):
            if ada_porduk()==True:
                print('Daftar seluruh produk')
                print('{:20}\t|{:10}\t|{:15}\t|{:7}\t|{:7}\t|{}'.format('nama produk','kategori','merk','unit price','unit sold','income'))
                for i in range(len(produk)):
                    print('{:20}\t|{:10}\t|{:15}\t|{:7}\t|{:7}\t|{}'
                    .format(produk[i]['nama'],produk[i]['kategori'],produk[i]['merk'],
                    produk[i]['unit price'],produk[i]['unit sold'],produk[i]['income']))
                total_sales()
            else:
                print("Tidak ada data produk")
        if(subMenu=='2'):
            print('Data produk tertentu')
            dicari_kat=input('kategori yang dicari: ')
            dicari_merk=input('merk yang dicari: ')
            dicari=dicari_kat+'_'+dicari_merk
            print('produk yang dicari: ',dicari)
            for i in range(len(produk)):
                if(dicari==produk[i]['nama']):
                    print('{:20}\t|{:10}\t|{:15}\t|{:7}\t|{:7}\t|{}'.format('nama produk','kategori','merk','unit price','unit sold','income'))
                    ket=('{:20}\t|{:10}\t|{:15}\t|{:7}\t|{:7}\t|{}'
                        .format(produk[i]['nama'],produk[i]['kategori'],produk[i]['merk'],
                        produk[i]['unit price'],produk[i]['unit sold'],produk[i]['income']))
                    break
                elif(dicari!=produk[i]['nama']):
                    ket=('produk tersebut tidak tersedia')
            
            print(ket)
        elif(subMenu=='3'):
            break

def menu_2():
    while True:
        subMenu=input('''
+++++Menambah Data Produk+++++

1. Tambah Data Produk
2. Kembali ke menu utama
Silahkan pilih submenu (1-2): ''')
        if(subMenu=='1'):
            tambah_kat=input('Kategori produk yang ingin ditambahkan: ')
            tambah_merk=input('Merk produk yang ingin ditambahkan: ')
            tambah_produk=tambah_kat+'_'+tambah_merk
            if (cek_tambah(tambah_produk)==True):
                tambah_unit_sold=int((input('Masukkan sold produk: ')))
                tambah_unit_price=int((input('Masukkan harga produk: ')))
                while True:
                    confirm=input('Apakah data akan disimpan? (Y/N): ')
                    if(confirm=='Y' or confirm=='y'):
                        produk.append({
                            'kategori':tambah_kat,
                            'merk':tambah_merk,
                            'unit price':tambah_unit_price,
                            'unit sold':tambah_unit_sold
                        })
                        print('Catatan produk berhasil ditambahkan')
                        upd_produk()
                        break
                    elif(confirm=='N' or confirm=='n'):
                        print('Batal menambahkan data')
                        break
            else:
                print('Data produk tersebut sudah ada')
        elif(subMenu=='2'):
            break
def menu_3():
    while True:
        subMenu=input('''
+++++Menghapus Data Produk+++++

1. Hapus Data Produk
2. Kembali ke menu utama
Silahkan Pilih submenu(1-2): ''')
        if(subMenu=='1'):
            hapus_kat=input('kategori produk yang ingin dihapus: ')
            hapus_merk=input('merk yang ingin dihapus: ')
            hapus_produk=hapus_kat+'_'+hapus_merk
            for i in range(len(produk)):
                if(hapus_produk==produk[i]['nama']):
                    while True:
                        confirm=input('Yakin menghapus data? (Y/N): ')
                        if(confirm=='Y' or confirm=='y'):
                            del(produk[i])
                            upd_produk()
                            ket=('berhasil menghapus')
                            break
                        elif(confirm=='N' or confirm=='n'):
                            ket=('batal menghapus data')
                            break
                    break
                elif(hapus_produk!=produk[i]['nama']):
                    ket=('produk tersebut tidak ditemukan')
            print(ket)
        elif(subMenu=='2'):
            break

def menu_4():
    while True:
        subMenu=input('''
+++++Mengubah Data Produk+++++

1. Ubah Data Produk
2. Kembali ke menu utama
Silahkan pilih submenu(1-2): ''')
        if (subMenu=='1'):
            update_kat=input('kategori produk yang ingin diubah: ')
            update_merk=input('merk yang ingin diubah: ')
            update=update_kat+'_'+update_merk
            for i in range(len(produk)):
                if(update==produk[i]['nama']):
                    print('nama produk: {}, kategori: {}, merk: {}, unit price: {}, unit sold: {}, sales: {}'
                    .format(produk[i]['nama'],produk[i]['kategori'],produk[i]['merk'],
                    produk[i]['unit price'],produk[i]['unit sold'],produk[i]['income']))
                    while True:
                        confirm=input('Yakin mengubah data? (Y/N): ')
                        if(confirm=='Y' or confirm=='y'):
                            keyUpdate=(input('Keterangan yang ingin di edit: '))
                            while True:
                                valUpdate=(input('Masukkan {} baru: '.format(keyUpdate)))
                                if(keyUpdate=='unit price' or keyUpdate=='unit sold'):
                                    cek=valUpdate.isnumeric()
                                    if (cek==True):
                                        valUpdate=int(valUpdate)
                                        break
                                    else:
                                        print('Hanya masukkan integer') 
                                else:
                                    break
                            produk[i][keyUpdate]=valUpdate   
                            upd_produk()
                            ket=('Berhasil merubah data')    
                            break
                        elif(confirm=='N' or confirm=='n'):
                            ket=('Batal merubah data')
                            break
                    break
                elif(update!=produk[i]['nama']):
                    ket=('produk tidak ada')
            print(ket)
        elif(subMenu=='2'):
            break

while True:
    upd_produk()
    pilihanMenu=input('''
=====Penjualan Toko Guido=====

Menu:
1. Menampilkan Daftar penjualan
2. Menambah data penjualan
3. Menghapus data penjualan
4. Update penjualan
5. Exit

Silahkan pilih Menu (1-5): ''')

    if(pilihanMenu == '1'):
        menu_1()
    elif(pilihanMenu == '2'):
        menu_2()
    elif(pilihanMenu == '3'):
        menu_3()
    elif(pilihanMenu == '4'):
        menu_4()
    elif(pilihanMenu == '5'):
        print("Have a great day!")
        break
    else:
        print("Tolong pilih menu 1-5")
