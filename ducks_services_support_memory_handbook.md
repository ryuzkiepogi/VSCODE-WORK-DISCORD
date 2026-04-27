# Duck's Services Support Memory Handbook

Prepared from extended training/chat notes.

Purpose: preserve the practical knowledge, reply patterns, workflows, source links, internal reminders, and people/context learned during this conversation so the information still exists even if the chat is gone later.

This is a personal working reference. It is not an official company manual.

## 1. Main Goal of This Handbook

This handbook is meant to preserve:

- the business/product overview
- how support tickets should be approached
- the difference between simple tickets and escalation tickets
- how to use the store, DMA page, docs, support tool, and Discord commands
- internal reminders learned from teammates and copypasta
- customer reply style
- safe escalation habits
- key people and team context
- source links used during training

The most important principle repeated throughout all of this:

- do not guess when the issue is unclear
- use the docs and official tools first
- ask for missing information
- escalate when needed

## 2. Team / People Context

Important names mentioned during training:

- `Sawyer / Mr. Duck`
- `Zesira`
- `BMP`
- `Trix`

Main relationship/flow learned:

- Sawyer is the main owner/decision-maker
- Zesira and BMP are major support references for technical/support clarification
- Trix/BMP/Zesira past replies are useful internal knowledge sources
- if something is unclear, especially DMA/firmware/backend issues, it is normal to ask them first

Important mindset from Sawyer/team:

- first days will involve many escalations
- asking smart questions is better than giving wrong information
- repetitive issues become easier with time
- docs are a main reference, but not every answer is in the docs

## 3. What Duck's Services Sells

High-level categories:

- `1PC products`
- `DMA products`
- `HWID Spoofers`
- `Installation Services`
- accessories and hardware through the DMA section

### 3.1 1PC Products

These are regular loader-based products used on the gaming PC.

Normal support pattern:

- easier to learn
- common beginner tickets
- many repeated issues

Most common issue types:

- key/access confusion
- loader not opening
- antivirus blocking files
- injection errors
- missing files
- browser/download problems

### 3.2 DMA Products

DMA is the more advanced side of support.

Main elements:

- DMA card
- firmware
- second PC or mini PC
- fuser
- aiming device like Makcu or KMBox
- drivers
- flashing tools

General support mindset:

- gather exact hardware model
- gather firmware
- gather game
- gather license key/order if relevant
- do not guess on advanced hardware/firmware questions

### 3.3 HWID Spoofers

Separate product category.

Common support pattern:

- compatibility checker issues
- download/page not opening
- crashes/sign-in issues after spoofing
- verifying whether serials changed

### 3.4 Installation Services

Customers may buy installation help separately.

Support handling pattern:

- confirm they bought the installation service
- ask for order number
- ask what product needs setup help
- ask if they are available now
- do not promise the live install yourself unless confirmed
- route to the right person/team member

## 4. Core Support Mindset

The biggest lessons from the chat:

- you do not need to know everything immediately
- you do need to know how to think through tickets
- the best support is careful, clear, and consistent
- the goal is not to sound smart; the goal is to avoid misinformation

The safest mental model:

1. What category is this?
2. What exact step failed?
3. Is the answer clearly in the docs/tool/site/internal notes?
4. If not, what information is missing?
5. Can I answer safely, or should I escalate?

## 5. Best Reply Style

Preferred tone:

- calm
- clear
- short
- polite
- not overly technical unless necessary
- not fake-confident

Good support habits:

- acknowledge the issue
- ask for the exact missing details
- use one-step-at-a-time troubleshooting when needed
- if unsure, say you are checking with the team

Good patterns:

`Checking first`

Hi, thanks for the details. I’m checking the correct steps for your setup now and will update you shortly.

`Need more info`

Please send your exact product, hardware model, firmware, or a screenshot of the error so I can check it properly.

`Escalation`

I want to confirm that properly first so I don’t give you the wrong information.

## 6. The Main 1PC Customer Flow

This is the most important beginner support flow:

`buy -> key -> redeem -> download -> extract -> run as admin -> log in -> inject/load -> launch -> use in-game`

Most normal issues happen because one step in this chain failed.

### 6.1 Buy / Product Confusion

Customer problems:

- bought wrong product
- does not know which product applies to their game
- cannot find where to start

