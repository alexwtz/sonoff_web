from pysonofflanr3 import SonoffSwitch
import time
import config
new_state='off'

async def state_callback(device):
  global new_state
  if device.basic_info is not None:
    print("ON" if device.is_on else "OFF")
    if ( device.is_on and new_state == 'on' ) or ( device.is_off and new_state == 'off' ):
      exit()
    if device.available:
      if device.is_on:
        new_state = "off"
        await device.turn_off()
      elif device.is_off:
        new_state = "on"
        await device.turn_on()

#async def setOn(device):
  #device.state='ON'
  #await device.turn_on()

def main():
  #Usage example when used as library:
  p = SonoffSwitch(
	host="",
        callback_after_update=state_callback,
        device_id=config.device_id,
        api_key=config.api_key
        )

if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    main()
