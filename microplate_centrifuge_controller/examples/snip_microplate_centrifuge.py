import time
import sys
import yaml

from pathlib import Path

from microplate_centrifuge_controller import Client as MicroplateCentrifugeClient
from microplate_centrifuge_controller.generated.microplatecentrifugecontroller import CommandIsRunning, NotInitialized, InstrumentErrorOccurred, InvalidInstrumentStatusError

with open("config.yml", 'r') as file:
    config = yaml.safe_load(file)

host, port, cert = config["MicroplateCentrifuge"]["host"], config["MicroplateCentrifuge"]["port"], config["MicroplateCentrifuge"]["cert_path"]
print(f"Connect to MicroplateCentrifuge Server. host: {host} port: {port} cert file: {cert}")
mc_client = MicroplateCentrifugeClient(host, port, root_certs=Path(cert).read_bytes())

#region OpenDoor command
print("OpenDoor command start!")
open_door_instance = mc_client.MicroplateCentrifugeController.OpenDoor(1)
while not open_door_instance.done:
    time.sleep(1)
    print("OpenDoor command is still running...")
print("OpenDoor command complete!")

try:
    open_door_instance.get_responses()
    print("OpenDoor succeeded.")
except CommandIsRunning:
    print("Command is running.")
    sys.exit()
except NotInitialized:
    print("Microplate Centrifuge is not initialized.")
    sys.exit()
except InstrumentErrorOccurred:
    print("Instrument Error occurred.")
    sys.exit()
except InvalidInstrumentStatusError:
    print("Invalid status.")
    sys.exit()
except:
    print("Undefined error occurred.")
    sys.exit()
#endregion

#region CloseDoor command
print("CloseDoor command start!")
close_door_instance = mc_client.MicroplateCentrifugeController.CloseDoor()
while not close_door_instance.done:
    time.sleep(1)
    print("CloseDoor command is still running...")
print("CloseDoor command complete!")

try:
    close_door_instance.get_responses()
    print("CloseDoor succeeded.")
except CommandIsRunning:
    print("Command is running.")
    sys.exit()
except NotInitialized:
    print("Microplate Centrifuge is not initialized.")
    sys.exit()
except InstrumentErrorOccurred:
    print("Instrument Error occurred.")
    sys.exit()
except InvalidInstrumentStatusError:
    print("Invalid status.")
    sys.exit()
except:
    print("Undefined error occurred.")
    sys.exit()
#endregion

#region SpinCycle command
print("SpinCycle command start!")
spin_cycle_instance = mc_client.MicroplateCentrifugeController.SpinCycle(20, # VelocityPercent
                                                                         20, # AccelerationPercent
                                                                         20, # DecelerationPercent
                                                                         0,  # TimerMode
                                                                         30, # Time
                                                                         1,  # BucketNumberToLoad
                                                                         1,  # BucketNumberToUnload
                                                                         8,  # GripperOffsetToLoad
                                                                         8,  # GripperOffsetToUnload
                                                                         15, # PlateHeightToLoad
                                                                         15, # PlateHeightToUnload
                                                                         1,  # SpeedToLoad
                                                                         1,  # SpeedToUnload
                                                                         0,  # OptionsToLoad
                                                                         0)  # OptionsToUnload
while not spin_cycle_instance.done:
    time.sleep(1)
    print("SpinCycle command is still running...")
print("SpinCycle command complete!")

try:
    spin_cycle_instance.get_responses()
    print("SpinCycle succeeded.")
except CommandIsRunning:
    print("Command is running.")
    sys.exit()
except NotInitialized:
    print("Microplate Centrifuge is not initialized.")
    sys.exit()
except InstrumentErrorOccurred:
    print("Instrument Error occurred.")
    sys.exit()
except InvalidInstrumentStatusError:
    print("Invalid status.")
    sys.exit()
except:
    print("Undefined error occurred.")
    sys.exit()