### 6.2 Key / Redeem

Customer problems:

- key not visible
- key not working
- wrong account
- wrong redemption process
- purchase not showing

### 6.3 Download / Loader

Customer problems:

- broken link
- cannot find loader
- launcher won’t open
- missing files
- browser blocks download

### 6.4 Security / AV / Windows Block

Common recurring cause:

- Windows Defender or antivirus blocked/removed files
- Windows blocked the downloaded file
- file wasn’t extracted

### 6.5 Injection / Launch

Common recurring cause:

- missed guide step
- setup order issue
- product update/status issue
- security block still active

## 7. Main Websites and What They Are For

### 7.1 Home

`https://ducks-services.com/`

Use for:

- company overview
- general categories
- trust/sales context

### 7.2 Store

`https://ducks-services.com/store/`

Use for:

- identifying product categories
- game/product listings
- checking what the customer likely bought
- pricing context

Important observed categories:

- games/products by title
- `DMA`
- `HWID Spoofer`
- `Installation Services`

### 7.3 DMA Page

`https://ducks-services.com/dma/`

Use for:

- DMA bundles
- DMA cards
- fusers
- aiming devices
- firmware pricing/options
- accessories
- mini PCs

Important text learned from DMA page:

- bundles are customizable
- customers can choose firmware that suits their needs
- higher-tier cards support more advanced firmware
- baller bundles include DC500 fuser

### 7.4 Admin

`https://ducks-services.com/admin`

Use for:

- searching users by username/email/license key
- checking support/backend info

### 7.5 Docs / GitBook

`https://docs.ducks-services.com/`

Use for:

- setup guides
- key access
- common issues
- DMA docs

Suggested reading order learned:

- `Pre-Setup Guide`
- `Injection Guide`
- `Accessing Your Key`
- `Common Issues`
- `DMA Hardware Docs`

### 7.6 Support Tool

`https://ducks-services.gitbook.io/pre-setup-support-tool`

Use for:

- basic troubleshooting
- loading issues
- connection issues
- download issues

## 8. The Support Tool Workflow

This is one of the biggest lessons.

For many basic issues:

1. tell customer to use `.tool` or the support tool link
2. ask them to fix anything green so it shows red
3. tell them to press `SEND TO SUPPORT`
4. ask for the `reference code` / `session code`
5. search the code in Discord with `CTRL + F`
6. inspect the embed

Big things the team said to check:

- `Real-Time Protection`
- `Vanguard Anti-Cheat`
- `FaceIT Anti-Cheat`

Also useful to review:

- `Firmware Virtualization`
- `Secure Boot`
- `UAC Status`

Expected safe-state pattern from example embeds:

- Real-Time Protection = disabled
- Vanguard = not detected
- FaceIT = not detected
- Virtualization = disabled
- Secure Boot = disabled
- UAC = disabled

Important internal wording:

`If anything is green, fix it so it shows red`

## 9. Most Common 1PC Issue Patterns

### 9.1 Loader Won’t Open

Most likely causes:

- antivirus/Defender blocked or removed loader files
- file blocked by Windows
- files not extracted properly

Best standard response pattern:

- disable Defender/AV
- check quarantined items
- re-download to fresh folder
- extract fully
- right-click Properties -> Unblock if present
- run as administrator

### 9.2 Missing Files / Missing Components

Known internal fix:

- install `Microsoft DirectX`
- install `all VCRedist`
- restart system

This came from internal copypasta and teammate guidance.

### 9.3 Missing DLLs

Internal note learned:

- sometimes `leechcore.dll` and `vmm.dll` need to be placed in the same folder as the loader
- versions matter
- some cheats use different leechcore versions
- `leechcore` and `vmm` should match the cheat library

### 9.4 Key / Access Problems

Best support habits:

- confirm correct account
- confirm order
- check key in admin search
- ask for screenshot of `My Keys` page if needed

### 9.5 Broken Download Link

Best support habit:

- do not guess a replacement link
- confirm the source first
- tell customer you are checking before they try anything else

## 10. DMA Overview

DMA is where support becomes more technical and more careful.

### 10.1 Main DMA Terms

`35t / 75t / 100t`

DMA card tiers/models.

`Firmware`

