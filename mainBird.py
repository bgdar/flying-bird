import pygame
import random
import array as ar

import pygame.locals

pygame.init() # inisialisasi game
pygame.mixer.init() # inisialisasi suara
pygame.font.init() # inisialisasi font

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

windowWidth,windowHeight = 800 ,450 # ukuran layar  16:9,

# Layar utama
birdImage = pygame.image.load("./image/bird.png")
windows = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_icon(birdImage)
pygame.display.set_caption("fly bird")


#popup untuk menampilkan Level halaman 
def popup_level(screen,level:int) :
    plevely = 20
    plevelx = 350
    font = pygame.font.Font(None, 18)
    font.set_bold(True)
    
    text = font.render(f"Level : {level}", True, color["hitam"])
    textOut = font.render("Mulai lah terbang , ketik Q untuk kembali ke menu", True, color["merah"])
    
    # Tambahkan latar belakang untuk popup
    pygame.draw.rect(screen, color["gold"], (plevelx - 10, plevely - 10, 420, 70))
    
    screen.blit(text, (plevelx, plevely))
    screen.blit(textOut, (plevelx, plevely + 30))
def draw_text(surface, text, font, color, position):
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, position)
    #contoh penggunaan 
    #draw_text(windows, "Tekan ENTER untuk masuk ke game", fontMenu, color["putih"], (230, 140))


# Fungsi untuk membuat popup
def popup_trabrakan(screen, tabrakan_ke ,nama_bird,):#barHP):
    """
    Fungsi untuk membuat popup yang menunjukkan tabrakan ke berapa.
    
    Parameters:
    - screen: Surface pygame untuk menggambar popup.
    - tabrakan_ke: Nomor tabrakan (integer), menunjukkan tabrakan ke-berapa yang terjadi.
    - barHP menunjukan status bar saat ini 
    """
    # Ukuran popup
    popup_width = 200
    popup_height = 80

    # Posisi popup (pojok kanan bawah)
    popup_x = 15
    popup_y = windowHeight - popup_height - 15  # Margin 15 px dari bawah

    # Gambar background popup
    popup_rect = pygame.Rect(popup_x, popup_y, popup_width, popup_height)
    pygame.draw.rect(screen, color["coklat"], popup_rect)  # Warna abu-abu
    pygame.draw.rect(screen, (0, 0, 0), popup_rect,2,border_radius=5,border_top_right_radius=7)     # Border hitam

    # Tampilkan teks pada popup
    font = pygame.font.Font(None, 28)  # Font untuk teks popup
    nameBird = font.render(nama_bird, True,color["darkcyan"])  
    message = f"Tabrakan ke: {tabrakan_ke}"
    text_surface = font.render(message, True, color["silver"])  
    text_rect = text_surface.get_rect(center=popup_rect.center)
    

    screen.blit(nameBird, (popup_x / popup_width, popup_y + 10))
    screen.blit(text_surface, text_rect)

    # Tombol "Close"
    # close_button_rect = pygame.Rect(popup_x + popup_width - 100, popup_y + popup_height - 50, 80, 30)
    # pygame.draw.rect(screen, merah, close_button_rect)
    # close_text = font.render("Close", True, putih)
    # close_text_rect = close_text.get_rect(center=close_button_rect.center)
    # screen.blit(close_text, close_text_rect)

#fungsi popup untuk meneriman inputan dari user
def popup_input(screen,judul_popup:str) -> str:
    input_text : str  =""
    popup_active : bool  = True
 
    font = pygame.font.Font(None, 30)

    while popup_active:
        screen.fill((0, 0, 0, 120))  # Layar transparan

        # Latar belakang popup
        popup_surface = pygame.Surface((400, 200), pygame.SRCALPHA)
        popup_surface.fill((255, 255, 255, 240))  # Warna putih dengan transparansi
        screen.blit(popup_surface, (200, 150))

        # Kotak utama popup
        pygame.draw.rect(screen, color["abu_abu"], (200, 150, 400, 200), border_radius=10)
        pygame.draw.rect(screen, color["hitam"], (200, 150, 400, 200), 2, border_radius=10)  # Outline

        # Judul Popup
        text_judul = font.render(judul_popup, True, color["hitam"])
        screen.blit(text_judul, (220, 170))

        # Kotak input
        pygame.draw.rect(screen, color["putih"], (220, 210, 360, 40), border_radius=5)
        pygame.draw.rect(screen, color["hitam"], (220, 210, 360, 40), 2, border_radius=5)

        # Tampilkan teks yang sudah diketik
        text_surface = font.render(input_text, True, color["hitam"])
        screen.blit(text_surface, (230, 220))

        # Tombol OK
        pygame.draw.rect(screen, color["biru"], (340, 270, 120, 40), border_radius=5)
        pygame.draw.rect(screen, color["hitam"], (340, 270, 120, 40), 2, border_radius=5)
        text_ok = font.render("OK", True, color["putih"])
        screen.blit(text_ok, (385, 280))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            if event.type == pygame.KEYDOWN:  # Jika tombol ditekan
                if event.key == pygame.K_RETURN:
                    popup_active = False  # Keluar saat ENTER ditekan
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]  # Hapus karakter terakhir
                else:
                    input_text += event.unicode  # Tambahkan karakter baru
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if 340 <= mouse_x <= 460 and 270 <= mouse_y <= 310:  # Cek jika tombol OK diklik
                    popup_active = False

        pygame.display.update()

    return input_text  # Kembalikan teks yang dimasukkan

