from pyModbusTCP.client import ModbusClient

# Define the Modbus server IP and port
PLC_IP = '192.168.0.1'  # Update to your PLC's IP
PLC_PORT = 502          # Default Modbus TCP port

# Create a Modbus client
client = ModbusClient(host=PLC_IP, port=PLC_PORT)

# Connect to the server
if client.open():
    print("Connected to PLC")

    # Define the register address to read from (assuming MB_DB1, holding register 1)
    register_address = 1  # Register address

    # Read the holding register
    response = client.read_holding_registers(register_address, 1)

    # Check if the read operation was successful
    if response:
        print(f"Successfully read value: {response[0]} from register {register_address}")
    else:
        print("Error reading from register")

    # Close the connection
    client.close()
else:
    print("Failed to connect to PLC")