Critical part of the DMA setup. Determines anti-cheat compatibility/support.

`Second PC / Mini PC`

Separate system used in DMA setup.

`Fuser`

Display-related hardware. Important for certain resolution/refresh setups.

`Makcu / KMBox`

Input/aiming-related devices in DMA ecosystem.

### 10.2 DMA Card / Driver Commands

Known Discord commands:

- `.dmainstall`
- `.jtag`
- `.ftdi`
- `.speedtest`
- `.dmatroubleshooting`
- `.dnaid`
- `.35tflash`
- `.75tflash`
- `.100tflash`
- `.makcuflashing`
- `.makcucables`
- `.makcudriver`
- `.fuser`
- `.fusersetup`
- `.dmaquiz`

These match the docs and are useful fast references.

## 11. DMA Ticket Handling Pattern

For DMA tickets, usually ask for:

- hardware model
- game
- firmware
- license key
- motherboard if relevant
- DNA ID if firmware-related
- screenshot/error

Internal firmware prep info request learned:

- DMA DNA ID
- motherboard model
- firmware order number

### 11.1 Do Not Guess On

- exact firmware compatibility not confirmed in docs/team
- advanced BIOS guidance unless clearly documented
- unique/private firmware availability/pricing
- whether something is safe/undetected in strong absolute terms
- whether a main account is 100% safe

## 12. DMA Page / Bundle / Firmware Knowledge

### 12.1 Firmware Options Seen

From DMA page information shared:

- `1:1 Emulated - BE / COD / BF / FiveM` — from `$49.99`
- `1:1 Emulated - ACE / EAC / BE / COD` — from `$149.99`
- `1:1 Emulated - VGK / ACE / EAC / BE` — from `$224.99`

Important known info from product text:

- firmware helps prevent device being identified as a DMA device
- emulated firmware is backed by a driver
- no yellow exclamation mark in Device Manager
- `BE / COD / BF / FiveM` firmware included a `3 month warranty`
- delivery for firmware may take up to `24 hours`

Important distinction:

- warranty is not always the same thing as usage duration

### 12.2 Firmware Recommendation Logic

If customer already has equipment and only needs firmware:

- ask what DMA card they have
- ask what games they play
- if `.dmaquiz` is used, rely on the recommendation wording

Example from chat:

- customer wanted firmware for `R6`, `COD`, and `FN`
- `.dmaquiz` result recommended `ACE / EAC / BE / COD / BF / FiveM Firmware`
- price associated in recommendation context was `$149.99`

### 12.3 Cheapest Firmware Question

Known safe answer:

- cheapest listed firmware currently is `1:1 Emulated - BE / COD / BF / FiveM` at `$49.99`

### 12.4 Bundle Customization

Text learned from DMA page:

- bundles are customizable
- firmware choice can be selected

So safe answer:

- yes, bundles are customizable for firmware choice

## 13. Mini PC / Hardware Recommendation Notes

Observed mini PC options:

- `Budget Mini PC`
- `Premium Mini PC`

Important distinction:

- `T100 / 100t` is the DMA card tier, not the PC

When asked what mini PC or bundle to get:

- best default answer is to use `.dmaquiz`
- if customer gives games/budget/refresh rate, you can help explain result

Example learned:

- Warzone / weekend use / low spend = budget-friendly direction + mini PC can make sense
- but safest sales-support path is still `.dmaquiz`

## 14. Fuser / Display Knowledge

Important learned case:

- `MSI MAG 342CQR E2` monitor
- `3440x1440`
- DisplayPort needed for full resolution/high refresh
- `DC500` was the better fit vs normal HDMI fuser for that kind of setup

General lesson:

- if customer is asking whether a fuser supports their monitor, check exact monitor model and specs first

## 15. Shipping / Delivery Knowledge

From DMA shipping information:

- DMA hardware ships from the United States
- orders usually ship within `0–1 business days`
- U.S. delivery: `2–4 business days`
- international: around `5–7 business days`

For older search results there were also Europe estimates, but safest internal memory from your later info:

- use `0–1 business days shipping`
- `5–7 business days international`

## 16. Installation Service Workflow

If customer bought installation service:

1. acknowledge purchase
2. ask for order number
3. ask what product needs help
4. ask whether they are available now
5. check who is available
6. do not promise live install yourself unless confirmed

