# Duck's Services DMA Master Summary

Prepared from the DMA Hardware Docs / GitBook pages provided in chat.

Purpose: preserve the full DMA flow in simple support language so it can be reviewed quickly while handling tickets.

## 1. Big Picture

The DMA docs are not one single setup. They are a chain of steps:

- main PC hardware setup
- second PC driver setup
- speed test
- troubleshooting
- firmware preparation
- firmware flashing
- accessory setup

Main accessory categories covered:

- Makcu
- 1K HDMI Fuser
- 4K DC500 Fuser
- KM Box Net
- KM Box B+

The most important support habit:

`Always identify what stage the customer is currently stuck on.`

That makes the ticket much easier to handle.

## 2. Main DMA Setup Flow

Recommended mental flow:

1. `Hardware Setup (Main PC)`
2. `JTAG Driver Setup (2nd PC)`
3. `DATA Driver Setup (2nd PC)`
4. `Speed Test (2nd PC)`
5. `Troubleshooting`
6. `DNA ID`
7. `Firmware Flashing`
8. `Makcu / Fuser / KM Box` if applicable

When a customer opens a DMA ticket, first ask yourself:

- are they stuck at hardware install?
- driver install?
- speed test?
- firmware flashing?
- Makcu?
- Fuser?
- KM Box?

## 3. Hardware Setup (Main PC)

This is the first physical setup step on the gaming PC.

### 3.1 Main Steps

- fully shut down the `Game PC`
- insert the DMA card into any available `PCI-e` slot
- connect the `JTAG` port on the DMA card to the `2nd PC`
- enter BIOS / UEFI

### 3.2 BIOS Changes

For `Intel`, disable:

- `VT-d`
- `Intel Virtualization Technology`
- `IOMMU` if available

For `AMD`, disable:

- `SVM`
- `IOMMU`

Optional if available:

- disable `NX-Bit / Execute Disable Bit`
- set PCIe slot to `Gen1` for compatibility

### 3.3 Windows Change

On the `Game PC`, disable:

- `Memory Integrity`

Path:

- `Windows Security`
- `Device Security`
- `Core Isolation`
- `Core Isolation Details`
- turn off `Memory Integrity`

If the section will not load:

- it may already be disabled
- or unsupported

### 3.4 Support Meaning

This step prepares the `Game PC` to work with DMA correctly.

If someone has early DMA problems, ask:

- is the card installed properly?
- is the JTAG cable connected to the `2nd PC`?
- is virtualization fully disabled?
- is Memory Integrity off?
- did they change PCIe slot to Gen1 if needed?

## 4. JTAG Driver Setup (2nd PC)

This is done on the `2nd PC`.

### 4.1 Main Steps

- download the `JTAG Driver`
- run the installer
- click `Install`
- click `OK` when done

### 4.2 Support Meaning

This is the basic communication driver for DMA setup/flashing steps.

### 4.3 Important Support Memory

- `JTAG Driver` goes on the `2nd PC`
- not on the gaming PC

## 5. DATA Driver Setup (2nd PC)

This is also done on the `2nd PC`.

Goal:

- make the DMA card appear correctly in `Device Manager`

### 5.1 Correct Result

Device should appear as:

- `FTDI FT601 USB 3.0 Bridge Device`

Under:

- `Universal Serial Bus devices`

### 5.2 Missing Driver

If it appears as:

- `FTDI SuperSpeed-FIFO Bridge`

Under:

- `Other devices`

With yellow exclamation mark:

- install the correct FTDI driver

### 5.3 Wrong Driver

If it appears as:

- `FTDI SuperSpeed-FIFO Bridge`

Under:

- `Universal Serial Bus devices`

Then:

- uninstall device
- check `Delete driver`
- install proper FTDI driver

### 5.4 Driver Files Mentioned

- `FTD3XX Driver v1.3.0.10`
- backup: `FTD3XX Driver v1.3.0.8`

### 5.5 Support Meaning

If customer says:

- device not detected correctly
- yellow mark in Device Manager
- FTDI issue

Ask:

- what exact device name appears?
- which Device Manager category is it under?
- is there a yellow exclamation mark?

## 6. Speed Test (2nd PC)

This is one of the most important steps.

### 6.1 Main Purpose

Confirm the DMA card and connection are functioning correctly.

### 6.2 Main Steps

- ensure cable is in the `DATA Port`
- run the speed test tool on the `2nd PC`
- select `[4] Mixed Test`
- wait for results

### 6.3 Speed Ratings

- `< 4000` = Low
- `4000+` = Warning
- `5200+` = Good
- `6500+` = Amazing
- `7500+` = Elite

