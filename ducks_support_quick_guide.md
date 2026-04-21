# Duck's Services Support Quick Guide

## Access Note

This quick guide was created from the local Duck's Services source material already present in this workspace:

- `ducks_support_master_handoff.md`
- `ducks_services_support_memory_handbook.md`
- `ducks_services_dma_master_summary.md`

It is a practical working guide, not an official company policy document.

## Main Goal

Use this guide to handle support tickets with short, safe, useful replies.

Main priorities:

1. identify the ticket category
2. identify the exact failed step
3. ask for missing information
4. use the docs, support tool, and known workflows first
5. escalate if the answer is unclear or risky

## Main Categories

- `1PC products`
- `DMA products`
- `HWID Spoofers`
- `Installation Services`
- `Pre-sale questions`

## Team Context

- `Sawyer = Mr. Duck`
- `Zesira` and `BMP` are stronger references for advanced DMA issues
- Duck's Services acts as a reseller/provider, not necessarily the direct developer of every product

## Reply Style

Replies should be:

- calm
- short
- polite
- practical
- not overconfident

Avoid:

- guessing
- promising things you cannot verify
- saying `100% safe`
- saying `guaranteed no bans`

Useful reply patterns:

- `Please send a screenshot of the exact issue.`
- `Please send your exact product and what happens when you try.`
- `Once I have that, I can point you to the correct next step.`
- `I don't want to guess and give you the wrong answer.`
- `I want to confirm that properly first.`

## Key Links

- Home: `https://ducks-services.com/`
- Store: `https://ducks-services.com/store/`
- DMA page: `https://ducks-services.com/dma/`
- Docs: `https://docs.ducks-services.com/`
- Support Tool docs: `https://ducks-services.gitbook.io/pre-setup-support-tool`
- Key access page: `https://www.ducks-services.com/clients/purchases/`

## Standard Ticket Workflow

For every ticket:

1. identify whether it is `1PC`, `DMA`, `spoofer`, `installation`, or `pre-sale`
2. find the exact step that failed
3. ask for missing details
4. check the matching docs or support tool flow
5. only escalate after basic checks are covered

Best default questions:

- what product did you purchase?
- what exactly happens when you try?
- can you send a screenshot?
- did Defender or antivirus block anything?
- did you fully extract the files?
- if DMA: what hardware model and what exact stage are you stuck on?

## 1PC Quick Handling

Most common issues:

- loader will not open
- Windows blocked the file
- Defender or antivirus deleted files
- injection failed
- customer cannot find the loader
- key or access confusion

Best common fixes:

- disable Defender or antivirus temporarily
- check quarantine or protection history
- re-download to a fresh folder
- fully extract the archive
- right-click the file and use `Properties > Unblock` if present
- run as administrator
- install `VCRedist`
- install `DirectX`
- restart the PC

If the issue still does not make sense after normal checks, escalate instead of improvising.

## Support Tool Workflow

This is one of the most useful first-line support paths.

Customer side:

1. run the support tool
2. correct flagged items if instructed
3. press `SEND TO SUPPORT`
4. send the reference code

Support side:

1. search the code
2. review the embed
3. check obvious blockers first

Important checks commonly mentioned:

- `Real-Time Protection`
- `Vanguard Anti-Cheat`
- `FaceIT Anti-Cheat`
- `Firmware Virtualization`
- `Secure Boot`
- `UAC`

## DMA Quick Handling

DMA tickets should be handled more carefully than normal 1PC tickets.

Always identify:

- card model
- firmware
- which PC they are working on
- exact error
- current stage in the setup flow

Recommended DMA thinking order:

1. hardware setup
2. JTAG driver
3. DATA driver
4. speed test
5. troubleshooting
6. firmware prep or DNA ID
7. firmware flashing
8. accessory setup such as `Makcu`, `Fuser`, or `KM Box`

Important DMA reminder:

Many DMA issues are not firmware issues first. They are often:

- wrong port
- bad cable
- wrong driver
- BIOS settings not changed
- unstable USB connection
- poor speed test results

## DMA Questions To Ask First

- what DMA card model are you using?
- what firmware are you using?
- what exact issue or error are you getting?
- what stage are you currently on?
- can you send a screenshot of the error or Device Manager?
- did this start after a specific change?

## Common DMA Trouble Areas

Check these before assuming something advanced is broken:

- correct PC being used for the step
- correct port used: `JTAG` vs `DATA`
- correct `FTDI` driver state in Device Manager
- BIOS virtualization settings disabled
- `Memory Integrity` disabled if required
- speed test healthy enough to proceed

## Accessories Quick Notes

`Makcu`

- cable placement matters
- COM port should usually be below `10`
- both left and right flashing steps matter

`Fuser`

- verify cable type and display mode first
- for `DC500`, do not mix `HDMI` and `DisplayPort`
- front indicators and EDID mode are important for troubleshooting

`KM Box`

- port layout matters
- IP or script setup mistakes are common

## Escalate Earlier If

- firmware advice is unclear
- BIOS guidance is uncertain
- website or download link appears broken
- backend, login, or payment issue is involved
- loader behavior is strange after normal checks
- the problem is outside docs and known workflows
- the customer is asking for guarantees about safety or bans

## Recent Ticket Memory

`DMA speed on a stronger 2nd PC`

- a stronger second PC does not automatically mean better DMA speed
- if speed improves after changing the cable, the most likely cause is still cable quality or the USB ports on the second PC
- `BMP` guidance in one ticket was that the issue was the second-PC USB ports or cable
- if the second PC is a laptop, ask that early because laptop USB behavior can be a major factor
- a jump from around `2000` to around `5000` after changing the cable strongly points to connection quality, not just raw PC performance

`ABI / firmware safety questions`

- do not promise a customer they will not get banned
- if a customer asks for an honest answer about whether firmware is worth buying after being banned before, keep the answer careful and avoid guarantees
- internal anecdotal feedback may suggest the firmware itself is considered safe, but that is not the same as a promise of no bans
- if the customer asks for a stronger safety claim, confirm with the team first instead of escalating your wording on your own

`Firmware delivery timing`

- one internal reply said firmware delivery typically does not take long
- support memory should still be phrased safely as delivery can depend on the setup and may take up to `24 hours`
- avoid overcommitting to a narrow delivery window unless the team confirms it for that product

`EFT Next feature questions`

- if a customer asks whether they can use all features, including risky ones, even in `PVE`, do not answer with a blanket yes from memory alone
- feature availability can change, and some options may be patched or removed
- one example from team chat was that `fast reload` was believed to be patched by the Tarkov developers with no workaround
- safest path is to answer only the clearly confirmed part and avoid promising every listed option is currently usable

`Password reset / email not received`

- treat missing password reset emails as an account or backend-style issue first
- check basic causes like wrong email, spam folder, or delay, but avoid guessing deeper causes if it still does not arrive
- if it continues after normal checks, confirm with the team or admin side

`Arma Reforger loader / vc_redist error`

- if the loader shows an error asking for the latest `vc_redist.x64.exe`, first tell the customer to install the latest Microsoft Visual C++ Redistributable and restart the PC
- one team reply from `Trix` said that if installing the latest libraries does not help and the customer has an `AMD` graphics card, there may be an AMD-specific fix
- the AMD-specific team flow was:
- close all AMD-related processes in Task Manager
- examples mentioned: `AMD Radeon`, `AMDSrv`, `AMDOW`, `CPUMetrics`, and other AMD-related processes
- go to the AMD software folder, usually `C:\Program Files\AMD\CNext\CNext`
- copy and replace the provided DLL files into that folder
- use this carefully as team-memory guidance, and do not freestyle missing file names if they were not provided in the ticket or by the team
- safest support order:
- install latest libraries first
- if still failing, ask whether the customer uses an AMD GPU
- if yes, follow the known AMD fix provided by the team

`Sync spoofer expiry / unspoof behavior`

- one team reply from `Trix` said the system unspoofs whenever the customer restarts the PC
- if the sync spoofer time ran out but the PC has not been restarted yet, support memory suggests the customer would still be in the current spoofed state until restart
- safest wording is to avoid overcomplicating it and explain that restart is the point where it unspoofs

`Vanguard / vgk.sys disable fix`

- if the loader error says to uninstall `vgk.sys`, one team reply from `Trix` was to do what the error says by disabling Vanguard from startup
- known command prompt fix from team memory:
- `sc config vgk start= disabled`
- `sc config vgc start= disabled`
- these should be run in an `Administrator Command Prompt`
- after running them, the customer should restart the PC
- safest support wording is to keep it simple and direct the customer to disable Vanguard startup, then reboot