If guiding step by step:

- do one step at a time
- ask customer to confirm after each step
- ask for screenshots when unclear
- stop and escalate if you become unsure

## 17. Internal Copypasta / Memory Notes

### 17.1 Ticket Closure / Follow-Up

Examples learned:

- checking in if anything else is needed
- saying ticket will be closed soon
- inviting customer to let support know before closure if they still need help

### 17.2 Scam / Payment Reminder

Important internal safety reminder:

- staff will never DM asking for payment details
- payments and inquiries should go through official website or official tickets

### 17.3 Review Templates

Internal review asks referenced:

- Trustpilot
- Discord reviews
- Elitepvpers

Important rule from Sawyer:

- only ask after issue is fully resolved
- do not be pushy

### 17.4 XIM / Makcu Memory

Important flow:

- XIM setup should work by itself first
- mouse should move crosshair correctly
- shooting should work
- if customer needs XIM config help, XIM forums/community are appropriate
- once XIM is working, then proceed with Makcu connection/setup

### 17.5 Windows Update / Direct DMA Warning

Important internal notes from BMP:

- do not update Windows on gaming PC when everything works
- certain Windows builds were not supported
- uninstall unsupported KBs if needed

Specific versions/KBs learned:

- `26100.3323` not supported (`KB5052093`)
- `26100.3476` not supported (`KB5053598`)
- supported mention: `26100.3194` (`KB5051987`)

### 17.6 Hyper-V Instructions

There is internal copypasta for enabling Hyper-V through Control Panel if needed.

### 17.7 WinRAR

Known simple fix:

- if extraction issues occur, direct customer to install WinRAR

### 17.8 Serial Checker / Spoofer Note

Known internal guidance:

- run tool as admin before using spoofer
- take screenshot of serial numbers first
- compare after spoofing to verify changes

## 18. How To Read Any Ticket

Use this checklist every time:

1. Is this `1PC`, `DMA`, `spoofer`, `installation service`, or `sales/pre-sale`?
2. What exact step failed?
3. What information is missing?
4. Is the answer clearly in the docs/support tool/internal notes?
5. If yes, guide them.
6. If no, escalate.

This is the core support habit.

## 19. Good Questions To Ask

### 19.1 For 1PC

- what exact product did you buy?
- what exactly happens?
- screenshot of error?
- did you redeem the key?
- are you on the correct account?
- did you extract the files?
- did antivirus block anything?
- support tool reference code?

### 19.2 For DMA

- hardware model?
- 35t/75t/100t?
- motherboard?
- firmware?
- game?
- DNA ID?
- order number?
- license key?
- exact symptom?

## 20. Ticket Types You Saw Often

Repeated patterns from the chat:

- broken loader links
- loader won’t open
- missing driver / missing files
- missing components
- support tool confusion
- firmware pricing and duration questions
- DMA bundle / mini PC / payment questions
- HDMI cables missing from bundle
- setup confusion after receiving hardware
- feature mismatch questions
- status questions

## 21. Cases Where You Should Be Extra Careful

Do not freestyle answers for:

- “will this keep me safe/undetected?”
- “can I use my main account safely after cheating?”
- “is this 100% safe?”
- “is FaceIt supported?”
- exact controller/KMBox/Makcu routing if not documented
- unique/private firmware pricing if not confirmed
- direct developer-side bug claims

Best pattern:

- acknowledge
- say you want to confirm first
- ask the team

## 22. Team Communication Style

Good internal message pattern:

- summarize customer issue
- include product/hardware details
- mention what you already checked
- mention your best guess without sounding absolute
- ask for confirmation

Example pattern:

Customer says X. I checked Y. It looks more like Z than A/B. Could someone confirm the best next step before I reply further?

This looks responsible and saves the team time.

## 23. Communication With Sawyer

Good things to update him on:

- starting/clocking in
- ticket progress
- first closed tickets
- possible deals
- learning progress
- trial-period clarification questions

Good style:

- respectful
- appreciative
- not pushy
- focused on learning and reliability

## 24. Trial / Work Mindset

Strong lessons from the chat:

- you do not need to act like an expert
- you do need to be active, accurate, and coachable
- handling simple tickets well matters a lot
- accurate escalation matters a lot
- being dependable makes the team trust you