### 6.4 Throughput Ratings

- `< 125` = Low
- `125+` = Warning
- `150+` = Good
- `200+` = Amazing
- `220+` = Elite

### 6.5 Support Meaning

If speed test is healthy, DMA connection is likely good.

If speed test is bad:

- check cable
- check USB port
- check FTDI driver
- check BIOS
- check hardware seating

### 6.6 Example of Strong Results

From the test image you shared:

- around `7312 RPS`
- throughput around `219.25 MB/s`

That is considered:

- `Amazing` speed
- `Amazing` throughput

## 7. DMA Troubleshooting

This is one of the most useful sections because it ties specific errors to likely causes.

### 7.1 `[FAIL] VMM INIT FAILED.`

Cause:

- card/connection is hung
- often due to fast reboot or waking from sleep

Fix:

- fully shut down the `Game PC`
- do not just reboot
- wait `5–10 seconds`
- cold boot again

### 7.2 `FPGA: ERROR: Unable to connect to USB/FT601 device`

Cause:

- `FTDI` driver missing
- wrong port used

Fix:

- confirm FTDI driver installed on `2nd PC`
- confirm cable is in the `DATA Port`

### 7.3 `Failed to retrieve Physical Memory Map`

Cause:

- unstable or faulty USB connection

Fix:

- reseat USB cable
- try another USB 3.0 cable
- try another USB port
- last resort: reinstall Windows on `Game PC`

### 7.4 `Offline symbols unavailable - info.db not found`

Cause:

- tool cannot get symbol data
- tool not fully extracted
- required support files missing
- internet/firewall issue

Fix:

- fully unzip tool
- confirm `symsrv.dll` and `dbghelp.dll` are in same folder
- confirm internet access
- check firewalls
- manually place latest `info.db` if needed

### 7.5 `FPGA: TINY PCIe TLP Algorithm auto-selected`

Cause:

- lower speeds
- poor USB connection
- sometimes firmware limitation

Fix:

- reseat cable
- try another USB port
- review firmware if needed

### 7.6 `[CORE] Initialization Failed. Unable to locate valid DTB / auto-identify OS`

Cause:

- BIOS settings wrong
- unstable USB link

Fix:

- review BIOS settings
- double-check cable stability and correct port
- last resort: reinstall Windows on `Game PC`

### 7.7 `DMA Test Tool FAIL / General Failures`

Cause:

- speed or throughput below working threshold

Common triggers:

- speed under `4000`
- throughput under `125 MB/s`

Fixes:

- use a proper USB 3.0 data cable
- reseat cable
- switch `2nd PC` to `High Performance` power plan
- try different ports/cables
- reseat DMA card
- check bracket fitment
- confirm `2nd PC` meets requirements
- some firmware types may reduce speed

### 7.8 `Software not loading / entities missing / glitchy behavior`

Cause:

- `Paged Out Memory`

Meaning:

- target process memory moved to the Windows page file
- DMA cannot read paged-out memory properly

Fix:

- install more RAM in `Game PC`
- optional page-file changes only if necessary

### 7.9 Biggest Support Lesson

Many DMA issues are **not** immediately firmware issues.

They are often:

- cable issues
- wrong port
- wrong driver
- wrong BIOS settings
- low speed
- RAM pressure

## 8. DNA ID

This step is used before firmware preparation.

Important support info to request for firmware prep:

- `DMA DNA ID`
- `motherboard model`
- `firmware order number`

Support meaning:

If customer is asking for firmware prep/help, this info is highly useful.

## 9. 35t Firmware Flashing

This section is only for `35t` cards.

### 9.1 Main Steps

- connect USB cable to `JTAG` port
- make sure `JTAG Driver` is installed on `2nd PC`
- open flashing tool
- select firmware file
- press `Start`
- wait for `Update Complete`
- restart the DMA device
- move cable from `JTAG` to `DATA`
- run speed test

### 9.2 Key Support Memory

Very important:

- after flashing `35t`, move the cable from `JTAG` to `DATA`

This is easy for customers to miss.

## 10. 75t / 100t Firmware Flashing

This section is for `75t` and `100t` cards.

### 10.1 Main Steps

- connect to `JTAG`
- make sure `JTAG Driver` is installed
- open `75t / 100t Flashing Tool`
- configure correct field values
- choose `.bin`
- press `Flash`
- wait until progress reaches `100%`
- run speed test

### 10.2 Required Tool Values

For `75t`:

- `Field 1: xc7a75t`

For `100t`:

- `Field 1: xc7a100t`

For both:

- `Field 2: BIN`
- `Field 3: 10000000`

### 10.3 Key Support Memory

