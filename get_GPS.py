import serial
import interp_gps
ser = serial.Serial("/dev/ttyS0",9600,8,serial.PARITY_NONE,serial.STOPBITS_ONE,1)
while True:
    received_data = ser.readline()
    if(received_data):
    #check if RMC 
    #GGA
        rmc_v = interp_gps.interp_rmc(received_data)
        if(rmc_v.NMEATYPE=="RMC"):
            print("valid rmc data recived : "+rmc_v.Latitudinal + " LAT : "+rmc_v.Longitudinal+" LONG : "+"no altitude in RMC")
    else:
        print("it seams that no device is connected, evt try flipping rx tx cables")