The right goal:

- reduce uncertainty over time
- answer more tickets confidently without misinformation
- make support lighter for Sawyer/team over time

## 25. Privacy / Safety Notes Learned

From your own reflections:

- Discord roles do not normally reveal everyone’s IP addresses
- website/backend/support tools can show public IPs
- public IP is not the same thing as exact home address
- if privacy matters, using a VPN before logging into work systems can reduce exposure of your public IP

This was not a company policy note, but a personal understanding note from the chat.

## 26. Ready-To-Use Short Templates

### 26.1 Need More Info

Hi, thanks for reaching out. Could you please send a screenshot of the error and confirm the exact product/setup you’re using so I can check it properly?

### 26.2 Broken Link

Hi, thanks for reaching out. I’m checking this for you now. Since you mentioned the link appears to be broken, I want to confirm the correct source first before having you try anything else.

### 26.3 Loader Won’t Open

Hi, thanks for reaching out. The most common cause of this is that Defender/antivirus blocked or removed part of the loader, or Windows is blocking the file after download. Please re-download to a fresh folder, extract fully, check Properties > Unblock if it appears, disable Defender/AV, and run as administrator.

### 26.4 DMA Clarification

Hi, thanks for reaching out. I’d like to confirm that properly first so I don’t give you the wrong information. Please send your hardware model, firmware, game, and license key so I can check it accurately.

### 26.5 Installation Service

Hi, thanks for reaching out. I can see that you purchased the Installation Service. Please send your order number, the product you need help with, and whether you’re available now so we can check the next step for you.

### 26.6 Close Ticket

Hi, do you have any other questions or concerns? If not, I’ll go ahead and close the ticket now.

## 27. Source / Reference List

Main website:

- `https://ducks-services.com/`

Store:

- `https://ducks-services.com/store/`

DMA page:

- `https://ducks-services.com/dma/`

Admin:

- `https://ducks-services.com/admin`

Main docs:

- `https://docs.ducks-services.com/`

Support tool:

- `https://ducks-services.gitbook.io/pre-setup-support-tool`

Trustpilot:

- `https://www.trustpilot.com/evaluate/www.ducks-services.com`

Discord invite mentioned:

- `discord.gg/ducknrun`

Amazon/mini PC references seen during training:

- `https://www.amazon.com/dp/B0C2P486GQ?social_share=cm_sw_r_cp_ud_dp_PZH49DHHDG2S959N7SBJ&th=1&linkCode=sl1&tag=ducksservices-20&linkId=42165f768bc5377afe74b97f3e894762&language=en_US&ref_=as_li_ss_tl`
- `https://www.amazon.com/Beelink-Lake-N100-Computer-Support-Family-NAS/dp/B0BVFKN7ZL?crid=RB0KJPX6FSQ5&dib=eyJ2IjoiMSJ9.ryiyxSLE-GfEApkKPFbVBkgu7e_ZVOvHDhEYShoHzDAK1cYi-UbRe5JmVs7pqXoNWY2yIQYLNuBfFQcCy-zwXTSai4BSXp84QhLX_eOj4nZxAkUHCWJ0ima8mSeO5z6Chcxl4Bzh46749Bu9BIyLtydvxzfo8ZpVR-HAvV6yWm1LYUfUcNXukCeX86kTQZn8UOdqKmxHoMZEQnPdaagJAS5MVHfZLYWmvv10Drjug8fyfOFA81UzHvudjSmr3c113QsSEmUa2UkoJLOshAYkAyDCk1BCGFvTp-X0o5JnvFoyxBs9hYxCyIX_rwjA3G2ngHw-ZRnK-c-LDZxrMs9EfzY5pPvMDBCQHOZWT4ZWrv4.v82C4bw_CG2y383U2m5WP-gAR3Xyf7SpLRyUbXYa5tA&dib_tag=se&keywords=Beelink%2BMini%2BPC&qid=1735457174&s=electronics&sprefix=beelink%2Bmini%2Bpc,electronics,93&sr=1-1&th=1&linkCode=sl1&tag=ducksservices-20&linkId=5bda8727a8f7adeff88f8260b810f399&language=en_US&ref_=as_li_ss_tl`