#endregion

#region StopSpinCycle command
print("StopSpinCycle command start!")
stop_spin_cycle_instance = mc_client.MicroplateCentrifugeController.StopSpinCycle(1)
while not stop_spin_cycle_instance.done:
    time.sleep(1)
    print("StopSpinCycle command is still running...")
print("StopSpinCycle command complete!")

try:
    stop_spin_cycle_instance.get_responses()
    print("StopSpinCycle succeeded.")
except CommandIsRunning:
    print("Command is running.")
    sys.exit()
except NotInitialized:
    print("Microplate Centrifuge is not initialized.")
    sys.exit()
except InstrumentErrorOccurred:
    print("Instrument Error occurred.")
    sys.exit()
except InvalidInstrumentStatusError:
    print("Invalid status.")
    sys.exit()
except:
    print("Undefined error occurred.")
    sys.exit()
#endregion

#region Reset command
print("Reset command start!")
reset_instance = mc_client.MicroplateCentrifugeController.Reset()
while not reset_instance.done:
    time.sleep(1)
    print("Reset command is still running...")
print("Reset command complete!")

try:
    reset_instance.get_responses()
    print("Reset succeeded.")
except CommandIsRunning:
    print("Command is running.")
    sys.exit()
except NotInitialized:
    print("Microplate Centrifuge is not initialized.")
    sys.exit()
except InstrumentErrorOccurred:
    print("Instrument Error occurred.")
    sys.exit()
except InvalidInstrumentStatusError:
    print("Invalid status.")
    sys.exit()
except:
    print("Undefined error occurred.")
    sys.exit()
#endregion

#region EnumerateProfiles command
print("EnumerateProfiles command start!")
try:
    enumerate_profiles_response = mc_client.MicroplateCentrifugeController.EnumerateProfiles()
    print("EnumerateProfiles command complete!")
    print(f"EnumerateProfiles succeeded. Profiles: {', '.join(enumerate_profiles_response.ProfileNames)}")
except NotInitialized:
    print("Microplate Centrifuge is not initialized.")
    sys.exit()
except InvalidInstrumentStatusError:
    print("Invalid status.")
    sys.exit()
except:
    print("Undefined error occurred.")
    sys.exit()
#endregion

#region Home command
print("Home command start!")
home_instance = mc_client.MicroplateCentrifugeController.Home()
while not home_instance.done:
    time.sleep(1)
    print("Home command is still running...")
print("Home command complete!")

try:
    home_instance.get_responses()
    print("Home succeeded.")
except CommandIsRunning:
    print("Command is running.")
    sys.exit()
except NotInitialized:
    print("Microplate Centrifuge is not initialized.")
    sys.exit()
except InstrumentErrorOccurred:
    print("Instrument Error occurred.")
    sys.exit()
except:
    print("Undefined error occurred.")
    sys.exit()
#endregion

#region Park command
print("Park command start!")
park_instance = mc_client.MicroplateCentrifugeController.Park()
while not park_instance.done:
    time.sleep(1)
    print("Park command is still running...")
print("Park command complete!")

try:
    park_instance.get_responses()
    print("Park succeeded.")
except CommandIsRunning:
    print("Command is running.")
    sys.exit()
except NotInitialized:
    print("Microplate Centrifuge is not initialized.")
    sys.exit()
except InstrumentErrorOccurred:
    print("Instrument Error occurred.")
    sys.exit()
except:
    print("Undefined error occurred.")
    sys.exit()
#endregion

#region LoadPlate command
print("LoadPlate command start!")
load_plate_instance = mc_client.MicroplateCentrifugeController.LoadPlate(1,  # BucketNumber
                                                                         8,  # GripperOffset
                                                                         15, # PlateHeight
                                                                         1,  # Speed
                                                                         0)  # Options
while not load_plate_instance.done:
    time.sleep(1)
    print("LoadPlate command is still running...")
