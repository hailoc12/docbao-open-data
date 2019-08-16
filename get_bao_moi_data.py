# Chương trình: Khai thác dữ liệu báo chí từ nguồn "Theo Dõi Báo Chí" thông qua API
# Tác giả     : hailoc12
# Ngày tạo    : 16/08/2019
#-------------------------------------------------------------------------------------------------------------
from lib.open_data import *
from time import sleep

API_URL = "http://baomoi.ap.ngrok.io/v1/search"
AUTH_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE1NjU4ODc0NzUsImV4cCI6MTY1MjI4NzQ4MCwic3ViIjoidGhlb2RvaWJhb2NoaSJ9.M9I01fkn-Qu34UTR-9UkMIGC-QSG201T7Hcz4AQmR74"
docbao = DocbaoOpenData("https://theodoibaochi.com", API_URL, AUTH_TOKEN) 

CATEGORY = ["xa_hoi", "thoi_su", "giao_thong", "moi_truong", "the_gioi", "van_hoa", "nghe_thuat", "du_lich", "am_thuc", "kinh_te", "kinh_doanh", "viec_lam", "tai_chinh", "chung_khoan", "giao_duc", "du_hoc", "the_thao", "bong_da_quoc_te", "bong_da_viet_nam", "quan_vot", "giai_tri", "thoi_trang", "phap_luat", "an_ninh", "cong_nghe", "cntt_vien_thong", "thiet_bi_phan_cung", "khoa_hoc", "doi_song", "lam_dep", "tinh_yeu_hon_nhan", "suc_khoe", "nha_dat", "quy_hoach", "kien_truc"]

print("Load Bao Moi data...")

data = {}
for cat in CATEGORY:
    print("Load articles in %s category" % cat)
    search_string = ''
    full_search = False
    tag_filter = cat
    result = docbao.search_articles(search_string, full_search, tag_filter)
    if result:
        print("Loaded %s articles" % len(result))
        data[cat] = result
    sleep(0.5)

# print an article for example
print("Print example article")
article = data['thoi_su'][0]
print(article['topic'])

# do other things with data here
#
#
#