#fungsi fungsi untuk halmana
def pageMenu():
    # windows.fill(color["putih"]) 
    # fontMenu = pygame.font.Font(None,24)
    # textMenu = fontMenu.render("Selamat datang di Flappy Bird", True, color["magenta"])
    # fontMenu.set_bold(True)
    # textStart = fontMenu.render("tekan enter  untuk masuk ke game",True,color["jingga"])
    # if not tombol_ditekan :
    #     textBirdname = fontMenu.render("tekan spasi kanan untuk memasukan nama ",False,color["gold"])
    #     windows.blit(textBirdname,(200,200))
    # else :
    #     textBirdname = fontMenu.render(f"burung kamu : {NameBird}",False,color["gold"])
    #     windows.blit(textBirdname,(200,200))
    # #desain tower 
    # tower = pygame.image.load("./image/Tower/office.png")
    # updateTower = pygame.transform.scale(tower,(100,100))

    # #rendering ke layar
    # windows.blit(updateTower,(2,500))
    # windows.blit(updateTower,(600,500))
    # windows.blit(textStart,(200,100))
    # windows.blit(textMenu,(200,30))
    # pygame.display.update()

    fontMenu = pygame.font.Font(None, 30)
    fontMenu.set_bold(True)

    # Gambar latar belakang
    background_image = pygame.image.load("./image/Background.png")  # Sesuaikan path
    background_image = pygame.transform.scale(background_image, (windowWidth, windowHeight))

    # Gambar tower
    tower = pygame.image.load("./image/Tower/office.png")
    tower_scaled = pygame.transform.scale(tower, (100, 100))

    windows.blit(background_image, (0, 0))  # Tampilkan latar belakang

    # Kotak semi transparan untuk teks menu
    menu_box = pygame.Surface((400, 200), pygame.SRCALPHA)  # Buat kotak transparan
    menu_box.fill((50, 50, 50, 180))  # RGBA (abu-abu dengan transparansi)
    windows.blit(menu_box, (200, 50))

    # Kotak tombol ENTER
    pygame.draw.rect(windows, color["biru"], (220, 130, 360, 40), border_radius=10)
    
    # Tampilkan teks menu
    draw_text(windows, "Selamat datang di Flappy Bird", fontMenu, color["magenta"], (260, 70))
    draw_text(windows, "Tekan ENTER untuk masuk ke game", fontMenu, color["putih"], (230, 140))

    # Tampilkan teks input nama burung
    if not tombol_ditekan:
        draw_text(windows, "Tekan spasi kanan untuk memasukkan nama", fontMenu, color["gold"], (200, 220))
    else:
        draw_text(windows, f"Burung kamu: {NameBird}", fontMenu, color["gold"], (250, 220))

    # Tampilkan tower di bawah layar
    windows.blit(tower_scaled, (50, 500))
    windows.blit(tower_scaled, (650, 500))

