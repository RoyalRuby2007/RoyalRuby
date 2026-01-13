import pandas as pd
import unicodedata
import time
s = time.time()

#Hàm xử lý yêu cầu
def ReQuest():
    print ("----------------------TRANG CHỦ----------------------")
    print ("--vui lòng nhập các số sau để thực hiện các yêu cầu--")
    print ("  1 : Tìm kiếm sinh viên")
    print ("  2 : Xếp hạng sinh viên")
    print ("  3 : Đánh giá học lực của sinh viên")
    print ("  4 : Gửi bảng qua Gmail (tỉ lệ hoạt động 10%)")
    print ("  5 : Thêm thông tin của một sinh viên vào bảng")
    print ("  6 : Xóa thông tin của một sinh viên trong bảng")
    print ("  7 : sắp xếp tên sinh viên theo alphabet")
    print ("  8 : Reset bảng lại từ đầu")
    print ("  9 : Xuất ra file CSV")
    print ("  10 : Thoát")

#Hàm tìm kiếm
def SearchFor():
    print ("--Bạn muốn tìm kiếm theo: ?--")
    print ("  1 : Tìm kiếm theo Số thứ tự")
    print ("  2 : Tìm kiếm theo mã sinh viên")
    print ("  3 : Tìm kiếm theo tên")
    print ("  4 : Tìm kiếm theo ngày sinh")
    print ("  5 : Quay trở lại trang chủ")

def SearchForSTT(n):
    if (1 <= n <= len(Ds)):
        print (Ds.loc[n].to_string())
    else:
        print ("Số thứ tự trên không có trong bảng dữ liệu!")
        
def SearchForMaSV(n):
    result = Ds[Ds.Mã_SV == n]
    if (result.empty == False):
        print (result.to_string())
    else:
        print ("Mã sinh viên trên không có trong bảng dữ liệu!")
        
def SearchForName(S):
    result = Ds[Ds.Họ_và_tên == S]
    if (result.empty == False):
        print (result.to_string())
    else:
        print ("Họ và tên trên không có trong bảng dữ liệu!")

def SearchForDate(S):
    result = Ds[Ds.Ngày_sinh == S]
    if (result.empty == False):
        print (result.to_string())
    else:
        print ("Ngày sinh như trên không có trong bảng dữ liệu!")

#Hàm xếp hạng
def RankingFor():
    print ("--Bạn muốn xếp hạng theo: ?--")
    print ("  1 : Xếp hạng theo điểm thành phần 1")
    print ("  2 : Xếp hạng theo điểm thành phần 2")
    print ("  3 : Xếp hạng theo tổng điểm")
    print ("  4 : Quay trở lại trang chủ")

def RankingForTP1(Ds):
    Dssort = Ds.sort_values("Điểm_TP_1" , ascending=False)
    
    Dssort = Dssort.reset_index(drop=True)
    Dssort.index += 1
    Dssort.index.name = "STT"
    
    print (Dssort.to_string())
    return Dssort
    
def RankingForTP2(Ds):    
    Dssort = Ds.sort_values("Điểm_TP_2" , ascending=False)
    
    Dssort = Dssort.reset_index(drop=True)
    Dssort.index += 1
    Dssort.index.name = "STT"
    
    print (Dssort.to_string())
    return Dssort
    
def RankingForScore(Ds):
    Dssort = Ds.sort_values("Tổng_điểm" , ascending=False)
    
    Dssort = Dssort.reset_index(drop=True)
    Dssort.index += 1
    Dssort.index.name = "STT"
    
    print (Dssort.to_string())
    return Dssort

#Hàm đánh giá học lực
def Assess(Ds):
    Ds["Xếp loại"] = pd.cut(
        Ds["Tổng_điểm"],
        bins=[0, 5, 6.5, 8, 10],
        labels=["Yếu", "TB", "Khá", "Giỏi"]
    )
    print (Ds.to_string())
    return Ds

#Hàm thêm thông tin sinh viên
def Add(Ds):
    ID = int(input("Mã sinh viên: "))
    Name = input("Tên sinh viên: ")
    Date = input("Ngày sinh của sinh viên: ")
    Class = "QH-2025-I/CQ-I-CS4"
    Tp1 = int(input("Điểm thành phần 1 của sinh viên: "))
    Tp2 = int(input("Điểm thành phần 2 của sinh viên: "))
    Score = 0.25 * (Tp1) + 0.75 * (Tp2)
    Ds.loc[len(Ds) + 1] = [ID , Name , Date , Class , Tp1 , Tp2 , Score]
    print (Ds.to_string())
    return Ds