Useful Discord command references:

- `.tool`
- `.dma`
- `.dmaquiz`
- `.dmainstall`
- `.jtag`
- `.ftdi`
- `.speedtest`
- `.dmatroubleshooting`
- `.dnaid`
- `.35tflash`
- `.75tflash`
- `.100tflash`
- `.makcuflashing`
- `.makcucables`
- `.makcudriver`
- `.fuser`
- `.fusersetup`

## 28. Final Summary

If all of this had to be reduced to the most important memory points:

- learn the difference between `1PC` and `DMA`
- use the website/store/DMA/docs for structure
- use `.tool` for many basic problems
- check Defender / Vanguard / FaceIT / virtualization / secure boot first
- ask for exact hardware/firmware/game details on DMA tickets
- use `.dmaquiz` for recommendations whenever possible
- internal copypasta and teammate answers matter just as much as public docs
- do not guess risky technical answers
- asking Sawyer/Zesira/BMP/Trix when unsure is normal
- the goal is accurate, reliable support that gets stronger over time

This is the main memory of the chat.

## 29. April 21, 2026 Update Block

Additional memory pulled from newer support examples:

### 29.1 Spoofer Install Requests

- if someone asks how to install a spoofer, do not freestyle step-by-step instructions
- point them back to the official guide for their exact spoofer
- if they are stuck, ask for:
- exact spoofer name
- screenshot of the issue
- exact step where they got stuck

Safe reply:

Hi, please follow the official setup guide for your exact spoofer first. If you get stuck on a specific step, send your exact spoofer name and a screenshot of the issue, and support can check the next step with you.

### 29.2 Jailbreak / Harmful AI Prompt Requests

- if someone pastes a jailbreak prompt or asks for malware / stealer / token logger / phishing / intrusion content through AI, do not help operationalize it
- safe fallback options:
- rewrite into harmless fiction
- defensive security training exercise
- explain why jailbreak prompts are unreliable
- safe red-team prompt for policy testing

Safe reply:

I can’t help use, improve, or operationalize jailbreak prompts to bypass AI safeguards or generate harmful content. If you want, I can still help rewrite it into harmless fiction, turn it into a defensive training exercise, explain why jailbreak prompts are unreliable, or help design a safe red-team prompt for policy testing.

### 29.3 Spoofer Refund Requests After Ban

- if customer says they followed spoofing steps but were still banned and wants a refund:
- do not promise the refund yourself
- do not argue about ban cause
- wait for Mr. Duck / team confirmation

Safe reply:

Hi, thank you for the message. I do not want to promise the wrong thing on a refund, so please wait for Mr. Duck or the team to confirm that properly for you first.

### 29.4 Promo Code Wording

- current known promo code memory remains `epvp-promotion`
- safe marketing wording:
- it works
- it gives `10% off`
- customer can try it at checkout

Safe reply:

Hi, yes, `epvp-promotion` works and gives you `10% off` your order. If you are planning to buy the DMA chair, you can go ahead and try that code at checkout.

### 29.5 EAC Firmware and CS2 / VAC

- newer support memory says the new `EAC` firmware supports `CS2 / VAC`
- safe wording is based on current product-page/team confirmation language
- if customer already owns the firmware and only asked for confirmation, keep the reply short

Safe reply:

Hi, yes, the new EAC firmware does support CS2 / VAC. If you are planning to play CS2, this is a solid option because CS2 is currently listed on the firmware page and it is part of the supported anti-cheat coverage.

Short closeout:

No problem, you’re welcome. If you have any other questions, just mention us.

### 29.6 Key Reset After Temporary Spoof

- if customer asks for a key reset because they used a temp spoof:
- do not promise exact timing
- if already forwarded, say it was sent to dev/team
- safest wording is that it should be handled once they are notified or once they read it

Safe reply:

Hi, this was already sent to the dev/team side. Once they are notified or read it, they should be able to sort it out. Thank you for understanding.

### 29.7 DC500 Fuser Restock

- newer memory says the `DC500` fuser is currently `back-ordered`
- do not promise a restock date unless the team confirms it

Safe reply:

Hi, the DC500 fuser is currently back-ordered. I would rather have the team confirm any restock timing properly before I promise that.

