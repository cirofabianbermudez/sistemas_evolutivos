Amplificador Cascode con Entrada Complementaria
* w1, w1, w2, w2, w3, w3, w4, w4, w5, w5, w5, w5, w6, w6, w7, w7, w7 
.subckt AmpCascode vin1 vin2 out vdd vss
M1 4 vin1 1 vdd P_18_MM L=1.0u W=W1
M2 8 vin2 1 vdd P_18_MM L=1.0u W=W1
M3 9 vin1 5 vss N_18_MM L=1.0u W=W2
M4 10 vin2 5 vss N_18_MM L=1.0u W=W2
M5  9 11 vdd vdd P_18_MM L=1.0u W=W3
M6 10 11 vdd vdd P_18_MM L=1.0u W=W3
M7  11 12  9 vdd P_18_MM L=1.0u W=W4
M8 out 12 10 vdd P_18_MM L=1.0u W=W4
M9   11 13  4 vss N_18_MM L=1.0u W=W5
M10 out 13  8 vss N_18_MM L=1.0u W=W5
M11   4 14  vss vss N_18_MM L=1.0u W=W5
M12   8 14  vss vss N_18_MM L=1.0u W=W5
*
M13  15 15  vdd vdd P_18_MM L=1.0u W=W6
M14   1 15  vdd vdd P_18_MM L=1.0u W=W6
M15  16 16  vss vss N_18_MM L=1.0u W=W6
M16  15 16  vss vss N_18_MM L=1.0u W=W7
M17   5 16  vss vss N_18_MM L=1.0u W=W7
Ibias vdd 16 30u
VB1 12 0 0.55V
VB2 13 0 -0.75V
VB3 14 0 -0.95V
.ends
*
*
*
* EL circuito para medicion
Xamp1 vpos vneg out vdd vss AmpCascode
CL out 0 10p
Vdd vdd 0 1.65V
Vss vss 0 -1.65V
V2 vneg 0 0V
V1 vpos 0 0V
*
.include ./MOSIS_018umparam.lib
.include ./wsvals.lib
*
* EL circuito para medicion
Xamp1 vpos vneg out vdd vss AmpCascode
CL out 0 10p
Vdd vdd 0 1.65V
Vss vss 0 -1.65V
V1 vneg 0 DC 0.0 AC 1.0
V2 vpos 0 0V
*
.include ./MOSIS_018umparam.lib
*
* Analisis
*
.options NOPAGE
.AC DEC 20 1 100e6
*.print ac vm(out) vp(out)
.control
run
meas ac Ao find vm(out) at=10
let aodb = 20.0 * log10( Ao )
print aodb
let ganCodo=0.7*Ao
meas ac BW find frequency when vm(out)=ganCodo
meas ac GBW find frequency when vm(out)=1.0
meas ac fase find vp(out) at=GBW
let faseok = 180.0 + fase*180.0/pi
print faseok
.endc
.END