print("LoadPlate command complete!")

try:
    load_plate_instance.get_responses()
    print("LoadPlate succeeded.")
except CommandIsRunning:
    print("Command is running.")
    sys.exit()
except NotInitialized:
    print("Microplate Centrifuge is not initialized.")
    sys.exit()
except InstrumentErrorOccurred:
    print("Instrument Error occurred.")
    sys.exit()
except:
    print("Undefined error occurred.")
    sys.exit()
#endregion

#region UnloadPlate command
print("UnloadPlate command start!")
unload_plate_instance = mc_client.MicroplateCentrifugeController.UnloadPlate(1,  # BucketNumber
                                                                             8,  # GripperOffset
                                                                             15, # PlateHeight
                                                                             1,  # Speed
                                                                             0)  # Options
while not unload_plate_instance.done:
    time.sleep(1)
    print("UnloadPlate command is still running...")
print("UnloadPlate command complete!")

try:
    unload_plate_instance.get_responses()
    print("LoadPlate succeeded.")
except CommandIsRunning:
    print("Command is running.")
    sys.exit()
except NotInitialized:
    print("Microplate Centrifuge is not initialized.")
    sys.exit()
except InstrumentErrorOccurred:
    print("Instrument Error occurred.")
    sys.exit()
except:
    print("Undefined error occurred.")
    sys.exit()
#endregion

#region ActiveXVersion Property
try:
    print(f"ActiveX Version: {mc_client.MicroplateCentrifugeController.ActiveXVersion.get()}")
except NotInitialized:
    print("Microplate Centrifuge is not initialized.")
    sys.exit()
except InvalidInstrumentStatusError:
    print("Invalid status.")
    sys.exit()
except:
    print("Undefined error occurred.")
    sys.exit()
#endregion

#region CentrifugeActiveXVersion Property
try:
    print(f"Centrifuge ActiveX Version: {mc_client.MicroplateCentrifugeController.CentrifugeActiveXVersion.get()}")
except NotInitialized:
    print("Microplate Centrifuge is not initialized.")
    sys.exit()
except InvalidInstrumentStatusError:
    print("Invalid status.")
    sys.exit()
except:
    print("Undefined error occurred.")
    sys.exit()
#endregion

#region CentrifugeHardwareVersion Property
try:
    print(f"Centrifuge Hardware Version: {mc_client.MicroplateCentrifugeController.CentrifugeHardwareVersion.get()}")
except NotInitialized:
    print("Microplate Centrifuge is not initialized.")
    sys.exit()
except InvalidInstrumentStatusError:
    print("Invalid status.")
    sys.exit()
except:
    print("Undefined error occurred.")
    sys.exit()
#endregion

#region FirmwareVersion Property
try:
    print(f"Firmware Version: {mc_client.MicroplateCentrifugeController.FirmwareVersion.get()}")
except NotInitialized:
    print("Microplate Centrifuge is not initialized.")
    sys.exit()
except InvalidInstrumentStatusError:
    print("Invalid status.")
    sys.exit()
except:
    print("Undefined error occurred.")
    sys.exit()
#endregion


#region HardwareVersion Property
try:
    print(f"Hardware Version: {mc_client.MicroplateCentrifugeController.HardwareVersion.get()}")
except NotInitialized:
    print("Microplate Centrifuge is not initialized.")
    sys.exit()
except InvalidInstrumentStatusError:
    print("Invalid status.")
    sys.exit()
except:
    print("Undefined error occurred.")
    sys.exit()
#endregion


#region Status property
print("Subscribe Status property start.")
print(f"Current status: {mc_client.MicroplateCentrifugeController.Status.get()}")
status_subscription = mc_client.MicroplateCentrifugeController.Status.subscribe()

print("New status:")
status_subscription.add_callback(print)

time.sleep(5)

status_subscription.cancel()
print("Subscribe Status property complete.")
#endregion