### 29.8 AI Usage-Limit Message Handling

- if an AI helper hits a usage limit and shows an obviously wrong retry date/time:
- do not paste that broken message to the customer as support
- switch to a manual human reply instead
- if needed, acknowledge the delay without quoting the broken system message

### 29.9 USB Removal / Ban Screenshot Case

- if a customer asks whether having the cheat/spoofer on a `USB stick` and removing the USB before launching the game made it safe, do not say yes
- if they later show a ban screen, do not guess that the ban was or was not caused by that
- do not argue with the customer about the ban reason
- do not promise a refund without team confirmation
- safest handling:
- acknowledge the screenshot
- avoid causal claims
- point them to the game's own ban/review or appeal process
- if they ask for compensation/refund, wait for `Mr. Duck` / team confirmation first

Safe reply:

Hi, thank you for the screenshot. I do not want to guess on the exact cause of the ban and give you the wrong answer. For the ban itself, please follow the game's review or appeal process shown there. If you want to ask about refund handling, I would rather have Mr. Duck or the team confirm that properly first.

### 29.10 AMD Libraries / CNext DLL Fix

- if the customer already installed the latest libraries and the issue still happens, and they have an `AMD` graphics card, there is a known AMD-specific fix flow
- end AMD-related processes in `Task Manager`
- examples mentioned in team memory:
- `AMD Radeon`
- `AMDSrv`
- `AMDOW`
- `CPUMetrics`
- and other AMD-related processes if present
- then go to the AMD software folder:
- `C:\Program Files\AMD\CNext\CNext`
- download and extract the provided `Libs` package
- copy and replace the `DLL` files into that folder
- use this carefully as a known fix path and do not freestyle missing DLL names if they were not provided by the team or ticket context

Safe reply:

Please install the latest library package first. If that still does not fix it and you have an AMD graphics card, please close all AMD-related processes in Task Manager, then go to `C:\Program Files\AMD\CNext\CNext`, and replace the DLL files there with the files from the provided `Libs` archive.

### 29.11 Exact DMA Service / Firmware Links

- exact `DMA Installation Service` product link:
- `https://ducks-services.com/store/product/1396-dma-installation-service/`
- exact lower-tier `BE / COD / BF / FiveM` firmware product link:
- `https://ducks-services.com/store/product/521-11-emulated-be-cod-bf-fivem/`
- for `Siege`-only sales questions, the saved exact product is:
- `1:1 Emulated - BE / COD / BF / FiveM`
- use the exact product link above when the customer asks for the direct link
- for `Apex` on the `$150` firmware, support-safe website wording is:
- `1:1 Emulated - ACE / EAC / BE / COD`
- product link:
- `https://ducks-services.com/store/product/662-11-emulated-ace-eac-be-cod/`

### 29.12 Webpage Not Secure / VPN First

- if a customer says the loader or website shows a `webpage not secure` warning:
- first ask them to try a `VPN`
- if it still fails, ask for:
- the exact link they clicked
- a screenshot of the exact warning
- reason:
- this can be browser / ISP / network / certificate-path related, so do not guess deeper before seeing the exact warning

Safe reply:

Hi, please try using a VPN first and then open the link again. If it still shows the same warning, please send a screenshot of the exact message and the link you clicked so I can check it properly.

### 29.13 Budget R6 DMA Recommendation

- for a budget `Rainbow Six Siege` DMA setup, the saved direct owner recommendation is:
- `Duck's DMA - 75t Ultimate Bundle`
- `R6 Caruso [DMA]`
- saved mini PC used in that recommendation:
- `https://amzn.to/3DJQzkF`
- saved exact product links:
- bundle:
- `https://ducks-services.com/store/product/1135-ducks-dma-75t-ultimate-bundle/`
- cheat:
- `https://ducks-services.com/store/product/1557-r6-caruso-30-days-dma/`
- saved rough price summary from Mr. Duck:
- Duck's Services: about `$320 + $47 / month`
- Amazon Mini PC: about `$200 - $300`
- if the customer asks whether there are longer subs or whether `Caruso` is the best option:
- current saved owner wording is that `Caruso` is the best on the market
- it is their most popular `R6 DMA` by far
- do not promise alternative longer subscription lengths unless the store/team confirms them

Safe reply:

