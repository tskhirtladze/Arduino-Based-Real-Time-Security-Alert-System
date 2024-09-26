import tkinter as tk
import serial
import threading
import time


def connect_serial():
    global ser, serial_thread, connected
    try:
        ser = serial.Serial('COM5', 9600, timeout=1)
        connected = True
        connect_button.config(state=tk.DISABLED)
        disconnect_button.config(state=tk.NORMAL)
        serial_thread = threading.Thread(target=read_serial)
        serial_thread.start()
        status_label.config(text="Status: Connected", bg="green")
    except Exception as e:
        status_label.config(text="Status: Error connecting to serial")


def disconnect_serial():
    global ser, connected
    if ser:
        ser.close()
    connected = False
    connect_button.config(state=tk.NORMAL)
    disconnect_button.config(state=tk.DISABLED)
    status_label.config(text="Status: Disconnected", bg="red")


def read_serial():
    global connected, count
    count = 1
    while connected:

        data = ser.readline().decode('utf-8').strip()
        if data:
            print(data)
            process_data(data)
            count = count + 1
        time.sleep(0.1)


def process_data(data):

    if "motion is detected" in data:

        alert_label.config(text=str(count) + ". Security Alert! Motion Detected!")
        time.sleep(2.5)
        alert_label.config(text="")



root = tk.Tk()
root.title("Security System")

status_label = tk.Label(root, text="Status: Waiting for motion...")
status_label.pack(pady=10)

alert_label = tk.Label(root, text="", fg="red")
alert_label.pack(pady=10)

connect_button = tk.Button(root, text="Connect", bg="green", fg="white", command=connect_serial)
connect_button.pack(pady=10)

disconnect_button = tk.Button(root, text="Disconnect", bg="red", fg="black", command=disconnect_serial, state=tk.DISABLED)
disconnect_button.pack(pady=10)

ser = None
serial_thread = None
connected = False



root.mainloop()
