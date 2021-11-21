import board
import busio,time
import digitalio


led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
light="yoo"
uart = busio.UART(tx=board.GP0, rx=board.GP1,baudrate=115200)
while True:
    time.sleep(1)
    uart.write(bytes(f"<L,{light}>", "ascii"))
    led.value=True