#Hàm xóa thông tin sinh viên
def PopFor():
    print ("--Bạn muốn xóa theo: ?--")
    print ("  1 : Xóa theo Số thứ tự")
    print ("  2 : Xóa theo mã sinh viên")
    print ("  3 : Xóa theo tên")
    print ("  4 : Xóa theo ngày sinh")
    print ("  5 : Xóa theo điểm TP1")
    print ("  6 : Xóa theo điểm TP2")
    print ("  7 : Xóa theo tổng điểm")
    print ("  8 : Xóa theo điều kiện")
    print ("  9 : Quay trở lại trang chủ")
    
def PopForSTT(Ds):
    n = int(input("Số thứ tự của sinh viên"))
    if (1 <= n <= len(Ds)):
        Ds.drop(n)
        
        DsS = Ds.reset_index(drop=True)
        DsS.index += 1
        DsS.index.name = "STT"
        
        print (DsS.to_string())
        
        return DsS    
    else:
        print ("Số thứ tự trên không có trong bảng dữ liệu!")

def PopForID(Ds):
    Dspoped = Ds[Ds["Mã_SV"] != int(input("Mã sinh viên: "))]
    
    Dspoped = Dspoped.reset_index(drop=True)
    Dspoped.index += 1
    Dspoped.index.name = "STT"
    
    print (Dspoped.to_string())
    return Dspoped

def PopForName(Ds):
    Dspoped = Ds[Ds["Họ_và_tên"] != input("Họ và tên của sinh viên: ")]
    
    Dspoped = Dspoped.reset_index(drop=True)
    Dspoped.index += 1
    Dspoped.index.name = "STT"
    
    print (Dspoped.to_string())
    return Dspoped

def PopForDate(Ds):
    Dspoped = Ds[Ds["Ngày_sinh"] != input("Ngày sinh của sinh viên: ")]
    
    Dspoped = Dspoped.reset_index(drop=True)
    Dspoped.index += 1
    Dspoped.index.name = "STT"
    
    print (Dspoped.to_string())
    return Dspoped

def PopForTP1(Ds):
    Dspoped = Ds[Ds["Điểm_TP_1"] != int(input("Điểm TP1 của sinh viên: "))]
    
    Dspoped = Dspoped.reset_index(drop=True)
    Dspoped.index += 1
    Dspoped.index.name = "STT"
    
    print (Dspoped.to_string())
    return Dspoped

def PopForTP2(Ds):
    Dspoped = Ds[Ds["Điểm_TP_2"] != int(input("Điểm TP2 của sinh viên: "))]
    
    Dspoped = Dspoped.reset_index(drop=True)
    Dspoped.index += 1
    Dspoped.index.name = "STT"
    
    print (Dspoped.to_string())
    return Dspoped

def PopForScore(Ds):
    Dspoped = Ds[Ds["Tổng_điểm"] != int(input("Tổng điểm của sinh viên: "))]
    
    Dspoped = Dspoped.reset_index(drop=True)
    Dspoped.index += 1
    Dspoped.index.name = "STT"
    
    print (Dspoped.to_string())
    return Dspoped

def PopForCondition():
    print ("--Bạn muốn xóa theo: ?--")
    print ("  1 : Xóa tất cả sinh viên có điểm TP1 bé hơn: ")
    print ("  2 : Xóa tất cả sinh viên có điểm TP1 bé hơn bằng: ")
    print ("  3 : Xóa tất cả sinh viên có điểm TP1 lớn hơn: ")
    print ("  4 : Xóa tất cả sinh viên có điểm TP1 lớn hơn bằng: ")
    print ("  5 : Xóa tất cả sinh viên có điểm TP2 bé hơn: ")
    print ("  6 : Xóa tất cả sinh viên có điểm TP2 bé hơn bằng: ")
    print ("  7 : Xóa tất cả sinh viên có điểm TP2 lớn hơn: ")
    print ("  8 : Xóa tất cả sinh viên có điểm TP2 lớn hơn bằng: ")
    print ("  9 : Xóa tất cả sinh viên có tổng điểm bé hơn: ")
    print ("  10 : Xóa tất cả sinh viên có tổng điểm bé hơn bằng: ")
    print ("  11 : Xóa tất cả sinh viên có tổng điểm lớn hơn: ")
    print ("  12 : Xóa tất cả sinh viên có tổng điểm lớn hơn bằng: ")
    print ("  13 : Quay trở lại")
    
