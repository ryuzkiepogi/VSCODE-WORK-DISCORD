# Duck's Services Support Master Handoff

## Purpose

This file summarizes the working support memory, reply style, ticket patterns, public-source notes, and internal behavior patterns learned throughout this chat.

It is written to help with:

- Discord ticket replies
- website support replies
- pre-sale bundle guidance
- DMA triage
- safe escalation habits
- messages to Sawyer / Mr. Duck

This is a working support reference, not a legal or official company manual.

## Core Support Role

Main role:

- handle Discord tickets
- answer short, practical, support-safe replies
- avoid guessing
- escalate unclear, undocumented, or high-risk questions

Main categories:

- 1PC products
- DMA products
- HWID Spoofers
- Installation Services
- pre-sale questions

Main team context:

- Sawyer = Mr. Duck
- Sawyer / Mr. Duck is the owner / manager
- Zesira and BMP are stronger DMA references
- Trix, BMP, and Zesira are useful internal reply references
- Duck's Services acts as a reseller/provider, not necessarily the direct developer of every product

## Support Mindset

Default process:

1. Identify the category
2. Identify the exact failed step
3. Ask for missing information
4. Use docs / support tool / public listing / known support memory
5. Escalate if unclear

Good habits:

- be calm
- keep replies short
- do not oversell
- do not promise things you cannot verify
- do not say "100% safe" or "guaranteed no bans"
- on DMA tickets, identify the stage before giving instructions

## Reply Style

Preferred tone:

- calm
- clear
- short
- polite
- practical

Best patterns:

- "Thanks for the details."
- "Please send..."
- "I don’t want to guess and give you the wrong answer."
- "Once I have that, I can point you to the correct next step."
- "I’d rather confirm that properly first."

## Official/Public Links

Main website:

- Home: https://ducks-services.com/
- Store: https://ducks-services.com/store/
- DMA page: https://ducks-services.com/dma/
- Docs: https://docs.ducks-services.com/
- Support Tool docs: https://ducks-services.gitbook.io/pre-setup-support-tool
- Trustpilot: https://www.trustpilot.com/review/www.ducks-services.com
- Key access page from docs: https://www.ducks-services.com/clients/purchases/

## 1PC Support Memory

Most common 1PC issues:

- loader will not open
- missing files
- Windows Defender / antivirus blocked files
- Windows blocked the file
- broken download link
- cannot find loader
- injection failed
- key/access confusion
- menu not opening

Best common fixes:

- disable Defender / antivirus
- check quarantine / protection history
- re-download to a fresh folder
- fully extract files
- right click -> Properties -> Unblock if shown
- run as Administrator
- install all VCRedist
- install DirectX
- restart PC

Public docs flow:

- Pre-Setup Guide
- Injection Guide
- Accessing Your Key

Useful 1PC support pattern:

"Please follow the official setup flow first:
- Pre-Setup Guide
- Injection Guide
- Accessing Your Key

If it still fails after that, send me the exact error, screenshot, and the point where it fails."

## Support Tool Memory

Support Tool use:

- ask customer to run the Support Tool
- ask for reference code if needed
- have them check the Windows Settings tab

Key settings to check:

- Real-Time Protection
- Vanguard
- FACEIT
- Virtualization
- Secure Boot
- UAC

If any are conflicting, customer should fix them first.

Utilities mentioned in docs:

- Redistributables x64
- DirectX
- Revo Uninstaller
- Proton VPN
- Windows 10 ISO

Safe support reply:

"Please run the Support Tool, go to the Windows Settings tab, and fix any conflicting items first. After that, let me know what still fails."

## Download / Link / Browser / ISP Issues

If customer sees:

- website not found
- ERR_CONNECTION_RESET
- ERR_SSL_PROTOCOL_ERROR
- MEGA stuck download

Safe reply pattern:

