from pyModbusTCP.client import ModbusClient

# Define the Modbus server IP and port
PLC_IP = 'xxx.xxx.xxx.xxx'  # Update to your PLC's IP
PLC_PORT = 502          # Default Modbus TCP port

# Create a Modbus client
client = ModbusClient(host=PLC_IP, port=PLC_PORT)

def read_register(address):
    """Read a holding register."""
    response = client.read_holding_registers(address, 1)
    if response:
        print(f"Successfully read value: {response[0]} from register {address}")
    else:
        print("Error reading from register")

def write_register(address, value):
    """Write to a holding register."""
    if client.write_single_register(address, value):
        print(f"Successfully wrote value: {value} to register {address}")
    else:
        print("Error writing to register")

try:
    # Connect to the server
    if client.open():
        print("Connected to PLC")

        # Define the register address to read from (assuming MB_DB1, holding register 1)
        register_address = 1  # Register address

        # Read the holding register
        read_register(register_address)

        # Write a value to the holding register (e.g., write 123)
        write_register(register_address, 123)

    else:
        print("Failed to connect to PLC")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Ensure the connection is closed
    client.close()

