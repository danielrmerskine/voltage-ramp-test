import time
from lager import Net, NetType

# Get supply1 net (Rigol DP821 channel 1 - vibration motor)
supply = Net.get('supply1', type=NetType.PowerSupply)

# Safety limits
supply.set_ovp(12.0)   # Over-voltage protection at 12V
supply.set_ocp(0.5)    # Over-current protection at 500mA

# Enable output
supply.enable()
time.sleep(0.5)

print('Starting voltage ramp on supply1...')

# Ramp from 1V to 10V in 1V steps
for voltage in range(1, 11):
    supply.set_voltage(voltage)
    time.sleep(1)
    measured_v = supply.voltage()
    measured_p = supply.power()
    print(f'Set: {voltage}V  Measured: {measured_v:.3f}V  Power: {measured_p:.3f}W')

print('Ramp complete. Disabling output.')
supply.set_voltage(0)
time.sleep(0.5)
supply.disable()
print('Done!')
