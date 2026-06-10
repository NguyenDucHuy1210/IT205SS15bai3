available_seats = 50
flight_revenue = 0.0
BASE_PRICE = 2000.0


def Book_flight_tickets():
    global available_seats

    while True:
        try:
            quantity = int(input("Nhập số lượng vé (nhập -1 nếu muốn thoát): "))

            if quantity == -1:
                return 0

            if 0 < quantity <= available_seats:
                break

            print("Số lượng ghế không thể đáp ứng!")

        except ValueError:
            print("Vui lòng nhập số nguyên!")

    while True:
        try:
            ticket = int(input("Hạng vé (1 cho Economy, 2 cho Business): "))

            if ticket == 1 or ticket == 2:
                break

            print("Lựa chọn hạng vé không hợp lệ!")

        except ValueError:
            print("Vui lòng nhập số nguyên!")

    if ticket == 1:
        ticket_type = "Economy"
        subtotal = quantity * BASE_PRICE
    else:
        ticket_type = "Business"
        subtotal = quantity * BASE_PRICE * 1.5

    service_fee = subtotal * 0.05
    total = subtotal + service_fee

    print("-> Xác nhận đặt chỗ:")
    print(f"Số lượng: {quantity} | Hạng: {ticket_type}")
    print(f"Tạm tính: ${subtotal:.1f}")
    print(f"Phí dịch vụ (5%): ${service_fee:.1f}")
    print(f"Tổng thanh toán: ${total:.1f}")

    available_seats -= quantity

    print(f"Đặt vé thành công! Ghế trống còn lại: {available_seats}")

    return total


def Cancellation_Refund():
    global available_seats

    print("--- HỦY VÉ & HOÀN TIỀN ---")

    while True:
        try:
            quantity = int(input("Nhập số lượng vé muốn hủy (nhập -1 nếu muốn thoát): "))

            if quantity == -1:
                return 0

            if quantity > 0 and available_seats + quantity <= 50:
                break

            print("Số lượng vé hủy không hợp lệ!")

        except ValueError:
            print("Vui lòng nhập số nguyên!")

    refund = quantity * BASE_PRICE * 0.8

    available_seats += quantity

    print(f"Hủy vé thành công. Hệ thống đã hoàn lại: ${refund:.1f}")
    print(f"Ghế trống hiện tại: {available_seats}")

    return refund


def Check_flight_status():
    print(f"""
--- TÌNH TRẠNG CHUYẾN BAY VN2026 ---
Sức chứa tối đa: 50
Ghế đã đặt: {50 - available_seats}
Ghế trống: {available_seats}
Tổng doanh thu hiện tại: ${flight_revenue:.1f}
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

            if 1 <= choice <= 4:
                break

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