import time
import pyvisa

rm = pyvisa.ResourceManager()
psu = rm.open_resource('USB0::0x1AB1::0x0E11::DP8G232400080::INSTR')

# Select channel 1 (supply1 - vibration motor)
psu.write(':INST:NSEL 1')
psu.write(':CURR 0.5')  # 500mA current limit for safety
psu.write(':OUTP ON')

print('Starting voltage ramp on supply1...')
print('Channel 1 output enabled')

for voltage in range(1, 11):
    psu.write(f':VOLT {voltage}')
    actual = psu.query(':MEAS:VOLT?')
    current = psu.query(':MEAS:CURR?')
    print(f'Set: {voltage}V  Measured: {actual.strip()}V  Current: {current.strip()}A')
    time.sleep(1)

print('Ramp complete. Disabling output.')
psu.write(':VOLT 0')
psu.write(':OUTP OFF')
psu.close()
print('Done!')
