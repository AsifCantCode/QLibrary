import serial

def read_number_from_serial( ser ):
    if ser.in_waiting <= 0:
        return -1
        # Read data from the serial port
    serial_data = ser.readline().decode('utf-8').strip()
    
    # Try to convert the received data to a number (assuming it's a numeric value)
    try:
        number = int(serial_data)
        return number
    except ValueError:
        print("Received data is not a valid number:", serial_data)
        return None
        
    
        

    

# Example usage
if __name__ == "__main__":
    number = read_number_from_serial('COM3',115200)
    if number is not None:
        print("Received number from serial port:", number)
    else:
        print("Failed to read number from serial port.")
