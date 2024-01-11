# qrgenerator/utils.py

import qrcode

def generate_qr_code(data_text):
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data_text)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        return img

    except Exception as e:
        # Log the error or print it for debugging
        print(f"Error generating QR code: {e}")
        return None