`Arcane / Hyper-V / PIN issue`

- if `Arcane Arc Raiders` says to disable `Hyper-V` and the customer says they already disabled it in normal ways, one team fix from `Trix` was to manually disable it using the Microsoft `DG_Readiness_Tool`
- known team wording included:
- `Please make sure PIN is not set in Windows sign-in options and manually disable Hyper-V using dgreadiness tool`
- the known team flow was:
- download the Microsoft `Device Guard and Credential Guard hardware readiness tool`
- extract the ZIP
- open `PowerShell` as administrator
- run: `Set-ExecutionPolicy Unrestricted -Scope Process`
- then run: `.\DG_Readiness_Tool_v3.6.ps1 -Disable`
- this was used to disable `Device Guard` and `Credential Guard`
- if the customer then gets stuck because Windows PIN is unavailable, one team reply from `Trix` was to use this guide:
- `https://www.youtube.com/watch?v=sHnv3NHOzG8`
- if the key expires while the customer is still actively troubleshooting, team memory shows that key time may sometimes be extended by staff, so do not assume the ticket is over just because the customer ran out of time mid-fix
- if the customer asks to switch from one cheat to another because one does not work on their machine, do not promise the swap yourself unless confirmed by `Mr. Duck` or team

`Caruso / 2nd PC requirements`

- one team reply from `Trix` gave these second-PC requirements:
- `4-core CPU`
- `8GB DDR4 RAM`
- `USB 3.0`
- in that same reply, `Trix` said the `DICHEN Official FPGA 75T DMA Card` works fine
- a `Dell OptiPlex 3060 Micro` with `Intel i5-8500T`, `8GB RAM`, and SSD was treated as a good fit for that requirement

`ACE Security Center / Secure Boot popup`

- if the customer gets an `ACE Security Center` popup saying `Secure Boot enable` is required, the team memory says to enable `Secure Boot` in BIOS
- one team reply from `Trix` said the cheat is not stream-proof, so it cannot be hidden on Discord screenshare
- safest support wording:
- tell the customer to enable `Secure Boot` in BIOS
- tell them the cheat cannot be hidden on Discord screenshare
- if they ask whether it is safe to use while secure boot is enabled, one team reply said `yes`

`Overlay / mouse / aimbot behavior`

- if the overlay is stuck on screen and the mouse stops working in-game, one team reply from `Trix` was to close the menu with `Insert`
- after closing the menu, the mouse should work again
- if the customer says aimbot is not working, check whether the bind is set to a hold key and remind them they must hold the key they assigned
- one team reply said the bind type can be changed by right-clicking the `hold` option
- `silent aimbot` was described by team memory as always on / risky compared with normal aimbot behavior
- if the customer thinks the feature is broken, first check whether the bind is actually being held and whether the menu is still open

`Firmware discount / game compatibility questions`

- if a customer asks whether they get a discount on firmware because their warranty ran out, treat it as a pricing/offer question that should be confirmed with `Mr. Duck` or the team
- one internal bot reply suggested replacement firmware may sometimes be offered at `50% off` with a new warranty, but do not promise that to customers without confirmation
- if the customer asks whether firmware works for a specific game like `Apex Legends` or `Fortnite`, do not give a blanket compatibility guarantee from memory
- safest path is to confirm the exact firmware option or use `.dmaquiz` / team confirmation before promising game support

`Firmware claim / boot issue after flash`

- firmware claims cannot be processed without a valid `order number`
- one firmware ticket flow used `order number`, `hardware model`, and `DNA ID` before building
- for a `100t MAVISDMA` claim, the known DNA output was used to compile the firmware successfully
- if the customer says Windows will not boot after flashing and it now hangs on the motherboard logo, the likely support path is:
- confirm BIOS settings are still correct
- check whether the flash was the correct one for the hardware model
- if the issue persists, the team may need to rebuild and flash a new firmware
- if a customer says they were able to reboot fast before flashing but not after, treat that as a post-flash boot problem rather than a normal Windows issue

`DMA testing firmware`

- default DMA firmwares are only for confirming the card is functioning correctly
- they are not meant for in-game use
- testing firmware names saved in memory:
- `35t Testing Firmware`
- `75t Testing Firmware`
- `100t Testing Firmware`