def PopForC1(Ds):
    Dspoped = Ds[Ds["Điểm_TP_1"] >= int(input())]
    
    Dspoped = Dspoped.reset_index(drop=True)
    Dspoped.index += 1
    Dspoped.index.name = "STT"
    
    print (Dspoped.to_string())
    return Dspoped

def PopForC2(Ds):
    Dspoped = Ds[Ds["Điểm_TP_1"] > int(input())]
    
    Dspoped = Dspoped.reset_index(drop=True)
    Dspoped.index += 1
    Dspoped.index.name = "STT"
    
    print (Dspoped.to_string())
    return Dspoped

def PopForC3(Ds):
    Dspoped = Ds[Ds["Điểm_TP_1"] <= int(input())]
    
    Dspoped = Dspoped.reset_index(drop=True)
    Dspoped.index += 1
    Dspoped.index.name = "STT"
    
    print (Dspoped.to_string())
    return Dspoped

def PopForC4(Ds):
    Dspoped = Ds[Ds["Điểm_TP_1"] < int(input())]
    
    Dspoped = Dspoped.reset_index(drop=True)
    Dspoped.index += 1
    Dspoped.index.name = "STT"
    
    print (Dspoped.to_string())
    return Dspoped

def PopForC5(Ds):
    Dspoped = Ds[Ds["Điểm_TP_2"] >= int(input())]
    
    Dspoped = Dspoped.reset_index(drop=True)
    Dspoped.index += 1
    Dspoped.index.name = "STT"
    
    print (Dspoped.to_string())
    return Dspoped

def PopForC6(Ds):
    Dspoped = Ds[Ds["Điểm_TP_2"] > int(input())]
    
    Dspoped = Dspoped.reset_index(drop=True)
    Dspoped.index += 1
    Dspoped.index.name = "STT"
    
    print (Dspoped.to_string())
    return Dspoped

def PopForC7(Ds):
    Dspoped = Ds[Ds["Điểm_TP_2"] <= int(input())]
    
    Dspoped = Dspoped.reset_index(drop=True)
    Dspoped.index += 1
    Dspoped.index.name = "STT"
    
    print (Dspoped.to_string())
    return Dspoped

def PopForC8(Ds):
    Dspoped = Ds[Ds["Điểm_TP_2"] < int(input())]
    
    Dspoped = Dspoped.reset_index(drop=True)
    Dspoped.index += 1
    Dspoped.index.name = "STT"
    
    print (Dspoped.to_string())
    return Dspoped

def PopForC9(Ds):
    Dspoped = Ds[Ds["Tổng_điểm"] >= int(input())]
    
    Dspoped = Dspoped.reset_index(drop=True)
    Dspoped.index += 1
    Dspoped.index.name = "STT"
    
    print (Dspoped.to_string())
    return Dspoped

def PopForC10(Ds):
    Dspoped = Ds[Ds["Tổng_điểm"] > int(input())]
    
    Dspoped = Dspoped.reset_index(drop=True)
    Dspoped.index += 1
    Dspoped.index.name = "STT"
    
    print (Dspoped.to_string())
    return Dspoped

def PopForC11(Ds):
    Dspoped = Ds[Ds["Tổng_điểm"] <= int(input())]
    
    Dspoped = Dspoped.reset_index(drop=True)
    Dspoped.index += 1
    Dspoped.index.name = "STT"
    
    print (Dspoped.to_string())
    return Dspoped

def PopForC12(Ds):
    Dspoped = Ds[Ds["Tổng_điểm"] < int(input())]
    
    Dspoped = Dspoped.reset_index(drop=True)
    Dspoped.index += 1
    Dspoped.index.name = "STT"
    
    print (Dspoped.to_string())
    return Dspoped