- try a VPN
- try another browser
- try a different network
- disable browser/security extensions temporarily
- send screenshot of the exact error
- send exact link clicked

Reason:

- often browser / ISP / firewall / network issue, not necessarily the product itself

## Accessing Keys

From docs:

- customers retrieve keys here: https://www.ducks-services.com/clients/purchases/

Safe reply:

"You can find your license key here: https://www.ducks-services.com/clients/purchases/
Please make sure you're signed into the same account used for the purchase."

## DMA Core Flow

Best mental order:

1. Hardware setup on main PC
2. JTAG driver on 2nd PC
3. FTDI / DATA driver on 2nd PC
4. Speed test
5. Troubleshooting
6. DNA ID if needed
7. Firmware flashing
8. Makcu / Fuser / KM Box if applicable

Always identify where they are stuck:

- hardware install
- JTAG
- DATA / FTDI
- speed test
- firmware
- Makcu
- Fuser
- KM Box

Key DMA questions:

- card model: 35t / 75t / 100t
- game
- firmware
- do they have a 2nd PC
- what exact stage are they on
- what accessory is involved

## DMA Setup Memory

Main PC:

- card installed in PCIe
- virtualization disabled in BIOS
- Memory Integrity off

2nd PC:

- JTAG driver goes here
- DATA / FTDI driver goes here

Speed test:

- critical step
- many DMA problems are cable / USB / driver / BIOS / speed related, not firmware first

## DMA Troubleshooting Memory

Known patterns:

- VMM INIT FAILED -> full shutdown / cold boot
- FT601 device error -> FTDI driver issue or wrong port
- Failed to retrieve Physical Memory Map -> bad USB connection
- info.db missing -> unzip fully, check dlls, internet/firewall
- TINY PCIe TLP -> poor USB or firmware limitation
- DTB / OS auto identify failure -> BIOS or USB issue
- DMA FAIL / low speed -> cable, port, power plan, card seating, weak 2nd PC
- missing entities / glitchy entities -> paged out memory, often more RAM needed on game PC

## DMA Product Guidance

Basic guidance:

- 35t = budget option
- 75t = best choice for most users
- 100t = higher-end, stronger long-term / future-proof option

From Sawyer:

- for Valorant / VGK, recommend 100t
- reason: larger capacity for larger, more complex firmware files
- more future proof than 35t / 75t

AMD note from Sawyer:

- AMD compatibility is no longer an issue
- firmware supports Intel and AMD now

## Firmware Memory

Known public tiers:

- lower tier: BE / COD / BF / FiveM
- middle tier: EAC / ACE / BE / COD
- higher tier: VGK / ACE / EAC / BE / COD

Coverage rule from Sawyer:

- if firmware bypasses EAC, it covers lower-tier anti-cheats by default
- if customer needs EAC, they do not need a separate BE-only version

Public firmware timing source:

- some firmware pages say:
  - not instant delivery
  - open a Discord ticket after purchase
  - firmware delivery can take up to 24 hours

Public sources:

- https://ducks-services.com/store/product/662-11-emulated-fw-ace-be-eac-cod/
- https://ducks-services.com/store/product/521-11-custom-fw-be-eac-cod/

Safe timing reply:

"Firmware delivery can take up to 24 hours depending on the product/setup."

## Firmware Upgrade / Warranty Memory

Important rules:

- do not assume all replacements are free
- warranty timing matters
- within warranty may be free replacement
- outside warranty may be 50% off replacement

Safe reply:

"I want to confirm the warranty timing first so I don’t give you the wrong replacement answer."

For payment / manual upgrade cases:

- better to mention Sawyer / Mr. Duck
- do not guess payment instructions

## DNA ID Memory

DNA ID is not always needed.

Important learned pattern:

- do not assume every firmware type needs DNA ID
- confirm first

Useful case:

- BE emulated firmware case did not need DNA ID
- Sawyer first asked:
  - Was it working before?
  - Did this happen all of a sudden?

