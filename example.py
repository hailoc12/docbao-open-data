# Chương trình: Khai thác dữ liệu báo chí từ nguồn "Theo Dõi Báo Chí"
# Tác giả     : hailoc12
# Mô tả       : Theo Dõi Báo Chí (http://theodoibaochi.com) là một website sử dụng mã nguồn Đọc Báo với mục tiêu quét toàn bộ các trang bbáo mạng phổ biến tại Việt Nam. Dữ liệu được quét 10p / lần và có thể truy cập dễ dàng thông qua dự án Docbao-Open-Data 

open_data = DocbaoOpenData("http://theodoibaochi.com")
open_data.update_data() # Tải dữ liệu từ server

# In ra một số thông tin cơ bản về tập data:
print("This dataset contains:")
print("Newspaper: %s"  % open_data.count_articles())  # Số nguồn báo quét
print("Articles : %s"  % open_data.count_newspapers())# Tổng số bài báo tập data này chứa
print("Updated  : %s"  % open_data.get_update_time()) # Thời điểm data này được cập nhật

# Một số thao tác cơ bản trên tập dữ liệu:
    # In bài báo cũ nhất trong tập dữ liệu
    article = open_data.get_article(0)
    print("In bài báo cũ nhất:")
    print("Tiêu đề     : %s" %s article.get_topic()
    print("Báo         : %s" %s article.get_newspaper())
    print("Xuất bản    : %s" %s article.get_published_dated())
    print("Link        : %s" %s article.get_href())

    # 
