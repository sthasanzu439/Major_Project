
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from flask import Flask, render_template, send_file

app = Flask(name)

# Define the route to serve the stego image
@app.route('/stego_image')
def serve_stego_image():
    stego_image_path = '/path/to/stego_image.png'  # Replace with the actual path to the stego image
    return send_file(stego_image_path, mimetype='image/png')

# Define a route to send the stego image via email
@app.route('/send_email')
def send_email():
    from_addr = 'relax01k@gmail.com'  # Replace with your Gmail email address
    to_addr = 'sthasanzu41@example.com'  # Replace with the recipient's email address
    password = 'nishant01k'  # Replace with your Gmail password

    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = 'Stego Image'

    body = 'Please find the stego image attached.'
    msg.attach(MIMEText(body, 'plain'))

    stego_image_path = 'C:\\Users\\acer\Downloads\\abc\abc\\final project file\\Major_Project1\\temp//path//to//stego_image.png'  # Replace with the actual path to the stego image

    with open(stego_image_path, 'rb') as f:
        image_data = f.read()

    image = MIMEImage(image_data, name='stego_image.png')
    msg.attach(image)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_addr, password)
        server.send_message(msg)
        server.quit()
        return 'Email sent successfully!'
    except Exception as e:
        return f'An error occurred: {str(e)}'

if name == 'main':
    app.run()