If customer says flash failed or still doesn’t work, verify:

- correct card model
- correct `Field 1`
- `BIN` selected
- `10000000` used
- progress really hit `100%`

## 11. Makcu Overview

Makcu has its own setup chain:

1. physical cable setup
2. driver install
3. COM port setup
4. flashing

## 12. Makcu Cable Setup

Cable layout:

- `LEFT cable` -> `Main PC`
- `MIDDLE cable` -> `Second PC`
- `RIGHT cable` -> `Mouse`

Key support memory:

Wrong cable placement is a common cause of Makcu problems.

## 13. Makcu Driver

This is done on the `Second PC`.

### 13.1 Main Steps

- install the `.inf` driver
- open `Device Manager`
- find the COM device
- set `COM Port Number` to anything below `10`
- close tool if open
- unplug/replug left-most cable to restart Makcu

### 13.2 Example Device

Something like:

- `USB-Enhanced-SERIAL CH343 (COM5)`

`COM5` is okay because it is below `10`

### 13.3 Key Support Memory

If Makcu is not detected or AIO tool behaves strangely, check:

- driver installed?
- COM below 10?
- Makcu restarted after COM changes?

## 14. Makcu Flashing

This is done from the `Second PC`.

### 14.1 Pre-Setup

- run `AIO Tool` on the `Second PC`
- do not run from the main PC
- download the AIO Tool
- let it update automatically

### 14.2 Main Steps

Flash left side:

- remove top cover
- hold `LEFT` button
- plug cable into `LEFT` port
- wait for `MCU connected in flash mode`
- click `Flash Left`
- wait for completion
- unplug left port cable

Flash right side:

- hold `RIGHT` button
- plug cable into `RIGHT` port
- click `Flash Right`
- wait for completion

### 14.3 Key Support Memory

Makcu flashing is a two-side process:

- left side must be flashed
- right side must be flashed

Common mistakes:

- wrong side button
- wrong port
- not seeing flash mode message
- only flashing one side

## 15. 1K Fuser Overview

This gives the fuser basics:

- indicator lights
- button functions
- cable/port layout

### 15.1 Lights

- `D1` = power
- `D2` = fusion active
- `H1` = primary/main PC signal
- `H2` = secondary PC signal

### 15.2 Buttons

- `Power` = power switch
- `K1` = secondary screen mode
- `K2` = main screen mode
- `K3` = enable / adjust fusion
- `K4` = reset / re-engage

### 15.3 Ports

- `Output` -> main monitor
- `Input1` -> main PC GPU
- `Input2` -> second PC GPU
- `DC12V` -> power

## 16. 1K Fuser Setup

### 16.1 Main Steps

- disconnect all displays except main monitor
- connect main monitor to fuser, not GPU
- on both PCs: set display mode to `Extend these displays`
- on `2nd PC`: set wallpaper/background to solid `black`
- use `3 HDMI 2.0 cables`

### 16.2 Important Troubleshooting

Merged desktop / two search bars:

- press `K2`

Second monitor no signal:

- make sure second monitor is turned on
- second monitor should connect to its own PC, not the fuser

Refresh rate stuck at `60Hz` or `90Hz`:

- likely not all cables are `HDMI 2.0`

### 16.3 Key Support Memory

Most 1K fuser problems are due to:

- wrong cable type
- wrong display mode
- monitor connected wrong
- second PC background not black
- wrong mode button

## 17. 4K DC500 Fuser Overview

This is the higher-end fuser.

### 17.1 Critical Rule

Use only **one interface type at a time**:

- `HDMI 2.1`
- or `DisplayPort 1.4 / 2.1`

Do **not** mix HDMI and DP.

### 17.2 Support Range

HDMI 2.1:

- `1080p` up to `480–540Hz`
- `1440p` up to `320–355Hz`
- `4K` up to `144–158Hz`

DisplayPort 1.4:

- `1080p` up to `480Hz`
- `1440p` up to `320Hz`
- `4K` up to `144Hz`

### 17.3 Hardware Requirements

For `HDMI`:

- `NVIDIA RTX 3060` / `AMD RX 6500 XT` or better

For `DP`:

- `NVIDIA GTX 10-series` / `AMD RX 500-series` or newer

Secondary PC CPU:

- minimum `6 threads`

Monitor:

- `HDMI 2.1 FRL 48 Gbps`
- or `DP 1.4 / DP 2.1`

## 18. DC500 Cables & Controls

### 18.1 Cable Layout

HDMI:

- Main PC -> `HDMI RX0`
- Second PC -> `HDMI RX1`
- Monitor -> `HDMI TX`

DP:

- Main PC -> `DP RX0`
- Second PC -> `DP RX1`
- Monitor -> `DP TX`

