#lib that checks uart gps data, and determin if usefull.
class returnInfo:
  def __init__(self,type_name, lat, long, alt):
    self.NMEATYPE = type_name
    self.Latitudinal = lat
    self.Longitudinal = long
    self.Altitude = alt

## first we check the rmc 
def interp_rmc(data_s):
    
    if(data_s[0:6]=="$GNRMC"):
        try:
            cs=data_s[data_s.index("$")+1:data_s.index("*")]
            cs_v = 0
            for c in cs:
                cs_v^=ord(c)
            css=data_s[data_s.index("*")+1:data_s.index("*")+3]
            hex_css = hex(int(css,16))
            hex_cs_v = hex(int(cs_v))

            step_v = 0
            data_arr = []
            for i in range(len(data_s)):
                if(data_s[i]==","):
                    data_arr.append(data_s[step_v:i])
                    step_v=i+1
        except:
            print("RMC data recived, but the data was corupt")
            return returnInfo("Fail",0,0,0)
        else:
            if(hex_css==hex_cs_v):
                if(data_arr[2]=="A"):
                    return returnInfo("RMC",data_arr[3],data_arr[5],"undefinde for RMC")
                else:
                    print("RMC recived bad connection, evt try go outside you kaeldermenske")
                    return returnInfo("Fail",0,0,0)
            else:
                print ( "RMC recived checksum failed")
                return returnInfo("Fail",0,0,0)

    return returnInfo("Fail",0,0,0)        



