# Classic_MIDI_FeatherWing

### _A classic MIDI interface FeatherWing with provisions for DIN-5 and TRS TypeB connectors_

![Image of Module](https://github.com/CedarGroveStudios/Classic_MIDI_FeatherWing/blob/master/photos/DSC05764a%20lores.jpg)

The Classic MIDI FeatherWing interface is an Adafruit Feather-compatible module. Deriving its power from the host Feather's 3.3V power, the interface converts incoming and outgoing classic MIDI current-loop input and output to Feather UART (RX and TX) logic pins.

The wing provides on-board input and output footprints for 3.5mm TRS Type B and DIN-5 connectors while maintaining the Feather dimensional format, thanks to John Park's inspirational _Feather MIDI Nub_ design (Twitter: @johnedgarpark). The MIDI input is an optically-isolated connection. MIDI output is buffered and current-limited. On-board receive (RX) and transmit (TX) LEDs indicate incoming and outgoing signals.

DIN-5 MIDI jack used: https://www.adafruit.com/product/1134

3.5mm TRS MIDI jack used: https://www.adafruit.com/product/1699

The Classic MIDI interface was tested with CircuitPython version 4.1.0 beta 1 and earlier releases. Example code is provided in the repository. Additional code examples can be found within the _adafruit__midi_ CircuitPython examples distribution.

OSH Park project: https://oshpark.com/shared_projects/SzjsJUV0

![FeatherWing Implementation Chart](https://github.com/CedarGroveStudios/Classic_MIDI_FeatherWing/blob/master/docs/FeatherWing_Impl_Chart.png)

![Image of Module](https://github.com/CedarGroveStudios/Classic_MIDI_FeatherWing/blob/master/photos/Classic%20MIDI%20FeatherWing%20glam.png)
