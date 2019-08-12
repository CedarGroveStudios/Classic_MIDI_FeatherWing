import adafruit_midi
import busio
import board
import time

from adafruit_midi.timing_clock            import TimingClock
from adafruit_midi.channel_pressure        import ChannelPressure
from adafruit_midi.control_change          import ControlChange
from adafruit_midi.note_off                import NoteOff
from adafruit_midi.note_on                 import NoteOn
from adafruit_midi.pitch_bend              import PitchBend
from adafruit_midi.polyphonic_key_pressure import PolyphonicKeyPressure
from adafruit_midi.program_change          import ProgramChange
from adafruit_midi.start                   import Start
from adafruit_midi.stop                    import Stop
from adafruit_midi.system_exclusive        import SystemExclusive
from adafruit_midi.midi_message            import MIDIUnknownEvent

import usb_midi
midi = adafruit_midi.MIDI(midi_in=usb_midi.ports[0], midi_out=usb_midi.ports[1], in_channel=0, out_channel=0, debug=True)

# UART = busio.UART(board.TX, board.RX, baudrate=31250, timeout=0.001)
# midi = adafruit_midi.MIDI(midi_in=UART, midi_out=UART, in_channel=0, out_channel=0, debug=True)

while True:
    print("-----")
    midi.send(Stop())
    midi.send(NoteOn(60, 100))
    midi.send(ControlChange(25, 127))
    midi.send(ProgramChange(33))
    time.sleep(1)