`Titan driver fix`

- one team fix from `Zesira` said to try this before switching to zero
- turn the DMA off
- boot the PC
- open `CMD` as admin
- run: `pnputil /delete-driver oem52.inf /uninstall /force`
- restart the main PC
- install the manual drivers using `Option 2`
- turn the card back on and reboot to test again
- if the exact `oem` number is different, confirm it from `pnputil /enum-drivers` before deleting

`Vellix EAC main PC driver`

- one shared team link for the main PC driver was:
- `https://drive.proton.me/urls/CCK3W5W3GG#N4UFuP4oE0TH`

`Creative / BE driver notes`

- after firmware flash and power cycle, install the matching driver for the firmware
- one team link for the standard driver was:
- `https://support.creative.com/downloads/download.aspx?nDownloadId=100373`
- after installing, set your preferred sound device as default
- do not disable devices in Device Manager
- if using `BE` firmware, install the matching `BE` driver package instead of the standard one
- another team guide said to unpack `TitaniumV3Guide.rar`, open the `2021` folder, then the `wdm` folder, and install `wdma_emu.inf`
- if doing a clean uninstall, the team flow was:
- open `CMD` as admin
- run `pnputil /enum-drivers`
- find the Creative entry and note the `oemXX.inf`
- run `pnputil /delete-driver oemXX.inf /uninstall /force`
- restart the PC

`75t / 100t flashing and driver placement`

- flashing the firmware is done on the `2nd PC`
- the `JTAG` driver goes on the `2nd PC`
- the flashing tool is also used on the `2nd PC`
- after flashing, the main PC needs the matching driver installed from the unzipped driver folder
- one team note said to unzip the driver package on the main PC, find `access.inf`, right-click it, and install it
- if the driver does not appear, re-download and unzip the driver package again
- one support note for the `DICHEN Official FPGA 75T DMA Card` showed a DNA ID and successful firmware claim flow using the order number plus hardware model

`DMA speed and crash follow-up`

- a speed around `5600` was treated as good enough in one ticket
- if the firmware is installed but the game crashes, do not assume the firmware is the only problem
- one team fix list for game crashing included:
- check whether `Enable Steam Input` is on
- verify game files
- try `Warp` or `Windscribe` on the `2nd PC`
- uninstall the latest Windows security update if needed
- disable Windows auto updates
- sync time in `Date & Time`
- run these as admin and wait for each to finish:
- `DISM /Online /Cleanup-Image /ScanHealth`
- `DISM /Online /Cleanup-Image /CheckHealth`
- `DISM /Online /Cleanup-Image /RestoreHealth`
- `SFC /Scannow`
- install the latest chipset driver from the motherboard manufacturer
- cold shut both PCs down for `2-3 minutes`
- reinstall the game/tool if needed
- let shaders rebuild
- turn off `Unlock Clothes`
- turn off `Hotzone`

`Close-out / Trustpilot template`

- if the ticket is resolved and there are no more questions, one common team close-out was:
- `If you don’t have any other questions, I can go ahead and close the ticket now.`
- then:
- `If I was able to help you today, I’d really appreciate it if you could leave a review on Trustpilot and mention RyuzukieShin. It would mean a lot.`
- then the Trustpilot link:
- `https://www.trustpilot.com/review/www.ducks-services.com`

## Safe Internal Message Template

Customer is using `[product/setup]` and is stuck at `[exact stage]`.
They reported `[exact error/symptom]`.
I already checked `[basic checks already covered]`.
This looks like it may need confirmation before I advise further. Can someone confirm the correct next step?

## Short Reply Templates

General first reply:

`Hi, please send your exact product and a screenshot of the issue so I can check the correct next step for you.`

Need more info:

`Please send the exact error, a screenshot, and tell me what happens when you try. Once I have that, I can guide you properly.`

Support tool:

`Please run the support tool, send the reference code here, and I'll review it for you.`

DMA clarification:

`Please tell me your DMA card model, firmware, and the exact stage you're stuck on, and send a screenshot if possible.`

Escalation-safe reply:

`I want to confirm this properly first so I do not give you the wrong steps. I'll check the correct guidance for your setup.`

## Bottom Line

The safest Duck's Services support habit is simple:

- identify the category
- identify the failed step
- gather the missing details
- use the official docs and support tool first
- escalate when the answer is not clear
