import pygame
import random
import array as ar

pygame.init()

running = True
awal_mulai = "menu"
color = {
    "biru": (0, 0, 255),
    "putih": (255, 255, 255),
    "merah": (255, 0, 0),
    "hitam": (0, 0, 0),
    "darkcyan": (0, 139, 139, 1),
    # Warna tambahan dalam format (R, G, B)
    "kuning": (255, 255, 0),
    "hijau": (0, 255, 0),
    "ungu": (128, 0, 128),
    "jingga": (255, 165, 0),
    "pink": (255, 105, 180),
    "coklat": (139, 69, 19),
    "abu_abu": (128, 128, 128),
    "biru_muda": (173, 216, 230),
    "hijau_tua": (0, 100, 0),
    "merah_tua": (139, 0, 0),

    # Warna dengan format (R, G, B, A) (dengan transparansi / alpha channel)
    "transparan": (0, 0, 0, 0),  # Transparan penuh
    "biru_transparan": (0, 0, 255, 128),  # Biru dengan transparansi 50%
    "hitam_transparan": (0, 0, 0, 100),  # Hitam dengan transparansi

    # Warna lain dengan nuansa berbeda
    "gold": (255, 215, 0),
    "silver": (192, 192, 192),
    "cyan": (0, 255, 255),
    "magenta": (255, 0, 255),
    "lime": (50, 205, 50),

    # Warna abu-abu tambahan
    "abu_abu_terang": (215, 219, 221)
}

# Ukuran layar
windowWidth = 700
windowHeight = 700
print(" lebar windows :",windowWidth,"tinggi windows :",windowHeight)

birdImage = pygame.image.load("./image/bird.png")
# Layar utama
windows = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_icon(birdImage)
pygame.display.set_caption("fly bird")

# Fungsi untuk membuat popup
def popup_trabrakan(screen, tabrakan_ke ,nama_bird):
    """
    Fungsi untuk membuat popup yang menunjukkan tabrakan ke berapa.
    
    Parameters:
    - screen: Surface pygame untuk menggambar popup.
    - tabrakan_ke: Nomor tabrakan (integer), menunjukkan tabrakan ke-berapa yang terjadi.
    """
    # Ukuran popup
    popup_width = 200
    popup_height = 50

    # Posisi popup (pojok kanan bawah)
    popup_x = 15
    popup_y = windowHeight - popup_height - 15  # Margin 15 px dari bawah

    # Gambar background popup
    popup_rect = pygame.Rect(popup_x, popup_y, popup_width, popup_height)
    pygame.draw.rect(screen, (200, 200, 200), popup_rect)  # Warna abu-abu
    pygame.draw.rect(screen, (0, 0, 0), popup_rect, 2)     # Border hitam

    # Tampilkan teks pada popup
    font = pygame.font.Font(None, 28)  # Font untuk teks popup
    nameBird = font.render(nama_bird, True,color["darkcyan"])  
    message = f"Tabrakan ke: {tabrakan_ke}"
    text_surface = font.render(message, True, color["silver"])  
    text_rect = text_surface.get_rect(center=popup_rect.center)
    screen.blit(nameBird, (popup_x + 10, popup_y + 10))
    screen.blit(text_surface, text_rect)

    # Tombol "Close"
    # close_button_rect = pygame.Rect(popup_x + popup_width - 100, popup_y + popup_height - 50, 80, 30)
    # pygame.draw.rect(screen, merah, close_button_rect)
    # close_text = font.render("Close", True, putih)
    # close_text_rect = close_text.get_rect(center=close_button_rect.center)
    # screen.blit(close_text, close_text_rect)

#fungsi popup untuk meneriman inputan dari user
def popup_input(screen,judul_popup:int) -> str:
    input_text : str  =""
    popup_active : bool  = True
    popup_y = windowHeight - 100
    popup_x = windowWidth - 100
    while popup_active:
        windows.fill(color["putih"])
        font = pygame.font.Font(None, 28)
        judul = font.render(judul_popup, True, color["abu_abu_terang"])
         # Gambar popup
        pygame.draw.rect(screen, color["abu_abu"], (100, 150, 300, 100), border_radius=10)
        pygame.draw.rect(screen, color["hitam"], (100, 150, 300, 100), 2, border_radius=10)  # Outline
         # Tampilkan teks input
        text_surface = font.render(input_text, True, color["hitam"])
        screen.blit(text_surface, (120, 180))
        screen.blit(judul, (150, 160))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            if event.type == pygame.KEYDOWN: #jika tombol di tekan
                if event.key == pygame.K_RETURN:
                    popup_active = False  # Keluar saat ENTER ditekan
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]  # Hapus karakter terakhir
                else:
                    input_text += event.unicode  # Tambahkan karakter baru

        pygame.display.update()

    return input_text  # Kembalikan teks yang dimasukkan