Meaning:

- timeline / what changed is very important in firmware tickets

## JTAG / DNA ID Error Memory

CH347 Open Error:

- can happen if customer runs tool inside WinRAR archive
- can happen if they run as Administrator
- JTAG driver can also be missing

Safe reply:

"Please fully extract the files to a normal folder first and do not run the tool as administrator. Then try again."

## Makcu Memory

Known setup:

- left -> main PC
- middle -> second PC
- right -> mouse
- driver on 2nd PC
- COM port below 10
- restart Makcu after COM changes
- flashing done on 2nd PC

Important support pattern from Sawyer:

- if Makcu worked before but stopped after a long break:
  - start over completely with the setup
  - follow the flashing guide again
  - try different ports on both PCs

## Fuser / Capture / KM Box Memory

1K Fuser:

- main monitor to Fuser output, not direct GPU
- both PCs on Extend these displays
- 2nd PC background should be black
- requires 3 HDMI 2.0 cables

DC500:

- do not mix HDMI and DP
- use one interface type only
- EDID mode B can help

KM Box Net:

- port 1 -> second PC
- port 2 -> main PC
- static IP 192.168.2.100 / 255.255.255.0

## 2nd PC / Mini PC Memory

Mac as 2nd PC:

- can work if Windows is installed
- but does not run very well

Cheap recommendation used by Sawyer:

- Beelink Mini S12 Pro Mini PC

Performance guidance:

- 8GB RAM can work but is a concern
- 16GB is more standard now
- if overlay/ESP disappears after some minutes, ask:
  - specs
  - RAM usage
  - CPU usage
  - cable / USB stability
  - video of the issue if unclear

## Pre-Sale Patterns

Always ask:

- what game(s)
- 1PC or DMA
- current hardware
- AMD or Intel if relevant
- budget if needed

Bundle guidance:

- 75t Ultimate Bundle is best for most users
- for VGK / Valorant, 100t is usually better
- higher firmware tiers mainly mean higher anti-cheat coverage

Safe firmware explanation:

"The main difference between the firmware options is the anti-cheat coverage. Higher tiers include lower-tier coverage by default."

## Shipping / Tracking Memory

Public-safe shipping guidance:

- hardware usually ships within 0-2 business days
- delivery after shipping can take around 2-5 business days
- sometimes up to about 1 week

Safe reply:

"Please wait a little longer and Mr. Duck will process it as soon as possible. Once it ships, you should receive the tracking information as well."

## Common Escalation Cases

Escalate or confirm first for:

- bans / ban reasons
- "100% safe" questions
- undetected guarantees
- dev-only errors
- firmware upgrade payment steps
- VGK file re-access
- discount / promo / coupon specifics
- backend account/order issues
- questions about whether Duck's directly made a product

## Useful Support Replies

Need more info:

"Please send the exact product, screenshot, and error message so I can check the correct next step."

Ban question:

"I don’t want to guess on ban-related behavior and give you the wrong answer. I’d rather have that confirmed properly first."

Loader/menu not opening:

"Please send a screenshot of the loader after injection, whether the injection shows as successful, and whether you already installed VCRedist and DirectX."

Broken link:

"Please try a VPN, another browser, or a different network. If it still fails, send the exact link and a screenshot of the error."

Shipping:

"Hardware orders usually ship within 0-2 business days, then delivery can take around 2-5 business days, and in some cases up to about 1 week."

Closing ticket:

"If you don’t have any other questions, I can go ahead and close the ticket now."

Trustpilot ask:

"If I was able to help you today, I’d really appreciate it if you could leave a review on Trustpilot and mention RyuzukieShin. It would mean a lot.
https://www.trustpilot.com/review/www.ducks-services.com"

## Sawyer / Mr. Duck Communication Notes

Useful patterns with Sawyer:

- call him "brother" naturally if he uses it too
- keep messages short
- be honest when you need guidance
- mention him for discounts / payment / special approvals

