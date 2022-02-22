produk=[
    {
        'kategori':'pensil',
        'merk':'stadler',
        'u_price':2000,
        'u_sold':20
    },
    {
        'kategori':'pulpen',
        'merk':'faster',
        'u_price':3000,
        'u_sold':10
    },
    {
        'kategori':'penghapus',
        'merk':'joyko',
        'u_price':5000,
        'u_sold':5
    }    
]
def upd_produk():
    for i in range(len(produk)):
        produk[i]['nama']=produk[i]['kategori']+'_'+produk[i]['merk']
        produk[i]['income']=produk[i]['u_sold']*produk[i]['u_price'] 
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

def tambah_unit_sold():
    while True:
        x=input('Masukkan unit sold: ')
        if x.isnumeric() == True:
            return int(x)
        else:
            print('hanya masukkan angka')

def tambah_unit_price():
    while True:
        x=input('Masukkan unit price: ')
        if x.isnumeric() == True:
            return int(x)
        else:
            print('hanya masukkan angka')

def ada_porduk():
    if len(produk)==0:
        return False
    else:
        return True

def cek_key(keyUpdate):
    if (keyUpdate=='kategori'or keyUpdate=='merk' or keyUpdate=='u_sold' or keyUpdate=='u_price'):
        return True
    else:
        return False

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
                print('\nDaftar seluruh produk\n')
                print('{:20}|{:10}|{:10}|{:7}|{:7}|{}'.format('nama produk','kategori','merk','u_price','u_sold','income'))
                for i in range(len(produk)):
                    print('{:20}|{:10}|{:10}|{:7}|{:7}|{}'
                    .format(produk[i]['nama'],produk[i]['kategori'],produk[i]['merk'],
                    produk[i]['u_price'],produk[i]['u_sold'],produk[i]['income']))
                total_sales()
            else:
                print("Tidak ada data produk")
        elif(subMenu=='2'):
            print('Data produk tertentu')
            dicari_kat=input('kategori yang dicari: ')
            dicari_merk=input('merk yang dicari: ')
            dicari=dicari_kat+'_'+dicari_merk
            print('produk yang dicari: ',dicari)
            for i in range(len(produk)):
                if(dicari==produk[i]['nama']):
                    print('{:20}|{:10}|{:10}|{:7}|{:7}|{}'.format('nama produk','kategori','merk','u_price','u_sold','income'))
                    ket=('{:20}|{:10}|{:10}|{:7}|{:7}|{}'
                        .format(produk[i]['nama'],produk[i]['kategori'],produk[i]['merk'],
                        produk[i]['u_price'],produk[i]['u_sold'],produk[i]['income']))
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
                x=tambah_unit_price()
                y=tambah_unit_sold()
                while True:
                    confirm=input('Apakah data akan disimpan? (Y/N): ')
                    if(confirm=='Y' or confirm=='y'):
                        produk.append({
                            'kategori':tambah_kat,
                            'merk':tambah_merk,
                            'u_price':x,
                            'u_sold':y
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
                    print('nama produk: {}, kategori: {}, merk: {}, u_price: {}, u_sold: {}, sales: {}'
                    .format(produk[i]['nama'],produk[i]['kategori'],produk[i]['merk'],
                    produk[i]['u_price'],produk[i]['u_sold'],produk[i]['income']))
                    while True:
                        confirm=input('Yakin mengubah data? (Y/N): ')
                        if(confirm=='Y' or confirm=='y'):
                            keyUpdate=(input('Keterangan yang ingin di edit: '))
                            if cek_key(keyUpdate)==True:
                                while True:
                                    valUpdate=(input('Masukkan {} baru: '.format(keyUpdate)))
                                    if(keyUpdate=='u_price' or keyUpdate=='u_sold'):
                                        cek=valUpdate.isnumeric()
                                        if (cek==True):
                                            valUpdate=int(valUpdate)
                                            break
                                        else:
                                            print('Hanya masukkan integer') 
                                    else:
                                        break
                                while True:
                                    confirm=input('Yakin update? (Y/N): ')
                                    if(confirm=='Y' or confirm=='y'):
                                        produk[i][keyUpdate]=valUpdate   
                                        upd_produk()
                                        ket=('Berhasil merubah data')
                                        break
                                    elif(confirm=='N' or confirm=='n'):
                                        ket=('Batal merubah data')
                                        break
                                break
                            else:
                                ket=('tidak ada field bernama',keyUpdate)
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
    pilihanMenu=input('''
=====Penjualan Toko Alat Tulis Guido=====

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