`RX0` and `RX1` can be swapped by holding `K4` for `3–5 seconds`

### 18.2 Ports / Power

- `DC12V` = main power
- `12V 3A` = optional backup power
- `USB-C` = debug / firmware updates

### 18.3 Buttons

- `K1` = info / EDID switch
- `K2` = increase overlay strength
- `K3` = decrease alpha / long-press reset
- `K4` = overlay enable/disable or swap layers

## 19. DC500 Troubleshooting & Indicators

### 19.1 Front Lights

- `DC` = monitor detected
- `RX0` = host/main PC detected
- `RX1` = secondary PC detected
- `RH` = overlay enabled

If a light is off, that signal is not detected.

### 19.2 `K1` Info Screen

Shows:

- `MAIN` resolution & refresh
- `SECOND` resolution & refresh
- `ALPHA`
- `BD`
- `UID`
- `EDID`
- `SEC`

### 19.3 EDID Modes

- `Mode A` = universal compatibility
- `Mode B` = native display compatibility

If customer has no image:

- long-press `K1` for `5 seconds`
- switch to `Mode B`

### 19.4 Common Fixes

No image but all lights on:

- long-press `K3` for reset
- reconnect cables
- reset monitor
- switch EDID

Black screen launching games:

- disable `G-SYNC`
- match game resolution to desktop
- reset GPU control panel settings

Repeating / tiled screen:

- same resolution on both PCs
- switch EDID
- long-press `K3`

Artifacts / image shift:

- long-press `K3`
- reboot fuser

### 19.5 Key Support Memory

For DC500 issues, first check:

- front lights
- K1 info
- EDID mode
- cable quality
- correct GPU ports

## 20. KM Box Net Setup

### 20.1 Port Layout

- `Port #1` -> `Second PC`
- `Port #2` -> `Main PC`
- `Port #3 or #4` -> keyboard or mouse

### 20.2 Network Setup

- open `Network and Sharing Center`
- open `Change adapter settings`
- find the `KM Box` network adapter
- if missing, unplug/replug KM Box
- open adapter `Properties`
- enable `Internet Protocol Version 4 (TCP/IPv4)`

### 20.3 Static IP

Set:

- `IP Address: 192.168.2.100`
- `Subnet Mask: 255.255.255.0`

### 20.4 Key Support Memory

If KM Box Net does not work:

- check ports
- check adapter visibility
- check IPv4 enabled
- check static IP

## 21. KM Box B+ Setup

### 21.1 Port Layout

- `Port #1` -> `Second PC`
- `Port #2` -> `Main PC`
- `Port #3 or #4` -> keyboard or mouse

### 21.2 Main Idea

KM Box B+ can mimic a mouse by using chosen:

- `VID`
- `PID`

Customer gets these from:

- `http://www.linux-usb.org/usb.ids`

### 21.3 Script Setup

- connect KM Box to `Second PC`
- run `upycraft.exe`
- ignore font message if shown
- under `Tools`, use `Board` / `Serial` as needed

In script:

- find dynamic VID/PID lines
- find `device.enable(1)`
- remove `#` from those lines

Replace default static values:

- `046d`
- `c07d`

With chosen `VID/PID`

### 21.4 Save & Upload

- `Ctrl + S`
- `Tools -> Download and Run`

### 21.5 Reboot KM Box

- unplug both blue USB cables
- wait until screen turns off
- plug them back in

Main PC should then detect the emulated mouse.

### 21.6 Key Support Memory

Most common failure points:

- wrong ports
- wrong VID/PID
- forgot to remove `#`
- forgot to upload script
- forgot to reboot KM Box

## 22. Best Support Habit for DMA Tickets

Always identify:

- card model
- exact stage
- which PC they are on
- exact error
- screenshot if possible

Best troubleshooting order:

1. wrong PC?
2. wrong port?
3. wrong cable?
4. wrong driver?
5. wrong BIOS setting?
6. bad speed test?
7. wrong flash setup?
8. accessory-specific issue?

## 23. Most Important DMA Support Lessons

- many DMA issues are not immediately firmware problems
- speed test is critical
- cable and port mistakes are very common
- BIOS mistakes are very common
- Makcu, Fuser, and KM Box each have separate setup logic
- customers often get lost because they do not know which stage they are in

## 24. Final Summary

The DMA docs are really teaching one big support idea:

Break every problem into a stage.

The stages are:

- main PC prep
- second PC drivers
- speed test
- troubleshooting
- firmware prep and flashing
- accessory setup

If you can identify the stage, the ticket becomes much easier to handle.

That is the core support skill for DMA.
