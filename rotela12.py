#hhttp://www.rotel.com/sites/default/files/product/rs232/A12-A14%20Protocol.pdf
#Thanks to https://github.com/denov/rotel-web for pointing the right path

#  Control a Rotel A12 amplifier via its RS232 connection


import serial
import sys
import os

ser = serial.Serial(
        port='/dev/ttyUSB0',
        baudrate = 115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=3
)

rotela12 = {
  # POWER & VOLUME COMMANDS
  "PowerOff": "power_off!",
  "PowerOn": "power_on!",
  "VolumeUp": "vol_up!",
  "VolumeDown": "vol_down!",
  "MuteToggle": "FE 03 A2 10 1E FA",

    # SOURCE SELECTION COMMANDS
  "SourceCD": "cd!",
  "SourceAux1": "aux1!",
  "SourceAux2": "aux2!",

  "SpeakerAOn": "speaker_a_on!",
  "SpeakerAOff": "speaker_a_off!",
  "SpeakerBOn": "speaker_b_on!",
  "SpeakerBOff": "speaker_b_off!",

   # VOLUME DIRECT COMMANDS
  "VolumeMin":  "FE 03 A2 30 00 FC",
  "Volume1":  "FE 03 A2 30 01 FD",
  "Volume2":  "FE 03 A2 30 02 FD",
  "Volume3":  "FE 03 A2 30 03 FF",
  "Volume4":  "FE 03 A2 30 04 00",
  "Volume5":  "FE 03 A2 30 05 01",
  "Volume6":  "FE 03 A2 30 06 02",
  "Volume 7": "FE 03 A2 30 07 03",
  "Volume8":  "FE 03 A2 30 08 04",
  "Volume9":  "FE 03 A2 30 09 05",
  "Volume10": "FE 03 A2 30 0A 06",
  "Volume11": "FE 03 A2 30 0B 07",
  "Volume12": "FE 03 A2 30 0C 08",
  "Volume13": "FE 03 A2 30 0D 09",
  "Volume14": "FE 03 A2 30 0E 0A",
  "Volume15": "FE 03 A2 30 0F 0B",
  "Volume16": "FE 03 A2 30 10 0C",
  "Volume32": "FE 03 A2 30 20 1C",
  "Volume48": "FE 03 A2 30 30 05",
  "Volume64": "FE 03 A2 30 40 15",
  "Volume80": "FE 03 A2 30 50 25",
  "Volume95": "FE 03 A2 30 5F 5B",
}

def sendCmd(cmd):
   global rotela12
   line = ""
   if cmd in rotela12:
      print "sending" + cmd
      ser.write(rotela12[cmd])
      return cmd
   else:
      return "Command not found."

rotelcommand = sys.argv[1]
print rotelcommand
sendCmd(rotelcommand)