#Hàm sắp xếp theo Alphabet
def remove_accents_keep_d(text: str) -> str:
    text = text.replace("Đ", "D~").replace("đ", "d~")
    text = ''.join(
        c for c in unicodedata.normalize('NFD', text)
        if unicodedata.category(c) != 'Mn'
    )
    return text.lower()

def vietnamese_name_sort_key(name: str) -> str:
    parts = name.strip().split()
    reordered = " ".join([parts[-1]] + parts[:-1])
    return remove_accents_keep_d(reordered)

def SortAlphabet(Ds):
    DsSorted = Ds.sort_values(
        by="Họ_và_tên",
        key=lambda col: col.apply(vietnamese_name_sort_key)
    )
    
    DsSort = DsSorted.reset_index(drop=True)
    DsSort.index += 1
    DsSort.index.name = "STT"
    
    print (DsSort.to_string())
    
    return DsSort

#Hàm Reset bảng
def reset():
    Ds = pd.read_csv("sv-1.csv" , index_col = "STT")
    print (Ds.to_string())
    return Ds

#Hàm xuất bảng ra file
def PrintOut(S):
    Ds.to_csv(S, index=False, encoding="utf-8-sig")

#Main
Ds = pd.read_csv("sv-1.csv" , index_col = "STT")

#***
pd.set_option("display.unicode.east_asian_width", True)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 140)
#***

print (Ds.to_string())

Drequest = []
request = -1
while (request != 10):
    ReQuest()
    request = int(input("Yêu cầu số: "))
    while (request == 1):
        SearchFor()
        n = int(input("Yêu cầu số: "))
        if (n == 1):
            SearchForSTT(int(input("Số thứ tự: ")))
        elif (n == 2):
            SearchForMaSV(int(input("Mã sinh viên: ")))
        elif (n == 3):
            SearchForName(input("Họ và tên: "))
        elif (n == 4):
            SearchForDate(input("Ngày sinh: "))
        elif (n == 5):
            break
    while (request == 2):
        RankingFor()
        n = int(input("Yêu cầu số: "))
        if (n == 1):
            Ds = RankingForTP1(Ds)
        elif (n == 2):
            Ds = RankingForTP2(Ds)
        elif (n == 3):
            Ds = RankingForScore(Ds)
        elif (n == 4):
            break
    if (request == 3):
        Ds = Assess(Ds)
    if (request == 4):
        print ("Xin lỗi vì sự bất tiện này nhưng công cụ chưa hoạt động :<")
    if (request == 5):
        Ds = Add(Ds)
    while (request == 6):
        PopFor()
        n = int(input("Yêu cầu số: "))
        if (n == 1):
            Ds = PopForSTT(Ds)
        elif (n == 2):
            Ds = PopForID(Ds)
        elif (n == 3):
            Ds = PopForName(Ds)
        elif (n == 4):
            Ds = PopForDate(Ds)
        elif (n == 5):
            Ds = PopForTP1(Ds)
        elif (n == 6):
            Ds = PopForTP2(Ds)
        elif (n == 7):
            Ds = PopForScore(Ds)
        elif (n == 8):
            PopForCondition()
            n = int(input("Yêu cầu số: "))
            if (n == 1):
                Ds = PopForC1(Ds)
            elif (n == 2):
                Ds = PopForC2(Ds)
            elif (n == 3):
                Ds = PopForC3(Ds)
            elif (n == 4):
                Ds = PopForC4(Ds)
            elif (n == 5):
                Ds = PopForC5(Ds)
            elif (n == 6):
                Ds = PopForC6(Ds)
            elif (n == 7):
                Ds = PopForC7(Ds)
            elif (n == 8):
                Ds = PopForC8(Ds)
            elif (n == 9):
                Ds = PopForC9(Ds)
            elif (n == 10):
                Ds = PopForC10(Ds)
            elif (n == 11):
                Ds = PopForC11(Ds)
            elif (n == 12):
                Ds = PopForC12(Ds)
            elif (n == 13):
                break
        elif (n == 9):
            break
    if (request == 7):
        Ds = SortAlphabet(Ds)
    if (request == 8):
        Ds = reset()
    if (request == 9):
        PrintOut(input("Tên file: "))
    if (request == 10):
        continue

e = time.time()
print ("Thời gian chạy chương trình: " + str(e - s) + "s")