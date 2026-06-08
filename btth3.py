available_seats = 50 
flight_revenue = 0.0
BASE_PRICE = 2000.0

def Book_flight_tickets():
    global available_seats, BASE_PRICE
    while True:
        try:
            quantity = int(input("nhập số lượng vé (nhập -1 nếu muốn thoát): "))
            if quantity == -1: break
            if quantity > 0 and quantity <= available_seats:
                break
            else:
                print("Số lượng ghế không thể đáp ứng!")
        except ValueError:
            print("Vui lòng nhập số nguyên!")
    while True:
        try:
            ticket = int(input("hạng vé (1 cho Economy, 2 cho Business): "))
            if ticket == 1 or ticket == 2:
                break
            else:
                print("Lựa chọn hạng vé không hợp lệ!")
                break
        except ValueError:
            print("Vui lòng nhập số nguyên!")
    text = ""
    total_tickets = 0
    if ticket == 1: 
        total_tickets = (BASE_PRICE * quantity)
        text = "Economy"
    else:
        total_tickets = (BASE_PRICE * quantity * 1.5)
        text = "Business"
    print("-> Xác nhận đặt chỗ:")
    print(f"Số lượng: {quantity} | Hạng: {text}")
    print(f"Tạm tính: ${total_tickets:.1f}")
    print(f"Phí dịch vụ (5%): ${total_tickets * 0.05}")
    total_tickets *= 1.05
    print(f"Tổng thanh toán: ${total_tickets}")
    available_seats -= quantity
    print(f"Đặt vé thành công! Ghế trống còn lại: {available_seats}")
    return total_tickets

def Cancellation_Refund():
    global available_seats, BASE_PRICE

    print("--- HỦY VÉ & HOÀN TIỀN ---")
    while True:
        try:
            quantity = int(input("Nhập số lượng vé muốn hủy (nhập -1 nếu muốn thoát): "))
            if quantity == -1: break
            if quantity > 0 and 50 >= available_seats + quantity:
                break
            else:
                print("Số lượng ghế hoàn không thể đáp ứng!")
        except ValueError:
            print("Vui lòng nhập số nguyên!")
    value = quantity * BASE_PRICE * 0.8
    print(f"Hủy vé thành công. Hệ thống đã hoàn lại: ${value} (80% giá cơ bản).")
    available_seats += quantity
    print(f"Ghế trống hiện tại: {available_seats}")
    return value


def Check_flight_status():
    global available_seats, flight_revenue
    print(f"""--- TÌNH TRẠNG CHUYẾN BAY VN2026 ---
Sức chứa tối đa: 50
Ghế đã đặt: {50 -available_seats}
Ghế trống: {available_seats}
Tổng doanh thu hiện tại: ${flight_revenue}
          """)



while True:
    print("""
============= SKYBOOKING SYSTEM =============
Chuyến bay: VN2026 | Khởi hành: Hà Nội
1. Đặt vé máy bay
2. Hủy vé & Hoàn tiền
3. Xem tình trạng chuyến bay
4. Đóng hệ thống
=============================================
""")
    while True:
        try:
            choice = int(input("Chọn chức năng (1-4): "))
            if choice >= 1 and choice <= 4:
                break
            else:
                print("Chọn từ 1 - 4")
        except ValueError:
            print("Chọn từ 1 - 4")
    match choice:
        case 1:
            flight_revenue += Book_flight_tickets()
        case 2:
            flight_revenue -= Cancellation_Refund()
        case 3:
            Check_flight_status()
        case 4:
            print("Kết thúc chương trình!")
            break
