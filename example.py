# Chương trình: Khai thác dữ liệu báo chí từ nguồn "Theo Dõi Báo Chí"
# Tác giả     : hailoc12
#-------------------------------------------------------------------------------------------------------------
from lib.open_data import *

open_data = DocbaoOpenData("http://theodoibaochi.com") 

print("Tải dữ liệu...")
open_data.download_data() 
open_data.load_data() 
print("OK")
print()

# Exam1: In ra một số thông tin cơ bản về dataset đã tải:

print("#Example 1: Thông tin cơ bản về dataset")

print("Tập dữ liệu này bao gồm:")
print("Số bài báo        : %s"  % open_data.count_articles())  # Số nguồn báo quét
print("Số nguốn báo quét : %s"  % open_data.count_newspapers())# Tổng số bài báo tập data này chứa
print("Cập nhật lúc      : %s"  % open_data.get_update_time()) # Thời điểm data này được cập nhật

print()
input("Nhấn Enter để tiếp tục")
print()

# Exam2: Hiển thị bài báo mới nhất trong dataset

article_list = open_data.get_article_list() ## Lấy danh sách toàn bộ các bài báo trong dataset

article = article_list[0] # Danh sách báo được sắp xếp theo thứ tự giảm dần của thời điểm quét

print("#Example 2: Hiển thị bài báo mới nhất")

print("In bài báo mới nhất:")
print("Tiêu đề     : %s" % article['topic'])
print("Báo         : %s" % article['newspaper'])
print("Xuất bản    : %s" % article['publish_time'])
print("Link        : %s" % article['href'])

print()
input("Nhấn Enter để tiếp tục")
print()

# Exam3: Hiển thị danh sách các bài báo có chứa từ khóa "startup"

article_list = open_data.get_articles_contain("startup")
open_data.display_list(message="#Example 3: Danh sách các bài báo có chứa từ khoá startup", articles=article_list, full_info=False)

print()
input("Nhấn Enter để tiếp tục")
print()

# Exam 4: Hiển thị danh sách các chủ đề hot trên báo chí trong 3h gần đây
trending_keyword_list = open_data.get_trending_keyword_list()
open_data.display_list(message="#Example 4: Danh sách các chủ đề hot trên báo chí trong 3h gần đây", keywords=trending_keyword_list, full_info=False)

print()
input("Nhấn Enter để tiếp tục")
print()

# Your Example Here
#
#
#