def PagePesawat(windowWidth, windowHeight,tabrakan_ke) -> str:
    """ halaman di mana banyak pesawat yg terbang untuk di tabrak ole si burung"""
 
    imagePesawat = pygame.image.load("./image/peswat.png")
    pesawat = pygame.transform.scale(imagePesawat,(70,70))
    data_pesawat = ar.array("i",[]) # simpan data pesawat
    #audio trabrakan 
    audio_trabrakan = pygame.mixer.Sound("./audio/tabrakan.wav")
    audio_trabrakan.set_volume(1.2)

    # Posisi awal letak burungnya 
    birdX = 50
    birdY = 50
    gravity = 1
    run_game =True

    bird_spriet_sheet = pygame.image.load("./image/bird_walk.png")
    FRAME_BIRD_WIDTH = bird_spriet_sheet.get_width() // 6
    FRAME_BIRD_HEIGHT = bird_spriet_sheet.get_height()
    FRAME_COUNT = 6 #frame di gambar burungnya ada 6
    FRAME_DELAY = 100 # Delay dalam milidetik (100ms = 10 FPS)
    index = 0
    #waktu yang di ambil saat sebelum render pertama di lakukan 
    last_update = pygame.time.get_ticks()

    # ============= Frame Bird =============
    #frames_bird = [bird_spriet_sheet.subsurface((i * FRAME_BIRD_WIDTH, 0, FRAME_BIRD_WIDTH, FRAME_BIRD_HEIGHT)) for i in range(FRAME_COUNT)]
    frames_bird = [
    pygame.transform.scale(
        bird_spriet_sheet.subsurface((i * FRAME_BIRD_WIDTH, 0, FRAME_BIRD_WIDTH, FRAME_BIRD_HEIGHT)), 
        (70, 70)  # Ukuran baru
    ) 
    for i in range(FRAME_COUNT)
    ]
    #simapan perubahan frame burung yang terbalik
    bird_frames_flipped = [pygame.transform.flip(frame,True,False) for frame in frames_bird]
    

    clock = pygame.time.Clock()

    isBalik = False
    windows.fill(color["putih"])
   
    while run_game:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False
                pygame.quit()#keluar dari sesi ini 
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    return "menu"  # ini langsung mengarahkana ke halama menu kedepanya tambah autotikasi
                
        birdY += gravity

        #tombol gerakan untuk burungnya        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]: 
            birdY -= 5 
        if keys[pygame.K_RIGHT]:
            birdX += 2
            isBalik = False
        elif keys[pygame.K_LEFT] :
            birdX -= 5
            isBalik = True
        
        pesawat_x = windowWidth
        pesawat_y = random.randint(0, windowHeight - pesawat.get_height())
        # Tambahkan pesawat baru secara acak degan .randint
        if random.randint(0, 100) < 2:  # 2% kemungkinan muncul pesawat baru
            data_pesawat.append([pesawat_x, pesawat_y])
        # Update posisi pesawat
        for i in range(len(data_pesawat)):
            data_pesawat[i][0] -= 1.7  # Gerakkan pesawat dari kanan ke kiri

       # Deteksi tabrakan desain selanjutnya | tapi tidak untuk jika berbalik ke arah kiri
        birdRect = pygame.Rect(birdX, birdY, frames_bird[index].get_width(), frames_bird[index].get_height())
        for psw in data_pesawat:
            pesawatRect = pygame.Rect(psw[0], psw[1], pesawat.get_width(), pesawat.get_height())
            if birdRect.colliderect(pesawatRect) :
                tabrakan_ke += 1
                audio_trabrakan.play()
                try :
                    data_pesawat.remove([psw[0], psw[1]])
                except ValueError as e :
                    print(f"Error removing pesawat: {e}")

        # Hapus pesawat yang keluar dari layar
        data_pesawat = [p for p in data_pesawat if p[0] > -pesawat.get_width()]

        #perbahrui halaman setiap looop jadi yg di bawahnya tampil setiap loop nya
        windows.fill(color["putih"])
        
        popup_level(windows,1)
        popup_trabrakan(windows,tabrakan_ke,NameBird)

        #upgrade perbaharuan frame nya 
        current_time = pygame.time.get_ticks()
        if current_time - last_update > FRAME_DELAY:
            index = (index + 1) % FRAME_COUNT  # Loop dari 0 ke FRAME_COUNT - 1
            last_update = current_time  # Reset waktu



       # index = (index + 1) % FRAME_COUNT  # Perbarui indeks frame
        
        if isBalik  :
            windows.blit(bird_frames_flipped[index],(birdX,birdY))
        else :
            windows.blit(frames_bird[index], (birdX, birdY))  # Tampilkan frame burung saat ini

         # Tampilkan semua pesawat
        for p in data_pesawat:
            windows.blit(pesawat, (p[0], p[1]))
                
        # Batasi posisi burung agar tidak keluar dari layar
        if birdY < 0:
            birdY = 0
        if birdY > windowHeight - frames_bird[index].get_height():
            birdY = windowHeight - frames_bird[index].get_height()
        if birdX > windowWidth - frames_bird[index].get_width() :
            birdX = windowWidth- frames_bird[index].get_width()
            birdX = 0 #agar saat sampai ujung dia kembali ke halaman awal 
        if birdX < 0 :
            birdX = 0
        pygame.display.update()  # Update layar
    return "menu" #kembalikan ke halaman menu jika ini di degan kembalian variabel ke fn nya

#halaman untuk level 2
def pipePage():
    pass

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
            awal_mulai = PagePesawat(windowWidth,windowHeight,CrashInto) #set awal_mulai dengan return value dari pageMain untuk navigasi halaman
    pygame.display.update()