Important conversation outcomes:

- he confirmed you are moving forward in the role
- your working schedule is 2 PM to 10 PM PH time
- there are currently no extra company benefits outside pay
- he said you can go through tickets together in real time to learn

Helpful message style to Sawyer:

"Hi Sawyer, someone is asking about [topic] in the website support request when you have time. Thank you."

## Personal Safety / Boundaries Notes

If staying in the role, safest boundaries are:

- keep answers at customer-service level
- avoid deep guidance on bans / bypasses / detection
- do not promise safety
- do not personally send files unless appropriate / approved
- escalate dev / advanced questions
- keep records of work and payments

Safe job description to others:

- "I do remote customer support."
- "I handle Discord tickets and online customer inquiries."

## Reusable Prompt

Use this prompt in a new chat if needed:

"You are helping me as a support assistant for Duck’s Services.

Important context:
- I handle Discord tickets and website support.
- Prioritize accurate, safe, support-style answers.
- Keep replies calm, short, polite, and practical.
- If something is unclear, undocumented, too technical, ban-related, payment-related, firmware-upgrade-related, or dev-related, prefer clarification or escalation instead of guessing.

Main categories:
- 1PC products
- DMA products
- HWID Spoofers
- Installation Services
- pre-sale questions

Important team context:
- Sawyer = Mr. Duck = main owner/manager
- Zesira and BMP are stronger for DMA questions
- We are resellers/providers, not necessarily the direct developers of every product

Main support flow:
1. Identify the category
2. Identify the exact failed step
3. Ask for missing info
4. Use docs/support tool/public listing/internal memory first
5. Escalate if unclear

Main links:
- Home: https://ducks-services.com/
- Store: https://ducks-services.com/store/
- DMA: https://ducks-services.com/dma/
- Docs: https://docs.ducks-services.com/
- Support Tool: https://ducks-services.gitbook.io/pre-setup-support-tool
- Trustpilot: https://www.trustpilot.com/review/www.ducks-services.com
- Keys: https://www.ducks-services.com/clients/purchases/

Important memory:
- 75t is the best choice for most users
- 100t is preferred for Valorant / VGK and more future-proof setups
- AMD is no longer an issue; firmware supports Intel and AMD now
- Higher firmware tiers mainly mean broader anti-cheat coverage; higher tiers include lower-tier support by default
- Firmware delivery can take up to 24 hours depending on the product/setup
- For shipping, hardware usually ships within 0-2 business days, then takes around 2-5 business days, sometimes up to about 1 week
- CH347 Open Error can be caused by not extracting files first or by running as admin
- If Makcu worked before but stopped after a long break, start over completely and try different ports
- For 1PC issues, common fixes are disabling antivirus, checking quarantine, re-downloading to a fresh folder, extracting fully, unblocking, running as admin, installing VCRedist and DirectX, and restarting

Reply rules:
- If I ask for a reply, draft the exact message I can send
- If I ask what the main issue is, give the likely cause first, then the safest answer
- Do not overwhelm me unless I ask for depth
- Default to support-safe wording
- If not sure, say so and suggest escalation

When possible, help me with:
- exact customer replies
- messages to Sawyer / Mr. Duck
- internal clarification messages
- memory notes from tickets
- support-safe explanations"

## Recent Updates

### Keys / Subscriptions

New memory from Sawyer:

- key timer is automatic
- time starts once the key is used for the first time
- if a customer says the time display looked wrong, one possible cause is a timezone mismatch with the server
- if they purchased a 24 hour key, they received 24 hours of use

Safe reply:

"Hi, the key timer is automatic and starts once the key is used for the first time. If the time looked off, it could have been a timezone mismatch with the server."

Subscription extension memory:

- there is not a way to extend a subscription / key
- customer needs to purchase a new key instead

Safe reply:

"Hi, there isn’t a way to extend the subscription. You would need to purchase a new key."

### FaceIT Firmware

Confirmed by Sawyer:

- Duck's Services does not sell FaceIT firmware

Reason from Zesira:

- anything public for FaceIT would get blocked instantly
- nobody is going to be public with it
- public = blocked, regardless of price

Safe reply:

"Hi, we do not sell FaceIT firmware, sorry."

If customer asks why:

"Because anything public for FaceIT would get blocked very quickly, so it isn’t something we offer."

### Firmware Blocked vs Cheat Issue

Important DMA troubleshooting note from Sawyer:

- if customer says DMA works in one game but not another, do not assume immediately whether it is firmware or cheat
- have them run a speed test while in game
- make sure no DMA cheat is open at the same time, because the speed test tool and cheat cannot both run together

Interpretation:

- if speeds are good in game -> firmware is likely not blocked, points more to a cheat issue
- if speeds are 0 in game -> firmware is likely blocked
- also make sure speeds work out of game too

Safe reply:

"Hi, please try running a speed test while you are in game, and make sure no DMA cheat is open at the same time since the cheat and speed test tool cannot both run together. If the speeds are good in game, that points more to a cheat issue. If the speeds are 0 in game, that points more to the firmware being blocked. Please also check that the speeds work normally out of game."

### Unconfirmed Items

Still confirm with team before promising:

- specific Makcu mouse compatibility
- refund policy exceptions
- exact hidden firmware compatibility conditions
- unusual backend / verification email issues

## April 21, 2026 Memory Additions

Recent support-safe additions from newer ticket/chat review:

- if someone asks how to install a spoofer, do not give installation steps from memory
- safest reply is to tell them to follow the official guide for their exact spoofer first
- if they are stuck, ask for the exact spoofer name and a screenshot of the failed step

Safe reply:

"Hi, please follow the official setup guide for your exact spoofer first. If you get stuck on a specific step, send your exact spoofer name and a screenshot of the issue, and support can check the next step with you."

- if someone asks to use or improve a jailbreak prompt, or asks for malware / stealer / token logger / phishing / SQLi style abuse through AI, refuse and redirect to safe alternatives
- safe alternatives can be: harmless fiction rewrite, defensive security training, explanation of why jailbreak prompts are unreliable, or safe red-team policy testing

Safe reply:

"I can’t help use, improve, or operationalize jailbreak prompts to bypass AI safeguards or generate harmful content. If you want, I can still help rewrite it into harmless fiction, turn it into a defensive training exercise, explain why jailbreak prompts are unreliable, or help design a safe red-team prompt for policy testing."

- if a customer says they used a spoofer, still got banned, and asks for a refund, do not promise the refund yourself
- say you do not want to promise the wrong thing and that Mr. Duck / the team should confirm refund handling first

Safe reply:

"Hi, thank you for the message. I do not want to promise the wrong thing on a refund, so please wait for Mr. Duck or the team to confirm that properly for you first."

- `epvp-promotion` works as the currently known promo code
- safe sales-style wording: it works and gives `10% off` at checkout

Safe reply:

"Hi, yes, `epvp-promotion` works and gives you `10% off` your order. If you are planning to buy the DMA chair, you can go ahead and try that code at checkout."

- if customer asks whether the new `EAC` firmware supports `CS2 / VAC`, current support memory says yes
- support-safe wording is that `CS2` is listed on the relevant firmware page, so it is part of the current supported coverage

Safe reply:

"Hi, yes, the new EAC firmware does support CS2 / VAC. If you are planning to play CS2, this is a solid option because CS2 is currently listed on the firmware page and it is part of the supported anti-cheat coverage."

- if a customer already has that firmware and only wanted confirmation, a short closeout is enough

Safe reply:

"No problem, you’re welcome. If you have any other questions, just mention us."

- if someone asks for a key reset because they used a temporary spoof, do not promise timing
- safest wording is that it was already sent to dev / team and they should resolve it once notified or once they read it