#fungsi fungsi untuk halmana
def pageMenu():
    windows.fill(color["putih"]) 
    fontMenu = pygame.font.Font(None,24)
    textMenu = fontMenu.render("Selamat datang di Flappy Bird", True, color["magenta"])
    fontMenu.set_bold(True)
    textStart = fontMenu.render("tekan enter  untuk masuk ke game",True,color["jingga"])
    if not tombol_ditekan :
        textBirdname = fontMenu.render("tekan spasi kanan untuk memasukan nama ",False,color["gold"])
        windows.blit(textBirdname,(200,200))
    else :
        textBirdname = fontMenu.render(f"burung kamu : {NameBird}",False,color["gold"])
        windows.blit(textBirdname,(200,200))
    #desain tower 
    tower = pygame.image.load("./image/Tower/office.png")
    updateTower = pygame.transform.scale(tower,(100,100))

    #rendering ke layar
    windows.blit(updateTower,(2,500))
    windows.blit(updateTower,(600,500))
    windows.blit(textStart,(200,100))
    windows.blit(textMenu,(200,30))
    pygame.display.update()

def pageGame(windowWidth, windowHeight,tabrakan_ke) -> str:
    imagePesawat = pygame.image.load("./image/peswat.png")
    pesawat = pygame.transform.scale(imagePesawat,(70,70))
    #data_pesawat=[] # simpan data pesawat
    data_pesawat = ar.array("i",[]) # simpan data pesawat

    # Posisi
    birdX = 50
    birdY = 50
    gravity = 0.5
    run_game =True
    #item image
    birdImage = pygame.image.load('./image/bird.png')  
    birdImage = pygame.transform.scale(birdImage,(25,25))
    clock = pygame.time.Clock()

    isBalik = False
    windows.fill(color["putih"])
    fontMain = pygame.font.Font(None,30)
    fontMain.set_italic(True)
    textMain = fontMain.render("Mulai lah terbang , ketik q untuk kembali ke menu", True, color["merah"])
    
    while run_game:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False
                pygame.quit()#keluar dari sesi ini 
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    return "menu"  # ini langsung mengarahkana ke halama menu kedepanya tambah autotikasi
                
        #tombol gerakan untuk burungnya        
        birdY += gravity

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:  # Naik sedikit jika tombol atas di klik
            birdY -= 5  # Mengurangi nilai birdY untuk membuat burung nail
        if keys[pygame.K_RIGHT]:
            birdX += 2
            if isBalik :
                birdImage = pygame.transform.flip(birdImage, True, False)
                isBalik = False
        elif keys[pygame.K_LEFT] :
            birdX -= 5
            if not isBalik :
                birdImage = pygame.transform.flip(birdImage, True, False)
                isBalik = True
      
        pesawat_x = windowWidth
        pesawat_y = random.randint(0, windowHeight - pesawat.get_height())
        # Tambahkan pesawat baru secara acak degan .randint
        if random.randint(0, 100) < 2:  # 2% kemungkinan muncul pesawat baru
            data_pesawat.append([pesawat_x, pesawat_y])
        # Update posisi pesawat
        for i in range(len(data_pesawat)):
            data_pesawat[i][0] -= 1.7  # Gerakkan pesawat dari kanan ke kiri

       # Deteksi tabrakan desain selanjutnya
        birdRect = pygame.Rect(birdX, birdY, birdImage.get_width(), birdImage.get_height())
        for psw in data_pesawat:
            pesawatRect = pygame.Rect(psw[0], psw[1], pesawat.get_width(), pesawat.get_height())
            if birdRect.colliderect(pesawatRect) :
                tabrakan_ke += 1
                try :
                    data_pesawat.remove([psw[0], psw[1]])
                except ValueError as e :
                    print(f"Error removing pesawat: {e}")

        # Hapus pesawat yang keluar dari layar
        data_pesawat = [p for p in data_pesawat if p[0] > -pesawat.get_width()]

        #perbahrui halaman setiap looop jadi yg di bawahnya tampil setiap loop nya
        windows.fill(color["putih"])

        popup_trabrakan(windows,tabrakan_ke,NameBird)

        windows.blit(textMain,(170,10))
        windows.blit(birdImage, (birdX, birdY))  #menampilkan gambar burungnya

         # Tampilkan semua pesawat
        for p in data_pesawat:
            windows.blit(pesawat, (p[0], p[1]))
                
        # Batasi posisi burung agar tidak keluar dari layar
        if birdY < 0:
            birdY = 0
        if birdY > windowHeight - birdImage.get_height():
            birdY = windowHeight - birdImage.get_height()
        if birdX > windowWidth - birdImage.get_width() :
            birdX = windowWidth- birdImage.get_width()
            birdX = 0 #agar saat sampai ujung dia kembali ke halaman awal 
        if birdX < 0 :
            birdX = 0
        pygame.display.update()  # Update layar
    return "menu" #kembalikan ke halaman menu jika ini di degan kembalian variabel ke fn nya

#=================================Main Menu game=======================================
#set hitungan trabeakan awal
CrashInto =0 
#nama yg di dapat dari popup
NameBird : str =" "
tombol_ditekan : bool = False
#  = set()
#loop utamana yg menjalanakn aplikasi nya
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_RETURN :
                awal_mulai = "game" #set awal_mulai dengan judul  game untuk halaman game 
            if event.key == pygame.K_LSHIFT and not tombol_ditekan:
                NameBird = popup_input(windows,"Masukkan nama nya",)
                tombol_ditekan = True
                
    match awal_mulai :
        case "menu":
            pageMenu()
        case "game":
            awal_mulai = pageGame(windowWidth,windowHeight,CrashInto) #set awal_mulai dengan return value dari pageMain untuk navigasi halaman
    pygame.display.update()