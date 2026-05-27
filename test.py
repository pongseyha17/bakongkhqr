from bakong_khqr import KHQR

khqr = KHQR("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7ImlkIjoiNWU2NGQwMzA2YjU4NDAyNiJ9LCJpYXQiOjE3Nzk4Njk2NjEsImV4cCI6MTc4NzY0NTY2MX0.sBcVUcDOEk2RblKmgzeoZVoXKGA7TaXgdTedkmyLCOc")

# Create QR with amount=0 and static=True for payer-input amount
qr_string = khqr.create_qr(
    bank_account="seyha_pong@bkrt",
    merchant_name="I AM",
    merchant_city="phnom penh",
    amount=0,  # Zero amount for payer input
    currency="KHR",
    store_label="I AM Store",
    phone_number="012345678",
    bill_number="1234567890",
    terminal_label="I AM Terminal",
    static=True,  # Static mode allows payer to input any amount
)

print("QR String:", qr_string)

khqr_image = khqr.qr_image(
    qr=qr_string,
    output_path="khqr.png",
    format="jpeg",
)

print("QR Image saved to:", khqr_image)