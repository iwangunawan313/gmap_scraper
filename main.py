from botasaurus import *
import urllib.parse

@browser(
    block_images=True,
)

def scrape_places(driver: AntiDetectDriver, link):

    # Visit an individual place and extract data
    def scrape_place_data():
        driver.get(link)

        # Accept Cookies for European users
        if driver.is_in_page("https://consent.google.com/"):
            agree_button_selector = 'form:nth-child(2) > div > div > button'
            driver.click(agree_button_selector)
            driver.get(link)

        # Extract title
        title_selector = 'h1'
        title = driver.text(title_selector)

        # Extract phone number
        phone_xpath = "//button[starts-with(@data-item-id,'phone')]"
        phone_element = driver.get_element_or_none(phone_xpath)
        phone = phone_element.get_attribute(
            "data-item-id").replace("phone:tel:", "") if phone_element else None

        return {
            "title": title,
            "phone": phone,
        }
    return scrape_place_data()

link = [
            "https://www.google.com/maps/place/Naomi+Hijab+Cirebon%2BQuinnza+Fashion/data=!4m7!3m6!1s0x2e6ee3814ba7805d:0xcdfc43d66679f690!8m2!3d-6.7027933!4d108.5417028!16s%2Fg%2F11h_v322dy!19sChIJXYCnS4Hjbi4RkPZ5ZtZD_M0?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Nobby+Hijab/data=!4m7!3m6!1s0x2e6ee3b741d03c7b:0x467f1563e5f0aa67!8m2!3d-6.7181266!4d108.54923!16s%2Fg%2F11c54gjlf6!19sChIJezzQQbfjbi4RZ6rw5WMVf0Y?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Agen+Wanoja+Hijab+Cirebon/data=!4m7!3m6!1s0x2e6f1ddc914c1293:0x57168e3cd7979691!8m2!3d-6.7362498!4d108.5526411!16s%2Fg%2F11fctd2g4m!19sChIJkxJMkdwdby4RkZaX1zyOFlc?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Afra+Hijab+Cirebon/data=!4m7!3m6!1s0x2e6eddb73fffffff:0xcf19ec3306e8e7b!8m2!3d-6.6285908!4d108.3851387!16s%2Fg%2F11c2pxgylv!19sChIJ____P7fdbi4Re45uMMOe8Qw?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Pusat+Grosir+Gamis+dan+Hijab+Cirebon+Kuningan-Althafunnisa+Pashmina/data=!4m7!3m6!1s0x2e6f1f406d343751:0x9e9d0235c715e8f!8m2!3d-6.775864!4d108.5198294!16s%2Fg%2F11q_3v3wkf!19sChIJUTc0bUAfby4Rj15xXCPQ6Qk?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Satria+Grosir+Hijab+Cirebon/data=!4m7!3m6!1s0x2e6f1f0ef3ca8323:0x63179d6b915c9090!8m2!3d-6.7530574!4d108.5172927!16s%2Fg%2F11fj4z0z45!19sChIJI4PK8w4fby4RkJBckWudF2M?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Supplier+Hijab+Cirebon+%28Antihijab.co.id%29/data=!4m7!3m6!1s0x2e6f1ffc3a647e8b:0x730c193ba22d662e!8m2!3d-6.7410278!4d108.5217455!16s%2Fg%2F11s0pyw27b!19sChIJi35kOvwfby4RLmYtojsZDHM?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Maryam+Hijab/data=!4m7!3m6!1s0x2e6ee37ed093873f:0xa65bfe620c9cbd1d!8m2!3d-6.7205063!4d108.5454966!16s%2Fg%2F11n5v51rfk!19sChIJP4eT0H7jbi4RHb2cDGL-W6Y?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Hijab+Alila+Cirebon/data=!4m7!3m6!1s0x2e6ee3f96ed2ec09:0xed718cb64dd3c57f!8m2!3d-6.6511787!4d108.5303926!16s%2Fg%2F11g8w2fc1q!19sChIJCezSbvnjbi4Rf8XTTbaMce0?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/hijab+murah+cirebon/data=!4m7!3m6!1s0x2e6f1fa7ecd07ae5:0x134505a71d7a86c!8m2!3d-6.7531077!4d108.4740826!16s%2Fg%2F11mv4dtztm!19sChIJ5XrQ7Kcfby4RbKjXcVpQNAE?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Agen+hijab+Cirebon/data=!4m7!3m6!1s0x2e6ee1ca27742e83:0x797b14684cc6c3f8!8m2!3d-6.7428626!4d108.554039!16s%2Fg%2F11lfkfknkj!19sChIJgy50J8rhbi4R-MPGTGgUe3k?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Kenes+Hijab/data=!4m7!3m6!1s0x2e6ee38285bb76b9:0x2e9d6e793a38e34c!8m2!3d-6.7179638!4d108.5499611!16s%2Fg%2F11g1lxlwqx!19sChIJuXa7hYLjbi4RTOM4OnlunS4?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Ratna+Hijab+Colection+Cirebon+%28RHCC%29/data=!4m7!3m6!1s0x2e6ee388c5e608c1:0x8676dd72ba58c9ad!8m2!3d-6.7123873!4d108.5536843!16s%2Fg%2F11fjqjk8_2!19sChIJwQjmxYjjbi4RrclYunLddoY?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Reseller+Khalifa+Hijab+%28plered-cirebon%29/data=!4m7!3m6!1s0x2e6ee1c9790df933:0xeba5617fb80f589d!8m2!3d-6.7001613!4d108.5165213!16s%2Fg%2F11pynk470m!19sChIJM_kNecnhbi4RnVgPuH9hpes?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Ar-Rohim+Hijab+Grosir+Dan+Eceran/data=!4m7!3m6!1s0x2e6ee3b529743829:0x80ab00d196423ed3!8m2!3d-6.7213974!4d108.5679506!16s%2Fg%2F11gjbdstj5!19sChIJKTh0KbXjbi4R0z5CltEAq4A?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/AZKA+Fashion+Muslim+Toko+Pakaian+Baju+Kerudung+Jilbab/data=!4m7!3m6!1s0x2e6f1d236dcc75c7:0x86605f9a46ea614f!8m2!3d-6.7549882!4d108.5450315!16s%2Fg%2F11jm6sx0w6!19sChIJx3XMbSMdby4RT2HqRppfYIY?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Yessana+Hijab+Cirebon/data=!4m7!3m6!1s0x2e6ee1ae2891ee59:0xa9d0aa09d4b13fc8!8m2!3d-6.7111598!4d108.4723637!16s%2Fg%2F11p542y1p9!19sChIJWe6RKK7hbi4RyD-x1Amq0Kk?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/AIRA+GROSIR+CIREBON+%28Aira+Hijab%29/data=!4m7!3m6!1s0x2e6ee3e3cda9368d:0x9ec3dafdd110a81a!8m2!3d-6.6989327!4d108.5395381!16s%2Fg%2F11ft6t21hg!19sChIJjTapzePjbi4RGqgQ0f3aw54?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/An-Isya+%28Anisya%29+Butik+Hijab/data=!4m7!3m6!1s0x2e6ee24944a9659d:0x488d249e93800b73!8m2!3d-6.6926542!4d108.5510836!16s%2Fg%2F11g8zy689t!19sChIJnWWpREnibi4RcwuAk54kjUg?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Aisy+Hijab+Cirebon/data=!4m7!3m6!1s0x2e6ee15cca0dbf07:0x72849cb4233d0c0!8m2!3d-6.7044565!4d108.5079237!16s%2Fg%2F11fn0s5k_v!19sChIJB78Nylzhbi4RwNAzQstJKAc?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Grosiran+Jilbab/data=!4m7!3m6!1s0x2e6f1d8d4d361d29:0x721fa3ccec457431!8m2!3d-6.730674!4d108.5432557!16s%2Fg%2F11c60djh3p!19sChIJKR02TY0dby4RMXRF7MyjH3I?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Ar-Rohim+Hijab+Grosir+Dan+Eceran/data=!4m7!3m6!1s0x2e6ee3b529743829:0x80ab00d196423ed3!8m2!3d-6.7213974!4d108.5679506!16s%2Fg%2F11gjbdstj5!19sChIJKTh0KbXjbi4R0z5CltEAq4A?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Alesha+Hijab/data=!4m7!3m6!1s0x2e6ee10a3ad578b3:0x40dac432da2d6093!8m2!3d-6.7289477!4d108.498656!16s%2Fg%2F11qpgwt2rj!19sChIJs3jVOgrhbi4Rk2At2jLE2kA?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Pusat+Hijab+Termurah+Cirebon+-+Hijab+by+Relistio/data=!4m7!3m6!1s0x2e6ee36a6d5757f9:0x19013c4c2d391370!8m2!3d-6.6872938!4d108.5476691!16s%2Fg%2F11vps7prwb!19sChIJ-VdXbWrjbi4RcBM5LUw8ARk?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Hijab/data=!4m7!3m6!1s0x2e6ee36294670685:0x9b5e661866f77db6!8m2!3d-6.7176689!4d108.560392!16s%2Fg%2F11lfk1rgqb!19sChIJhQZnlGLjbi4Rtn33ZhhmXps?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Nayla+Hijab+Grosir+Cirebon/data=!4m7!3m6!1s0x2e6edd81a0e82821:0x4da43fdd24d5515e!8m2!3d-6.6190246!4d108.3873726!16s%2Fg%2F11fwwkzqsr!19sChIJISjooIHdbi4RXlHVJN0_pE0?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Yessana+Hijab+Cirebon/data=!4m7!3m6!1s0x2e6ee1ae2891ee59:0xa9d0aa09d4b13fc8!8m2!3d-6.7111598!4d108.4723637!16s%2Fg%2F11p542y1p9!19sChIJWe6RKK7hbi4RyD-x1Amq0Kk?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/MERA+Hijab+Store/data=!4m7!3m6!1s0x2e6f1d502c26b8af:0x1f9280f6829ec469!8m2!3d-6.7400598!4d108.5236435!16s%2Fg%2F11j0wkznb9!19sChIJr7gmLFAdby4RacSegvaAkh8?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Riva+Collection+Hijab/data=!4m7!3m6!1s0x2e6ee37fbaacbde1:0x2d4424160cd75508!8m2!3d-6.72219!4d108.5299293!16s%2Fg%2F11h2nl1w_5!19sChIJ4b2sun_jbi4RCFXXDBYkRC0?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Gallery+Spirit+of+Hijab/data=!4m7!3m6!1s0x2e6f1d31a1066a1f:0x588a8fc51893f755!8m2!3d-6.7407053!4d108.5640978!16s%2Fg%2F11hz2l4z2b!19sChIJH2oGoTEdby4RVfeTGMWPilg?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/GIVAN+HIJAB/data=!4m7!3m6!1s0x2e6ee368df223d61:0x52bd002146500d4f!8m2!3d-6.7073739!4d108.5455134!16s%2Fg%2F11qnb16c4f!19sChIJYT0i32jjbi4RTw1QRiEAvVI?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Pengusaha+Hijab/data=!4m7!3m6!1s0x2e6f1d8ecfb4a1eb:0x8972c3e23d50da81!8m2!3d-6.7333668!4d108.5542531!16s%2Fg%2F11f0kswv7h!19sChIJ66G0z44dby4RgdpQPeLDcok?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Alif+Ba+Hijab+Cirebon/data=!4m7!3m6!1s0x2e6f1ddb0e98c1bd:0x59eeaf37999a1f4b!8m2!3d-6.7954131!4d108.5235559!16s%2Fg%2F11hfck897j!19sChIJvcGYDtsdby4RSx-amTev7lk?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Umama+Gallery+Cirebon/data=!4m7!3m6!1s0x2e6ee27272d1f3ff:0x27220bc4b41e8674!8m2!3d-6.7181642!4d108.5507372!16s%2Fg%2F11f_wh10r3!19sChIJ__PRcnLibi4RdIYetMQLIic?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Tafana+Hijab/data=!4m7!3m6!1s0x2e6f1d9f4e4ef0ff:0x6af2f51a98a02660!8m2!3d-6.7440761!4d108.5398651!16s%2Fg%2F11kscrkvjd!19sChIJ__BOTp8dby4RYCagmBr18mo?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/dhea+Hijab+Pasar+Balong+Cirebon/data=!4m7!3m6!1s0x2e6ee3b137802ea7:0xc21625bbc7a07c0e!8m2!3d-6.7205602!4d108.5623667!16s%2Fg%2F11f7dq4y75!19sChIJpy6AN7Hjbi4RDnygx7slFsI?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Rumah+Hijab+Nafeeza/data=!4m7!3m6!1s0x2e6ee1408b27917b:0x1e71db2fdc07337a!8m2!3d-6.7303795!4d108.466423!16s%2Fg%2F11h5w7g9nw!19sChIJe5Eni0Dhbi4RejMH3C_bcR4?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/VHIE+HIJAB+COLLECTION/data=!4m7!3m6!1s0x2e6f1d9b2ee26ebf:0x83e9658991fa1ac3!8m2!3d-6.7351629!4d108.5347821!16s%2Fg%2F11s4dh67j0!19sChIJv27iLpsdby4Rwxr6kYll6YM?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Fyla+Houseofhijab/data=!4m7!3m6!1s0x2e6ee1cfa505023d:0x82e3a398732ea714!8m2!3d-6.7183114!4d108.4849196!16s%2Fg%2F11f_dp2z27!19sChIJPQIFpc_hbi4RFKcuc5ij44I?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Ann+Hijab+Official/data=!4m7!3m6!1s0x2e6ee39aee30fa55:0x7e36dd5c64b74226!8m2!3d-6.709608!4d108.5641299!16s%2Fg%2F11lh6h8gym!19sChIJVfow7prjbi4RJkK3ZFzdNn4?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Adara+Hijab/data=!4m7!3m6!1s0x2e6ee157c2f840e1:0xb8f4dc7bd3bedcb1!8m2!3d-6.7184193!4d108.4725851!16s%2Fg%2F11g1pn3608!19sChIJ4UD4wlfhbi4Rsdy-03vc9Lg?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Qonita+Hijab+Cirebon/data=!4m7!3m6!1s0x2e6ee1bc7d7aeebb:0xac5e4226501ca4d6!8m2!3d-6.7210217!4d108.4887121!16s%2Fg%2F11t7j_ghjf!19sChIJu-56fbzhbi4R1qQcUCZCXqw?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Saqinah+Hijab/data=!4m7!3m6!1s0x2e6f1f71184ee05d:0xbc75ca897edb663a!8m2!3d-6.7598533!4d108.5147528!16s%2Fg%2F11s54644pc!19sChIJXeBOGHEfby4ROmbbfonKdbw?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Khalia%27s+Hijab/data=!4m7!3m6!1s0x2e6ee2643343b227:0xeb66852eb2b0478f!8m2!3d-6.712987!4d108.561238!16s%2Fg%2F1pzxqtc01!19sChIJJ7JDM2Tibi4Rj0ewsi6FZus?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Azzahra+Hijab+Cirebon/data=!4m7!3m6!1s0x2e6edd8e41feeb87:0x502a4ca3edee8584!8m2!3d-6.5927931!4d108.4230298!16s%2Fg%2F11s8nn6pkj!19sChIJh-v-QY7dbi4RhIXu7aNMKlA?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/zahrana+hijab/data=!4m7!3m6!1s0x2e6ee3d52a8242eb:0x82a633b5adb79f22!8m2!3d-6.6524665!4d108.535448!16s%2Fg%2F11h25sgmkh!19sChIJ60KCKtXjbi4RIp-3rbUzpoI?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Ash-fa+hijab+cirebon/data=!4m7!3m6!1s0x2e6ee114a6232499:0xb7bcd0d635cfa43d!8m2!3d-6.7197021!4d108.4905687!16s%2Fg%2F11llg5h78g!19sChIJmSQjphThbi4RPaTPNdbQvLc?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Bulma+hijab/data=!4m7!3m6!1s0x2e6ee24500000001:0x4c2f4e7957c8c26f!8m2!3d-6.7114324!4d108.5478467!16s%2Fg%2F11js77pfrs!19sChIJAQAAAEXibi4Rb8LIV3lOL0w?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/AL-Jawi+Hijab/data=!4m7!3m6!1s0x2e6ee187e834cefd:0x231a76e42cc64801!8m2!3d-6.7182131!4d108.498136!16s%2Fg%2F11fl3w_9sm!19sChIJ_c406Ifhbi4RAUjGLOR2GiM?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Dinnalul+Hijab+Butik/data=!4m7!3m6!1s0x2e6ee31552a0d733:0x1a7a141fde6a8ed9!8m2!3d-6.699148!4d108.5239632!16s%2Fg%2F11kx2wgm7y!19sChIJM9egUhXjbi4R2Y5q3h8Ueho?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Zhafira+Hijab/data=!4m7!3m6!1s0x2e6ee16ca82597b9:0xe51af332bb168465!8m2!3d-6.6634807!4d108.4920006!16s%2Fg%2F11sghy9v1h!19sChIJuZclqGzhbi4RZYQWuzLzGuU?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Berkah+Hijab+Cirebon/data=!4m7!3m6!1s0x2e6ee1b57eea11f7:0xe6e3361e21b5212!8m2!3d-6.7200742!4d108.489454!16s%2Fg%2F11v0_ff38b!19sChIJ9xHqfrXhbi4RElIb4mEzbg4?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/D%27FALISHA+HIJAB/data=!4m7!3m6!1s0x2e6f1df590293bc5:0xe53ec0b7b2493085!8m2!3d-6.7387174!4d108.5411875!16s%2Fg%2F11q4m9rmss!19sChIJxTspkPUdby4RhTBJsrfAPuU?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Deandra+Hijab/data=!4m7!3m6!1s0x2e6ee341fa2cb0e1:0x7863288f7539802e!8m2!3d-6.6890984!4d108.5505677!16s%2Fg%2F11trv6_2bt!19sChIJ4bAs-kHjbi4RLoA5dY8oY3g?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Mandjha+Ivan+Gunawan+Cirebon/data=!4m7!3m6!1s0x2e6ee268dec3f43d:0x5b967d49e4a81e4a!8m2!3d-6.7109381!4d108.5427057!16s%2Fg%2F11f126d18l!19sChIJPfTD3mjibi4RSh6o5El9lls?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/HIJAB+IN+Boutique/data=!4m7!3m6!1s0x2e6f21fa9bba896b:0x4f5592e975d485c6!8m2!3d-6.7662902!4d108.416116!16s%2Fg%2F11f7bzz24y!19sChIJa4m6m_ohby4RxoXUdemSVU8?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/SI+HIJAB+STORE/data=!4m7!3m6!1s0x2e6f05f802e7593b:0xda1f7c3514dba4a2!8m2!3d-6.837903!4d108.639186!16s%2Fg%2F11s7lx0xlw!19sChIJO1nnAvgFby4RoqTbFDV8H9o?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Mazaya+Hijab/data=!4m7!3m6!1s0x2e6f1d00d80411cb:0x2630eef260e95264!8m2!3d-6.7633785!4d108.5730053!16s%2Fg%2F11f08zf3bw!19sChIJyxEE2AAdby4RZFLpYPLuMCY?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Hilyanaa+Hijab/data=!4m7!3m6!1s0x2e6f1fc88fe28a0b:0xbc29b796970585e7!8m2!3d-6.7514227!4d108.4852256!16s%2Fg%2F11krjr8n7t!19sChIJC4rij8gfby4R54UFl5a3Kbw?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Riski+Rich+Butik+Pusat+Tempat+Penjualan+Gamis+Hijab+Terbaru/data=!4m7!3m6!1s0x2e6ee3cabc97a243:0x1a3cb6633ce1a8ac!8m2!3d-6.7113275!4d108.5426238!16s%2Fg%2F11df6b_y1_!19sChIJQ6KXvMrjbi4RrKjhPGO2PBo?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Nunia+Hijab/data=!4m7!3m6!1s0x2e6f1daf5f3fcc0f:0x11378e1229b3c22e!8m2!3d-6.758448!4d108.5628078!16s%2Fg%2F11clwk2rn3!19sChIJD8w_X68dby4RLsKzKRKONxE?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Hijab+MD+muslims/data=!4m7!3m6!1s0x2e6f1d77ece80f13:0xca141e3c3a582506!8m2!3d-6.7372886!4d108.5462929!16s%2Fg%2F11smgtmg4t!19sChIJEw_o7Hcdby4RBiVYOjweFMo?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/HBI.HIJAB/data=!4m7!3m6!1s0x2e6eddace66cb891:0x885670bd6a266f09!8m2!3d-6.6335073!4d108.3906097!16s%2Fg%2F11j9jktzzf!19sChIJkbhs5qzdbi4RCW8mar1wVog?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Andre+Va+Hijab/data=!4m7!3m6!1s0x2e6f1e4fbf27ea89:0xbfb0a15ab1ba58ac!8m2!3d-6.7596137!4d108.4851521!16s%2Fg%2F11rd9f5jrd!19sChIJieonv08eby4RrFi6sVqhsL8?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Toko+Busana+Muslim+Munadiya/data=!4m7!3m6!1s0x2e6ee27bbbdc30b1:0xc7125196eca31df1!8m2!3d-6.720642!4d108.5621644!16s%2Fg%2F11cs1h40dr!19sChIJsTDcu3vibi4R8R2j7JZREsc?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Habibah+Hijabstore+Indonesia/data=!4m7!3m6!1s0x2e6f1dae856689d9:0x311b5459753327e8!8m2!3d-6.751395!4d108.5018805!16s%2Fg%2F11gkt52r0r!19sChIJ2Ylmha4dby4R6CczdVlUGzE?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Butik+Amnia+Hijab/data=!4m7!3m6!1s0x2e6ee3561c2501ff:0x771d7ddbb8886193!8m2!3d-6.7005514!4d108.5453552!16s%2Fg%2F11hz0xx3f9!19sChIJ_wElHFbjbi4Rk2GIuNt9HXc?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Toko+Hijab+Bunda+Collection/data=!4m7!3m6!1s0x2e6ee1fbe956757f:0x38f4f2ea4650b7!8m2!3d-6.7169388!4d108.4896483!16s%2Fg%2F11jcj3f3_l!19sChIJf3VW6fvhbi4Rt1BG6vL0OAA?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Ummah+Hijab+%28GROSIR+%26+ECER+%29/data=!4m7!3m6!1s0x2e6eddbe48411cc9:0x36976a212784c011!8m2!3d-6.6122896!4d108.3860214!16s%2Fg%2F11h_67h8bx!19sChIJyRxBSL7dbi4REcCEJyFqlzY?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Toko+Hijab+Qintara/data=!4m7!3m6!1s0x2e6ee3d334a89f11:0xe6ef3ac422d4822f!8m2!3d-6.7130247!4d108.561456!16s%2Fg%2F11f7797dks!19sChIJEZ-oNNPjbi4RL4LUIsQ67-Y?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Zhitta+Hijab/data=!4m7!3m6!1s0x2e6ee3c2d5ab3b2f:0xd343c54ea9eb0a52!8m2!3d-6.6859894!4d108.5446154!16s%2Fg%2F11f7ptdb5n!19sChIJLzur1cLjbi4RUgrrqU7FQ9M?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Sumber+Hijab+Najaah+Clt+%28+Rabbani+Elzatta+Zoya+Nibras+Alnita+Scraft%29/data=!4m7!3m6!1s0x2e6f1ff79a6b60ad:0x53fbdad0066ad1e4!8m2!3d-6.7588356!4d108.4776!16s%2Fg%2F11g2337zlm!19sChIJrWBrmvcfby4R5NFqBtDa-1M?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Casriyana+Hijab+Collection/data=!4m7!3m6!1s0x2e6f1f7660b305e1:0xd0a8c237f92b1a71!8m2!3d-6.7365726!4d108.4706578!16s%2Fg%2F11j490xlqm!19sChIJ4QWzYHYfby4RcRor-TfCqNA?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Nihaya+Hijab/data=!4m7!3m6!1s0x2e6eddbe2ee3bdd5:0x38e0dddc0ed0e863!8m2!3d-6.6215315!4d108.3860843!16s%2Fg%2F11h7yg034g!19sChIJ1b3jLr7dbi4RY-jQDtzd4Dg?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Zifani+Hijab+Cirebon/data=!4m7!3m6!1s0x2e6eddaea0d6bd9b:0x2d25c62f1cd8ecb0!8m2!3d-6.6177324!4d108.386223!16s%2Fg%2F11dxm9h8hh!19sChIJm73WoK7dbi4RsOzYHC_GJS0?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Ezaya+Hijab/data=!4m7!3m6!1s0x2e6f1f83a551e677:0xe30f2d88a0b9a93d!8m2!3d-6.7557834!4d108.4706827!16s%2Fg%2F11rz2xf40b!19sChIJd-ZRpYMfby4RPam5oIgtD-M?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/VIONA+HIJAB+Grosir/data=!4m7!3m6!1s0x2e6edd21d8013cb3:0x49496760f24485c0!8m2!3d-6.6351179!4d108.3902275!16s%2Fg%2F11fnppbj1x!19sChIJszwB2CHdbi4RwIVE8mBnSUk?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Afzal+Hijab+Collection/data=!4m7!3m6!1s0x2e6ee1dc2a395675:0x3859cca627e49b6f!8m2!3d-6.67285!4d108.4648873!16s%2Fg%2F11hzsldc_m!19sChIJdVY5Ktzhbi4Rb5vkJ6bMWTg?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Toko+Ridhani+Hijab/data=!4m7!3m6!1s0x2e6f1db63e7b611b:0x8462e6de863f96c3!8m2!3d-6.7379842!4d108.531169!16s%2Fg%2F11j_2rf99p!19sChIJG2F7PrYdby4Rw5Y_ht7mYoQ?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Galeri+19+%28Hijab+Gallery%29/data=!4m7!3m6!1s0x2e6ee1922d6f8563:0x3f1c70caa202019f!8m2!3d-6.7045462!4d108.5078991!16s%2Fg%2F11bc7qz50l!19sChIJY4VvLZLhbi4RnwECospwHD8?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Jihan+Hijab/data=!4m7!3m6!1s0x2e6ee3e05ea1afc3:0x1a2f157465c8559e!8m2!3d-6.708328!4d108.5253411!16s%2Fg%2F11pcwz1_fl!19sChIJw6-hXuDjbi4RnlXIZXQVLxo?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Salma+Hijab/data=!4m7!3m6!1s0x2e6ee1e0e714b4cb:0x96d5072b4c4ced49!8m2!3d-6.6875454!4d108.4473637!16s%2Fg%2F11pklkmtl_!19sChIJy7QU5-Dhbi4RSe1MTCsH1ZY?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Dqueen+Hijab/data=!4m7!3m6!1s0x2e6f1dc1816cf48d:0xdcb715233702a7fe!8m2!3d-6.7570952!4d108.5714076!16s%2Fg%2F11stwpb7kj!19sChIJjfRsgcEdby4R_qcCNyMVt9w?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Toko+Adila+Hijab/data=!4m7!3m6!1s0x2e6f1ba462aafb0f:0x133ec057283d7308!8m2!3d-6.8250406!4d108.5338342!16s%2Fg%2F11tmy8nfrl!19sChIJD_uqYqQbby4RCHM9KFfAPhM?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Elqossam+Hijab/data=!4m7!3m6!1s0x2e6f1de87a2e6821:0x3c7e35f94c4b45b7!8m2!3d-6.7693087!4d108.5486214!16s%2Fg%2F11fwxdpdyz!19sChIJIWgueugdby4Rt0VLTPk1fjw?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Albuna+Hijab/data=!4m7!3m6!1s0x2e6f19d6edae7c5d:0xd627927b7649c4bc!8m2!3d-6.8199748!4d108.5194602!16s%2Fg%2F11sbp_9byw!19sChIJXXyu7dYZby4RvMRJdnuSJ9Y?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/HijabStory/data=!4m7!3m6!1s0x2e6f1de81344a9ad:0x6bbd9747abbe74cd!8m2!3d-6.741208!4d108.570965!16s%2Fg%2F11g1n22s6l!19sChIJralEE-gdby4RzXS-q0eXvWs?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Julia+Hijab+Collection/data=!4m7!3m6!1s0x2e6f1da52fa46edb:0xdc53bcd98aac3f72!8m2!3d-6.7643911!4d108.5528813!16s%2Fg%2F11v02v2t3d!19sChIJ226kL6Udby4Rcj-sitm8U9w?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Anti+Hijab/data=!4m7!3m6!1s0x2e6f1fe733ac5cfd:0x3e2e9792c9989cb!8m2!3d-6.7409959!4d108.5217486!16s%2Fg%2F11h32_8byz!19sChIJ_VysM-cfby4Ry4mZLHnp4gM?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/RIZKI+HIJAB/data=!4m7!3m6!1s0x2e6f1d2cdbb69ca9:0x54bcbcaa05760496!8m2!3d-6.7629499!4d108.5629956!16s%2Fg%2F11nmydw0kv!19sChIJqZy22ywdby4RlgR2Baq8vFQ?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Isti+Hijab/data=!4m7!3m6!1s0x2e6eddc21364ca99:0xed53cb6b161f4a9e!8m2!3d-6.6291324!4d108.3845945!16s%2Fg%2F11g0wspvl1!19sChIJmcpkE8Ldbi4RnkofFmvLU-0?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Rumah+Hijab+Rose/data=!4m7!3m6!1s0x2e6f079e23a05e91:0x2fd9439e424b4e8e!8m2!3d-6.8297664!4d108.7262409!16s%2Fg%2F11td4jcjs2!19sChIJkV6gI54Hby4Rjk5LQp5D2S8?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/NABILLA+HIJAB/data=!4m7!3m6!1s0x2e6ee15df2b81c81:0xad0075f78785f218!8m2!3d-6.7080333!4d108.4990091!16s%2Fg%2F11j8f80j_7!19sChIJgRy48l3hbi4RGPKFh_d1AK0?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Alvi+Hijab+Talun/data=!4m7!3m6!1s0x2e6f1f709283b3bb:0x37cfd7eee37f0833!8m2!3d-6.7512056!4d108.5142991!16s%2Fg%2F11jp01kn0d!19sChIJu7ODknAfby4RMwh_4-7Xzzc?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Hy+Hijab/data=!4m7!3m6!1s0x2e6ee1df72266f8f:0x7d0d611f1a376bb5!8m2!3d-6.7139542!4d108.5043276!16s%2Fg%2F11p_6s6qn9!19sChIJj28mct_hbi4RtWs3Gh9hDX0?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Hijab+Ali+Official/data=!4m7!3m6!1s0x2e6edd4f36872331:0xb543b9068e35b545!8m2!3d-6.6209698!4d108.3860106!16s%2Fg%2F11gslv3cmg!19sChIJMSOHNk_dbi4RRbU1jga5Q7U?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Kartika+Hijab/data=!4m7!3m6!1s0x2e6f1d185cd4b37d:0x9e24e443a1e51a5c!8m2!3d-6.7483294!4d108.5660284!16s%2Fg%2F11fm42krcj!19sChIJfbPUXBgdby4RXBrloUPkJJ4?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Gantari+Hijab/data=!4m7!3m6!1s0x2e6f1ba24003d155:0x5de88fd380d09e2b!8m2!3d-6.8294599!4d108.609611!16s%2Fg%2F11tdsws20g!19sChIJVdEDQKIbby4RK57QgNOP6F0?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Florie+Stuff+%28Fashion,+Kids+%26+Hijab%29/data=!4m7!3m6!1s0x2e6edda9b97d040f:0xa7967f3fd46a805b!8m2!3d-6.6092017!4d108.4194293!16s%2Fg%2F11ppn659k6!19sChIJDwR9uandbi4RW4Bq1D9_lqc?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Toko+Hijab+Tiga+Putri+%28Bunda+Ghea%29/data=!4m7!3m6!1s0x2e6ee3e3d5abc223:0xf9c6c2e1f3b6f0da!8m2!3d-6.7208415!4d108.5679503!16s%2Fg%2F11h4gq99dv!19sChIJI8Kr1ePjbi4R2vC28-HCxvk?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/MAZAY+HIJAB/data=!4m7!3m6!1s0x2e6f05b37bcda111:0xbc2965e91db16e13!8m2!3d-6.8082315!4d108.6335119!16s%2Fg%2F11k4v9c9bg!19sChIJEaHNe7MFby4RE26xHellKbw?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Dessi+hijab/data=!4m7!3m6!1s0x2e6ee301e8ba0c27:0x6ac8af635f4b6f0b!8m2!3d-6.7082963!4d108.5674754!16s%2Fg%2F11q3_pgqz7!19sChIJJwy66AHjbi4RC29LX2OvyGo?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Shanum+Store+Cirebon/data=!4m7!3m6!1s0x2e6ee1062db94e6d:0x787fa0e617ed12a5!8m2!3d-6.7152494!4d108.5028853!16s%2Fg%2F11rx0m5vmw!19sChIJbU65LQbhbi4RpRLtF-agf3g?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Grosir+Hijab+Almaya/data=!4m7!3m6!1s0x2e6edd91402d2b7d:0xeb835f79b2f1ae00!8m2!3d-6.6340983!4d108.3904016!16s%2Fg%2F11sh4s14t9!19sChIJfSstQJHdbi4RAK7xsnlfg-s?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Zea+Hijab+Grosir+%26+Eceran/data=!4m7!3m6!1s0x2e6ee375408f5bd7:0xc6a52274b5891865!8m2!3d-6.7217628!4d108.5637041!16s%2Fg%2F11gjv72zcq!19sChIJ11uPQHXjbi4RZRiJtXQipcY?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Zoya+Cirebon/data=!4m7!3m6!1s0x2e6ee2144ff9dae1:0xcda59a5805dcd629!8m2!3d-6.7145982!4d108.5530141!16s%2Fg%2F11cs132stf!19sChIJ4dr5TxTibi4RKdbcBViapc0?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Evamshop+Toko+Hijab+Turki+Original/data=!4m7!3m6!1s0x2e6f1d9df719a3a5:0xfb01a6dd5d4abdc6!8m2!3d-6.806066!4d108.614736!16s%2Fg%2F11q3mv4rj5!19sChIJpaMZ950dby4Rxr1KXd2mAfs?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/BEVERLY+INDONESIA+GROSIR+BAJU+KOKO+MUSLIM+CIREBON/data=!4m7!3m6!1s0x2e6f1daee97e4635:0x5055e75bfb5c61c4!8m2!3d-6.7536271!4d108.5248667!16s%2Fg%2F11tdrd6k76!19sChIJNUZ-6a4dby4RxGFc-1vnVVA?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/AnnisaStore+Hijabers+Cirebon/data=!4m7!3m6!1s0x2e6f04cd7629f7ff:0x992660c3052cbc7d!8m2!3d-6.8342623!4d108.6212164!16s%2Fg%2F11c325qzz3!19sChIJ__cpds0Eby4RfbwsBcNgJpk?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/NakNik+Hijab/data=!4m7!3m6!1s0x2e6f05dc7aeec421:0x48f56066d7c87ae3!8m2!3d-6.825127!4d108.6186655!16s%2Fg%2F11pckh1svq!19sChIJIcTuetwFby4R43rI12Zg9Ug?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Rensiie+Shop+Grosir+hijab+%26+Gamis+Murah/data=!4m7!3m6!1s0x2e6f1f01add107e5:0xcc0e5e9c58d8f4ce!8m2!3d-6.7409091!4d108.4497643!16s%2Fg%2F11rpx0nb26!19sChIJ5QfRrQEfby4RzvTYWJxeDsw?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/ZAYN+HIJAB+STORE/data=!4m7!3m6!1s0x2e6f1f34c3572d31:0x569ddf0c1f054f58!8m2!3d-6.7580274!4d108.5071718!16s%2Fg%2F11v0hm8zb4!19sChIJMS1XwzQfby4RWE8FHwzfnVY?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/An+Nafi+Hijab/data=!4m7!3m6!1s0x2e6ee10abdb614b5:0x5148e4c9b4a6ff18!8m2!3d-6.7260607!4d108.4880359!16s%2Fg%2F11p9b7jg5s!19sChIJtRS2vQrhbi4RGP-mtMnkSFE?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Hijab+Collections/data=!4m7!3m6!1s0x2e6f1f04ed42b68d:0xc7678258f5844a0f!8m2!3d-6.7557996!4d108.5093896!16s%2Fg%2F11pbyhkmzg!19sChIJjbZC7QQfby4RD0qE9ViCZ8c?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Nataij+Hijab+Store/data=!4m7!3m6!1s0x2e6edd22a687c241:0xe173ae7d5dd1538a!8m2!3d-6.6182961!4d108.3874397!16s%2Fg%2F11hzcyb23v!19sChIJQcKHpiLdbi4RilPRXX2uc-E?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Toko+Erlinah+Hijab/data=!4m7!3m6!1s0x2e6f1f75904f3f17:0x37f67f92f2fe2f71!8m2!3d-6.7564847!4d108.4624704!16s%2Fg%2F11j9d4444m!19sChIJFz9PkHUfby4RcS_-8pJ_9jc?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Jj+Grosir+Hijab/data=!4m7!3m6!1s0x2e6edd243e787f37:0x6da918456f6ea86b!8m2!3d-6.6136733!4d108.3835045!16s%2Fg%2F11rjw54lg4!19sChIJN394PiTdbi4Ra6hub0UYqW0?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Saffanah+Hijab+Style/data=!4m7!3m6!1s0x2e6f1f7d1db53a97:0x45f7153dffe9995e!8m2!3d-6.7585721!4d108.4907161!16s%2Fg%2F11qy98cjvx!19sChIJlzq1HX0fby4RXpnp_z0V90U?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Hijab+Segi+Empat+Motif+Terbaru/data=!4m7!3m6!1s0x2e6edd3c88017a03:0x19a85bc0273827e8!8m2!3d-6.6211191!4d108.3894169!16s%2Fg%2F11f8hy8d97!19sChIJA3oBiDzdbi4R6Cc4J8BbqBk?authuser=0&hl=en&rclk=1",
            "https://www.google.com/maps/place/Hijabelline.co/data=!4m7!3m6!1s0x2e6f0527c171446b:0x126b20f6c923a846!8m2!3d-6.8307897!4d108.6317487!16s%2Fg%2F11jfl_j96f!19sChIJa0RxwScFby4RRqgjyfYgaxI?authuser=0&hl=en&rclk=1"
]
     
if __name__ == "__main__":
    # Initiate the web scraping link
    scrape_places(link)
