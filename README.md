# Arduino-Based-Real-Time-Security-Alert-System
This Python script monitors a serial connection (specifically to an Arduino device) and sends an email alert whenever new data is received.

## Key Components

### Libraries Used
- **`time`**: Manages timing functions.
- **`serial`**: Facilitates serial communication with the Arduino.
- **`smtplib`** and **`ssl`**: Enable secure email sending via Gmail.
- **`EmailMessage`** from `email.message`: Constructs the email content.

### Hardware
- **PIR Sensor**: Detects motion and triggers the alert system.

### Email Configuration
- The script sets up the subject and body for the email alert.
- Sender and receiver email addresses are specified, and the sender's email password is securely obtained through user input.

### Email Composition
- An `EmailMessage` object is created with HTML content to indicate a security alert.

### Serial Connection
- Establishes a connection with the Arduino on **COM5** at a baud rate of **9600**.
- Includes a one-second pause to stabilize the connection.

### Data Monitoring Loop
- An infinite loop checks for incoming data from the Arduino.
- When data is available, the script reads the data packet, decodes it, and strips any unwanted newline characters.

### Email Sending
- Upon receiving new data, the script logs into the Gmail SMTP server using the provided credentials and sends the constructed email.
- Success messages and the received data packet are printed to the console.

## Use Case
This script is ideal for security applications where real-time monitoring and alerting are crucial, allowing users to receive immediate notifications when specific events, such as motion detected by the PIR sensor, occur in the connected Arduino device.

## Use Case
This script is ideal for security applications where real-time monitoring and alerting are crucial, allowing users to receive immediate notifications when specific events occur in the connected Arduino device.