Hi, for a budget R6 DMA setup, the saved recommendation is the `Duck's DMA - 75t Ultimate Bundle` together with `R6 Caruso [DMA]`.

Bundle:
https://ducks-services.com/store/product/1135-ducks-dma-75t-ultimate-bundle/

Cheat:
https://ducks-services.com/store/product/1557-r6-caruso-30-days-dma/

Mini PC:
https://amzn.to/3DJQzkF

As a rough estimate, that setup was summarized as about `$320 + $47/month` from Duck's Services, plus around `$200-$300` for the mini PC.

### 29.14 DNA ID Not Needed Exception

- do not assume `DNA ID` is required for every firmware type
- saved specific exception from Mr. Duck:
- for a `75t` `BE emu firmware` case, the customer did not need to provide `DNA ID`
- safest handling:
- treat `DNA ID` requirements as firmware-dependent
- if the case appears to match a known `BE emu 75t` flow, do not force the customer to wait on `DNA ID`
- if not fully sure the firmware type matches, confirm with the team first

Safe reply:

Hi, for this firmware type we do not need the DNA ID, so you do not need to wait on that part. We can continue from here.

### 29.15 Firmware Blocked Speed Test Check

- confirmed support flow from Mr. Duck when checking if firmware is blocked:
- close all games and cheats completely
- open DMA tool and run a speed test on desktop
- if speeds look normal, launch the game
- run the same speed test while in-game
- interpretation:
- speeds work on desktop and in-game = firmware is likely functional / not blocked
- speeds work on desktop but not in-game = firmware is likely being blocked
- no speeds at all = likely setup or connection issue
- ask customer to send results after testing

Safe reply:

Hi, please try the speed test flow first. Close all games and cheats, run a speed test on desktop, then launch the game and run the speed test again in-game.

If speeds work on both desktop and in-game, the firmware is likely not blocked. If speeds only work on desktop but not in-game, that points to the firmware being blocked. If there are no speeds at all, that points more to a setup or connection issue.

Please send the results after testing.

### 29.16 Arma Reforger / DControl Memory

- for an Arma Reforger pre-sale question involving modded servers / ReforgedZ style servers, Mr. Duck recommended `Malevolence`
- customer later bought `Malevolence`
- `DControl` unlock password from Mr. Duck:
- `sordum`
- do not guarantee every custom or modded server works unless the team confirms that exact server/mod setup

Safe reply:

Hi, for Arma Reforger, Mr. Duck recommended `Malevolence` for this case. I still would not want to guarantee every custom/modded server unless the team confirms that exact server setup, but that is the saved recommendation.

### 29.17 $50 FW / Virtualization Memory

- customer asked if the `$50 FW` works with virtualization on
- Mr. Duck confirmed:
- yes
- saved support-safe answer:
- for the `$50 FW`, virtualization on was confirmed as okay by Mr. Duck
- caveat:
- do not generalize this to every DMA/firmware issue
- virtualization is still a common setting to check during DMA troubleshooting unless the exact product/team confirmation says otherwise

Safe reply:

Hi, yes, Mr. Duck confirmed the `$50 FW` works with virtualization on.

### 29.18 COD DMA Bundle / Installation Memory

- customer asked if the `$319` DMA bundle includes firmware preinstalled
- BMP confirmed:
- firmware does not come preinstalled
- if customer pays the `$20` installation fee, team can handle setup/flashing
- DMA works great on COD / BO7 / Warzone
- BMP said many top 100 league players use DMA and he plays COD strictly with DMA
- customer asked which bundle is offered
- Mr. Duck said the most popular COD bundle is:
- `Duck's DMA - 75t Ultimate Bundle`
- link:
- `https://ducks-services.com/store/product/1135-ducks-dma-75t-ultimate-bundle/`
- do not promise preinstalled firmware unless team specifically says it for that order

Safe reply:

Hi, firmware does not come preinstalled with the DMA bundle. If you want us to handle the setup/flashing for you, you can purchase the `$20` DMA Installation Service.

For COD / BO7 / Warzone, the most popular bundle Mr. Duck recommended is the `Duck's DMA - 75t Ultimate Bundle`:
https://ducks-services.com/store/product/1135-ducks-dma-75t-ultimate-bundle/