Safe reply:

"Hi, this was already sent to the dev/team side. Once they are notified or read it, they should be able to sort it out. Thank you for understanding."

- `DC500` fuser restock memory from the newer chat says it is currently `back-ordered`
- do not promise exact restock timing unless team confirms it

Safe reply:

"Hi, the DC500 fuser is currently back-ordered. I would rather have the team confirm any restock timing properly before I promise that."

- if an AI helper hits a usage limit and shows an obviously wrong future time/date, do not repeat it to the customer as if it were a real support answer
- switch to a manual reply instead of forwarding the broken limit message

### April 23, 2026 Memory Additions

Ban case memory:

- if a customer says they kept the cheat/spoofer on a `USB stick`, removed the USB, and only then launched the game, do not confirm that this makes them safe
- if they later show a ban screen such as `THE FINALS - Permanently suspended`, do not guess the exact cause of the ban
- do not promise a refund yourself on that basis
- safest path is:
  - acknowledge the screenshot
  - say you do not want to guess on ban causation
  - direct them to the game's own ban/review policy for appeal handling
  - if they ask about refund handling, wait for `Mr. Duck` / team confirmation first

Safe reply:

"Hi, thank you for the screenshot. I do not want to guess on the exact cause of the ban and give you the wrong answer. For the ban itself, please follow the game's review/appeal process shown there. If you want to ask about refund handling, I would rather have Mr. Duck / the team confirm that properly first."

AMD library fix memory:

- if a loader or product still fails after installing the latest libraries, and the customer has an `AMD` graphics card, there is a known AMD-specific fix flow
- support order:
  - install the latest libraries first
  - if that does not help, confirm they have an AMD GPU
  - open `Task Manager` and end AMD-related processes such as `AMD Radeon`, `AMDSrv`, `AMDOW`, `CPUMetrics`, and similar AMD processes
  - go to the AMD software folder, usually `C:\Program Files\AMD\CNext\CNext`
  - download/extract the replacement `Libs`
  - copy and replace the `DLL` files into `CNext\CNext`
- use this as a team-confirmed fix path and do not freestyle missing file names if they were not provided in the ticket/team message

Safe reply:

"Please install the latest library package first. If that still does not fix it and you have an AMD graphics card, please close all AMD-related processes in Task Manager, then go to `C:\Program Files\AMD\CNext\CNext`, and replace the DLL files there with the files from the provided `Libs` archive."

Additional confirmed support memory:

- exact `DMA Installation Service` product link:
  - `https://ducks-services.com/store/product/1396-dma-installation-service/`
- exact lower-tier `BE / COD / BF / FiveM` firmware product link:
  - `https://ducks-services.com/store/product/521-11-emulated-be-cod-bf-fivem/`
- for `Siege`-only firmware sales questions, the saved product is:
  - `1:1 Emulated - BE / COD / BF / FiveM`
  - product link: `https://ducks-services.com/store/product/521-11-emulated-be-cod-bf-fivem/`
- for `Apex` on the `$150` firmware, support-safe website wording is:
  - `1:1 Emulated - ACE / EAC / BE / COD`
  - product link: `https://ducks-services.com/store/product/662-11-emulated-ace-eac-be-cod/`
- if a customer says the loader/download page says `webpage not secure`, a safe first step is:
  - ask them to try a `VPN`
  - if it still fails, ask for the exact link and a screenshot

Safe replies:

"Hi, please try using a VPN first and then open the link again. If it still shows the same warning, please send a screenshot of the exact message and the link you clicked so I can check it properly."

"Hi, for Siege only, the firmware you want is `1:1 Emulated - BE / COD / BF / FiveM`.

Here is the link:
https://ducks-services.com/store/product/521-11-emulated-be-cod-bf-fivem/

Once your mini PC arrives, just notify us and we can help you with the next step."
