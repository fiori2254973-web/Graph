# PVX-(107-241) Series Smart String ESS - Alarm Manual

Source PDF: `PVX-(107-241) Series Alarm Manual REV_A 2026.05.14.pdf`  
PDF pages: 193  
Source revision/date visible in filename: `REV_A 2026.05.14`

## Conversion notes

- Text was extracted from the PDF with `pypdf`.
- The PDF is text-based, not a scan; page 2 contains no useful extracted text.
- Alarm tables were preserved as readable line-oriented Markdown because the PDF text layer does not expose reliable table structure.
- Symbols were normalized where useful for Markdown portability, for example bullets and comparison signs.
- PDF page separators are preserved to make verification against the source document easier.

---

## PDF page 1

PVX-(107-241) Series Smart String ESS

Alarm Manual

---

## PDF page 2

_No extractable text on this page._

---

## PDF page 3

## About this document
### Purpose
This document describes how to handle all alarms of the following products:
- PVX-241
- PVX-215
- PVX-215-HV
- PVX-107-HV
### Intended Audience
The document is intended for:
- Technical support engineers
- Installation engineers
- Commissioning engineers
- Maintenance engineers
### Change History
Changes between document issues are cumulative. The latest document issue contains all the changes
made in earlier issues.
### Issue 01 (2026-05-14)
This issue is the first official release.

---

## PDF page 4

## Contents
About This Document 1
Contents 2
Description of Alarm Reference 7
Alarm Reference 8
1.1 Battery Pack (PACK) 8
### 1.1.1 3100 Battery Pack and External Power Connected Abnormally 8
### 1.1.2 3101 Battery Pack Lifespan Reached 9
### 1.1.3 3102 Battery Pack Overvoltage 10
### 1.1.4 3103 Battery Pack Undervoltage 11
### 1.1.5 3104 Battery Overcurrent Protection 13
### 1.1.6 3105 Battery Pack Overtemperature 14
### 1.1.7 3106 Battery Pack Undertemperature 15
### 1.1.8 3107 Battery Pack Locked 16
### 1.1.9 3108 Battery Faulty 19
### 1.1.10 3109 Battery Pack SOH Low 20
### 1.1.11 3112 Power Connection Sampling of Battery Pack Abnormal 21
### 1.1.12 3113 Battery Pack Configuration Data Abnormal 22
### 1.1.13 3114 Battery Pack and System Specifications Mismatched 23
### 1.1.14 3115 Cell Temperature Rises Abnormally 24
### 1.1.15 3116 PACK Thermal Runaway 25
### 1.1.16 3117 Battery Pack Charging Failed 26
1.2 Battery Pack (Balancing Module) 27
### 1.2.1 3161 Balancing Module Overcurrent Protection 27
### 1.2.2 3162 Balancing Module Internal Error 29
### 1.2.3 3163 Balancing Module Bus Voltage Abnormal 32
### 1.2.4 3164 Balancing Module Battery Voltage Abnormal 33
### 1.2.5 3165 Overtemperature Protection Inside Balancing Module 34
### 1.2.6 3166 MCU Overtemperature Protection on the Battery Side of the Balancing
Module 35
### 1.2.7 3167 Overtemperature Protection for the Wiring Terminal of the Balancing
Module 36
### 1.2.8 3169 Balancing Module Bus Soft-Start Failed 37
### 1.2.9 3170 Balancing Module Version Mismatch 37
### 1.2.10 3171 Balancing Module Address Pairing Timeout 38
### 1.2.11 3172 Balancing Module Soft-Start Circuit Abnormal 38
### 1.2.12 3173 Balancing Module Abnormal 39
### 1.2.13 3174 Balancing Module Overcurrent Fault 42
1.3 RCM (BCU) 43
### 1.3.1 3222 BMU Internal Short Circuit 43

---

## PDF page 5

### 1.3.2 3223 BMU Sampling Cable Disconnected 44
### 1.3.3 3224 BMU Faulty 46
### 1.3.4 3226 Disconnection Between BMUs 48
### 1.3.5 3229 BMU Communication Failure 48
### 1.3.6 3351 Inconsistent BCU Software Versions 49
### 1.3.7 3352 Abnormal Total Voltage of Battery Rack 49
### 1.3.8 3353 Total Voltage of Battery Rack and Total Cell Voltage Inconsistent 50
### 1.3.9 3354 Battery Pack Mixed Use Failed 50
### 1.3.10 3355 BCU Chip Overtemperature 51
### 1.3.11 3356 BCU Internal Exception 52
### 1.3.12 3357 Balancing Module Software Versions Inconsistent 53
### 1.3.13 3358 BCU Auxiliary Power Abnormal 54
### 1.3.14 3359 BCU Memory Abnormal 56
### 1.3.15 3360 RPCB Communication Failure 56
### 1.3.16 3361 DCDC Communication Failure 57
### 1.3.17 3362 PCS Communication Failure 57
### 1.3.18 3363 Balancing Module Communication Failure 58
### 1.3.19 3369 ESS SOH Calibration 59
### 1.3.20 3371 Battery Rack Voltage Exceeding Threshold 60
### 1.3.21 3373 Battery Pack Sampling Abnormal 62
### 1.3.22 3375 Battery Voltage Inconsistent 63
### 1.3.23 3376 Battery Temperature Inconsistent 65
## 1.4 RCM (RPCB) 66
### 1.4.1 3300 RPCB Voltage Abnormal 66
### 1.4.2 3301 RPCB Port Short-Circuited 67
### 1.4.3 3302 Internal RPCB Temperature Abnormal 68
### 1.4.4 3303 RPCB Overcurrent Fault 70
### 1.4.5 3304 Battery-Side ISO Insulation Detection Abnormal 71
### 1.4.6 3305 RPCB Power Loop Abnormal 72
### 1.4.7 3306 RPCB Version Mismatch 73
### 1.4.8 3307 RPCB Abnormal 74
### 1.4.9 3308 Battery RCD Protection Triggered 77
### 1.4.10 3309 RPCB Overcurrent Protection Triggered 78
### 1.4.11 3310 RPCB Fan Alarm 79
### 1.4.12 3311 RPCB SPD Faulty 79
### 1.4.13 3312 Battery-Side ISO Insulation Detection Alarm 80
### 1.4.14 3313 Auxiliary Power Abnormal 81
### 1.4.15 3314 RPCB Overcurrent Alarm 82
## 1.5 Power System (DCDC) 83
### 1.5.1 3400 DCDC Protection 83
### 1.5.2 3401 DCDC Faulty 85
### 1.5.3 3402 Overvoltage Protection for DCDC Bus Port 87
### 1.5.4 3403 DCDC Overhumidity Protection 87
### 1.5.5 3404 DCDC Overtemperature Protection 88

---

## PDF page 6

### 1.5.6 3405 DCDC Undertemperature Protection 90
### 1.5.7 3406 Overtemperature Protection for DCDC Bus Terminal 90
### 1.5.8 3407 Overtemperature Protection for DCDC Battery Terminal 91
### 1.5.9 3408 DCDC Liquid Cooling Abnormal 92
### 1.5.10 3409 DCDC Versions Mismatched 92
### 1.5.11 3410 DCDC NTC Faulty 93
### 1.5.12 3411 DCDC DSP_EPO Faulty 93
### 1.5.13 3412 DCDC Bus Port Undervoltage 94
### 1.5.14 3413 DCDC Bus Overvoltage 94
## 1.6 Power System (PCS) 95
### 1.6.1 3500 PCS DC Overvoltage 95
### 1.6.2 3501 PCS DC Bus in Reverse Polarity 95
### 1.6.3 3503 PCS Grid Phase Wire Short-Circuited to PE 96
### 1.6.4 3504 PCS Grid Failed 96
### 1.6.5 3505 PCS Grid Undervoltage 97
### 1.6.6 3506 PCS Grid Overvoltage 98
### 1.6.7 3507 PCS Grid Voltage Imbalanced 99
### 1.6.8 3508 PCS Grid Overfrequency 100
### 1.6.9 3509 PCS Grid Underfrequency 101
### 1.6.10 3510 PCS Grid Frequency Unstable 101
### 1.6.11 3511 PCS AC Overcurrent 102
### 1.6.12 3512 PCS DC Component Overhigh 102
### 1.6.13 3513 Reverse Phase Sequence on PCS AC Side 103
### 1.6.14 3514 PCS Residual Current Abnormal 103
### 1.6.15 3515 PCS Grounding Abnormal 104
### 1.6.16 3516 Low PCS Insulation Resistance 105
### 1.6.17 3517 PCS Temperature High 105
### 1.6.18 3518 PCS Abnormal 106
### 1.6.19 3519 PCS Update Failed or Versions Mismatched 108
### 1.6.20 3520 PCS Internal Fan Abnormal 109
3521 PCS AC Terminal Temperature Abnormal 110
### 1.6.21 3522 PCS DC Terminal Temperature Abnormal 111
### 1.6.22 3523 PCS Black Start Failed 112
### 1.6.23 3524 Incorrect Black Start Instruction Sequence of PCS 113
### 1.6.24 3525 PCS Fuse Broken 113
### 1.6.25 3526 PCS Fuse Self-Check Abnormal 114
### 1.6.26 3527 PCS FAST I/O Self-Test Abnormal 114
### 1.6.27 3528 PCS DC Bus Short-Circuited 115
### 1.6.28 3529 PCS Relay Overtemperature 115
### 1.6.29 3530 PCS AC Resonance 116
### 1.6.30 3531 PCS Derated 117
### 1.6.31 3532 PCS Startup Abnormal 118
## 1.7 Temperature Control System 119
### 1.7.1 3600 Power loss alarm 119

---

## PDF page 7

### 1.7.2 3601 Power voltage abnormal 120
### 1.7.3 3602 Power frequency abnormal 121
### 1.7.4 3603 Outdoor temperature sensor fault 122
### 1.7.5 3604 Outdoor low temperature alarm 122
### 1.7.6 3605 LTMS Communication Abnormal 123
### 1.7.7 3606 LTMS expiration alarm 124
### 1.7.8 3608 Certificate about to expire 124
### 1.7.9 3609 Certificate has expired 125
### 1.7.10 3620 Compressor discharge high pressure alarm 126
### 1.7.11 3621 Compressor suction low pressure alarm 127
### 1.7.12 3622 Compressor Low Superheat Degree 128
### 1.7.13 3623 Compressor discharge pressure sensor fault 129
### 1.7.14 3624 Condenser outlet pressure sensor fault 129
### 1.7.15 3625 Condenser outlet temperature sensor fault 130
### 1.7.16 3626 Compressor suction pressure sensor fault 131
### 1.7.17 3627 Compressor suction temperature sensor fault 131
### 1.7.18 3628 Dehumidifying temperature sensor fault 132
### 1.7.19 3640 Compressor drive alarm 132
### 1.7.20 3641 Compressor drive output abnormal 133
### 1.7.21 3642 Compressor Overcurrent Alarm 134
### 1.7.22 3643 Compressor drive communication abnormal 135
### 1.7.23 3644 High discharge temperature alarm 136
### 1.7.24 3645 Compressor discharge temperature sensor fault 137
### 1.7.25 3646 Insufficient Refrigerant 137
### 1.7.26 3650 Insufficient Cooling Capacity 138
### 1.7.27 3651 LCC Output Overcurrent 139
### 1.7.28 3652 Inconsistent Software Version of Drive and Auxiliary Power Module 140
### 1.7.29 3653 Inconsistent LCC Software Version 140
### 1.7.30 3655 Auxiliary power abnormal 141
### 1.7.31 3660 Outdoor cooling module blocked 141
### 1.7.32 3661 Outdoor heat exchanger temperature sensor fault 142
### 1.7.33 3665 Fan fault 142
### 1.7.34 3666 Fan fault 144
### 1.7.35 3675 Electric heater fault 145
### 1.7.36 3676 Electric heater power overvoltage alarm 146
### 1.7.37 3680 Power-side supply water temperature sensor fault 146
### 1.7.38 3681 Power-side return water temperature sensor fault 147
### 1.7.39 3682 Power-side supply/return water temperature sensor abnormal 148
### 1.7.40 3683 Battery-side supply water temperature sensor fault 149
### 1.7.41 3684 Battery-side return water temperature sensor fault 149
### 1.7.42 3685 Battery-side supply/return water temperature sensor abnormal 150
### 1.7.43 3686 Battery-side supply water high temperature alarm 151
### 1.7.44 3687 Battery-side supply water low temperature alarm 152
### 1.7.45 3688 Coolant expiration alarm 153

---

## PDF page 8

### 1.7.46 3689 Shutdown due to coolant expiration 154
### 1.7.47 3690 Coolant replacement not completed 154
### 1.7.48 3705 Water pump power supply abnormal 155
### 1.7.49 3706 Water pump function abnormal 156
### 1.7.50 3707 Water pump fault 157
### 1.7.51 3715 Multi-way valve communication abnormal 158
### 1.7.52 3716 Multi-way valve power supply abnormal 159
### 1.7.53 3717 The multi-way valve is faulty 160
### 1.7.54 3725 Water tank low liquid level alarm 161
## 1.8 ESU 162
### 1.8.1 3380 RPCB Software Versions Inconsistent 162
### 1.8.2 3381 Inconsistent DCDC Software Versions 163
### 1.8.3 3382 Inconsistent PCS Software Versions 163
### 1.8.4 3384 AC Startup Conditions Not Met 164
### 1.8.5 3880 AC SPD Faulty 165
### 1.8.6 3881 Door Status Alarm 165
### 1.8.7 3882 ESS Door Open 166
### 1.8.8 3883 Water Alarm 166
### 1.8.9 3884 Smoke Detector Alarm 167
### 1.8.10 3885 High Concentration of Combustible Gas 168
### 1.8.11 3886 Combustible Gas Detector Communication Failed 170
### 1.8.12 3887 Combustible Gas Detector Faulty 170
### 1.8.13 3888 Temperature and Humidity Sensor Communication Failed 171
### 1.8.14 3889 Temperature and Humidity Sensor Faulty 171
### 1.8.15 3890 Heat Detector Alarm 172
### 1.8.16 3891 High Ambient Temperature Inside ESS Cabin 173
### 1.8.17 3892 EPO Alarm 174
### 1.8.18 3893 Fire Alarm 175
### 1.8.19 3894 Exhaust Fan Faulty 176
### 1.8.20 3895 Devices Connected and System Configuration Inconsistent 177
### 1.8.21 3900 High Relative Humidity Inside ESS Cabin 180
### 1.8.22 3901 Offering Software Update Package Not Backed Up 180
### 1.8.23 3902 Inconsistent Display Module Software Versions 181
### 1.8.24 3903 E-label Board Data Abnormal 182
### 1.8.25 3904 Certificate About to Expire 183
### 1.8.26 3905 Certificate Expired 184
### 1.8.27 3906 Communication with Upper-layer Controller Abnormal 185
### 1.8.28 3908 Component End of Life 186
### 1.8.29 3910 Auxiliary Power Meter Communication Abnormal 187
### 1.8.30 3911 Display Module Communication Failure 187
### 1.8.31 3912 Startup Authorization Not Obtained 188
## Acronyms and abbreviations

---

## PDF page 9

## Description of alarm reference
Item Description
Alarm ID Indicates the ID of an alarm. Unique identifier of an alarm in one product.
Alarm Name Indicates the name of an alarm. In the same product, alarm names and alarm IDs
correspond to each other, which clearly and accurately reflect the meaning of
alarms.
Alarm Severity Alarm severities are defined as follows:
- Major: The device is faulty or the external environment is abnormal. As a
result, the output power decreases or the device stops feeding to the grid.
- Minor: Some components of the device are faulty but the device can still
connect to the grid and generate power.
- Warning: The device functions normally, but its output power decreases or
some authorization functions fail due to external factors.
Alarm Type Alarms are classified according to their contents. For example, the alarms of the
environment system include alarms related to temperature, humidity, and door
status.
Clearance Category - ADAC: After the fault is rectified, this alarm is automatically cleared.
- ADMC: This alarm needs to be manually cleared after the fault is rectified.
Impact on the System Impact on the system or services after an alarm is generated.
Possible Cause Indicates the possible cause of the alarm, including the cause ID and cause
description.
Suggestion Indicates the procedure for handling the alarm.

---

## PDF page 10

## Alarm reference
## 1.1 Battery Pack (PACK)
### 1.1.1 3100 Battery Pack and External Power Connected Abnormally
### Attribute
Alarm ID Alarm Name  Alarm Severity Alarm Type Clearance
Category
3100 Battery Pack and External Power
Connected Abnormally
Major Environmental
alarm
ADAC
### Impact on the System
The ESS cannot work properly.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The battery pack copper
bar experiences
overtemperature.
1.Check that the ESS is not charged and does not discharge.
Wait for 30 minutes and check whether the alarm is cleared.
2.If the alarm persists, power off the ESS by referring to the
user manual.
3.Wait for 5 minutes, wear protective equipment, take
protective measures, open the front panel of the battery pack,
and check whether the positive and negative copper bars are
loose. If they are loose, tighten the screws.
4.After checking that the screws are tightened, start the ESS
on the user interface.
5.If the alarm persists, export logs and contact technical
support.
2 1 The battery pack copper
bar experiences
overtemperature.
1.Check that the ESS is not charged and does not discharge.
Wait for 30 minutes and check whether the alarm is cleared.
2.If the alarm persists, power off the ESS by referring to the
user manual.
3.Wait for 5 minutes, wear protective equipment, take
protective measures, open the front panel of the battery pack,
and check whether the positive and negative copper bars are
loose. If they are loose, tighten the screws.
4.After checking that the screws are tightened, start the ESS
on the user interface.
5.If the alarm persists, export logs and contact technical
support.

---

## PDF page 11

### 1.1.2 3101 Battery Pack Lifespan Reached
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3101 Battery Pack Lifespan Reached Major Equipment
alarm
ADAC
### Impact on the System
The ESS cannot work properly.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The battery pack has
reached the end of its
lifespan.
1.Check whether an alarm indicating abnormal battery
sampling is generated. If yes, handle the alarm by referring to
the alarm handling suggestions.
2.If no, export logs and contact technical support.
3.If the battery pack has reached the end of its lifespan,
contact a local recycling agency to dispose of it in compliance
with local laws and regulations as well as applicable standards.

---

## PDF page 12

### 1.1.3 3102 Battery Pack Overvoltage
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3102 Battery Pack Overvoltage Major Equipment
alarm
ADAC
### Impact on the System
The ESS cannot work properly.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The voltage of the
battery pack or its
cells is too high.
1.Check that the ESS is not charged and check whether an alarm
indicating abnormal battery sampling is generated. If yes, handle
the alarm by referring to the alarm handling suggestions.
2.If no alarm indicating abnormal battery sampling is generated,
wait for 5 minutes and check whether the alarm is cleared.
3.If the alarm persists, export logs and contact technical support.
2 1 The voltage of the
battery pack or its
cells is too high.
1.Check that the ESS is not charged and check whether an alarm
indicating abnormal battery sampling is generated. If yes, handle
the alarm by referring to the alarm handling suggestions.
2.If no alarm indicating abnormal battery sampling is generated,
wait for 5 minutes and check whether the alarm is cleared.
3.If the alarm persists, export logs and contact technical support.
3 1 The voltage of the
battery pack or its
cells is too high.
1.Check that the ESS is not charged and check whether an alarm
indicating abnormal battery sampling is generated. If yes, handle
the alarm by referring to the alarm handling suggestions.
2.If no alarm indicating abnormal battery sampling is generated,
wait for 5 minutes and check whether the alarm is cleared.
3.If the alarm persists, export logs and contact technical support.
4 1 The voltage of the
battery pack or its
cells is too high.
1.Check that the ESS is not charged and check whether an alarm
indicating abnormal battery sampling is generated. If yes, handle
the alarm by referring to the alarm handling suggestions.
2.If no alarm indicating abnormal battery sampling is generated,
wait for 5 minutes and check whether the alarm is cleared.
3.If the alarm persists, export logs and contact technical support.
5 1 The voltage of the
battery pack or its
cells is too high.
1.Check that the ESS is not charged and check whether an alarm
indicating abnormal battery sampling is generated. If yes, handle
the alarm by referring to the alarm handling suggestions.
2.If no alarm indicating abnormal battery sampling is generated,
wait for 5 minutes and check whether the alarm is cleared.
3.If the alarm persists, export logs and contact technical support.

---

## PDF page 13

### 1.1.4 3103 Battery Pack Undervoltage
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3103 Battery Pack Undervoltage Major Equipment
alarm
ADAC
### Impact on the System
The ESS cannot work properly.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 1.The voltage of the
battery pack or its cells
is too low.
2.The battery pack has
been stored for
extended periods of time
when off-grid.
3.The battery pack has
been idle for a long time
after grid connection.
1.Check that the ESS does not discharge and check whether
an alarm indicating abnormal battery sampling is generated. If
yes, handle the alarm by referring to the alarm handling
suggestions.
2.If no alarm indicating abnormal battery sampling is
generated, wait for 5 minutes and check whether the alarm is
cleared.
3.If the alarm persists, connect to the power grid and charge
the ESS within 48 hours.
4.If the alarm persists after the ESS is charged for 1 hour,
export logs and contact technical support.
2 1 1.The voltage of the
battery pack or its cells
is too low.
2.The battery pack has
been stored for
extended periods of time
when off-grid.
3.The battery pack has
been idle for a long time
after grid connection.
1.Check that the ESS does not discharge and check whether
an alarm indicating abnormal battery sampling is generated. If
yes, handle the alarm by referring to the alarm handling
suggestions.
2.If no alarm indicating abnormal battery sampling is
generated, wait for 5 minutes and check whether the alarm is
cleared.
3.If the alarm persists, connect to the power grid and charge
the ESS within 48 hours.
4.If the alarm persists after the ESS is charged for 1 hour,
export logs and contact technical support.
3 1 1.The voltage of the
battery pack or its cells
is too low.
2.The battery pack has
been stored for
extended periods of time
when off-grid.
3.The battery pack has
been idle for a long time
after grid connection.
1.Check that the ESS does not discharge and check whether
an alarm indicating abnormal battery sampling is generated. If
yes, handle the alarm by referring to the alarm handling
suggestions.
2.If no alarm indicating abnormal battery sampling is
generated, wait for 5 minutes and check whether the alarm is
cleared.
3.If the alarm persists, connect to the power grid and charge
the ESS within 48 hours.
4.If the alarm persists after the ESS is charged for 1 hour,
export logs and contact technical support.
4 1 1.The voltage of the 1.Check that the ESS does not discharge and check whether

---

## PDF page 14

battery pack or its cells
is too low.
2.The battery pack has
been stored for
extended periods of time
when off-grid.
3.The battery pack has
been idle for a long time
after grid connection.
an alarm indicating abnormal battery sampling is generated. If
yes, handle the alarm by referring to the alarm handling
suggestions.
2.If no alarm indicating abnormal battery sampling is
generated, wait for 5 minutes and check whether the alarm is
cleared.
3.If the alarm persists, connect to the power grid and charge
the ESS within 48 hours.
4.If the alarm persists after the ESS is charged for 1 hour,
export logs and contact technical support.
5 1 1.The voltage of the
battery pack or its cells
is too low.
2.The battery pack has
been stored for
extended periods of time
when off-grid.
3.The battery pack has
been idle for a long time
after grid connection.
1.Check that the ESS does not discharge and check whether
an alarm indicating abnormal battery sampling is generated. If
yes, handle the alarm by referring to the alarm handling
suggestions.
2.If no alarm indicating abnormal battery sampling is
generated, wait for 5 minutes and check whether the alarm is
cleared.
3.If the alarm persists, connect to the power grid and charge
the ESS within 48 hours.
4.If the alarm persists after the ESS is charged for 1 hour,
export logs and contact technical support.

---

## PDF page 15

### 1.1.5 3104 Battery Overcurrent Protection
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3104 Battery Overcurrent Protection Major Equipment
alarm
ADMC
### Impact on the System
The ESS cannot work properly.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The battery pack current
exceeds the maximum
operating current for a
long time due to a
system current limiting
failure.
1.Check whether the power and communications cables of the
ESS are correctly connected.
2.If the cables are correctly connected, clear the alarm and
start the ESS on the user interface.
3.If cables are incorrectly connected, correct the cable
connection according to the user manual and repeat step 2.
4.If the alarm persists, export logs and contact technical
support.
2 1 The battery pack current
exceeds the maximum
operating current for a
long time due to a
system current limiting
failure.
1.Check whether the power and communications cables of the
ESS are correctly connected.
2.If the cables are correctly connected, clear the alarm and
start the ESS on the user interface.
3.If cables are incorrectly connected, correct the cable
connection according to the user manual and repeat step 2.
4.If the alarm persists, export logs and contact technical
support.

---

## PDF page 16

### 1.1.6 3105 Battery Pack Overtemperature
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3105 Battery Pack Overtemperature Major Equipment
alarm
ADAC
### Impact on the System
The ESS cannot work properly.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The Liquid Thermal
Management System
(LTMS) is faulty.
1.Check that the ESS is not charged and does not discharge.
Wait for 30 minutes and check whether the alarm is cleared.
2.If the alarm persists, check whether an alarm is generated for
the LTMS. If yes, handle the alarm by referring to the alarm
handling suggestions.
2 The battery cell NTC is
faulty, causing
overtemperature.
1.Check that the ESS has been powered off by referring to the
user manual.
2.Wear protective clothing and take protective measures. Open
the front panel of the battery pack, remove the NTC terminal,
and check whether the NTC impedance is normal.
3.After checking that the NTC impedance is normal, start the
ESS on the user interface.
4.If the alarm persists, export logs and contact technical
support.
2 1 The LTMS is faulty. 1.Check that the ESS is not charged and does not discharge.
Wait for 30 minutes and check whether the alarm is cleared.
2.If the alarm persists, check whether an alarm is generated for
the LTMS. If yes, handle the alarm by referring to the alarm
handling suggestions.
2 The battery cell NTC is
faulty, causing
overtemperature.
1.Check that the ESS has been powered off by referring to the
user manual.
2.Wear protective clothing and take protective measures. Open
the front panel of the battery pack, remove the NTC terminal,
and check whether the NTC impedance is normal.
3.After checking that the NTC impedance is normal, start the
ESS on the user interface.
4.If the alarm persists, export logs and contact technical
support.

---

## PDF page 17

### 1.1.7 3106 Battery Pack Undertemperature
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3106 Battery Pack Undertemperature Major Equipment
alarm
ADAC
### Impact on the System
The ESS cannot work properly.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The ambient
temperature is too low,
reaching the charge
undertemperature
protection threshold.
1.Check whether an alarm is generated for the LTMS. If yes,
handle the alarm by referring to the alarm handling suggestions.
2.After checking that the LTMS is normal, check that the LTMS
works in heating mode on the user interface. Wait for more than
4 hours and check whether the undertemperature protection
alarm is cleared.
3.If the alarm persists, export logs and contact technical
support.
2 1 The ambient
temperature is too low,
which triggers
discharge protection.
1.Check whether an alarm is generated for the LTMS. If yes,
handle the alarm by referring to the alarm handling suggestions.
2.After checking that the LTMS is normal, check that the LTMS
works in heating mode on the user interface. Wait for more than
6 hours and check whether the undertemperature protection
alarm is cleared.
3.If the alarm persists, export logs and contact technical
support.
3 1 The ambient
temperature is too low,
which triggers charge
protection.
1.Check whether an alarm is generated for the LTMS. If yes,
handle the alarm by referring to the alarm handling suggestions.
2.After checking that the LTMS is normal, check that the LTMS
works in heating mode on the user interface. Wait for more than
4 hours and check whether the undertemperature protection
alarm is cleared.
3.If the alarm persists, export logs and contact technical
support.
4 1 The ambient
temperature is too low,
which triggers
discharge protection.
1.Check whether an alarm is generated for the LTMS. If yes,
handle the alarm by referring to the alarm handling suggestions.
2.After checking that the LTMS is normal, check that the LTMS
works in heating mode on the user interface. Wait for more than
6 hours and check whether the undertemperature protection
alarm is cleared.
3.If the alarm persists, export logs and contact technical
support.

---

## PDF page 18

### 1.1.8 3107 Battery Pack Locked
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3107 Battery Pack Locked Major Equipment
alarm
ADMC
### Impact on the System
The ESS cannot work properly.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The copper bar torque
does not meet
requirements.
1.Check that the ESS is not charged and does not discharge
and clear the alarm on the user interface.
2.Power off the ESS by referring to the user manual.
3.Wait for 5 minutes, wear protective equipment, take
protective measures, open the front panel of the battery
pack, and check whether the positive and negative copper
bars are loose. If they are loose, tighten the screws.
4.After checking that the screws are tightened, start the ESS
on the user interface and check whether the alarm is
generated again after 24 hours.
2 The LTMS does not
run properly.
1.Check that the ESS is not charged and does not discharge
and clear the alarm on the user interface.
2.Check whether an alarm is generated for the LTMS. If yes,
handle the alarm by referring to the alarm handling
suggestions.
3.If no, wait for 5 minutes, start the ESS on the user
interface, and check whether the alarm is generated again
after 24 hours.
4.If the alarm persists, export logs and contact technical
support.
2 1 The LTMS does not
run properly.
1.Check that the ESS is not charged and does not discharge
and clear the alarm on the user interface.
2.Check whether an alarm is generated for the LTMS. If yes,
handle the alarm by referring to the alarm handling
suggestions.
3.If no, wait for 5 minutes, start the ESS on the user
interface, and check whether the alarm is generated again
after 24 hours.
4.If the alarm persists, export logs and contact technical
support.
3 1 The battery pack has
triggered the same
undervoltage fault
multiple times.
1.Check that the ESS does not discharge. Clear the alarm on
the user interface and check whether the alarm is generated
again 10 minutes later.
2.If the alarm persists, connect to the power grid and charge

---

## PDF page 19

the ESS within 48 hours.
3.Clear the alarm and start the ESS on the user interface to
start charging.
4.If the alarm persists after the ESS is charged for 1 hour,
export logs and contact technical support.
4 1 The battery pack has
triggered the same
overvoltage fault
multiple times.
1.Check that the ESS is not charged, clear the alarm on the
user interface, wait for 10 minutes, and check whether the
alarm is generated again.
2.If the alarm persists, shut down the ESS on the user
interface.
3.Wait for 5 minutes.
4.Start the ESS and clear the alarm on the user interface.
5.If the alarm persists, export logs and contact technical
support.
5 1 The battery pack has
triggered the same
overcurrent fault
multiple times.
1.Check that the ESS is not charged and does not discharge,
clear the alarm on the user interface, wait for 10 minutes,
and check whether the alarm is generated again.
2.If the alarm persists, shut down the ESS on the user
interface.
3.Wait for 5 minutes.
4.Start the ESS and clear the alarm on the user interface.
5.If the alarm persists, export logs and contact technical
support.
6 1 The cell voltage in the
battery pack is too
high.
1.Check that the battery rack is not charged and does not
discharge, wait for 5 minutes, and check whether the alarm
is generated again.
2.If the alarm is generated again, confirm on the user
interface that the battery rack has been shut down.
3.Wait for 5 minutes.
4.Clear the alarm on the user interface and start the battery
rack.
5.If the alarm persists, export logs and contact technical
support.
7 1 1.The voltage of the
battery pack or its cells
is too low.
2.The battery pack has
been stored for
extended periods of
time when off-grid.
3.The battery pack has
been idle for a long
time after grid
connection.
1.Power off the ESS by referring to the user manual, remove
the battery pack, and use a charger to charge the battery
pack by referring to the charge guide.
2.Reinstall the battery pack after charging. After the ESS is
powered on, clear the alarm on the user interface and check
whether the alarm persists.
3.If the alarm persists, export logs and contact technical
support.
8 1 The LTMS is faulty. 1.Check that the ESS is not charged and does not discharge.
2.Check whether an alarm is generated for the LTMS. If yes,
handle the alarm by referring to the alarm handling
suggestions.
3.After confirming that the LTMS is normal, clear the alarm

---

## PDF page 20

on the user interface.
2 The battery cell NTC is
faulty, causing
overtemperature.
1.Check that the ESS has been powered off by referring to
the user manual.
2.Wear protective clothing and take protective measures.
Open the front panel of the battery pack, remove the NTC
terminal, and check whether the NTC impedance is normal.
3.After checking that the NTC impedance is normal, clear the
alarm and start the ESS on the user interface.
4.If the alarm persists, export logs and contact technical
support.
9 1 The ambient
temperature is too low,
which triggers charge
protection.
1.Check whether an alarm is generated for the LTMS. If yes,
handle the alarm by referring to the alarm handling
suggestions.
2.After confirming that the LTMS is normal, clear the alarm
on the user interface. Check that the LTMS works in heating
mode. Monitor the battery temperature for more than 20
hours to check whether it slowly rises.
3.If the alarm persists, export logs and contact technical
support.
10 1 The ambient
temperature is too low,
which triggers
discharge protection.
1.Check whether an alarm is generated for the LTMS. If yes,
handle the alarm by referring to the alarm handling
suggestions.
2.After confirming that the LTMS is normal, clear the alarm
on the user interface. Check that the LTMS works in heating
mode. Monitor the battery temperature for more than 6 hours
to check whether it slowly rises.
3.If the alarm persists, export logs and contact technical
support.

---

## PDF page 21

### 1.1.9 3108 Battery Faulty
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3108 Battery Faulty Major Equipment
alarm
ADAC
### Impact on the System
The ESS cannot work properly.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 A major fault has
occurred on the battery
pack.
Export logs and contact technical support.
2 1 A major fault has
occurred on the battery
pack.
Export logs and contact technical support.
3 1 A major fault has
occurred on the battery
pack.
Export logs and contact technical support.
4 1 The battery pack
experiences
overtemperature, which
may cause thermal
runaway.
1.Observe the system remotely for 30 minutes to check
whether other exceptions (such as abnormal battery voltage,
battery temperature, and combustible gas concentration) occur.
During the remote observation, do not approach the ESS or
open the ESS cabin doors.
2.If no exception is found during the 30 -minute remote
observation, send trained personnel to the site and observe the
system for 30 minutes from a safe distance. If there is smoke
or fire, evacuate onsite personnel as soon as possible, and call
the fire emergency service.
3.If no fault is found during the 30 -minute remote observation
and 30 -minute onsite observation, export logs and contact
technical support.

---

## PDF page 22

### 1.1.10 3109 Battery Pack SOH Low
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3109 Battery Pack SOH Low Warning Equipment
alarm
ADMC
### Impact on the System
The ESS works properly, and the battery pack may approach the end of its lifespan.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The battery pack SOH is
low.
1. Check whether an alarm indicating abnormal battery
sampling is generated. If yes, handle the alarm by referring to
the alarm handling suggestions.
2. If no, contact technical support to check the battery pack
SOH.
3. If the battery pack SOH reaches the low alarm threshold,
enable the SOH calibration function.
4. After the calibration is complete, clear the alarm on the user
interface.
5. If the alarm persists, the battery pack SOH is low. Pay
attention to the operating status and replace the battery pack in
advance.

---

## PDF page 23

### 1.1.11 3112 Power Connection Sampling of Battery Pack Abnormal
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3112 Power Connection Sampling of
Battery Pack Abnormal
Major Equipment
alarm
ADMC
### Impact on the System
The ESS cannot work properly.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 A major fault has
occurred on the internal
circuit of the BMU.
1.Power off the ESS by referring to the user manual.
2.Wear protective equipment, take protective measures, open
the front panel of the battery pack, and replace the faulty BMU.
3.Wait for 5 minutes, clear the alarm on the user interface, and
start the ESS.
4.If the alarm persists, export logs and contact technical
support.

---

## PDF page 24

### 1.1.12 3113 Battery Pack Configuration Data Abnormal
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3113 Battery Pack Configuration Data
Abnormal
Major Equipment
alarm
ADMC
### Impact on the System
The ESS cannot work properly.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The differentiated data
and backup data of each
BMU are inconsistent or
some data is corrupted.
1.If the BCU has been replaced, replace it on the "Device
Replacement" page of the DataLoggerWebUI.
2.If only the BMU or battery pack is replaced or no spare part is
replaced, check the SN on the battery pack label and connect
to the FusionSolar app beside the ESS.
3.On the alarm screen of the app, tap "Proceed" to go to the
SN confirming screen and select the SN displayed on the
battery pack label. If the SN is not the one displayed on the
battery pack label, data errors may occur and safety risks may
occur during system running.
4.After the SN is confirmed, the device automatically
synchronizes data and restarts.
2 1 The differentiated data
and backup data on
each BMU are corrupted.
1.If the BMU and BCU have been replaced, replace them on
the "Device Replacement" page of the DataLogger WebUI.
2.If the alarm persists, export logs and contact technical
support.

---

## PDF page 25

### 1.1.13 3114 Battery Pack and System Specifications Mismatched
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3114 Battery Pack and System
Specifications Mismatched
Major Equipment
alarm
ADAC
### Impact on the System
The ESS cannot work properly.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 1.The versions of the
rack controller and
battery packs are
inconsistent. 2.The
update fails. 3.The
battery pack has been
replaced.
1.The battery pack model is incompatible with the system.
Replace the battery pack with the original one.
2.If the alarm persists, export logs and contact technical
support.

---

## PDF page 26

### 1.1.14 3115 Cell Temperature Rises Abnormally
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3115 Cell Temperature Rises Abnormally Major Equipment
alarm
ADMC
### Impact on the System
The ESS cannot work properly.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The battery pack has
thermal runaway risks.
1.Observe the system remotely for 30 minutes to check
whether other exceptions (such as abnormal battery voltage,
battery temperature, and combustible gas concentration) occur.
During the remote observation, do not approach the ESS or
open the ESS cabin doors.
2.If no exception is found during the 30 -minute remote
observation, send trained personnel to the site and observe the
system for 30 minutes from a safe distance. If there is smoke
or fire, evacuate onsite personnel as soon as possible, and call
the fire emergency service.
3.If no fault is found during the 30 -minute remote observation
and 30 -minute onsite observation, clear the alarm and power
on the system again.

---

## PDF page 27

### 1.1.15 3116 PACK Thermal Runaway
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3116 Pack Thermal Runaway Major Equipment
alarm
ADAC
### Impact on the System
The ESS cannot work properly.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The battery pack has
thermal runaway risks.
1.Observe the system remotely for 30 minutes to check
whether other exceptions (such as abnormal battery voltage,
battery temperature, and combustible gas concentration) occur.
During the remote observation, do not approach the ESS or
open the ESS cabin doors.
2.If no exception is found during the 30 -minute remote
observation, send trained personnel to the site and observe the
system for 30 minutes from a safe distance. If there is smoke
or fire, evacuate onsite personnel as soon as possible, call the
fire emergency service, and provide firefighters with related
product information, including the battery pack type, ESS
capacity, and battery pack location.
3.Do not enter the affected building or equipment area under
any circumstances, and do not open the ESS cabin doors.
Isolate and monitor the site. Keep irrelevant personnel away
from the site.
4.After calling the fire emergency service, remotely power off
the peripheral devices (such as the Smart Transformer Station,
Smart PCS, auxiliary power supply devices, and combiner box
power supply) while ensuring your own safety.
5.After the fire is extinguished, the site must be handled by
professionals in accordance with local laws and regulations. Do
not open the ESS cabin doors without permission.

---

## PDF page 28

### 1.1.16 3117 Battery Pack Charging Failed
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3117 Battery Pack Charging Failed Major Communications
alarm
ADMC
### Impact on the System
The ESS cannot work properly.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 Charging fails. 1.Power off the ESS by referring to the user manual.
2.Wait for 5 minutes and check whether cables to the ESS are
correctly connected by referring to the user manual.
3.After checking that the cable connection is normal, clear the
alarm and start the ESS on the user interface.
4.If the alarm persists, export logs and contact technical
support.

---

## PDF page 29

## 1.2 Battery Pack (Balancing Module)
### 1.2.1 3161 Balancing Module Overcurrent Protection
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3161 Balancing Module Overcurrent
Protection
Minor Equipment
alarm
ADAC
### Impact on the System
The balancing module stops working, but the system is charged and discharges normally.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 Overload or a short
circuit occurs.
1. If the alarm is automatically cleared after a short period of
time and the system recovers, the module may be overloaded
for a short period of time. In this case, no manual intervention
is required.
2. If overcurrent protection alarm persists, reset the rack on the
user interface. After the system restarts, check whether the
alarm is cleared.
3. If the alarm persists, replace the balancing module by
referring to the maintenance manual.
4. If the alarm persists, export logs and contact technical
support.
2 1 Overload or a short
circuit occurs.
1. If the alarm is automatically cleared after a short period of
time and the system recovers, the module may be overloaded
for a short period of time. In this case, no manual intervention
is required.
2. If overcurrent protection alarm persists, reset the rack on the
user interface. After the system restarts, check whether the
alarm is cleared.
3. If the alarm persists, replace the balancing module by
referring to the maintenance manual.
4. If the alarm persists, export logs and contact technical
support.
3 1 Overload or a short
circuit occurs.
1. If the alarm is automatically cleared after a short period of
time and the system recovers, the module may be overloaded
for a short period of time. In this case, no manual intervention
is required.
2. If overcurrent protection alarm persists, reset the rack on the
user interface. After the system restarts, check whether the
alarm is cleared.
3. If the alarm persists, replace the balancing module by
referring to the maintenance manual.
4. If the alarm persists, export logs and contact technical
support.

---

## PDF page 30

4 1 Overload or a short
circuit occurs.
1. If the alarm is automatically cleared after a short period of
time and the system recovers, the module may be overloaded
for a short period of time. In this case, no manual intervention
is required.
2. If overcurrent protection alarm persists, reset the rack on the
user interface. After the system restarts, check whether the
alarm is cleared.
3. If the alarm persists, replace the balancing module by
referring to the maintenance manual.
4. If the alarm persists, export logs and contact technical
support.

---

## PDF page 31

### 1.2.2 3162 Balancing Module Internal Error
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3162 Balancing Module Internal Error Minor Equipment
alarm
ADAC
### Impact on the System
The balancing module stops working, but the system is charged and discharges normally.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The communication
circuit is not properly
connected or the
communication circuit
components are
damaged.
1. If the alarm is automatically cleared after a short period of time
and the system recovers, the communication may be abnormal
for a short period of time. In this case, no manual intervention is
required.
2. If the alarm persists, reset the rack on the user interface. After
the system restarts, check whether the alarm is cleared.
3. If the alarm persists, replace the balancing module by referring
to the maintenance manual.
4. If the alarm persists, export logs and contact technical support.
2 1 The communication
circuit is not properly
connected or the
communication circuit
components are
damaged.
1. If the alarm is automatically cleared after a short period of time
and the system recovers, the communication may be abnormal
for a short period of time. In this case, no manual intervention is
required.
2. If the alarm persists, reset the rack on the user interface. After
the system restarts, check whether the alarm is cleared.
3. If the alarm persists, replace the balancing module by referring
to the maintenance manual.
4. If the alarm persists, export logs and contact technical support.
3 1 The communication
circuit is not properly
connected or the
communication circuit
components are
damaged.
1. If the alarm is automatically cleared after a short period of time
and the system recovers, the communication may be abnormal
for a short period of time. In this case, no manual intervention is
required.
2. If the alarm persists, reset the rack on the user interface. After
the system restarts, check whether the alarm is cleared.
3. If the alarm persists, replace the balancing module by referring
to the maintenance manual.
4. If the alarm persists, export logs and contact technical support.
4 1 The board hardware
circuit is damaged.
1. If the alarm is automatically cleared after a short period of time
and the system recovers, no manual intervention is required.
2. If the alarm persists, reset the rack on the user interface. After
the system restarts, check whether the alarm is cleared.
3. If the alarm persists, replace the balancing module by referring
to the maintenance manual.

---

## PDF page 32

4. If the alarm persists, export logs and contact technical support.
5 1 Overcurrent occurs on
the bus side.
1. If the alarm is automatically cleared after a short period of time
and the system recovers, no manual intervention is required.
2. If the alarm persists, reset the rack on the user interface. After
the system restarts, check whether the alarm is cleared.
3. If the alarm persists, replace the balancing module by referring
to the maintenance manual.
4. If the alarm persists, export logs and contact technical support.
6 1 The EEPROM is faulty
or the I2C
communication is
abnormal.
1. If the alarm is automatically cleared after a short period of time
and the system recovers, no manual intervention is required.
2. If the alarm persists, reset the rack on the user interface. After
the system restarts, check whether the alarm is cleared.
3. If the alarm persists, replace the balancing module by referring
to the maintenance manual.
4. If the alarm persists, export logs and contact technical support.
7 1 The EEPROM is faulty
or the I2C
communication is
abnormal.
1. If the alarm is automatically cleared after a short period of time
and the system recovers, no manual intervention is required.
2. If the alarm persists, reset the rack on the user interface. After
the system restarts, check whether the alarm is cleared.
3. If the alarm persists, replace the balancing module by referring
to the maintenance manual.
4. If the alarm persists, export logs and contact technical support.
8 1 The temperature
sampling circuit is
damaged.
1. If the alarm is automatically cleared after a short period of time
and the system recovers, no manual intervention is required.
2. If the alarm persists, reset the rack on the user interface. After
the system restarts, check whether the alarm is cleared.
3. If the alarm persists, replace the balancing module by referring
to the maintenance manual.
4. If the alarm persists, export logs and contact technical support.
9 1 The temperature
sampling circuit is
damaged.
1. If the alarm is automatically cleared after a short period of time
and the system recovers, no manual intervention is required.
2. If the alarm persists, reset the rack on the user interface. After
the system restarts, check whether the alarm is cleared.
3. If the alarm persists, replace the balancing module by referring
to the maintenance manual.
4. If the alarm persists, export logs and contact technical support.
10 1 The MCU on the
battery side is
abnormal.
1. If the alarm is automatically cleared after a short period of time
and the system recovers, the MCU may be abnormal for a short
period of time. In this case, no manual intervention is required.
2. If the alarm persists, reset the rack on the user interface. After
the system restarts, check whether the alarm is cleared.
3. If the alarm persists, replace the balancing module by referring
to the maintenance manual.
4. If the alarm persists, export logs and contact technical support.
11 1 The MCU on the bus
side is abnormal.
1. If the alarm is automatically cleared after a short period of time
and the system recovers, the MCU may be abnormal for a short
period of time. In this case, no manual intervention is required.
2. If the alarm persists, reset the rack on the user interface. After

---

## PDF page 33

the system restarts, check whether the alarm is cleared.
3. If the alarm persists, replace the balancing module by referring
to the maintenance manual.
4. If the alarm persists, export logs and contact technical support.
12 1 The lightning current
causes the SPD to trip.
1. If the alarm is automatically cleared after a short period of time
and the system recovers, no manual intervention is required.
2. If the alarm persists, reset the rack on the user interface. After
the system restarts, check whether the alarm is cleared.
3. If the alarm persists, replace the balancing module by referring
to the maintenance manual.
4. If the alarm persists, export logs and contact technical support.

---

## PDF page 34

### 1.2.3 3163 Balancing Module Bus Voltage Abnormal
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3163 Balancing Module Bus Voltage
Abnormal
Minor Equipment
alarm
ADAC
### Impact on the System
The balancing module stops working, but the system is charged and discharges normally.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The voltage control
loop in the
discharging state is
out of control.
1. If the alarm is automatically cleared after a short period of time
and the system recovers, the bus voltage may be abnormal for a
short period of time. In this case, no manual intervention is
required.
2. If the alarm persists, reset the rack on the user interface. After
the system restarts, check whether the alarm is cleared.
3. If the alarm persists, replace the balancing module by referring
to the maintenance manual.
4. If the alarm persists, export logs and contact technical support.
2 1 The bus voltage
control loop is out of
control.
1. If the alarm is automatically cleared after a short period of time
and the system recovers, the bus voltage may be abnormal for a
short period of time. In this case, no manual intervention is
required.
2. If the alarm persists, reset the rack on the user interface. After
the system restarts, check whether the alarm is cleared.
3. If the alarm persists, replace the balancing module by referring
to the maintenance manual.
4. If the alarm persists, export logs and contact technical support.
2 Cables on the bus
side are not
connected or BCU
scheduling is
abnormal.
1. Power off the ESS by referring to the user manual. Check
whether the balancing bus cable is securely connected. If yes,
power on the ESS again.
2. If the alarm persists, replace the balancing module by referring
to the maintenance manual.
3. If the alarm persists, export logs and contact technical support.
3 1 The bus voltage
control loop is out of
control.
1. If the alarm is automatically cleared after a short period of time
and the system recovers, the bus voltage may be abnormal for a
short period of time. In this case, no manual intervention is
required.
2. If the alarm persists, reset the rack on the user interface. After
the system restarts, check whether the alarm is cleared.
3. If the alarm persists, replace the balancing module by referring
to the maintenance manual.
4. If the alarm persists, export logs and contact technical support.

---

## PDF page 35

### 1.2.4 3164 Balancing Module Battery Voltage Abnormal
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3164 Balancing Module Battery Voltage
Abnormal
Minor Equipment
alarm
ADAC
### Impact on the System
The balancing module stops working, but the system is charged and discharges normally.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The PACK voltage is too
high.
1. Check whether a battery pack overvoltage alarm is
generated. If yes, clear the overvoltage alarm by referring to
the handling suggestions.
2. If no, reset the rack on the user interface. After the system
restarts, check whether the alarm is cleared.
3. If the alarm persists, replace the balancing module by
referring to the maintenance manual.
4. If the alarm persists, export logs and contact technical
support.
2 1 The PACK voltage is too
low.
1. Check whether a battery pack undervoltage alarm is
generated. If yes, clear the undervoltage alarm by referring to
the handling suggestions.
2. If no, reset the rack on the user interface. After the system
restarts, check whether the alarm is cleared.
3. If the alarm persists, replace the balancing module by
referring to the maintenance manual.
4. If the alarm persists, export logs and contact technical
support.

---

## PDF page 36

### 1.2.5 3165 Overtemperature Protection Inside Balancing Module
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3165 Overtemperature Protection Inside
Balancing Module
Minor Equipment
alarm
ADAC
### Impact on the System
The balancing module stops working, but the system is charged and discharges normally.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The output is
overloaded, a
component is abnormal
(MOS short-circuited), or
the ambient temperature
is too high.
1. If the alarm is automatically cleared after a short period of
time and the system recovers, the temperature inside the
cabinet may be too high for a short period of time. In this case,
no manual intervention is required.
2. If the alarm persists, reset the rack on the user interface.
After the system restarts, check whether the alarm is cleared.
3. If the alarm persists, replace the balancing module by
referring to the maintenance manual.
4. If the alarm persists, export logs and contact technical
support.
2 1 The output is
overloaded, a
component is abnormal
(MOS short-circuited), or
the ambient temperature
is too high.
1. If the alarm is automatically cleared after a short period of
time and the system recovers, the temperature inside the
cabinet may be too high for a short period of time. In this case,
no manual intervention is required.
2. If the alarm persists, reset the rack on the user interface.
After the system restarts, check whether the alarm is cleared.
3. If the alarm persists, replace the balancing module by
referring to the maintenance manual.
4. If the alarm persists, export logs and contact technical
support.

---

## PDF page 37

### 1.2.6 3166 MCU Overtemperature Protection on the Battery Side of
the Balancing Module
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3166 MCU Overtemperature Protection
on the Battery Side of the Balancing
Module
Minor Equipment
alarm
ADMC
### Impact on the System
The balancing module stops working, but the system is charged and discharges normally.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The MCU is short -
circuited.
1. Reset the rack on the user interface. After the system
restarts, check whether the alarm is cleared.
2. If the alarm persists, replace the balancing module by
referring to the maintenance manual.
3. If the alarm persists, export logs and contact technical
support.

---

## PDF page 38

### 1.2.7 3167 Overtemperature Protection for the Wiring Terminal of
the Balancing Module
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3167 Overtemperature Protection for the
Wiring Terminal of the Balancing
Module
Minor Equipment
alarm
ADAC
### Impact on the System
The balancing module stops working, but the system is charged and discharges normally.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The bus port is not
properly connected.
1. Power off the ESS by referring to the user manual. Check
whether the balancing bus cable is securely connected. If yes,
power on the ESS again.
2. If the alarm persists, replace the balancing module by
referring to the maintenance manual.
3. If the alarm persists, export logs and contact technical
support.
2 1 The battery port is not
properly connected.
1. Power off the ESS by referring to the user manual.
Disassemble the balancing module. Check whether the
balancing bus cable is securely connected. If yes, power on the
ESS again.
2. If the alarm persists, replace the balancing module by
referring to the maintenance manual.
3. If the alarm persists, export logs and contact technical
support.

---

## PDF page 39

### 1.2.8 3169 Balancing Module Bus Soft-Start Failed
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3169 Balancing Module Bus Soft -Start
Failed
Minor Equipment
alarm
ADAC
### Impact on the System
The balancing module stops working, but the system is charged and discharges normally.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 Exceptions, such as soft-
start with load, occur.
1. Power off the ESS by referring to the user manual. Check
whether the balancing bus cable is intact and securely
connected. If yes, power on the ESS again.
2. If the alarm persists, replace the balancing module by
referring to the maintenance manual.
3. If the alarm persists, export logs and contact technical
support.

### 1.2.9 3170 Balancing Module Version Mismatch
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3170 Balancing Module Version
Mismatch
Minor Equipment
alarm
ADMC
### Impact on the System
The balancing module stops working, but the system is charged and discharges normally.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 An error occurs during
software loading.
1. Obtain the matching version and perform an update.
2. If the alarm persists, replace the balancing module by
referring to the maintenance manual.
3. If the alarm persists, export logs and contact technical
support.

---

## PDF page 40

### 1.2.10 3171 Balancing Module Address Pairing Timeout
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3171 Balancing Module Address Pairing
Timeout
Minor Equipment
alarm
ADAC
### Impact on the System
The balancing module stops working, but the system is charged and discharges normally.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 Failed to save the
address.
1. If the alarm is automatically cleared after a short period of
time and the system recovers, the communication may be
abnormal for a short period of time. In this case, no manual
intervention is required.
2. If the alarm persists, reset the rack on the user interface.
After the system restarts, check whether the alarm is cleared.
3. If the alarm persists, replace the balancing module by
referring to the maintenance manual.
4. If the alarm persists, export logs and contact technical
support.

### 1.2.11 3172 Balancing Module Soft-Start Circuit Abnormal
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3172 Balancing Module Soft -Start Circuit
Abnormal
Minor Equipment
alarm
ADMC
### Impact on the System
The balancing module stops working, but the system is charged and discharges normally.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The soft -start circuit is
abnormal.
1. Reset the rack on the user interface. After the system
restarts, check whether the alarm is cleared.
2. If the alarm persists, replace the balancing module by
referring to the maintenance manual.
3. If the alarm persists, export logs and contact technical
support.

---

## PDF page 41

### 1.2.12 3173 Balancing Module Abnormal
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3173 Balancing Module Abnormal Minor Equipment
alarm
ADMC
### Impact on the System
The balancing module stops working, but the system is charged and discharges normally.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The auxiliary power
circuit is abnormal.
1. Reset the rack on the user interface. After the system restarts,
check whether the alarm is cleared.
2. If the alarm persists, replace the balancing module by referring
to the maintenance manual.
3. If the alarm persists, export logs and contact technical support.
2 1 The auxiliary power
circuit is abnormal.
1. Reset the rack on the user interface. After the system restarts,
check whether the alarm is cleared.
2. If the alarm persists, replace the balancing module by referring
to the maintenance manual.
3. If the alarm persists, export logs and contact technical support.
3 1 The auxiliary power
circuit is abnormal.
1. Reset the rack on the user interface. After the system restarts,
check whether the alarm is cleared.
2. If the alarm persists, replace the balancing module by referring
to the maintenance manual.
3. If the alarm persists, export logs and contact technical support.
4 1 Electromagnetic
interference or a
memory access
exception occurs.
1. Reset the rack on the user interface. After the system restarts,
check whether the alarm is cleared.
2. If the alarm persists, replace the balancing module by referring
to the maintenance manual.
3. If the alarm persists, export logs and contact technical support.
5 1 Electromagnetic
interference or a
memory access
exception occurs.
1. Reset the rack on the user interface. After the system restarts,
check whether the alarm is cleared.
2. If the alarm persists, replace the balancing module by referring
to the maintenance manual.
3. If the alarm persists, export logs and contact technical support.
6 1 The MOS tube on the
bus side is short -
circuited.
1. Reset the rack on the user interface. After the system restarts,
check whether the alarm is cleared.
2. If the alarm persists, replace the balancing module by referring
to the maintenance manual.
3. If the alarm persists, export logs and contact technical support.
7 1 The MOS tube on the
battery side is short -
1. Reset the rack on the user interface. After the system restarts,

---

## PDF page 42

circuited. check whether the alarm is cleared.
2. If the alarm persists, replace the balancing module by referring
to the maintenance manual.
3. If the alarm persists, export logs and contact technical support.
8 1 The relay control loop
fails or relay adhesion
exists.
1. Reset the rack on the user interface. After the system restarts,
check whether the alarm is cleared.
2. If the alarm persists, replace the balancing module by referring
to the maintenance manual.
3. If the alarm persists, export logs and contact technical support.
9 1 Open circuit: The relay
control loop fails.
Short circuit: A high
current causes
shutdown and then
adhesion.
1. Reset the rack on the user interface. After the system restarts,
check whether the alarm is cleared.
2. If the alarm persists, replace the balancing module by referring
to the maintenance manual.
3. If the alarm persists, export logs and contact technical support.
11 1 The voltage control
loop in the discharging
state is out of control.
1. Reset the rack on the user interface. After the system restarts,
check whether the alarm is cleared.
2. If the alarm persists, replace the balancing module by referring
to the maintenance manual.
3. If the alarm persists, export logs and contact technical support.
14 1 The MCU is damaged
or the sampling circuit
is abnormal.
1. Reset the rack on the user interface. After the system restarts,
check whether the alarm is cleared.
2. If the alarm persists, replace the balancing module by referring
to the maintenance manual.
3. If the alarm persists, export logs and contact technical support.
16 1 The board is short -
circuited.
1. Reset the rack on the user interface. After the system restarts,
check whether the alarm is cleared.
2. If the alarm persists, replace the balancing module by referring
to the maintenance manual.
3. If the alarm persists, export logs and contact technical support.
17 1 The interrupt task is
blocked or the task
times out.
1. Reset the rack on the user interface. After the system restarts,
check whether the alarm is cleared.
2. If the alarm persists, replace the balancing module by referring
to the maintenance manual.
3. If the alarm persists, export logs and contact technical support.
18 1 Electromagnetic
interference or a
memory access
exception occurs.
1. Reset the rack on the user interface. After the system restarts,
check whether the alarm is cleared.
2. If the alarm persists, replace the balancing module by referring
to the maintenance manual.
3. If the alarm persists, export logs and contact technical support.
19 1 Electromagnetic
interference or a
memory access
exception occurs.
1. Reset the rack on the user interface. After the system restarts,
check whether the alarm is cleared.
2. If the alarm persists, replace the balancing module by referring
to the maintenance manual.
3. If the alarm persists, export logs and contact technical support.
20 1 The communication
link is interfered.
1. Reset the rack on the user interface. After the system restarts,
check whether the alarm is cleared.

---

## PDF page 43

2. If the alarm persists, replace the balancing module by referring
to the maintenance manual.
3. If the alarm persists, export logs and contact technical support.

---

## PDF page 44

### 1.2.13 3174 Balancing Module Overcurrent Fault
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3174 Balancing Module Overcurrent
Fault
Minor Equipment
alarm
ADMC
### Impact on the System
The balancing module stops working, but the system is charged and discharges normally.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 Overload or a short
circuit occurs.
1. Reset the rack on the user interface. After the system
restarts, check whether the alarm is cleared.
2. If the alarm persists, replace the balancing module by
referring to the maintenance manual.
3. If the alarm persists, export logs and contact technical
support.
2 1 Overload or a short
circuit occurs.
1. Reset the rack on the user interface. After the system
restarts, check whether the alarm is cleared.
2. If the alarm persists, replace the balancing module by
referring to the maintenance manual.
3. If the alarm persists, export logs and contact technical
support.
3 1 Overload or a short
circuit occurs.
1. Reset the rack on the user interface. After the system
restarts, check whether the alarm is cleared.
2. If the alarm persists, replace the balancing module by
referring to the maintenance manual.
3. If the alarm persists, export logs and contact technical
support.
4 1 Overload or a short
circuit occurs.
1. Reset the rack on the user interface. After the system
restarts, check whether the alarm is cleared.
2. If the alarm persists, replace the balancing module by
referring to the maintenance manual.
3. If the alarm persists, export logs and contact technical
support.

---

## PDF page 45

## 1.3 RCM (BCU)
### 1.3.1 3222 BMU Internal Short Circuit
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3222 BMU Internal Short Circuit Major Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally when a minor fault occurs on the BMU. In case of a
serious fault, the battery rack shuts down.
Possible Causes and Procedure
Reason
ID
No. Possible Cause Suggestion
1 1 The pins are short -
circuited due to foreign
objects inside the BMU.
1. Replace the BMU, run the new BMU, and check whether the
alarm persists.
2. If the alarm persists after the BMU is replaced, replace the
battery pack.
2 1 The pins are short -
circuited due to foreign
objects inside the BMU.
1. Replace the BMU, run the new BMU, and check whether the
alarm persists.
2. If the alarm persists after the BMU is replaced, replace the
battery pack.
3 1 The pins are short -
circuited due to foreign
objects inside the BMU.
1. Replace the BMU, run the new BMU, and check whether the
alarm persists.
2. If the alarm persists after the BMU is replaced, export logs
and contact technical support.
4 1 The pins are short -
circuited due to foreign
objects inside the BMU.
1. Replace the BMU, run the new BMU, and check whether the
alarm persists.
2. If the alarm persists after the BMU is replaced, replace the
fuse temperature sampling cable harness.
3. If the alarm persists after the fuse temperature sampling
cable harness connected to the J3 connector (4 -pin) on the
BMU is replaced, replace the battery pack.
5 1 The pins are short -
circuited due to foreign
objects inside the BMU.
1. Replace the BMU, run the new BMU, and check whether the
alarm persists.
2. If the alarm persists after the BMU is replaced, replace the
positive and negative busbar temperature sampling cable
harnesses connected to the J3 connector (4-pin) on the BMU.
3. If the alarm persists after the positive and negative busbar
temperature sampling cable harnesses are replaced, replace
the battery pack.

---

## PDF page 46

### 1.3.2 3223 BMU Sampling Cable Disconnected
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3223 BMU Sampling Cable Disconnected Major Equipment
alarm
ADAC
### Impact on the System
The battery rack shuts down.
Possible Causes and Procedure
Reason
ID
No. Possible Cause Suggestion
1 1 The FPC connector is
loose, the cable is
disconnected, or the
BMU is faulty.
1. Remove and reinstall the FPC connector to the BMU and
check whether the alarm persists. If yes, replace the BMU.
2. If the alarm persists after the BMU is replaced, replace the
battery pack.
3. If the alarm persists, export logs and contact technical
support.
2 1 The FPC connector is
loose, the cable is
disconnected, or the
BMU is faulty.
1. Remove and reinstall the FPC connector to the BMU and
check whether the alarm persists. If yes, replace the BMU.
2. If the alarm persists, export logs and contact technical
support.
3 1 The FPC connector is
loose, the cell
temperature sampling
cable is disconnected, or
the BMU is faulty.
1. Remove and reinstall the FPC connector to the BMU and
check whether the alarm persists. If yes, replace the BMU.
2. If the alarm persists after the BMU is replaced, replace the
battery pack.
3. If the alarm persists, export logs and contact technical
support.
4 1 The BMU is faulty. 1. Replace the BMU, run the new BMU, and check whether the
alarm persists.
2. If the alarm persists after the BMU is replaced, export logs
and contact technical support.
5 1 The battery pack fuse
temperature detection
NTC is faulty, the
temperature sampling
cable is disconnected,
the battery pack fuse
temperature detection
connector is loose, or the
BMU is faulty.
1. Remove and reinstall the J3 connector (4 -pin) to the BMU
and check whether the alarm persists. If yes, replace the BMU.
2. If the alarm persists after the BMU is replaced, replace the
fuse temperature sampling cable harness.
3. If the alarm persists after the fuse temperature sampling
cable harness connected to the J3 connector (4 -pin) on the
BMU is replaced, replace the battery pack.
6 1 The positive and
negative busbar
temperature detection
NTC is faulty, the
temperature sampling
1. Remove and reinstall the J3 connector (4 -pin) to the BMU
and check whether the alarm persists. If yes, replace the BMU.
2. If the alarm persists after the BMU is replaced, replace the
positive and negative busbar temperature sampling cable
harnesses connected to the J3 connector (4-pin) on the BMU.

---

## PDF page 47

cables are disconnected,
the positive and negative
busbar temperature
detection connector is
loose, or the BMU is
faulty.
3. If the alarm persists after the positive and negative busbar
temperature sampling cable harnesses are replaced, replace
the battery pack.

---

## PDF page 48

### 1.3.3 3224 BMU Faulty
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3224 BMU Faulty Major Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally when a minor fault occurs on the BMU. In case of a
serious fault, the battery rack shuts down.
Possible Causes and Procedure
Reason
ID
No. Possible Cause Suggestion
1 1 The EEPROM of the
BMU is faulty.
1. Replace the BMU, run the new BMU, and check whether the
alarm persists.
2. If the alarm persists after the BMU is replaced, export logs
and contact technical support.
2 1 An internal fault has
occurred in the BMU.
1. Replace the BMU, run the new BMU, and check whether the
alarm persists.
2. If the alarm persists after the BMU is replaced, export logs
and contact technical support.
3 1 An internal fault has
occurred in the BMU.
1. Replace the BMU, run the new BMU, and check whether the
alarm persists.
2. If the alarm persists after the BMU is replaced, export logs
and contact technical support.
4 1 An internal fault has
occurred in the BMU.
1. Replace the BMU, run the new BMU, and check whether the
alarm persists.
2. If the alarm persists after the BMU is replaced, export logs
and contact technical support.
5 1 An internal fault has
occurred in the BMU.
1. Replace the BMU, run the new BMU, and check whether the
alarm persists.
2. If the alarm persists after the BMU is replaced, export logs
and contact technical support.
6 1 An internal fault has
occurred in the BMU.
1. Replace the BMU, run the new BMU, and check whether the
alarm persists.
2. If the alarm persists after the BMU is replaced, export logs
and contact technical support.
7 1 An internal fault has
occurred in the BMU.
1. Replace the BMU, run the new BMU, and check whether the
alarm persists.
2. If the alarm persists after the BMU is replaced, export logs
and contact technical support.
8 1 An internal fault has
occurred in the BMU.
1. Replace the BMU, run the new BMU, and check whether the
alarm persists.
2. If the alarm persists after the BMU is replaced, export logs

---

## PDF page 49

and contact technical support.
9 1 An internal fault has
occurred in the BMU.
1. Replace the BMU, run the new BMU, and check whether the
alarm persists.
2. If the alarm persists after the BMU is replaced, export logs
and contact technical support.
10 1 The BMU detects that
the MOS of the
balancing circuit is faulty.
1. Replace the BMU, run the new BMU, and check whether the
alarm persists.
2. If the alarm persists after the BMU is replaced, export logs
and contact technical support.

---

## PDF page 50

### 1.3.4 3226 Disconnection Between BMUs
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3226 Disconnection Between BMUs Minor Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally. If the alarm spreads, the battery rack may shut down.
Possible Causes and Procedure
Reason
ID
No. Possible Cause Suggestion
1 1 The communication is
disconnected or a BMU
is faulty.
1. Check whether the BMU communications cable is loose,
disconnected, or incorrectly connected. If yes, reconnect the
cable.
2. If the alarm persists, export logs and contact technical
support.

### 1.3.5 3229 BMU Communication Failure
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3229 BMU Communication Failure Major Communications
alarm
ADAC
### Impact on the System
The battery rack shuts down.
Possible Causes and Procedure
Reason
ID
No. Possible Cause Suggestion
1 1 1. The communications
cable is not properly
connected. 2. The
communication failed
because the BMU is
faulty.
1. Check whether the communications cable between the
COM-IN/COM-OUT port on the pack and the
CON_IN/CON_OUT port on the RCM is loose, disconnected,
or incorrectly connected. If yes, rectify the fault.
2. If the alarm persists, replace the BMU.

---

## PDF page 51

### 1.3.6 3351 Inconsistent BCU Software Versions
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3351 Inconsistent BCU Software
Versions
Minor Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally, but some value-added features may be unavailable.
Possible Causes and Procedure
Reason
ID
No. Possible Cause Suggestion
1 1 The software version of
the BCU is inconsistent
with the system software
package.
1. If the component version is inconsistent with the system
software package version due to a manual update failure, the
system running is not affected. You are advised to perform the
update at a proper time.
2. If the version is inconsistent with the system software
package version due to component replacement, perform a
manual update.
3. If the update fails for several times, contact technical
support.

### 1.3.7 3352 Abnormal Total Voltage of Battery Rack
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3352 Abnormal Total Voltage of Battery
Rack
Major Equipment
alarm
ADMC
### Impact on the System
The battery rack shuts down.
Possible Causes and Procedure
Reason
ID
No. Possible Cause Suggestion
1 1 The detected total
voltage of the battery
rack is incorrect.
1. Clear the alarm on the user interface.
2. Check whether the number of battery packs configured on the
user interface is consistent with the number of battery packs
installed onsite.
3. If the alarm 3373 -1 "Battery Pack Sampling Abnormal" is
generated, handle it first.
4. If the alarm persists, export logs and contact technical support.

---

## PDF page 52

### 1.3.8 3353 Total Voltage of Battery Rack and Total Cell Voltage
Inconsistent
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3353 Total Voltage of Battery Rack and
Total Cell Voltage Inconsistent
Major Equipment
alarm
ADMC
### Impact on the System
The battery rack shuts down.
Possible Causes and Procedure
Reason
ID
No. Possible Cause Suggestion
1 1 The detected total
voltage of the battery
rack is incorrect.
1. If the alarm 3373-1 "Battery Pack Sampling Abnormal", 3360
"RPCB Communication Failure", or 3307-14 "RPCB Abnormal"
is generated, handle it first.
2. If not, check whether the number of battery packs installed in
the rack is correct.
3. After the check is complete, clear the alarm on the user
interface.
4. If the alarm persists, export logs and contact technical
support.

### 1.3.9 3354 Battery Pack Mixed Use Failed
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3354 Battery Pack Mixed Use Failed Major Equipment
alarm
ADAC
### Impact on the System
The battery rack shuts down.
Possible Causes and Procedure
Reason
ID
No. Possible Cause Suggestion
1 1 Different models of
battery packs are used
together.
Replace battery packs to ensure that all battery packs are of
the same model. If the alarm persists, export logs and contact
technical support.

---

## PDF page 53

### 1.3.10 3355 BCU Chip Overtemperature
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3355 BCU Chip Overtemperature Minor Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally. Continuous overtemperature may cause the battery rack
to shut down.
Possible Causes and Procedure
Reason
ID
No. Possible Cause Suggestion
1 1 The internal circuit is
faulty.
1. Reset the system on the user interface. If the alarm is
cleared, no further action is required.
2. If the alarm persists, replace the BCU. (If the BCU cannot be
replaced independently, replace the RCM.) If the alarm
persists, export logs and contact technical support.

---

## PDF page 54

### 1.3.11 3356 BCU Internal Exception
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3356 BCU Internal Exception Major Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally when a minor fault occurs on the BCU. In case of a
serious fault, the battery rack shuts down.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The internal power
supply circuit is faulty.
1. Reset the system on the user interface. If the alarm is
cleared, no further action is required.
2. If the alarm persists, replace the BCU. (If the BCU cannot be
replaced independently, replace the RCM.)
2 1 The internal power
supply circuit is faulty.
1. Reset the system on the user interface. If the alarm is
cleared, no further action is required.
2. If the alarm persists, replace the BCU. (If the BCU cannot be
replaced independently, replace the RCM.)
3 1 The internal sampling
circuit is faulty.
1. Reset the system on the user interface. If the alarm is
cleared, no further action is required.
2. If the alarm persists, replace the BCU. (If the BCU cannot be
replaced independently, replace the RCM.)
4 1 The internal sampling
circuit is faulty.
1. Reset the system on the user interface. If the alarm is
cleared, no further action is required.
2. If the alarm persists, replace the BCU. (If the BCU cannot be
replaced independently, replace the RCM.)
5 1 The chip or program is
faulty.
1. Reset the system on the user interface. If the alarm is
cleared, no further action is required.
2. If the alarm persists, update the ESS software to the latest
version on the user interface. If the alarm is cleared after the
update, no further action is required.
3. If the alarm persists after the software update, replace the
BCU. (If the BCU cannot be replaced independently, replace
the RCM.)

---

## PDF page 55

### 1.3.12 3357 Balancing Module Software Versions Inconsistent
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3357 Balancing Module Software
Versions Inconsistent
Minor Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally, but some value-added features may be unavailable.
Possible Causes and Procedure
Reason
ID
No. Possible Cause Suggestion
1 1 The software version of
the balancing module is
inconsistent with the
system software
package.
1. If the component version is inconsistent with the system
software package version due to a manual update failure, the
system running is not affected. You are advised to perform the
update at a proper time.
2. If the version is inconsistent with the system software
package version due to component replacement, perform a
manual update.
3. If the update fails for several times, contact technical
support.

---

## PDF page 56

### 1.3.13 3358 BCU Auxiliary Power Abnormal
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3358 BCU Auxiliary Power Abnormal Major Equipment
alarm
ADMC
### Impact on the System
The sensor power supply is abnormal. If multiple power supplies are abnormal at the same time, the battery
rack may shut down.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 1. The power supply circuit
is faulty.
2. A short circuit has
occurred due to a sensor
fault.
1. Remove the connector from the COM2/12 V port (all
sensors are disconnected), reset or restart the BCU, and
check whether the alarm is cleared.
2. If the alarm persists, replace the BCU.
3. If the alarm is cleared, connect the cable harnesses
and sensors one by one to locate the faulty cable
harness or sensor. Replace the faulty cable harness or
sensor (T/H sensor or CO sensor).
2 1 1. The power supply circuit
is faulty.
2. A short circuit has
occurred due to a sensor
fault.
1. Remove the connectors from the COM1/12V port and
COM3/12V port (all sensors are disconnected), reset or
restart the BCU, and check whether the alarm is cleared.
2. If the alarm persists, replace the BCU. (If the BCU
cannot be replaced independently, replace the RCM.)
3. If the alarm is cleared, connect the cable harnesses
and sensors one by one to locate the faulty cable
harness or sensor. Replace the faulty cable harness or
sensor (T/H sensor or CO sensor).
3 1 1. The power supply circuit
is faulty.
2. A short circuit has
occurred due to an alarm
beacon fault.
1. Check whether the alarm beacon is faulty. If yes,
replace the alarm beacon. If not, replace the BCU.
4 1 1. The power supply circuit
is faulty.2. An external
short circuit has occurred.
1. Check whether an external short circuit has occurred.
If yes, rectify the short circuit. If not, replace the BCU.
5 1 1. The power cable
harness is not properly
connected.
2. The BCU or RCM is
faulty.
1. Power off the ESS by referring to the user manual.
Remove the BAT+ or BAT– cable on the RCM panel and
reinstall it, and then power on the ESS by referring to
the user manual. After the RCM is reset, check whether
the alarm is cleared.
2. If the alarm persists, remove the BCU and check
whether the power cable harness is properly connected
to the DC_IN port on the rear panel of the BCU. If not,
remove and reinstall the power cable harness.

---

## PDF page 57

3. If the alarm persists, replace the BCU.
4. If the alarm persists, replace the RCM.

---

## PDF page 58

### 1.3.14 3359 BCU Memory Abnormal
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3359 BCU Memory Abnormal Minor Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally, but data such as alarms and performance data cannot
be recorded.
Possible Causes and Procedure
Reason
ID
No. Possible Cause Suggestion
1 1 1. The storage space is
insufficient
2. The memory is faulty.
Replace the BCU. (If the BCU cannot be replaced
independently, replace the RCM.) If the alarm persists, export
logs and contact technical support.
2 1 The EEPROM of the
BCU is faulty.
Replace the BCU. (If the BCU cannot be replaced
independently, replace the RCM.) If the alarm persists, export
logs and contact technical support.

### 1.3.15 3360 RPCB Communication Failure
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3360 RPCB Communication Failure Major Communications
alarm
ADAC
### Impact on the System
The battery rack shuts down.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The communications
cable is disconnected.
1. Power off the ESS by referring to the user manual.
2. Check whether the wiring terminal between the RPCB and
the BCU is loose, disconnected, or incorrectly connected.
3. If the alarm persists, replace the RCM.
4. If the alarm persists, export logs and contact technical
support.

---

## PDF page 59

### 1.3.16 3361 DCDC Communication Failure
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3361 DCDC Communication Failure Major Communications
alarm
ADAC
### Impact on the System
The battery rack shuts down.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The communications
cable is disconnected.
Check whether the cable connections of the DCDC,PCS
communication port and the CON4 port of the RCM are loose,
disconnected, or incorrectly connected. If yes, reconnect the
cables. If not, export logs and contact technical support.

### 1.3.17 3362 PCS Communication Failure
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3362 PCS Communication Failure Major Communications
alarm
ADAC
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The communications
cable is disconnected.
Check whether the cable connections of the PCS
communication port, J9 communication port of RPCB, and the
CON3 and CON4 ports of the RCM are loose, disconnected, or
incorrectly connected. If yes, reconnect the cables. If not,
contact technical support.
2 1 The communications
cable is disconnected.
Check whether the cable connections of the PCS
communication port and the CON3 port of the RCM are loose,
disconnected, or incorrectly connected. If yes, reconnect the
cables. If not, export logs and contact technical support.

---

## PDF page 60

### 1.3.18 3363 Balancing Module Communication Failure
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3363 Balancing Module Communication
Failure
Minor Communications
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally, but active balancing stops.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The communications
cable is disconnected.
1. Check whether the communications cable between the
COM-IN/COM-OUT port on the pack where the balancing
module is located and the CON_IN/CON_OUT port on the
RCM is loose, disconnected, or incorrectly connected. If yes,
rectify the fault.
2. Check whether the cables between all packs in the rack are
loose, disconnected, or incorrectly connected. If yes, reconnect
the cables.
3. Check whether the screws on the front panel of the pack are
tightened to a torque of 1.6 N·m.
4. After the fault is rectified, click "Activate balancing module"
on the user interface. Wait for 1 minute and check whether the
alarm is automatically cleared.
5. If the alarm persists, export logs and contact technical
support.

---

## PDF page 61

### 1.3.19 3369 ESS SOH Calibration
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3369 ESS SOH Calibration Warning Equipment
alarm
ADAC
### Impact on the System
During the calibration, the ESS cannot respond to normal power scheduling.
Possible Causes and Procedure
Reason
ID
No. Possible Cause Suggestion
1 1 ESS SOH calibration is
in progress.
1. The SOH calibration in the ESS is in progress. During the
calibration, the end -of-charge/discharge SOC settings will be
overridden to preferentially charge the battery rack to the full
capacity during the charge process and preferentially discharge
the full capacity of the battery rack during the discharge
process. Then, the battery capacity will be calculated. The
charge and discharge response will be affected during the
calibration.
2. If you do not want to affect the charge and discharge
functions, disable "Automatic SOH calibration" and enable it at
a proper time.
3. During SOH calibration, you are advised to wait for 30 to 60
minutes after the system is fully charged and after the
discharge is complete if you want to manually send a switching
command.
2 1 SOH calibration has not
been performed for the
ESS for a long time.
1. The SOH calibration in the ESS will be performed recently.
During the calibration, the end -of-charge/discharge SOC
settings will be overridden to preferentially charge the battery
rack to the full capacity during the charge process and
preferentially discharge the full capacity of the battery rack
during the discharge process. Then, the battery capacity will be
calculated. The charge and discharge response will be affected
during the calibration.
2. If you do not want to affect the charge and discharge
functions, disable "Automatic SOH calibration" and enable it at
a proper time.
3. During SOH calibration, you are advised to wait for 30 to 60
minutes after the system is fully charged and after the
discharge is complete if you want to manually send a switching
command.

---

## PDF page 62

### 1.3.20 3371 Battery Rack Voltage Exceeding Threshold
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3371 Battery Rack Voltage Exceeding
Threshold
Major Equipment
alarm
ADAC
### Impact on the System
When the threshold is slightly exceeded, charge/discharge stops. When the threshold is seriously exceeded,
the battery rack shuts down.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The detected total
voltage of the battery
rack is high.
1. Check that the ESS is not charged. Wait for 30 minutes and
check whether the alarm is cleared.
2. If the alarm persists, shut down the ESS on the user
interface.
3. Wait for 5 minutes.
4. Start the ESS on the user interface.
5. If the alarm persists, handle the battery pack and cell
overvoltage alarms first.
6. If the alarm persists, export logs and contact technical
support.
2 1 The detected total
voltage of the battery
rack is too high.
1. Check that the ESS is not charged. Wait for 30 minutes and
check whether the alarm is cleared.
2. If the alarm persists, shut down the ESS on the user
interface.
3. Wait for 5 minutes.
4. Start the ESS on the user interface.
5. If the alarm persists, handle the battery pack and cell
overvoltage alarms first.
6. If the alarm persists, contact technical support.
3 1 The detected total
voltage of the battery
rack is far too high.
1. Check that the ESS is not charged. Wait for 30 minutes and
check whether the alarm is cleared.
2. If the alarm persists, shut down the ESS on the user
interface.
3. Wait for 5 minutes.
4. Start the ESS on the user interface.
5. If the alarm persists, handle the battery pack and cell
overvoltage alarms first.
6. If the alarm persists, contact technical support.
4 1 Battery Rack
Undervoltage 1
1. Check that the ESS does not discharge. Wait for 30 minutes
and check whether the alarm is cleared.
2. If the alarm persists, connect to the power grid and charge

---

## PDF page 63

the ESS within 48 hours.
3. If the alarm persists after the batteries are charged for 1
hour, contact technical support.
5 1 Battery Rack
Undervoltage 2
1. Check that the ESS does not discharge. Wait for 30 minutes
and check whether the alarm is cleared.
2. If the alarm persists, connect to the power grid and charge
the ESS within 48 hours.
3. If the alarm persists after the batteries are charged for 1
hour, contact technical support.
6 1 Battery Rack
Undervoltage 3
1. Check that the ESS does not discharge. Wait for 30 minutes
and check whether the alarm is cleared.
2. If the alarm persists, connect to the power grid and charge
the ESS within 48 hours.
3. If the alarm persists after the batteries are charged for 1
hour, contact technical support.

---

## PDF page 64

### 1.3.21 3373 Battery Pack Sampling Abnormal
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3373 Battery Pack Sampling Abnormal Major Equipment
alarm
ADMC
### Impact on the System
The battery rack shuts down.
Possible Causes and Procedure
Reason
ID
No. Possible Cause Suggestion
1 1 The internal circuit or
cable harness of the
BMU is faulty.
1. Replace the BMU and clear the alarm on the alarm
management interface.
2. If the alarm persists, export logs and contact technical
support.
2 1 The internal circuit or
cable harness of the
BMU is faulty.
1. Replace the BMU and clear the alarm on the alarm
management interface.
2. If the alarm persists, export logs and contact technical
support.
3 1 The internal circuit or
cable harness of the
BMU is faulty.
1. Check whether the interconnection terminal of the BMU is
loose.
2. If the alarm persists, replace the BMU and clear the alarm on
the alarm management interface.
3. If the alarm persists, export logs and contact technical
support.
4 1 The internal circuit or
cable harness of the
BMU is faulty.
1. Check whether the interconnection terminal of the BMU is
loose.
2. If the alarm persists, replace the BMU and clear the alarm on
the alarm management interface.
3. If the alarm persists, export logs and contact technical
support.
5 1 An NTC open circuit or
short circuit fault occurs
inside the BMU.
1. Check whether the interconnection terminal of the BMU is
loose.
2. If the alarm persists, replace the BMU and clear the alarm on
the alarm management interface.
3. If the alarm persists, export logs and contact technical
support.

---

## PDF page 65

### 1.3.22 3375 Battery Voltage Inconsistent
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3375 Battery Voltage Inconsistent Major Equipment
alarm
ADAC
### Impact on the System
The battery rack may shut down.
Possible Causes and Procedure
Reason
ID
No. Possible Cause Suggestion
1 1 1. The cell inconsistency is
severe or passive balancing
fails.
2. A battery pack is replaced
in the battery rack, but the
balancing is not complete.
1. If a battery pack is replaced, the alarm is automatically
cleared after the balancing is complete.
2. Check whether the balancing module is faulty. If yes,
rectify the fault according to the handling suggestions.
3. Restart the ESS. If the alarm persists, export logs and
contact technical support.
2 1 1. The cell inconsistency is
severe or passive balancing
fails.
2. A battery pack is replaced
in the battery rack, but the
balancing is not complete.
1. If a battery pack is replaced, the alarm is automatically
cleared after the balancing is complete.
2. Check whether the balancing module is faulty. If yes,
rectify the fault according to the handling suggestions.
3. Restart the ESS. If the alarm persists, export logs and
contact technical support.
3 1 1. The cell inconsistency is
severe or passive balancing
fails.
2. A battery pack is replaced
in the battery rack, but the
balancing is not complete.
Restart the ESS. If the alarm persists, export logs and
contact technical support.
4 1 1. The cell inconsistency is
severe or passive balancing
fails.
2. A battery pack is replaced
in the battery rack, but the
balancing is not complete.
1. If a battery pack is replaced, the alarm is automatically
cleared after the balancing is complete.
2. Check whether the balancing module is faulty. If yes,
rectify the fault according to the handling suggestions.
3. Restart the ESS. If the alarm persists, export logs and
contact technical support.
5 1 1. The cell inconsistency is
severe or passive balancing
fails.
2. A battery pack is replaced
in the battery rack, but the
balancing is not complete.
1. If a battery pack is replaced, the alarm is automatically
cleared after the balancing is complete.
2. Check whether the balancing module is faulty. If yes,
rectify the fault according to the handling suggestions.
3. Restart the ESS. If the alarm persists, export logs and
contact technical support.
6 1 1. The cell inconsistency is
severe or passive balancing
fails.
Restart the ESS. If the alarm persists, export logs and
contact technical support.

---

## PDF page 66

2. A battery pack is replaced
in the battery rack, but the
balancing is not complete.
7 1 1. The battery pack
inconsistency is severe.
2. The battery pack
balancing module is faulty.
3. A battery pack is replaced
in the battery rack, but the
balancing is not complete.
1. If a battery pack is replaced, the alarm is automatically
cleared after the balancing is complete.
2. Check whether the balancing module is faulty. If yes,
rectify the fault according to the handling suggestions.
3. Restart the ESS. If the alarm persists, export logs and
contact technical support.
8 1 1. The battery pack
inconsistency is severe.
2. The battery pack
balancing module is faulty.
3. A battery pack is replaced
in the battery rack, but the
balancing is not complete.
1. If a battery pack is replaced, the alarm is automatically
cleared after the balancing is complete.
2. Check whether the balancing module is faulty. If yes,
rectify the fault according to the handling suggestions.
3. Restart the ESS. If the alarm persists, export logs and
contact technical support.
9 1 1. The battery pack
inconsistency is severe.
2. The battery pack
balancing module is faulty
3. A battery pack is replaced
in the battery rack, but the
balancing is not complete.
Restart the ESS. If the alarm persists, export logs and
contact technical support.
10 1 1. The battery pack
inconsistency is severe.
2. The battery pack
balancing module is faulty.
3. A battery pack is replaced
in the battery rack, but the
balancing is not complete.
1. If a battery pack is replaced, the alarm is automatically
cleared after the balancing is complete.
2. Check whether the balancing module is faulty. If yes,
rectify the fault according to the handling suggestions.
3. Restart the ESS. If the alarm persists, export logs and
contact technical support.
11 1 1. The battery pack
inconsistency is severe.
2. The battery pack
balancing module is faulty.
3. A battery pack is replaced
in the battery rack, but the
balancing is not complete.
1. If a battery pack is replaced, the alarm is automatically
cleared after the balancing is complete.
2. Check whether the balancing module is faulty. If yes,
rectify the fault according to the handling suggestions.
3. Restart the ESS. If the alarm persists, export logs and
contact technical support.
12 1 1. The battery pack
inconsistency is severe.
2. The battery pack
balancing module is faulty.
3. A battery pack is replaced
in the battery rack, but the
balancing is not complete.
Restart the ESS. If the alarm persists, export logs and
contact technical support.

---

## PDF page 67

### 1.3.23 3376 Battery Temperature Inconsistent
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3376 Battery Temperature Inconsistent Major Equipment
alarm
ADAC
### Impact on the System
When the temperature deviation is minor, charge/discharge stops. If the deviation is severe, the battery rack
shuts down.
Possible Causes and Procedure
Reason
ID
No. Possible Cause Suggestion
1 1 1. The cell inconsistency
is severe.
2. The cell temperature
sampling is abnormal.
1. Wait for 30 minutes and check whether the alarm is cleared.
2. If the alarm persists, handle the LTMS and BMU
temperature sampling exception alarms first.
3. If the alarm persists, export logs and contact technical
support.
2 1 1. The cell inconsistency
is severe.
2. The cell temperature
sampling is abnormal.
1. Wait for 30 minutes and check whether the alarm is cleared.
2. If the alarm persists, handle the LTMS and BMU
temperature sampling exception alarms first.
3. If the alarm persists, export logs and contact technical
support.
3 1 1. The cell inconsistency
is severe.
2. The cell temperature
sampling is abnormal.
1. Wait for 30 minutes and check whether the alarm is cleared.
2. If the alarm persists, handle the LTMS and BMU
temperature sampling exception alarms first.
3. If the alarm persists, export logs and contact technical
support.
4 1 1. The cell inconsistency
is severe.
2. The cell temperature
sampling is abnormal.
1. Wait for 30 minutes and check whether the alarm is cleared.
2. If the alarm persists, handle the LTMS and BMU
temperature sampling exception alarms first.
3. If the alarm persists, export logs and contact technical
support.
5 1 1. The cell inconsistency
is severe.
2. The cell temperature
sampling is abnormal.
1. Wait for 30 minutes and check whether the alarm is cleared.
2. If the alarm persists, handle the LTMS and BMU
temperature sampling exception alarms first.
3. If the alarm persists, export logs and contact technical
support.
6 1 1. The cell inconsistency
is severe.
2. The cell temperature
sampling is abnormal.
1. Wait for 30 minutes and check whether the alarm is cleared.
2. If the alarm persists, handle the LTMS and BMU
temperature sampling exception alarms first.
3. If the alarm persists, export logs and contact technical
support.

---

## PDF page 68

## 1.4 RCM (RPCB)
### 1.4.1 3300 RPCB Voltage Abnormal
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3300 RPCB Voltage Abnormal Major Equipment
alarm
ADAC
### Impact on the System
The system is shut down.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 Overvoltage occurs on
the battery.
1. Ensure that the ESS is shut down.
2. After 5 minutes, start the ESS on the user interface and
check whether the alarm is cleared.
3. If the alarm persists, export logs and contact technical
support.
2 1 Undervoltage occurs on
the battery.
1. Ensure that the ESS is shut down.
2. Check whether the RCM has a disconnector. If not, skip this
step. If there is a disconnector, check whether it is turned on. If
not, turn it on.
3. After 5 minutes, start the ESS on the user interface and
check whether the alarm is cleared.
4. If the alarm persists, connect to the power grid and charge
the ESS within 48 hours.
5. If the alarm persists after the ESS is charged for 1 hour,
export logs and contact technical support.
3 1 1. The bus or battery
voltage sampling circuit
fails. 2. The sampling is
interfered or the
calculation is abnormal.
1. Power off the ESS by referring to the user manual. Remove
the BAT+ or BAT– cable on the RCM panel, wait for 5 minutes,
and then power on the ESS by referring to the user manual.
After the RCM restarts, check whether the alarm is cleared.
2. If the alarm persists, replace the RCM by referring to the
maintenance manual.
3. If the alarm persists, export logs and contact technical
support.

---

## PDF page 69

### 1.4.2 3301 RPCB Port Short-Circuited
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3301 RPCB Port Short-Circuited Major Equipment
alarm
ADAC
### Impact on the System
The system is shut down.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The PCS/DCDC is
damaged or short -
circuited, or the RCM is
short-circuited.
1. Power off the ESS by referring to the user manual, remove
the BAT+ or BAT – cable on the RCM panel, and remove the
power cables between the RCM and the PCS.
2. Use a multimeter to check whether the removed positive and
negative power cables are short-circuited. If yes, replace them.
3. Use a multimeter to check whether the BUS+/ – terminals on
the right of the RCM are short -circuited. If yes, replace the
RCM by referring to the maintenance manual.
4. Use a multimeter to check whether the output BUS+/ –
terminals of the PCS are short -circuited. If yes, replace the
PCS by referring to the maintenance manual.
5. If the alarm persists, export logs and contact technical
support.
2 1 The PCS/DCDC is
damaged or short -
circuited, or the RCM is
short-circuited.
1. Power off the ESS by referring to the user manual, and
remove the BAT+ or BAT– cable on the RCM panel.
2. Use a multimeter to check whether the BAT+/ – terminals of
the RCM are short -circuited. If yes, replace the RCM by
referring to the maintenance manual.
3. If the alarm persists, export logs and contact technical
support.

---

## PDF page 70

### 1.4.3 3302 Internal RPCB Temperature Abnormal
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3302 Internal RPCB Temperature
Abnormal
Major Equipment
alarm
ADAC
### Impact on the System
The system is shut down.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The output is
overloaded.
1. Check whether output overcurrent protection or an
overcurrent fault occurs in the ESS. The overtemperature
alarm is automatically cleared after the system temperature is
restored to the normal range.
2. If the alarm persists, replace the RCM by referring to the
maintenance manual.
3. If the alarm persists, export logs and contact technical
support.
2 1 The heat dissipation fan
is faulty.
1. Check whether output overcurrent protection or an
overcurrent fault occurs in the ESS. The overtemperature
alarm is automatically cleared after the system temperature is
restored to the normal range.
2. If the alarm persists, replace the RCM by referring to the
maintenance manual.
3. If the alarm persists, export logs and contact technical
support.
3 1 The wiring terminal on
the bus side is
improperly connected.
1. Power off the ESS by referring to the user manual. Check
whether the BUS+/ – power terminals on the right of the RCM
are securely connected. If the terminals are loose, secure
them.
2. Power on the ESS by referring to the user manual. After the
RCM restarts, check whether the alarm is cleared.
3. If the alarm persists, replace the RCM by referring to the
maintenance manual.
4. If the alarm persists, export logs and contact technical
support.
4 1 The wiring terminal on
the battery side is
improperly connected.
1. Power off the ESS by referring to the user manual. Check
whether the BAT+/ – power terminals on the right of the RCM
are securely connected. If the terminals are loose, secure
them.
2. Power on the ESS by referring to the user manual. After the
RCM restarts, check whether the alarm is cleared.
3. If the alarm persists, replace the RCM by referring to the
maintenance manual.

---

## PDF page 71

4. If the alarm persists, export logs and contact technical
support.
5 1 The output is
overloaded. The heat
dissipation fan is faulty.
1. Check whether output overcurrent protection or an
overcurrent fault occurs in the ESS. The overtemperature
alarm is automatically cleared after the system temperature is
restored to the normal range.
2. If the alarm persists, replace the RCM by referring to the
maintenance manual.
3. If the alarm persists, export logs and contact technical
support.
6 1 The NTC sensor is short-
circuited or open -
circuited.
1. Power off the ESS by referring to the user manual. Remove
the BAT+ or BAT– cable on the RCM panel, wait for 5 minutes,
and then power on the ESS by referring to the user manual.
After the RCM restarts, check whether the alarm is cleared.
2. If the alarm persists, replace the RCM by referring to the
maintenance manual.
3. If the alarm persists, export logs and contact technical
support.

---

## PDF page 72

### 1.4.4 3303 RPCB Overcurrent Fault
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3303 RPCB Overcurrent Fault Major Equipment
alarm
ADMC
### Impact on the System
The system is shut down.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 Overload occurs during
battery charging or
discharging.
1. Arrange manual site visits to check whether the devices and
power cables are normal.
2. If no exception occurs, wait for 5 minutes and clear the alarm
on the user interface.
3. If the alarm persists, export logs and contact technical
support.
2 1 Overload occurs during
battery discharging.
1. Check whether the devices and power cables are normal.
2. If no exception occurs, wait for 5 minutes and clear the alarm
on the user interface.
3. If the alarm persists, export logs and contact technical
support.
3 1 Overload occurs during
battery charging.
1. Check whether the devices and power cables are normal.
2. If no exception occurs, wait for 5 minutes and clear the alarm
on the user interface.
3. If the alarm persists, export logs and contact technical
support.

---

## PDF page 73

### 1.4.5 3304 Battery-Side ISO Insulation Detection Abnormal
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3304 Battery-Side ISO Insulation
Detection Abnormal
Major Equipment
alarm
ADAC
### Impact on the System
The system is shut down.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The battery side is short -
circuited to the ground,
or the battery is in a
humid environment and
the insulation between
the circuit and ground is
poor.
1. Power off the ESS by referring to the user manual. Check
whether the PE cable of the device is correctly connected
according to the maintenance manual.
2. Check whether the system enclosure and PE cable are
damaged. If they are damaged, replace them.
3. Power on the ESS by referring to the user manual. After the
RCM restarts, check whether the alarm is cleared.
4. If the alarm persists, export logs and contact technical
support.

---

## PDF page 74

### 1.4.6 3305 RPCB Power Loop Abnormal
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3305 RPCB Power Loop Abnormal Major Equipment
alarm
ADAC
### Impact on the System
The system is shut down.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The battery input is in
reverse polarity.
1. Power off the ESS by referring to the user manual. Check
that the BAT+ and BAT – cables of the RCM are correctly
connected by referring to the maintenance manual.
2. Power on the ESS by referring to the user manual. After the
RCM restarts, check whether the alarm is cleared.
3. If the alarm persists, export logs and contact technical
support.
2 1 The cables on the bus
side are connected in
reverse polarity.
1. Power off the ESS by referring to the user manual. Check
that the BUS+ and BUS – cables of the RCM are correctly
connected by referring to the maintenance manual.
2. Power on the ESS by referring to the user manual. After the
RCM restarts, check whether the alarm is cleared.
3. If the alarm persists, export logs and contact technical
support.
3 1 Overload, a short circuit,
or a bus voltage
detection failure occurs.
1. Power off the ESS by referring to the user manual.
2. Use a multimeter to check whether the positive and negative
power cables on the RCM bus side are short -circuited. If yes,
replace the power cables.
3. Use a multimeter to check whether the BUS+/ – terminals on
the right of the RCM are short -circuited. If yes, replace the
RCM by referring to the maintenance manual.
4. After steps 2 and 3 are complete, power on the ESS by
referring to the user manual. After the RCM restarts, check
whether the alarm is cleared.
5. If the alarm persists, export logs and contact technical
support.
3 2 The communication is
abnormal or the
parameters delivered by
the BCU are invalid.
1. Power off the ESS and then power on the ESS by referring
to the user manual. After the RCM restarts, check whether the
alarm is cleared.
2. If the alarm persists, replace the RCM by referring to the
maintenance manual.
3. If the alarm persists, export logs and contact technical
support.

---

## PDF page 75

### 1.4.7 3306 RPCB Version Mismatch
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3306 RPCB Version Mismatch Major Equipment
alarm
ADAC
### Impact on the System
The system is shut down.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The software version is
incompatible with the
hardware version, or an
incorrect software
version is loaded.
1. Check the RCM model and SN, obtain the latest software
version through the service hotline, and perform the upgrade
again on the user interface.
2. If the alarm persists, export logs and contact technical
support.

---

## PDF page 76

### 1.4.8 3307 RPCB Abnormal
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3307 RPCB Abnormal Major Equipment
alarm
ADAC
### Impact on the System
The system is shut down.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The contactor is
damaged or stuck.
1. Shut down the ESS on the user interface. After 5 minutes,
start the ESS on the user interface and check whether the
alarm is cleared.
2. If the alarm persists, shut down the ESS on the user
interface, replace the corresponding RPCB. After the
replacement, restart the system and check whether the
alarm is cleared.
3. If the alarm persists, contact technical support.
2 1 The contactor is
damaged.
1. Shut down the ESS on the user interface. After 5 minutes,
start the ESS on the user interface and check whether the
alarm is cleared.
2. If the alarm persists, shut down the ESS on the user
interface and replace the corresponding RPCB. Restart the
system and check whether the alarm is cleared.
3. If the alarm persists, contact technical support.
3 1 The contactor is
damaged or the cable
connection is
abnormal.
1. Shut down the ESS on the user interface. After 5 minutes,
start the ESS on the user interface and check whether the
alarm is cleared.
2. If the alarm persists, shut down the ESS on the user
interface and replace the corresponding RPCB. Restart the
system and check whether the alarm is cleared.
3. If the alarm persists, contact technical support.
4 1 Both the AC and DC
auxiliary power
supplies are faulty.
1. Shut down the ESS on the user interface. After 5 minutes,
start the ESS on the user interface and check whether the
alarm is cleared.
2. If the alarm persists, shut down the ESS on the user
interface and replace the corresponding RPCB. Restart the
system and check whether the alarm is cleared.
3. If the alarm persists, contact technical support.
5 1 The auxiliary power is
faulty.
1. Shut down the ESS on the user interface. After 5 minutes,
start the ESS on the user interface and check whether the
alarm is cleared.
2. If the alarm persists, shut down the ESS on the user
interface and replace the corresponding RPCB. Restart the

---

## PDF page 77

system and check whether the alarm is cleared.
3. If the alarm persists, contact technical support.
6 1 Multiple soft-start faults
occur.
1. Shut down the ESS on the user interface. After 5 minutes,
start the ESS on the user interface and check whether the
alarm is cleared.
2. If the alarm persists, shut down the ESS on the user
interface and replace the corresponding RPCB. Restart the
system and check whether the alarm is cleared.
3. If the alarm persists, contact technical support.
7 1 The MCU is damaged
or the sampling circuit
is abnormal.
1. Shut down the ESS on the user interface. After 5 minutes,
start the ESS on the user interface and check whether the
alarm is cleared.
2. If the alarm persists, shut down the ESS on the user
interface and replace the corresponding RPCB. Restart the
system and check whether the alarm is cleared.
3. If the alarm persists, contact technical support.
8 1 The MCU is damaged
or the sampling circuit
is abnormal.
1. Shut down the ESS on the user interface. After 5 minutes,
start the ESS on the user interface and check whether the
alarm is cleared.
2. If the alarm persists, shut down the ESS on the user
interface and replace the corresponding RPCB. Restart the
system and check whether the alarm is cleared.
3. If the alarm persists, contact technical support.
9 1 The MCU is damaged. 1. Shut down the ESS on the user interface. After 5 minutes,
start the ESS on the user interface and check whether the
alarm is cleared.
2. If the alarm persists, shut down the ESS on the user
interface and replace the corresponding RPCB. Restart the
system and check whether the alarm is cleared.
3. If the alarm persists, contact technical support.
10 1 The EEPROM is faulty. 1. Shut down the ESS on the user interface. After 5 minutes,
start the ESS on the user interface and check whether the
alarm is cleared.
2. If the alarm persists, shut down the ESS on the user
interface and replace the corresponding RPCB. Restart the
system and check whether the alarm is cleared.
3. If the alarm persists, contact technical support.
11 1 The RCD circuit is
abnormal.
1. Shut down the ESS on the user interface. After 5 minutes,
start the ESS on the user interface and check whether the
alarm is cleared.
2. If the alarm persists, shut down the ESS on the user
interface and replace the corresponding RPCB. Restart the
system and check whether the alarm is cleared.
3. If the alarm persists, contact technical support.
12 1 The auxiliary power is
faulty.
1. Shut down the ESS on the user interface. After 5 minutes,
start the ESS on the user interface and check whether the
alarm is cleared.
2. If the alarm persists, shut down the ESS on the user
interface and replace the corresponding RPCB. Restart the

---

## PDF page 78

system and check whether the alarm is cleared.
3. If the alarm persists, contact technical support.
13 1 The black start button
is stuck.
1. Shut down the ESS on the user interface. After 5 minutes,
start the ESS on the user interface and check whether the
alarm is cleared.
2. If the alarm persists, shut down the ESS on the user
interface and replace the corresponding RPCB. Restart the
system and check whether the alarm is cleared.
3. If the alarm persists, contact technical support.
15 1 The interrupt usage is
too high.
1. Shut down the ESS on the user interface. After 5 minutes,
start the ESS on the user interface and check whether the
alarm is cleared.
2. If the alarm persists, shut down the ESS on the user
interface and replace the corresponding RPCB. Restart the
system and check whether the alarm is cleared.
3. If the alarm persists, contact technical support.
16 1 The chip is abnormal. 1. Shut down the ESS on the user interface. After 5 minutes,
start the ESS on the user interface and check whether the
alarm is cleared.
2. If the alarm persists, shut down the ESS on the user
interface and replace the corresponding RPCB. Restart the
system and check whether the alarm is cleared.
3. If the alarm persists, contact technical support.
17 1 EEPROM read data is
abnormal or damaged.
1. Shut down the ESS on the user interface. After 5 minutes,
start the ESS on the user interface and check whether the
alarm is cleared.
2. If the alarm persists, shut down the ESS on the user
interface and replace the corresponding RPCB. Restart the
system and check whether the alarm is cleared.
3. If the alarm persists, contact technical support.
18 1 EEPROM read data is
abnormal or damaged.
1. Shut down the ESS on the user interface. After 5 minutes,
start the ESS on the user interface and check whether the
alarm is cleared.
2. If the alarm persists, shut down the ESS on the user
interface and replace the corresponding RPCB. Restart the
system and check whether the alarm is cleared.
3. If the alarm persists, contact technical support.
19 1 Current sampling is
abnormal.
1. Shut down the ESS on the user interface. After 5 minutes,
start the ESS on the user interface and check whether the
alarm is cleared.
2. If the alarm persists, shut down the ESS on the user
interface and replace the corresponding RPCB. Restart the
system and check whether the alarm is cleared.
3. If the alarm persists, contact technical support.

---

## PDF page 79

### 1.4.9 3308 Battery RCD Protection Triggered
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3308 Battery RCD Protection Triggered Major Equipment
alarm
ADMC
### Impact on the System
The system is shut down.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The ground insulation
resistance on the battery
side decreases during
device operation.
1. Arrange manual site visits. Power off the ESS by referring to
the user manual.
2. Check whether battery leakage occurs and whether the PE
cable of the ESS is correctly connected as required in the user
manual. Check whether the enclosure of the ESS and the PE
cable are damaged. If yes, replace them.
3. Power on the ESS by referring to the user manual. After the
RCM restarts, check whether the alarm is cleared.
4. If the alarm persists, export logs and contact technical
support.

---

## PDF page 80

### 1.4.10 3309 RPCB Overcurrent Protection Triggered
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3309 RPCB Overcurrent Protection
Triggered
Major Equipment
alarm
ADAC
### Impact on the System
The system is shut down.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 Overload occurs during
battery discharging.
1. Shut down the ESS on the user interface.
2. After 5 minutes, start the ESS on the user interface and
check whether the alarm is cleared.
3. If the alarm persists, export logs and contact technical
support.
2 1 Overload occurs during
battery charging.
1. Shut down the ESS on the user interface.
2. After 5 minutes, start the ESS on the user interface and
check whether the alarm is cleared.
3. If the alarm persists, export logs and contact technical
support.

---

## PDF page 81

### 1.4.11 3310 RPCB Fan Alarm
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3310 RPCB Fan Alarm Minor Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally.
Possible Causes and Procedure
Reason
ID
No. Possible Cause Suggestion
1 1 The fan is damaged or
the cable connection is
abnormal.
1. If the system does not have other faults and can run
properly, ignore this alarm.
2. If the fault affects the use of the system, replace the RCM by
referring to the maintenance manual. Then, check whether the
alarm is cleared.
3. If the alarm persists, export logs and contact technical
support.

### 1.4.12 3311 RPCB SPD Faulty
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3311 RPCB SPD Faulty Minor Equipment
alarm
ADAC
### Impact on the System
The surge protection function of the RPCB fails, which does not affect the charging and discharging of the
system but may cause lightning strikes.
Possible Causes and Procedure
Reason
ID
No. Possible Cause Suggestion
1 1 The SPD is faulty. 1. Power off the ESS and then power on the ESS by referring
to the user manual. After the RCM restarts, check whether the
alarm is cleared.
2. If the alarm persists, replace the RCM by referring to the
maintenance manual.
3. If the alarm persists, export logs and contact technical
support.

---

## PDF page 82

### 1.4.13 3312 Battery-Side ISO Insulation Detection Alarm
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3312 Battery-Side ISO Insulation
Detection Alarm
Minor Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally.
Possible Causes and Procedure
Reason
ID
No. Possible Cause Suggestion
1 1 The PE cable on the
battery side is improperly
insulated.
1. Power off the ESS by referring to the user manual. Check
whether the PE cable of the device is correctly connected
according to the maintenance manual.
2. Check whether the system enclosure and PE cable are
damaged. If they are damaged, replace them.
3. Power on the ESS by referring to the user manual. After the
RCM restarts, check whether the alarm is cleared.
4. If the alarm persists, export logs and contact technical
support.

---

## PDF page 83

### 1.4.14 3313 Auxiliary Power Abnormal
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3313 Auxiliary Power Abnormal Minor Equipment
alarm
ADAC
### Impact on the System
The auxiliary power supply on the DC or AC side fails, which may affect system charging and discharging.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The AC auxiliary power
experiences
undervoltage.
1. Power off the ESS by referring to the user manual. Remove
the BAT+ or BAT– cable on the RCM panel, check whether the
AC power cable is loose, and reinstall the BAT+ or BAT– cable.
Then power on the ESS by referring to the user manual. After
the RCM restarts, check whether the alarm is cleared.
2. If the alarm persists, export logs and contact technical
support.
2 1 The DC auxiliary power
experiences
undervoltage.
1. Power off the ESS by referring to the user manual. Check
whether the DC power cable is loose. If there is a disconnector,
ensure that the disconnector is turned on. Then power on the
ESS by referring to the user manual. After the RCM restarts,
check whether the alarm is cleared.
2. If the alarm persists, export logs and contact technical
support.
3 1 Output undervoltage
occurs on the 12V OUT
port of the RCM.
1. Power off the ESS by referring to the user manual. Remove
the BAT+ or BAT– cable on the RCM panel and reinstall it, and
then power on the ESS by referring to the user manual. After
the RCM restarts, check whether the alarm is cleared.
2. If the alarm persists, export logs and contact technical
support.

---

## PDF page 84

### 1.4.15 3314 RPCB Overcurrent Alarm
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3314 RPCB Overcurrent Alarm Minor Equipment
alarm
ADAC
### Impact on the System
The charge and discharge are forbidden.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 Overload occurs during
battery charging.
1. Shut down the ESS on the user interface.
2. After 5 minutes, start the ESS on the user interface and
check whether the alarm is cleared.
3. If the alarm persists, export logs and contact technical
support.
2 1 Overload occurs during
battery discharging.
1. Shut down the ESS on the user interface.
2. After 5 minutes, start the ESS on the user interface and
check whether the alarm is cleared.
3. If the alarm persists, export logs and contact technical
support.

---

## PDF page 85

## 1.5 Power System (DCDC)
### 1.5.1 3400 DCDC Protection
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3400 DCDC Protection Major Equipment
alarm
ADAC
### Impact on the System
The system may be derated. When the fault is serious, the system shuts down.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 An exception occurs
in the module.
1. After the alarm is cleared, the device automatically recovers.
2. If the alarm persists, power off the ESS by referring to the user
manual.
3. After 5 minutes, power on the ESS by referring to the user
manual. If the alarm persists, export logs and contact technical
support.
2 1 1. The PCS DC bus
port is abnormal.
2. The bus port of the
module is abnormal.
1. Check whether an overcurrent alarm is generated for the PCS.
2. If yes, handle the PCS overcurrent alarm.
3. If not, power off the ESS by referring to the user manual. After
5 minutes, power on the ESS by referring to the user manual. If
the alarm persists, export logs and contact technical support.
3 1 1. The RCM bus port
is abnormal.
2. The battery port of
the module is
abnormal.
1. Check whether an overcurrent alarm is generated for the RCM.
2. If yes, handle the RCM overcurrent alarm.
3. If not, power off the ESS by referring to the user manual. After
5 minutes, power on the ESS by referring to the user manual. If
the alarm persists, export logs and contact technical support.
4 1 1. AC port
overvoltage occurs.
2. PCS DC bus
overvoltage occurs.
3. The module bus
voltage control is
abnormal.
1. Check whether the power grid voltage is within the allowed
range. If not, contact the local power operator.
2. Check whether a DC bus overvoltage alarm is generated for
the PCS.
3. If yes, handle the PCS DC bus overvoltage alarm.
4. If not, power off the ESS by referring to the user manual. After
5 minutes, power on the ESS by referring to the user manual. If
the alarm persists, export logs and contact technical support.
5 1 1. The PCS DC bus
voltage is abnormal.
2. The module bus
voltage control is
abnormal.
1. Check whether the power grid voltage is within the allowed
range. If not, contact the local power operator.
2. Check whether a DC bus undervoltage alarm is generated for
the PCS.
3. If yes, handle the PCS DC bus undervoltage alarm.
4. If not, power off the ESS by referring to the user manual. After
5 minutes, power on the ESS by referring to the user manual. If

---

## PDF page 86

the alarm persists, export logs and contact technical support.
6 1 The CAN
communications
cable between the
DCDC and BCU is
loose or damaged.
1. Power off the ESS by referring to the user manual. Check
whether the communications port on the DCDC is securely
connected and whether the CON4 communications port on the
BCU is securely connected.
2. After 5 minutes, power on the ESS by referring to the user
manual.
3. If the alarm persists, export logs and contact technical support.
7 1 The communications
link or PCS CAN is
abnormal.
1. Power off the ESS by referring to the user manual. Check
whether the communications port on the DCDC is securely
connected and whether the communications port on the PCS is
securely connected.
2. After 5 minutes, power on the ESS by referring to the user
manual.
3. If the alarm persists, export logs and contact technical support.
8 1 The battery pack
voltage is too high.
1. After the alarm is cleared, the device automatically recovers.
2. If the alarm persists, power off the ESS by referring to the user
manual.
3. After 5 minutes, power on the ESS by referring to the user
manual.
4. If the alarm persists, export logs and contact technical support.
9 1 The battery pack
voltage is too low.
1. Check whether an undervoltage alarm is generated for the
battery pack or RCM.
2. If yes, handle the pack or RCM undervoltage alarm.
3. If not, power off the ESS by referring to the user manual.
4. After 5 minutes, power on the ESS by referring to the user
manual.
5. If the alarm persists, export logs and contact technical support.
10 1 1. The RCM bus port
is abnormal.
2. The battery port of
the module is
abnormal.
1. Check whether an overcurrent alarm is generated for the RCM.
2. If yes, handle the RCM overcurrent alarm.
3. If not, power off the ESS by referring to the user manual. After
5 minutes, power on the ESS by referring to the user manual. If
the alarm persists, export logs and contact technical support.
11 1 An exception occurs
in the module.
1. After the alarm is cleared, the device automatically recovers.
2. If the alarm persists, power off the ESS by referring to the user
manual.
3. After 5 minutes, power on the ESS by referring to the user
manual. If the alarm persists, export logs and contact technical
support.

---

## PDF page 87

### 1.5.2 3401 DCDC Faulty
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3401 DCDC Faulty Major Equipment
alarm
ADAC
### Impact on the System
The system shuts down.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The drive circuit is faulty
or the bridge IGBT is
faulty.
1. Power off the ESS by referring to the user manual.
2. After 5 minutes, power on the ESS by referring to the user
manual.
3. If the alarm persists, export logs and contact technical
support.
2 1 The control system or
chip is faulty.
1. Power off the ESS by referring to the user manual.
2. After 5 minutes, power on the ESS by referring to the user
manual.
3. If the alarm persists, export logs and contact technical
support.
3 1 The auxiliary power
circuit does not work
properly.
1. Power off the ESS by referring to the user manual.
2. After 5 minutes, power on the ESS by referring to the user
manual.
3. If the alarm persists, export logs and contact technical
support.
4 1 The sampling link is
abnormal.
1. Power off the ESS by referring to the user manual.
2. After 5 minutes, power on the ESS by referring to the user
manual.
3. If the alarm persists, export logs and contact technical
support.
5 1 The EEPROM is faulty or
the I2C communication is
abnormal.
1. Power off the ESS by referring to the user manual.
2. After 5 minutes, power on the ESS by referring to the user
manual.
3. If the alarm persists, export logs and contact technical
support.
6 1 The IGBT module is
faulty.
1. Power off the ESS by referring to the user manual.
2. After 5 minutes, power on the ESS by referring to the user
manual.
3. If the alarm persists, export logs and contact technical
support.
7 1 1. The voltage on the
battery side or bus side
1. Power off the ESS by referring to the user manual.

---

## PDF page 88

goes beyond the module
startup range.
2. The number of battery
packs and battery
overvoltage/undervoltage
protection threshold are
not received from the
monitoring module.
3. The module relay is
not closed.
4. The voltage on the
bus side cannot be
increased during startup
on the battery side.
2. After 5 minutes, power on the ESS by referring to the user
manual. If the alarm persists, export logs and contact technical
support.
8 1 1. The fan is faulty.
2. The fan drive circuit is
faulty. 3. The fan
feedback signal is
abnormal.
1. Power off the ESS by referring to the user manual.
2. After 5 minutes, power on the ESS by referring to the user
manual.
3. If the alarm persists, export logs and contact technical
support.
9 1 The chip driver fails to be
initialized.
1. Power off the ESS by referring to the user manual.Constants
2. After 5 minutes, power on the ESS by referring to the user
manual.
3. If the alarm persists, export logs and contact technical
support.
10 1 The relay is
disconnected abnormally
during operation.
1. Power off the ESS by referring to the user manual.
2. After 5 minutes, power on the ESS by referring to the user
manual.
3. If the alarm persists, export logs and contact technical
support.

---

## PDF page 89

### 1.5.3 3402 Overvoltage Protection for DCDC Bus Port
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3402 Overvoltage Protection for DCDC
Bus Port
Major Equipment
alarm
ADAC
### Impact on the System
The system shuts down.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 1. AC port overvoltage
occurs.
2. PCS DC bus
overvoltage occurs.
3. The module bus
voltage control is
abnormal.
1. Check whether the power grid voltage is within the allowed
range. If not, contact the local power operator.
2. Check whether a DC bus overvoltage alarm is generated for
the PCS.
3. If yes, handle the PCS DC bus overvoltage alarm.
4. If not, power off the ESS by referring to the user manual.
After 5 minutes, power on the ESS by referring to the user
manual. If the alarm persists, export logs and contact technical
support.

### 1.5.4 3403 DCDC Overhumidity Protection
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3403 DCDC Overhumidity Protection Major Equipment
alarm
ADAC
### Impact on the System
The system shuts down.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The ambient humidity is
high.
1. After the alarm is cleared, the device automatically recovers.
2. If the alarm persists, power off the ESS by referring to the
user manual.
3. After 5 minutes, power on the ESS by referring to the user
manual. If the alarm persists, export logs and contact technical
support.

---

## PDF page 90

### 1.5.5 3404 DCDC Overtemperature Protection
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3404 DCDC Overtemperature Protection Major Equipment
alarm
ADAC
### Impact on the System
The system shuts down.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 1. The LTMS is
abnormal.
2. The heat dissipation of
the inductor inside the
module is abnormal.
1. Check whether an alarm is generated for the LTMS.
2. If yes, handle the LTMS alarm.
3. If not, power off the ESS by referring to the user manual.
After 5 minutes, power on the ESS by referring to the user
manual. If the alarm persists, export logs and contact technical
support.
2 1 1. The LTMS is
abnormal.
2. The screws on the
copper bar inside the
module are not tightened
or the heat dissipation is
abnormal.
1. Check whether an alarm is generated for the LTMS.
2. If yes, handle the LTMS alarm.
3. If not, power off the ESS by referring to the user manual.
After 5 minutes, power on the ESS by referring to the user
manual. If the alarm persists, export logs and contact technical
support.
3 1 1. The LTMS is
abnormal.
2. The heat dissipation of
the IGBT inside the
module is abnormal.
1. Check whether an alarm is generated for the LTMS.
2. If yes, handle the LTMS alarm.
3. If not, power off the ESS by referring to the user manual.
After 5 minutes, power on the ESS by referring to the user
manual. If the alarm persists, export logs and contact technical
support.
4 1 The LTMS is abnormal. 1. Check whether an alarm is generated for the LTMS.
2. If yes, handle the LTMS alarm.
3. If not, power off the ESS by referring to the user manual.
After 5 minutes, power on the ESS by referring to the user
manual. If the alarm persists, export logs and contact technical
support.
5 1 1. The LTMS is
abnormal.
2. The heat dissipation
inside the module is
abnormal.
1. Check whether an alarm is generated for the LTMS.
2. If yes, handle the LTMS alarm.
3. If not, power off the ESS by referring to the user manual.
After 5 minutes, power on the ESS by referring to the user
manual. If the alarm persists, export logs and contact technical
support.
6 1 1. The LTMS is
abnormal.
1. Check whether an alarm is generated for the LTMS.
2. If yes, handle the LTMS alarm.

---

## PDF page 91

2. The heat dissipation of
the through -current
terminal inside the
module is abnormal.
3. If not, power off the ESS by referring to the user manual.
After 5 minutes, power on the ESS by referring to the user
manual. If the alarm persists, export logs and contact technical
support.
7 1 1. The LTMS is
abnormal.
2. The oxidized relay
contact causes contact
resistance increase,
which consequently
leads to
overtemperature.
1. Check whether an alarm is generated for the LTMS.
2. If yes, handle the LTMS alarm.
3. If not, power off the ESS by referring to the user manual.
After 5 minutes, power on the ESS by referring to the user
manual. If the alarm persists, export logs and contact technical
support.

---

## PDF page 92

### 1.5.6 3405 DCDC Undertemperature Protection
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3405 DCDC Undertemperature
Protection
Major Equipment
alarm
ADAC
### Impact on the System
The system shuts down.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The ambient
temperature is too low.
1. Check whether the ambient temperature is too low.
2. If the ambient temperature is normal, contact technical
support.

### 1.5.7 3406 Overtemperature Protection for DCDC Bus Terminal
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3406 Overtemperature Protection for
DCDC Bus Terminal
Major Equipment
alarm
ADAC
### Impact on the System
The system shuts down.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 1. The DC connector on
the bus side is not
properly inserted.
2. The LTMS is
abnormal.
3. The screws on the
copper bar inside the
module are not tightened
or the heat dissipation is
abnormal.
1. Check whether the DC connector is not properly inserted by
referring to the user manual.
2. Check whether an alarm is generated for the LTMS.
3. If yes, handle the LTMS alarm.
4. If not, power off the ESS by referring to the user manual.
After 5 minutes, power on the ESS by referring to the user
manual. If the alarm persists, export logs and contact technical
support.

---

## PDF page 93

### 1.5.8 3407 Overtemperature Protection for DCDC Battery Terminal
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3407 Overtemperature Protection for
DCDC Battery Terminal
Major Equipment
alarm
ADAC
### Impact on the System
The system shuts down.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 1. The DC connector on
the battery side is not
properly inserted.
2. The LTMS is
abnormal.
3. The screws on the
copper bar inside the
module are not tightened
or the heat dissipation is
abnormal.
1. Check whether the DC connector is not properly inserted by
referring to the user manual.
2. Check whether an alarm is generated for the LTMS.
3. If yes, handle the LTMS alarm.
4. If not, power off the ESS by referring to the user manual.
After 5 minutes, power on the ESS by referring to the user
manual. If the alarm persists, export logs and contact technical
support.

---

## PDF page 94

### 1.5.9 3408 DCDC Liquid Cooling Abnormal
### Attribute
Alarm ID Alarm Name Alarm
Severity
Alarm
Type
Clearance
Category
Introduced Since
3408 DCDC Liquid Cooling
Abnormal
Major Equipment
alarm
ADAC
### Impact on the System
The system shuts down.
Possible Causes and Procedure
Reason
ID
No. Possible Cause Suggestion
1 1 1. The ambient
temperature is high.
2. The LTMS is
abnormal.
1. Check whether the ambient temperature is beyond the range
specified in the user manual, and check whether there are heat
sources around or whether the heat dissipation vents are
blocked.Constants
2. Check whether an alarm is generated for the LTMS.
3. If yes, handle the LTMS alarm.
4. If not, power off the ESS by referring to the user manual.
After 5 minutes, power on the ESS by referring to the user
manual. If the alarm persists, export logs and contact technical
support.

### 1.5.10 3409 DCDC Versions Mismatched
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3409 DCDC Versions Mismatched Major Equipment
alarm
ADAC
### Impact on the System
The system shuts down.
Possible Causes and Procedure
Reason
ID
No. Possible Cause Suggestion
1 1 The board hardware
version is incorrect.
1. Obtain the latest version and perform an update.
2. If the update fails for three consecutive times, export logs
and contact technical support.

---

## PDF page 95

### 1.5.11 3410 DCDC NTC Faulty
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3410 DCDC NTC Faulty Major Equipment
alarm
ADAC
### Impact on the System
The system shuts down.
Possible Causes and Procedure
Reason
ID
No. Possible Cause Suggestion
1 1 1. The NTC sensor is
short-circuited due to a
fault.
2. The NTC sensor is
open-circuited due to
poor connection.
1. Power off the ESS by referring to the user manual.
2. After 5 minutes, power on the ESS by referring to the user
manual.
3. If the alarm persists, export logs and contact technical
support.

### 1.5.12 3411 DCDC DSP_EPO Faulty
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3411 DCDC DSP_EPO Faulty Major Equipment
alarm
ADAC
### Impact on the System
The system shuts down.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The FAST I/O self -test is
abnormal.
1. Power off the ESS by referring to the user manual. Check
whether the communications port on the DCDC is securely
connected and whether the CON4 communications port on the
RCM is securely connected.
2. After 5 minutes, power on the ESS by referring to the user
manual. Reset the system on the user interface.
3. If the alarm persists, export logs and contact technical
support.

---

## PDF page 96

### 1.5.13 3412 DCDC Bus Port Undervoltage
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3412 DCDC Bus Port Undervoltage Major Equipment
alarm
ADAC
### Impact on the System
The system shuts down.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 1. The PCS DC bus port
is abnormal. 2. The bus
port of the module is
abnormal.
1. Check whether an overcurrent alarm is generated for the
PCS.
2. If yes, handle the PCS overcurrent alarm.
3. If not, power off the ESS by referring to the user manual.
After 5 minutes, power on the ESS by referring to the user
manual. If the alarm persists, export logs and contact technical
support.

### 1.5.14 3413 DCDC Bus Overvoltage
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3413 DCDC Bus Overvoltage Major Equipment
alarm
ADAC
### Impact on the System
The system shuts down.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The voltage regulation
is abnormal or external
overvoltage occurs.
1. Check whether the power grid voltage is within the allowed
range. If not, contact the local power operator.
2. Check whether a DC bus overvoltage alarm is generated for
the PCS.
3. If yes, handle the PCS DC bus overvoltage alarm.
4. If not, power off the ESS by referring to the user manual. After
5 minutes, power on the ESS by referring to the user manual. If
the alarm persists, export logs and contact technical support.

---

## PDF page 97

## 1.6 Power System (PCS)
### 1.6.1 3500 PCS DC Overvoltage
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3500 PCS DC Overvoltage Major Equipment
alarm
ADAC
### Impact on the System
The PCS is shut down.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The DC bus voltage of
the device exceeds the
upper threshold.
1.Power off the ESS by referring to the user manual.
2.After 5 minutes, power on the ESS by referring to the user
manual.
3.If the alarm persists, export logs and contact technical
support.

### 1.6.2 3501 PCS DC Bus in Reverse Polarity
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3501 PCS DC Bus in Reverse Polarity Major Equipment
alarm
ADAC
### Impact on the System
The ESS is shut down.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The DC bus is
connected in reverse
polarity.
1.Power off the ESS by referring to the user manual.
2.Check whether the DC bus is connected in reverse polarity. If
yes, adjust the DC polarities. If not, export logs and contact
technical support.

---

## PDF page 98

### 1.6.3 3503 PCS Grid Phase Wire Short-Circuited to PE
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3503 PCS Grid Phase Wire Short -
Circuited to PE
Major Equipment
alarm
ADAC
### Impact on the System
The PCS is shut down.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The phase wire is short -
circuited to PE or its
impedance to PE is low.
1.Power off the ESS by referring to the user manual.
2.Turn off the secondary circuit breaker of the transformer.
3.Use a megohmmeter to measure the impedance between the
AC side and the ground. If the impedance is abnormal (for
example, lower than 100 kΩ), rectify the fault. If the impedance
is normal, contact technical support.

### 1.6.4 3504 PCS Grid Failed
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3504 PCS Grid Failed Major Environmental
alarm
ADAC
### Impact on the System
The PCS is shut down.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 1.The power grid
experiences an outage.
2.The AC circuit is
disconnected or the AC
circuit breaker is off.
1.Use a multimeter to check whether the AC voltage meets the
power grid standard.
2.Use a multimeter to check whether the AC circuit is
disconnected or the AC circuit breaker is off.

---

## PDF page 99

### 1.6.5 3505 PCS Grid Undervoltage
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3505 PCS Grid Undervoltage Major Environmental
alarm
ADAC
### Impact on the System
The PCS is shut down.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The grid voltage is below
the lower threshold or
the low voltage has
lasted for more than the
value specified for low
voltage ride -through
(LVRT).
1.If the power grid is abnormal temporarily, the device
automatically recovers after detecting that the power grid
becomes normal.
2.Check whether the power grid voltage is within the allowed
range. If not, contact the local power operator. If yes, modify
the power grid undervoltage protection threshold after obtaining
the consent of the local power operator.
3.Check whether the peak voltage of the power grid is too low.
If the fault occurs frequently and persists, contact the local
power operator.
4.If the alarm persists, contact technical support.

---

## PDF page 100

### 1.6.6 3506 PCS Grid Overvoltage
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3506 PCS Grid Overvoltage Major Environmental
alarm
ADAC
### Impact on the System
The PCS is shut down.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The grid voltage exceeds
the higher threshold or
the high voltage has
lasted for more than the
value specified for high
voltage ride -through
(HVRT).
1.If the power grid is abnormal temporarily, the device
automatically recovers after detecting that the power grid
becomes normal.
2.Check whether the power grid voltage is within the allowed
range. If not, contact the local power operator. If yes, modify
the power grid overvoltage protection threshold after obtaining
the consent of the local power operator.
3.Check whether the peak voltage of the power grid is too high.
If the fault occurs frequently and persists, contact the local
power operator.
4.If the alarm persists, contact technical support.

---

## PDF page 101

### 1.6.7 3507 PCS Grid Voltage Imbalanced
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3507 PCS Grid Voltage Imbalanced Major Environmental
alarm
ADAC
### Impact on the System
The PCS is shut down.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The difference between
grid phase voltages
exceeds the upper
threshold.
1.If the power grid is abnormal temporarily, the device
automatically recovers after detecting that the power grid
becomes normal.
2.Check whether the power grid voltage is within the allowed
range. If not, contact the local power operator. If yes, modify
the power grid imbalance protection threshold after obtaining
the consent of the local power operator.
3.Check whether the peak voltage of the power grid is too high.
If the fault occurs frequently and persists, contact the local
power operator.
4.If the alarm persists, contact technical support.

---

## PDF page 102

### 1.6.8 3508 PCS Grid Overfrequency
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3508 PCS Grid Overfrequency Major Environmental
alarm
ADAC
### Impact on the System
The PCS is shut down.
Possible Causes and Procedure
Reason
ID
No. Possible Cause Suggestion
1 1 Power grid exception:
The actual grid
frequency is lower than
the local power grid
standard.
1.If the power grid is abnormal temporarily, the device
automatically recovers after detecting that the power grid
becomes normal.
2.Check whether the power grid frequency is within the allowed
range. If not, contact the local power operator. If yes, modify
the power grid frequency protection threshold after obtaining
the consent of the local power operator.
3.If the alarm persists, export logs and contact technical
support.

---

## PDF page 103

### 1.6.9 3509 PCS Grid Underfrequency
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3509 PCS Grid Underfrequency Major Environmental
alarm
ADAC
### Impact on the System
The PCS is shut down.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 Power grid exception:
The actual grid
frequency is lower than
the local power grid
standard.
1.If the power grid is abnormal temporarily, the device
automatically recovers after detecting that the power grid
becomes normal.
2.Check whether the power grid frequency is within the allowed
range. If not, contact the local power operator. If yes, modify
the power grid frequency protection threshold after obtaining
the consent of the local power operator.
3.If the alarm persists, export logs and contact technical
support.

### 1.6.10 3510 PCS Grid Frequency Unstable
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3510 PCS Grid Frequency Unstable Major Environmental
alarm
ADAC
### Impact on the System
The PCS is shut down.
Possible Causes and Procedure
Reason
ID
No. Possible Cause Suggestion
1 1 Power grid exception:
The actual grid
frequency change rate
does not comply with the
local power grid
standard.
1.If the power grid is abnormal temporarily, the device
automatically recovers after detecting that the power grid
becomes normal.
2.Check whether the power grid frequency is within the allowed
range. If not, contact the local power operator.
3.If the alarm persists, export logs and contact technical
support.

---

## PDF page 104

### 1.6.11 3511 PCS AC Overcurrent
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3511 PCS AC Overcurrent Major Equipment
alarm
ADAC
### Impact on the System
The PCS is shut down.
Possible Causes and Procedure
Reason
ID
No. Possible Cause Suggestion
1 1 The grid experiences a
dramatic voltage drop or
is short -circuited. As a
result, the transient AC
current of the device
exceeds the upper
threshold and triggers
protection.
1.After the alarm is cleared, the device automatically recovers.
2.If the alarm persists and affects the operation of the plant,
export logs and contact technical support.

### 1.6.12 3512 PCS DC Component Overhigh
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3512 PCS DC Component Overhigh Major Equipment
alarm
ADAC
### Impact on the System
The PCS is shut down.
Possible Causes and Procedure
Reason
ID
No. Possible Cause Suggestion
1 1 The DC component in
the AC current exceeds
the upper threshold.
1.After the alarm is cleared, the device automatically recovers.
2.If the alarm persists and affects the operation of the plant,
export logs and contact technical support.
2 1 The DC component in
the AC voltage exceeds
the upper threshold.
1.After the alarm is cleared, the device automatically recovers.
2.If the alarm persists and affects the operation of the plant,
export logs and contact technical support.

---

## PDF page 105

### 1.6.13 3513 Reverse Phase Sequence on PCS AC Side
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3513 Reverse Phase Sequence on PCS
AC Side
Major Environmental
alarm
ADAC
### Impact on the System
The PCS is shut down.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The phase sequence
of lines A, B, and C on
the AC side is
reversed.
Check whether lines A, B, and C to the AC port of the ESS
and to the transformer port are properly connected by
referring to the user manual.

### 1.6.14 3514 PCS Residual Current Abnormal
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3514 PCS Residual Current Abnormal Major Environmental
alarm
ADAC
### Impact on the System
The PCS is shut down.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The ground insulation
resistance decreases
during device
operation.
1. The external circuit may be abnormal temporarily. The
device will automatically recover after the fault is rectified.
2. If the alarm persists, use a megohmmeter to check
whether the DC -side resistance values of the positive and
negative poles to the ground are less than the grid standard
values. If yes, rectify the fault. If not, contact technical
support.

---

## PDF page 106

### 1.6.15 3515 PCS Grounding Abnormal
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3515 PCS Grounding Abnormal Major Environmental
alarm
ADAC
### Impact on the System
The PCS is shut down.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 1.The neutral wire or
PE cable is not
connected.  2.The
output mode set on the
user interface is
inconsistent with the
actual cable
connection mode.
1.Power off the ESS by referring to the user manual.
2.Check whether the PE cable is properly connected.
3.If the PCS is connected to the TN power grid, check
whether the neutral wire is properly connected.
4.Power on the ESS by referring to the user manual. Check
whether the output mode set on the user interface is
consistent with the actual cable connection mode. If they are
inconsistent, change the output mode on the user interface
to the actual cable connection mode. If they are consistent
but the alarm persists and affects the operation of the plant,
export logs and contact technical support.

---

## PDF page 107

### 1.6.16 3516 Low PCS Insulation Resistance
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3516 Low PCS Insulation Resistance Major Environmental
alarm
ADAC
### Impact on the System
The ESS is shut down.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 1.The DC side is short -
circuited to the ground.
2.The device is in a
humid environment and
the insulation between
the circuit and ground is
poor.
1.Set the insulation resistance protection threshold on the user
interface to the minimum value by referring to the power grid
standard.
2.Power off the ESS by referring to the user manual.
3.Check that the PE cable of the device is correctly connected.
4.Use a megohmmeter to check the common-mode impedance
between the system and PE cable. If a short circuit occurs,
rectify the fault. If no short circuit occurs but the alarm persists
and affects the operation of the plant, export logs and contact
technical support.

### 1.6.17 3517 PCS Temperature High
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3517 PCS Temperature High Major Equipment
alarm
ADAC
### Impact on the System
The PCS is shut down.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 1.The ambient
temperature is too high.
2.The device is faulty.
1.Check whether an alarm is generated for the LTMS.
2.If yes, handle the alarm.
3.If not, power off the ESS by referring to the user manual.
After 5 minutes, power on the ESS by referring to the user
manual. If the alarm persists, export logs and contact technical
support.

---

## PDF page 108

### 1.6.18 3518 PCS Abnormal
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3518 PCS Abnormal Major Equipment
alarm
ADAC
### Impact on the System
The PCS is shut down.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 A major fault has
occurred on a circuit
inside the device.
1.Power off the ESS by referring to the user manual.
2.After 5 minutes, power on the ESS by referring to the user
manual.
3.If the alarm persists, export logs and contact technical
support.
2 1 A major fault has
occurred on a circuit
inside the device.
1.Power off the ESS by referring to the user manual.
2.After 5 minutes, power on the ESS by referring to the user
manual.
3.If the alarm persists, export logs and contact technical
support.
3 1 A major fault has
occurred on a circuit
inside the device.
1.Power off the ESS by referring to the user manual.
2.After 5 minutes, power on the ESS by referring to the user
manual.
3.If the alarm persists, export logs and contact technical
support.
4 1 A major fault has
occurred on a circuit
inside the device.
1.Power off the ESS by referring to the user manual.
2.After 5 minutes, power on the ESS by referring to the user
manual.
3.If the alarm persists, export logs and contact technical
support.
5 1 A major fault has
occurred on a circuit
inside the device.
1.Power off the ESS by referring to the user manual.
2.After 5 minutes, power on the ESS by referring to the user
manual.
3.If the alarm persists, export logs and contact technical
support.
6 1 A major fault has
occurred on a circuit
inside the device.
1.Power off the ESS by referring to the user manual.
2.After 5 minutes, power on the ESS by referring to the user
manual.
3.If the alarm persists, export logs and contact technical
support.
7 1 A major fault has
occurred on a circuit
1.Power off the ESS by referring to the user manual.

---

## PDF page 109

inside the device. 2.After 5 minutes, power on the ESS by referring to the user
manual.
3.If the alarm persists, export logs and contact technical
support.
8 1 A major fault has
occurred on a circuit
inside the device.
1.Power off the ESS by referring to the user manual.
2.After 5 minutes, power on the ESS by referring to the user
manual.
3.If the alarm persists, export logs and contact technical
support.
9 1 A major fault has
occurred on a circuit
inside the device.
1.Power off the ESS by referring to the user manual.
2.After 5 minutes, power on the ESS by referring to the user
manual.
3.If the alarm persists, export logs and contact technical
support.
10 1 A major fault has
occurred on a circuit
inside the device.
1.Power off the ESS by referring to the user manual.
2.After 5 minutes, power on the ESS by referring to the user
manual.
3.If the alarm persists, export logs and contact technical
support.
11 1 A major fault has
occurred on a circuit
inside the device.
1.Power off the ESS by referring to the user manual.
2.After 5 minutes, power on the ESS by referring to the user
manual.
3.If the alarm persists, export logs and contact technical
support.
12 1 The precharge circuit
is abnormal, or the
common DC bus is
short-circuited.
1.Power off the ESS by referring to the user manual.
2.Use a multimeter to check whether the common DC bus is
short-circuited.
3.If not, power on the ESS by referring to the user manual.
4.If the alarm persists and affects the operation of the plant,
export logs and contact technical support.
13 1 The current of the
balanced bridge
exceeds the maximum
operating current.
1.After the alarm is cleared, the device automatically
recovers.
2.If the alarm persists and affects the operation of the plant,
export logs and contact technical support.
14 1 A major fault has
occurred on a circuit
inside the device.
1.Power off the ESS by referring to the user manual.
2.After 5 minutes, power on the ESS by referring to the user
manual.
3.If the alarm persists, export logs and contact technical
support.

---

## PDF page 110

### 1.6.19 3519 PCS Update Failed or Versions Mismatched
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3519 PCS Update Failed or Versions
Mismatched
Major Equipment
alarm
ADAC
### Impact on the System
The PCS is shut down.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The update fails. 1.Perform the update again.
2.If the update fails for three consecutive times, export logs and
contact technical support.
2 1 The update fails. 1.Perform the update again.
2.If the update fails for three consecutive times, export logs and
contact technical support.
3 1 The communications
protocol version is
incorrect.
1.Perform the update again.
2.If the update fails for three consecutive times, export logs and
contact technical support.

---

## PDF page 111

### 1.6.20 3520 PCS Internal Fan Abnormal
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3520 PCS Internal Fan Abnormal Major Equipment
alarm
ADAC
### Impact on the System
The PCS may be derated.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The internal fan is short -
circuited, the power
supply is insufficient, or
the fan is damaged.
1.Power off the ESS by referring to the user manual.
2.After 5 minutes, power on the ESS by referring to the user
manual.
3.If the alarm persists, export logs and contact technical
support.
2 1 The internal fan is short -
circuited, the power
supply is insufficient, or
the fan is damaged.
1.Power off the ESS by referring to the user manual.
2.After 5 minutes, power on the ESS by referring to the user
manual.
3.If the alarm persists, export logs and contact technical
support.
3 1 The internal fan is short -
circuited, the power
supply is insufficient, or
the fan is damaged.
1.Power off the ESS by referring to the user manual.
2.After 5 minutes, power on the ESS by referring to the user
manual.
3.If the alarm persists, export logs and contact technical
support.

---

## PDF page 112

3521 PCS AC Terminal Temperature Abnormal
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3521 PCS AC Terminal Temperature
Abnormal
Major Equipment
alarm
ADAC
### Impact on the System
The PCS is shut down.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 1.The AC power cable is
not of the recommended
specifications or is
oxidized.  2.The OT/OD
terminal of the AC power
cable is not crimped as
required.  3.The
fastening torque of the
AC terminal does not
meet the requirement.
1.Power off the ESS by referring to the user manual.
2.Check whether the cables meet the specifications by
referring to the user manual.
3.Check whether the OT/OD terminal is crimped as required by
referring to the user manual.
4.Check whether the fastening torque of wiring terminals meets
the requirement by referring to the user manual.
5.Power on the ESS by referring to the user manual. If the
alarm persists, export logs and contact technical support.

---

## PDF page 113

### 1.6.21 3522 PCS DC Terminal Temperature Abnormal
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3522 PCS DC Terminal Temperature
Abnormal
Major Equipment
alarm
ADAC
### Impact on the System
The ESS is shut down.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 1.The DC power cable is
not of the recommended
specifications or is
oxidized.  2.The DC
connector is not properly
inserted.  3.The OT/OD
terminals of the DC
cable are not crimped as
required, or the fastening
torque of the wiring
terminals on the DC side
does not meet the
requirement.
1.Power off the ESS by referring to the user manual.
2.Check whether the DC connector is not properly inserted by
referring to the user manual.
3.Power on the ESS by referring to the user manual. If the
alarm persists, export logs and contact technical support.

---

## PDF page 114

### 1.6.22 3523 PCS Black Start Failed
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3523 PCS Black Start Failed Major Equipment
alarm
ADAC
### Impact on the System
The PCS is shut down.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 1.The grid codes
configured on PCSs are
inconsistent.  2.The
external load is abnormal
or the power cable is not
properly connected.
1.Shut down the ESS on the user interface.
2.Check whether the grid codes configured on all PCSs are
consistent on the user interface.
3.If the grid codes are different, correctly set the grid code to an
identical value on all PCSs and perform black start again.
4.If the grid codes are the same, perform the following steps:
(1) Power off the ESS by referring to the user manual.
(2) Check whether the external load power is lower than the
current system output power. It is recommended that black
start be performed without loads.
(3) Check whether the power cable is correctly connected by
referring to the user manual.
(4) After the check is complete, perform black start again.
(5) If the alarm persists, export logs and contact technical
support.

---

## PDF page 115

### 1.6.23 3524 Incorrect Black Start Instruction Sequence of PCS
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3524 Incorrect Black Start Instruction
Sequence of PCS
Major Equipment
alarm
ADAC
### Impact on the System
The PCS is shut down.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The black start
instructions are incorrect.
1.Power off the ESS by referring to the user manual.
2.After 5 minutes, power on the ESS by referring to the user
manual.
3.If the alarm persists, export logs and contact technical
support.

### 1.6.24 3525 PCS Fuse Broken
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3525 PCS Fuse Broken Major Equipment
alarm
ADAC
### Impact on the System
The ESS is shut down.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The internal circuit of the
device is faulty.
Export logs and contact technical support.

---

## PDF page 116

### 1.6.25 3526 PCS Fuse Self-Check Abnormal
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3526 PCS Fuse Self-Check Abnormal Major Equipment
alarm
ADAC
### Impact on the System
The PCS is shut down.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The internal circuit of the
device is faulty.
1.After the alarm is cleared, the device automatically recovers.
2.If the alarm persists and affects the operation of the plant,
export logs and contact technical support.

### 1.6.26 3527 PCS FAST I/O Self-Test Abnormal
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3527 PCS FAST I/O Self-Test Abnormal Major Equipment
alarm
ADAC
### Impact on the System
The ESS is shut down.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The rapid shutdown
cable between the PCS
and the ESS is not
properly connected.
1.Power off the ESS by referring to the user manual and check
whether the communications port is securely connected.
2.After 5 minutes, power on the ESS by referring to the user
manual.
3.If the alarm persists, export logs and contact technical
support.

---

## PDF page 117

### 1.6.27 3528 PCS DC Bus Short-Circuited
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3528 PCS DC Bus Short-Circuited Major Equipment
alarm
ADAC
### Impact on the System
The ESS is shut down.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The PCS DC bus is
short-circuited.
1.Power off the ESS by referring to the user manual and check
whether a PCS DC short circuit occurs.
2.If a short circuit occurs, rectify the fault. After the fault is
rectified, power on the system again.
3.If the line is normal, export logs and contact technical
support.

### 1.6.28 3529 PCS Relay Overtemperature
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3529 PCS Relay Overtemperature Major Communications
alarm
ADAC
### Impact on the System
The PCS is derated and may shut down in severe cases.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The oxidized relay
contact causes contact
resistance increase,
which consequently
leads to
overtemperature.
1.Check whether no grid scheduling instruction is received in
on-grid scenarios or whether the PCS output power is greater
than the load power in off-grid scenarios. If yes, shut down and
start the PCS by referring to step 2.If not, no further action is
required.
2.Shut down the ESS on the user interface. After 5 minutes,
start the ESS.
3.If the alarm persists after the restart, export logs and contact
technical support.

---

## PDF page 118

### 1.6.29 3530 PCS AC Resonance
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3530 PCS AC Resonance Major Environmental
alarm
ADAC
### Impact on the System
The system is powered off.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 Resonance occurs
between the external
device and the current
device.
Turn off the AC circuit breaker in the power distribution cabinet.
If the RCM has a DC disconnector, you also need to turn off
the DC disconnector. Collect the information about the distance
between the ESS and inverter (if any) and the grid connection
point, number of parallel -connected devices, device models,
and logs (all devices connected to the same grid connection
point), and contact technical support.

---

## PDF page 119

### 1.6.30 3531 PCS Derated
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3531 PCS Derated Major Equipment
alarm
ADAC
### Impact on the System
The PCS is derated.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 1.The AC power cable is
not of the recommended
specifications or is
oxidized.
2.The OT/OD terminal of
the AC power cable is
not crimped as required.
3.The fastening torque of
the AC terminal does not
meet the requirement.
1.Power off the ESS by referring to the user manual.
2.Check whether the cables meet the specifications by
referring to the user manual.
3.Check whether the OT/OD terminal is crimped as required by
referring to the user manual.
4.Check whether the fastening torque of wiring terminals meets
the requirement by referring to the user manual.
5.Turn on the AC circuit breaker of the RCM and then the AC
circuit breaker of the power distribution cabinet. If the alarm
persists, export logs and contact technical support.
2 1 1.The DC connector is
oxidized.
2.The DC connector is
not properly inserted.
3.The OT/OD terminal of
the internal DC power
cable or the NTC sensor
cable is loosely
connected.
1.Power off the ESS by referring to the user manual.
2.Check whether the DC connector is not properly inserted by
referring to the user manual.
3.Turn on the AC circuit breaker of the RCM and then the AC
circuit breaker of the power distribution cabinet. If the alarm
persists, export logs and contact technical support.
3 1 The internal copper bar
and NTC are loosely
connected.
Export logs and contact technical support.
4 1 Resonance occurs
between the external
device and the current
device.
Collect the information about the distance between the ESS
and inverter (if any) and the grid connection point, number of
parallel-connected devices, device models, and logs (all
devices connected to the same grid connection point), and
contact technical support.

---

## PDF page 120

### 1.6.31 3532 PCS Startup Abnormal
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3532 PCS Startup Abnormal Major Equipment
alarm
ADAC
### Impact on the System
The PCS is shut down.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The working mode is not
supported.
1. If the ESS SOC is less than the array end-of-discharge SOC,
adjust the array end-of-discharge SOC to a value less than the
ESS SOC and start the device again. After the device is started
successfully, restore the array end -of-discharge SOC to the
original value.
2. If the alarm persists, set the working mode to PQ and restart
the device. After the device is started successfully, charge the
ESS and restore the working mode to the original value when
the ESS SOC is greater than the array end-of-discharge SOC.
3. If the alarm persists, export logs and contact technical
support.
2 1 The grid THDu value is
too large.
1. If the alarm occurs occasionally, the power grid may be
abnormal temporarily. The device automatically recovers after
detecting that the power grid becomes normal.
2. If the alarm occurs frequently, check whether the grid THDu
value is within the normal range. If not, contact the local power
operator.
3. If the alarm persists, export logs and contact technical
support.

---

## PDF page 121

## 1.7 Temperature Control System
### 1.7.1 3600 Power loss alarm
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3600 Power loss alarm Major Equipment
alarm
ADAC
### Impact on the System
The LTMS shuts down.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The power supply to the
LTMS is abnormal.
1. Use a voltmeter to check whether the power supply to the
LTMS is normal.
2. If the power supply is abnormal, locate the cause and
resume the power supply.
3. If the fault persists, check for other causes. If all possible
causes have been ruled out, contact technical support.

---

## PDF page 122

### 1.7.2 3601 Power voltage abnormal
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3601 Power voltage abnormal Major Equipment
alarm
ADAC
### Impact on the System
The system cannot be charged or discharge, and the LTMS shuts down.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The power supply
voltage exceeds the
upper threshold.
1. Use a voltmeter to check whether the power supply to the
LTMS is normal.
2. If the power supply is abnormal, locate the cause and
resume the power supply.
1 2 The corresponding
power detection device
is faulty.
1. Replace the auxiliary power module by referring to the
maintenance manual.
2. If the alarm persists, export logs and contact technical
support.
2 1 The power supply
voltage is below the
lower threshold.
1. Use a voltmeter to check whether the power supply to the
LTMS is normal.
2. If the power supply is abnormal, locate the cause and
resume the power supply.
2 2 The corresponding
power detection device
is faulty.
1. Replace the auxiliary power module by referring to the
maintenance manual.
2. If the alarm persists, export logs and contact technical
support.

---

## PDF page 123

### 1.7.3 3602 Power frequency abnormal
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3602 Power frequency abnormal Warning Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally, but the system reliability may be affected.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The power supply
frequency is below the
lower threshold.
1. Check whether the power supply frequency of the LTMS is
normal on the user interface.
2. If the power supply is abnormal, locate the cause and
resume the power supply.
2 The corresponding
power detection device
is faulty.
1. Replace the component by referring to the corresponding
replacement guide in the maintenance manual.
2. If the fault persists, check for other causes. If all possible
causes have been ruled out, contact technical support.
2 1 The power supply
frequency exceeds the
upper threshold.
1. Check whether the power supply frequency of the LTMS is
normal on the user interface.
2. If the power supply is abnormal, locate the cause and
resume the power supply.
2 The corresponding
power detection device
is faulty.
1. Replace the component by referring to the corresponding
replacement guide in the maintenance manual.
2. If the fault persists, check for other causes. If all possible
causes have been ruled out, contact technical support.

---

## PDF page 124

### 1.7.4 3603 Outdoor temperature sensor fault
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3603 Outdoor temperature sensor fault Major Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally, but the outdoor temperature cannot be detected. The
system may fail to respond to the heat dissipation requirements on the power side in a timely manner.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The cable to the
temperature sensor is
loose or damaged.
1. Power off the ESS by referring to the user manual.
2. Check whether the cable to the temperature sensor is
disconnected or broken. If the cable is disconnected or broken,
reconnect the sensor connector.
2 The temperature sensor
is faulty.
1. Replace the temperature sensor by referring to the
maintenance manual.
2. If the alarm persists, export logs and contact technical
support.

### 1.7.5 3604 Outdoor low temperature alarm
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3604 Outdoor low temperature alarm Minor Environmental
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally, but the LTMS may fail to run properly.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The outdoor temperature
is too low.
Use the device within the nominal temperature range.

---

## PDF page 125

### 1.7.6 3605 LTMS Communication Abnormal
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3605 LTMS Communication Abnormal Major Communications
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally, but the LTMS may fail to run properly.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The power supply to the
LTMS is abnormal.
1. Use a voltmeter to check whether the power supply to the
LTMS is normal.
2. If the power supply is abnormal, locate the cause and
resume the power supply.
1 3 The cable to the LTMS is
loose or damaged.
1. Power off the ESS by referring to the user manual.
2. Check whether the wiring terminals of the FE_1 or FE_2 port
on the LCC and the LAN3 port on the BCU are loose,
disconnected, or incorrectly connected. If yes, reconnect them.
3. If the alarm persists, export logs and contact technical
support.

---

## PDF page 126

### 1.7.7 3606 LTMS expiration alarm
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3606 LTMS expiration alarm Warning Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally, but the LTMS may fail to run properly.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The system time is
incorrectly set.
1. Check whether the time of the ESS is consistent with the local
time on the user interface. If they are inconsistent, set the time on
the user interface to the local time.
2. If the alarm persists, export logs and contact technical support.
2 The service time of
the LTMS exceeds the
threshold.
1. Replace the LTMS and liquid cooling pipes by referring to the
maintenance manual.
2. If the alarm persists, export logs and contact technical support.

### 1.7.8 3608 Certificate about to expire
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3608 Certificate about to expire Minor Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally, but the certificate-related functions are restricted.
Possible Causes and Procedure
Reason
ID
No. Possible Cause Suggestion
1 1 The northbound
communication
certificate is about to
expire or the system
time is incorrectly set.
1. Check whether the time of the ESS is consistent with the local
time on the user interface. If they are inconsistent, set the time on
the user interface to the local time.
2. Otherwise, apply for a new certificate from the CA and update
the certificate.
3. If the alarm persists, export logs and contact technical support.

---

## PDF page 127

### 1.7.9 3609 Certificate has expired
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3609 Certificate has expired Minor Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally, but the certificate-related functions are restricted.
Possible Causes and Procedure
Reason
ID
No. Possible Cause Suggestion
1 1 The northbound
communication
certificate has expired or
the system time is
incorrectly set.
1. Check whether the time of the ESS is consistent with the
local time on the user interface. If they are inconsistent, set the
time on the user interface to the local time.
2. Otherwise, apply for a new certificate from the CA and
update the certificate.
3. If the alarm persists, export logs and contact technical
support.

---

## PDF page 128

### 1.7.10 3620 Compressor discharge high pressure alarm
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3620 Compressor discharge high
pressure alarm
Major Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally, but the compressor cannot run properly.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The air filter or outdoor
heat exchanger is dirty
or blocked.
1. Check whether the air filter is dirty or blocked. If yes, clean
it up or replace it.
2. Check whether the outdoor heat exchanger is dirty or
blocked. If yes, clean it up.
1 2 The outdoor fan is
abnormal.
1. Check whether a fan alarm is generated on the user
interface.
2. If a fan alarm is generated, rectify the fault by referring to
the suggestions related to the fan first.
1 3 The data reported from
the pressure sensor is
abnormal.
1. Check whether a water pump alarm is generated on the
user interface.
2. If a water pump alarm is generated, rectify the fault by
referring to the suggestions related to the water pump first.
3. If the alarm persists, check whether a multi -way valve
alarm is generated on the user interface.
4. If a multi-way valve alarm is generated, rectify the fault by
referring to the suggestions related to the multi -way valve
first.
1 4 The temperature of
water supplied to the
condenser is too high
or the water supply is
insufficient.
1. If the alarm persists, export logs and contact technical
support.
1 6 The data reported from
the pressure sensor is
abnormal.
1. Power off the ESS by referring to the user manual.
2. Check whether the cable to the pressure sensor is
disconnected or broken. If the cable is disconnected or
broken, reconnect the sensor connector.
3. If the fault persists, replace the LTMS by referring to the
maintenance manual.
4. If the alarm persists, export logs and contact technical
support.

---

## PDF page 129

### 1.7.11 3621 Compressor suction low pressure alarm
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3621 Compressor suction low pressure
alarm
Major Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally, but the compressor cannot run properly.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 2 The refrigerant
leaks.
1. Use a halogen detector to check whether a leakage occurs in a
refrigerant pipe of the LTMS.
2. If a leakage occurs, replace the corresponding component by
referring to the maintenance manual.
3. Charge refrigerant by referring to the refrigerant charging guide in
the maintenance manual.
1 4 The data reported
from the pressure
sensor is
abnormal.
1. Power off the ESS by referring to the user manual.
2. Check whether the cable to the pressure sensor is disconnected
or broken. If the cable is disconnected or broken, reconnect the
sensor connector.
1 5 The EEV is faulty. 1. Check whether the cable to the EEV is disconnected or broken. If
the cable is disconnected or broken, reconnect the EEV connector.
2. If the alarm persists, replace the LTMS by referring to the
maintenance manual.
3. If the alarm persists, export logs and contact technical support.
2 1 The data reported
from the pressure
sensor is
abnormal.
1. Power off the ESS by referring to the user manual.
2. Check whether the cable to the pressure sensor is disconnected
or broken. If the cable is disconnected or broken, reconnect the
sensor connector.
2 The refrigerant
leaks.
1. Use a halogen detector to check whether a leakage occurs in a
refrigerant pipe of the LTMS.
2. If a leakage occurs, replace the corresponding component by
referring to the maintenance manual.
3. Charge refrigerant by referring to the refrigerant charging guide in
the maintenance manual.
3 The EEV is faulty. 1. Power off the ESS by referring to the user manual.
2. Check whether the cable to the EEV is disconnected or broken. If
the cable is disconnected or broken, reconnect the EEV connector.
3. If the alarm persists, replace the LTMS by referring to the
maintenance manual.
4. If the alarm persists, export logs and contact technical support.

---

## PDF page 130

### 1.7.12 3622 Compressor Low Superheat Degree
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3622 Compressor Low Superheat
Degree
Major Equipment
alarm
ADAC
### Impact on the System
The compressor cannot run properly.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The data reported
from the pressure and
temperature sensor is
abnormal.
1. Power off the ESS by referring to the user manual.
2. Check whether the cable to the pressure and temperature
sensor is disconnected or broken. If the cable is disconnected
or broken, reconnect the connector of the pressure and
temperature sensor.
4 There is insufficient
coolant.
1. Check whether a "Water Tank Low Liquid Level" alarm is
generated. If yes, handle the alarm first. If no, go to the next
step.
2. Power off the ESS by referring to the user manual.
3. Check whether a leakage occurs in the LTMS or a pipe.
4. If a leakage occurs, replace the corresponding component
or pipe by referring to the maintenance manual.
5. Fill coolant into the coolant refill tank by referring to the
corresponding guide in the maintenance manual.
6 The EEV is faulty. 1. Check whether the cable to the EEV is disconnected or
broken. If the cable is disconnected or broken, reconnect the
EEV connector.
2. If the alarm persists, replace the LTMS by referring to the
maintenance manual.
3. If the alarm persists, export logs and contact technical
support.

---

## PDF page 131

### 1.7.13 3623 Compressor discharge pressure sensor fault
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3623 Compressor discharge pressure
sensor fault
Major Equipment
alarm
ADAC
### Impact on the System
The discharge pressure cannot be properly monitored, and the compressor may not run properly.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The cable to the
pressure sensor is loose
or damaged.
1. Power off the ESS by referring to the user manual.
2. Check whether the cable to the pressure sensor is
disconnected or broken. If the cable is disconnected or broken,
reconnect the sensor connector.
1 3 The pressure and
temperature sensor is
faulty.
1. Replace the LTMS by referring to the corresponding
replacement guide in the maintenance manual.
2. If the alarm persists, export logs and contact technical
support.

### 1.7.14 3624 Condenser outlet pressure sensor fault
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3624 Condenser outlet pressure sensor
fault
Minor Equipment
alarm
ADAC
### Impact on the System
The condenser outlet pressure cannot be properly monitored.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The cable to the
pressure sensor is loose
or damaged.
1. Power off the ESS by referring to the user manual.
2. Check whether the cable to the pressure sensor is
disconnected or broken. If the cable is disconnected or broken,
reconnect the sensor connector.
1 3 The pressure and
temperature sensor is
faulty.
1. Replace the LTMS by referring to the maintenance manual.
2. If the alarm persists, export logs and contact technical
support.

---

## PDF page 132

### 1.7.15 3625 Condenser outlet temperature sensor fault
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3625 Condenser outlet temperature
sensor fault
Minor Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally, but the suction pressure cannot be detected properly.
The compressor cannot run properly.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The cable to the
pressure sensor is
loose or damaged.
1. Power off the ESS by referring to the user manual.
2. Check whether the cable to the pressure sensor is
disconnected or broken. If the cable is disconnected or
broken, reconnect the sensor connector.
1 3 The pressure and
temperature sensor is
faulty.
1. Replace the LTMS by referring to the maintenance
manual.
2. If the alarm persists, export logs and contact technical
support.

---

## PDF page 133

### 1.7.16 3626 Compressor suction pressure sensor fault
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3626 Compressor suction pressure
sensor fault
Major Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally, but the suction pressure cannot be detected properly.
The compressor cannot run properly.
Possible Causes and Procedure
Reason
ID
No. Possible Cause Suggestion
1 1 The cable to the
pressure sensor is loose
or damaged.
1. Power off the ESS by referring to the user manual.
2. Check whether the cable to the pressure sensor is
disconnected or broken. If the cable is disconnected or broken,
reconnect the sensor connector.
1 3 The pressure and
temperature sensor is
faulty.
1. Replace the LTMS by referring to the maintenance manual.
2. If the alarm persists, export logs and contact technical
support.

### 1.7.17 3627 Compressor suction temperature sensor fault
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3627 Compressor suction temperature
sensor fault
Major Equipment
alarm
ADAC
### Impact on the System
The suction temperature cannot be properly monitored, and the compressor may not run properly.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The cable to the
temperature sensor
is loose or damaged.
1. Power off the ESS by referring to the user manual.
2. Check whether the cable to the temperature sensor is
disconnected or broken. If the cable is disconnected or broken,
reconnect the sensor connector.
1 3 The pressure and
temperature sensor
is faulty.
1. Replace the LTMS by referring to the maintenance manual.
2. If the alarm persists, export logs and contact technical
support.

---

## PDF page 134

### 1.7.18 3628 Dehumidifying temperature sensor fault
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3628 Dehumidifying temperature sensor
fault
Minor Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally, but the dehumidifying evaporator outlet temperature
cannot be detected. Dehumidifying may fail.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The cable to the
temperature sensor is
loose or damaged.
1. Power off the ESS by referring to the user manual.
2. Check whether the cable to the temperature sensor is
disconnected or broken. If the cable is disconnected or
broken, reconnect the sensor connector.
2 The temperature
sensor is faulty.
1. Replace the LTMS by referring to the maintenance
manual.
2. If the alarm persists, export logs and contact technical
support.

### 1.7.19 3640 Compressor drive alarm
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3640 Compressor drive alarm Major Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally, but the compressor cannot run properly.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 2 The compressor drive
is faulty.
Replace the drive by referring to the corresponding
replacement guide in the maintenance manual.
1 4 The compressor is
faulty.
1. Replace the LTMS by referring to the maintenance
manual.
2. If the alarm persists, export logs and contact technical
support.

---

## PDF page 135

### 1.7.20 3641 Compressor drive output abnormal
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3641 Compressor drive output abnormal Major Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally, but the compressor cannot run properly.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The cable to the
compressor drive is
loose or damaged.
1. Power off the ESS by referring to the user manual.
2. Check whether the cable to the drive is disconnected or
broken. If the cable is disconnected or broken, reconnect the
cable.
1 2 The compressor drive
is faulty.
Replace the drive by referring to the corresponding
replacement guide in the maintenance manual.
1 4 The compressor is
faulty.
1. Replace the LTMS by referring to the maintenance
manual.
2. If the alarm persists, export logs and contact technical
support.

---

## PDF page 136

### 1.7.21 3642 Compressor Overcurrent Alarm
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3642 Compressor Overcurrent Alarm Major Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally, but the compressor cannot run properly.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The air filter or outdoor
heat exchanger is dirty
or blocked.
1. Check whether the air filter is dirty or blocked. If yes, clean
it up or replace it.
2. Check whether the outdoor heat exchanger is dirty or
blocked. If yes, clean it up.
1 2 The outdoor fan is
abnormal.
1. Check whether a fan alarm is generated on the user
interface.
2. If a fan alarm is generated, rectify the fault by referring to
the suggestions related to the fan first.
1 3 The power supply
voltage exceeds the
upper threshold.
1. Use a voltmeter to check whether the power supply to the
LTMS is normal.
2. If the power supply is abnormal, locate the cause and
resume the power supply.
1 4 The refrigerant is
overfilled.
1. Withdraw an appropriate amount of the refrigerant in the
system by referring to the maintenance manual.
1 6 The compressor is
faulty.
1. Replace the LTMS by referring to the maintenance
manual.
2. If the alarm persists, export logs and contact technical
support.

---

## PDF page 137

### 1.7.22 3643 Compressor drive communication abnormal
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3643 Compressor drive communication
abnormal
Major Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally, but the compressor cannot run properly.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 2 The cable to the
compressor drive is
loose or damaged.
Check whether the cable to the drive is disconnected or
broken. If the cable is disconnected or broken, reconnect the
cable.
3 The compressor drive
is absent.
1. Power off the ESS by referring to the user manual.
2. Check whether the drive is in position. If not, reconnect the
drive.
4 The compressor drive
is faulty.
1. Replace the drive by referring to the corresponding
replacement guide in the maintenance manual.
2. If the alarm persists, export logs and contact technical
support.

---

## PDF page 138

### 1.7.23 3644 High discharge temperature alarm
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3644 High discharge temperature alarm Major Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally, but the compressor cannot run properly.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The air filter or outdoor
heat exchanger is dirty
or blocked.
1. Check whether the air filter is dirty or blocked. If yes, clean it
up or replace it.
2. Check whether the outdoor heat exchanger is dirty or
blocked. If yes, clean it up.
2 The outdoor temperature
is too high.
1. Check whether the device is used within the nominal
temperature range.
3 The outdoor fan is
abnormal.
1. Check whether a fan alarm is generated on the user
interface.
2. If a fan alarm is generated, rectify the fault by referring to
the suggestions related to the fan first.
4 The temperature of
water supplied to the
condenser is too high or
the water supply is
insufficient.
1. Check whether a water pump alarm is generated on the
user interface.
2. If a water pump alarm is generated, rectify the fault by
referring to the suggestions related to the water pump first.
3. If the fault persists, check whether a multi -way valve alarm
is generated on the user interface.
4. If a multi -way valve alarm is generated, rectify the fault by
referring to the suggestions related to the multi-way valve first.
5 Refrigerant leaks. 1. Use a halogen detector to check whether a leakage occurs
in a refrigerant pipe of the LTMS.
2. If a leakage occurs, replace the corresponding component
by referring to the maintenance manual.
3. Charge refrigerant by referring to the refrigerant charging
guide in the maintenance manual.
7 The data reported from
the discharge
temperature sensor is
abnormal.
1. Power off the ESS by referring to the user manual.
2. Check whether the cable to the temperature sensor is
disconnected or broken. If the cable is disconnected or broken,
reconnect the sensor connector.
3. Replace the LTMS by referring to the maintenance manual.
4. If the alarm persists, export logs and contact technical
support.

---

## PDF page 139

### 1.7.24 3645 Compressor discharge temperature sensor fault
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3645 Compressor discharge temperature
sensor fault
Major Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally, but the discharge temperature cannot be detected
properly. The compressor cannot run properly.
Possible Causes and Procedure
Reason
ID
No. Possible Cause Suggestion
1 1 The cable to the
temperature sensor is
loose or damaged.
1. Power off the ESS by referring to the user manual.
2. Check whether the cable to the temperature sensor is
disconnected or broken. If the cable is disconnected or broken,
reconnect the sensor connector.
1 3 The pressure and
temperature sensor is
faulty.
1. Replace the LTMS by referring to the maintenance manual.
2. If the alarm persists, export logs and contact technical
support.

### 1.7.25 3646 Insufficient Refrigerant
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3646 Insufficient Refrigerant Major Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally, but the cooling capacity may be insufficient.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 Refrigerant leaks. 1. Use a halogen detector to check whether a leakage occurs in a
refrigerant pipe of the LTMS.
2. If a leakage occurs, replace the corresponding component by
referring to the maintenance manual.
3. Charge refrigerant by referring to the refrigerant charging guide
in the maintenance manual.
4. If the alarm persists, export logs and contact technical support.

---

## PDF page 140

### 1.7.26 3650 Insufficient Cooling Capacity
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3650 Insufficient Cooling Capacity Warning Equipment
alarm
ADMC
### Impact on the System
The system can be charged and discharge normally, but the cooling capacity is insufficient.
Possible Causes and Procedure
Reason
ID
No. Possible Cause Suggestion
1 1 Refrigerant leaks. 1. Use a halogen detector to check whether a leakage occurs
in a refrigerant pipe of the LTMS.
2. If a leakage occurs, replace the LTMS by referring to the
maintenance manual.
3. Charge refrigerant by referring to the refrigerant charging
guide in the maintenance manual.
2 Multi-way valve sealing
fails.
1. Replace the LTMS by referring to the maintenance manual.
2. If the alarm persists, export logs and contact technical
support.

---

## PDF page 141

### 1.7.27 3651 LCC Output Overcurrent
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3651 LCC Output Overcurrent Major Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally, but the LTMS may fail to run properly.
Possible Causes and Procedure
Reason
ID
No. Possible Cause Suggestion
1 1 The external cables to
the LCC are faulty.
1. Check whether the system reports any alarm related to the
water pressure sensor, high pressure sensor, or suction
pressure sensor.
2. Power off the ESS by referring to the user manual.
3. If an alarm is reported for the water pressure sensor, high
pressure sensor, or suction pressure sensor, check the cables
to the water pressure sensor, high pressure sensor, and
suction pressure sensor in sequence. If any cables are
damaged or short-circuited, reconnect them.
4. If no pressure sensor alarm is reported, check the cables to
the electronic expansion valve, electric heater contactor, oil
heating belt, and coolant refilling solenoid valve in sequence. If
any cables are damaged or short-circuited, reconnect them.
5. Power on the system, wait for 5 minutes, and check whether
the alarm is generated. If the alarm persists, check for other
possible causes.
2 The external load of the
LCC is abnormal.
1. If an alarm is reported for the water pressure sensor, high
pressure sensor, or suction pressure sensor, disconnect the
connectors of the water pressure sensor, high pressure sensor,
and suction pressure sensor in sequence. Power on the
system, wait for 5 minutes, and check whether the alarm is
generated. If not, replace the corresponding pressure sensor
by referring to the maintenance manual.
2. If no alarm is reported for the water pressure sensor, high
pressure sensor, or suction pressure sensor, disconnect the
cables to the electronic expansion valve connector, electric
heater contactor, oil heating belt connector, and coolant refilling
solenoid valve connector in sequence. Power on the system,
wait for 5 minutes, and check whether the alarm is generated.
If the alarm is not generated, replace the corresponding
component by referring to the maintenance manual.
3 The LCC is faulty. 1. Replace the LCC by referring to the maintenance manual.
2. If the alarm persists, export logs and contact technical
support.

---

## PDF page 142

### 1.7.28 3652 Inconsistent Software Version of Drive and Auxiliary
Power Module
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3652 Inconsistent Software Version of
Drive and Auxiliary Power Module
Minor Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally, but some value-added features may be unavailable.
Possible Causes and Procedure
Reason
ID
No. Possible Cause Suggestion
1 1 The software
version of the drive
and auxiliary power
module is
inconsistent.
1. If the component version is inconsistent with the system software
package version due to a manual update failure, the system running
is not affected. You are advised to perform the update at a proper
time.
2. If the version is inconsistent with the system software package
version due to component replacement, perform a manual update.
3. If the update fails for several times, contact technical support.

### 1.7.29 3653 Inconsistent LCC Software Version
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3653 Inconsistent LCC Software Version Minor Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally, but some value-added features may be unavailable.
Possible Causes and Procedure
Reason
ID
No. Possible Cause Suggestion
1 1 The LCC software
is inconsistent.
1. If the component version is inconsistent with the system software
package version due to a manual update failure, the system running
is not affected. You are advised to perform the update at a proper
time.
2. If the version is inconsistent with the system software package
version due to component replacement, perform a manual update.
3. If the update fails for several times, contact technical support.

---

## PDF page 143

### 1.7.30 3655 Auxiliary power abnormal
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3655 Auxiliary power abnormal Major Equipment
alarm
ADAC
### Impact on the System
The system shuts down, and the LTMS shuts down.
Possible Causes and Procedure
Reason
ID
No. Possible Cause Suggestion
1 1 The cable to the
auxiliary power
supply is loose or
damaged.
1. Power off the ESS by referring to the user manual.
2. Check whether the cable to the auxiliary power supply is
disconnected or broken. If the cable is disconnected or broken,
reconnect the connector of the auxiliary power supply.
2 The auxiliary power
supply is faulty.
1. Replace the drive and auxiliary power module by referring to
the corresponding replacement guide in the maintenance manual.
2. If the alarm persists, export logs and contact technical support.

### 1.7.31 3660 Outdoor cooling module blocked
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3660 Outdoor cooling module blocked Major Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally, but the air volume may be insufficient.
Possible Causes and Procedure
Reason
ID
No. Possible Cause Suggestion
1 1 The air filter or outdoor
heat exchanger is dirty
or blocked.
1. Check whether the air filter is dirty or blocked. If yes, clean it
up or replace it.
2. Check whether the outdoor heat exchanger is dirty or
blocked. If yes, clean it up.
3. If the alarm persists, export logs and contact technical
support.

---

## PDF page 144

### 1.7.32 3661 Outdoor heat exchanger temperature sensor fault
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3661 Outdoor heat exchanger
temperature sensor fault
Minor Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally, but the temperature of the outdoor heat exchanger
cannot be detected.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The cable to the
temperature sensor is
loose or damaged.
1. Power off the ESS by referring to the user manual.
2. Check whether the cable to the temperature sensor is
disconnected or broken. If the cable is disconnected or broken,
reconnect the sensor connector.
2 The temperature sensor
is faulty.
1. Replace the temperature sensor by referring to the
maintenance manual.
2. If the alarm persists, export logs and contact technical
support.

### 1.7.33 3665 Fan fault
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3665 Fan fault Major Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally, but the air volume cannot be controlled.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The cable to the fan is
loose or damaged.
1. Power off the ESS by referring to the user manual.
2. Check whether the cable to the fan is disconnected or
broken. If the cable is disconnected or broken, reconnect the
fan connector.
2 The fan is faulty. 1. Replace the fan by referring to the maintenance manual.
2. If the alarm persists, export logs and contact technical

---

## PDF page 145

support.
2 1 The power supply to
the fan is abnormal.
1. Use a voltmeter to check whether the fan power supply is
normal.
2. If the power supply is abnormal, locate the cause and
resume the power supply.
2 The cable to the fan is
loose or damaged.
1. Power off the ESS by referring to the user manual.
2. Check whether the cable to the fan is disconnected or
broken. If the cable is disconnected or broken, reconnect the
fan connector.
3 The fan is faulty. 1. Replace the fan by referring to the maintenance manual.
2. If the alarm persists, export logs and contact technical
support.

---

## PDF page 146

### 1.7.34 3666 Fan fault
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3666 Fan fault Major Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharged normally, but the air volume cannot be controlled.
Possible Causes and Procedure
Reason
ID
No. Possible Cause Suggestion
1 1 The cable to the fan is
not connected properly.
1. Power off the ESS by referring to the user manual.
2. Check whether the cable to the fan is disconnected or
broken. If the cable is disconnected or broken, reconnect the
fan connector.
2 The fan is faulty. 1. Replace the fan by referring to the maintenance manual.
2. If the alarm persists, export logs and contact technical
support.
2 1 The power supply to the
fan is abnormal.
1. Use a voltmeter to check whether the fan power supply is
normal.
2. If the power supply is abnormal, locate the cause and
resume the power supply.
2 The cable to the fan is
not connected properly.
1. Power off the ESS by referring to the user manual.
2. Check whether the cable to the fan is disconnected or
broken. If the cable is disconnected or broken, reconnect the
fan connector.
3 The fan is faulty. 1. Replace the fan by referring to the maintenance manual.
2. If the alarm persists, export logs and contact technical
support.

---

## PDF page 147

### 1.7.35 3675 Electric heater fault
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3675 Electric heater fault Major Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally, but the electric heater cannot run properly.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The cable to the
electric heater is loose
or damaged.
1. Power off the ESS by referring to the user manual.
2. Check whether the cable to the electric heater is
disconnected or broken. If the cable is disconnected or
broken, reconnect the electric heater connector.
1 2 The coolant is
insufficient.
1. Check whether a leakage occurs in the LTMS or a pipe.
2. If a leakage occurs, replace the LTMS by referring to the
maintenance manual.
1 5 The electric heater is
faulty.
1. Replace the LTMS by referring to the maintenance
manual.
2. If the alarm persists, export logs and contact technical
support.

---

## PDF page 148

### 1.7.36 3676 Electric heater power overvoltage alarm
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3676 Electric heater power overvoltage
alarm
Major Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally, but the electric heater cannot run properly.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The power supply
voltage exceeds
the upper
threshold.
1. Use a voltmeter to check whether the power supply to the
LTMS is normal.
2. If the power supply is abnormal, locate the cause and resume
the power supply.
2 The
corresponding
power detection
device is faulty.
1. Replace the auxiliary power module by referring to the
maintenance manual.
2. If the alarm persists, export logs and contact technical support.

### 1.7.37 3680 Power-side supply water temperature sensor fault
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3680 Power-side supply water
temperature sensor fault
Major Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally, but the supply water temperature on the power side
cannot be detected normally. The cooling capacity may be insufficient.
Possible Causes and Procedure
Reason
ID
No. Possible Cause Suggestion
1 1 The cable to the
temperature sensor is
loose or damaged.
1. Power off the ESS by referring to the user manual.
2. Check whether the cable to the temperature sensor is
disconnected or broken. If the cable is disconnected or broken,
reconnect the sensor connector.
2 The temperature
sensor is faulty.
1. Replace the LTMS by referring to the maintenance manual.
2. If the alarm persists, export logs and contact technical support.

---

## PDF page 149

### 1.7.38 3681 Power-side return water temperature sensor fault
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3681 Power-side return water
temperature sensor fault
Major Equipment
alarm
ADAC
### Impact on the System
The return water temperature on the power side cannot be monitored.
### Possible Cause and Solution
Reason
ID
Cause ID Possible Causes Suggestion
1 1 The cable to the
temperature sensor is
loose or damaged.
1. Power off the ESS by referring to the user manual.
2. Check whether the cable to the temperature sensor is
disconnected or broken. If the cable is disconnected or
broken, reconnect the sensor connector.
2 The temperature
sensor is faulty.
1. Replace the LTMS by referring to the maintenance
manual.
2. If the alarm persists, export logs and contact technical
support.

---

## PDF page 150

### 1.7.39 3682 Power -side supply/return water temperature sensor
abnormal
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3682 Power-side supply/return water
temperature sensor abnormal
Major Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally, but the supply/return water temperature on the power
side cannot be detected normally. The cooling capacity may be insufficient.
Possible Causes and Procedure
Reason
ID
No. Possible Cause Suggestion
1 1 The data reported from
the power -side supply
water temperature
sensor is abnormal.
1. Power off the ESS by referring to the user manual.
2. Check whether the cable to the temperature sensor is
disconnected or broken. If the cable is disconnected or broken,
reconnect the sensor connector.
2 The data reported from
the power -side return
water temperature
sensor is abnormal.
1. Check whether the cable to the temperature sensor is
disconnected or broken. If the cable is disconnected or broken,
reconnect the sensor connector.
2. If the fault persists, replace the LTMS by referring to the
maintenance manual.
3. If the alarm persists, export logs and contact technical
support.

---

## PDF page 151

### 1.7.40 3683 Battery-side supply water temperature sensor fault
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3683 Battery-side supply water
temperature sensor fault
Major Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally, but the supply water temperature on the battery side
cannot be detected. The supply water temperature may be too low.
Possible Causes and Procedure
Reason
ID
No. Possible Cause Suggestion
1 1 The cable to the
temperature sensor is
loose or damaged.
1. Power off the ESS by referring to the user manual.
2. Check whether the cable to the temperature sensor is
disconnected or broken. If the cable is disconnected or broken,
reconnect the sensor connector.
1 2 The temperature
sensor is faulty.
1. Replace the LTMS by referring to the maintenance manual.
2. If the alarm persists, export logs and contact technical support.

### 1.7.41 3684 Battery-side return water temperature sensor fault
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3684 Battery-side return water
temperature sensor fault
Major Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally, but the return water temperature on the battery side
cannot be detected.
Possible Causes and Procedure
Reason
ID
No. Possible Cause Suggestion
1 1 The cable to the
temperature sensor is
loose or damaged.
1. Power off the ESS by referring to the user manual.
2. Check whether the cable to the temperature sensor is
disconnected or broken. If the cable is disconnected or broken,
reconnect the sensor connector.
1 2 The temperature
sensor is faulty.
1. Replace the LTMS by referring to the maintenance manual.
2. If the alarm persists, export logs and contact technical support.

---

## PDF page 152

### 1.7.42 3685 Battery -side supply/return water temperature sensor
abnormal
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3685 Battery-side supply/return water
temperature sensor abnormal
Major Equipment
alarm
ADAC
### Impact on the System
The supply/return water temperature on the battery side cannot be monitored. The supply water temperature
may be high or low.
### Possible Cause and Solution
Reason
ID
Cause ID Possible Causes Suggestion
1 1 The data reported from
the battery -side supply
water temperature
sensor is abnormal.
1. Power off the ESS by referring to the user manual.
2. Check whether the cable to the supply or return water
temperature sensor on the battery side is disconnected or
broken. If the cable is disconnected or broken, reconnect the
sensor connector.
3. If the fault persists, replace the LTMS by referring to the
maintenance manual.
4. If the alarm persists, export logs and contact technical
support.

---

## PDF page 153

### 1.7.43 3686 Battery-side supply water high temperature alarm
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3686 Battery-side supply water high
temperature alarm
Major Equipment
alarm
ADAC
### Impact on the System
The system shuts down, and the LTMS shuts down.
### Possible Cause and Solution
Reason
ID
Cause ID Possible Causes Suggestion
1 1 The air filter or outdoor
heat exchanger is dirty
or blocked.
1. Power off the ESS by referring to the user manual.
2. Check whether the air filter or outdoor heat exchanger is
dirty or blocked.
3. If the air filter is dirty or blocked, clean it up or replace it.
4. If the outdoor heat exchanger is dirty or blocked, clean it
up.
1 2 The data reported from
the battery -side supply
water temperature
sensor is abnormal.
1. Check whether the cables to the temperature sensor,
multi-way valve, and water pump are disconnected or
broken. If yes, reconnect the corresponding connectors.
2. If the fault persists, replace the LTMS by referring to the
maintenance manual.
3. If the alarm persists, export logs and contact technical
support.

---

## PDF page 154

### 1.7.44 3687 Battery-side supply water low temperature alarm
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3687 Battery-side supply water low
temperature alarm
Major Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally, but condensation may occur on the pipe surface.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The diagnostic mode
runtime exceeds the
upper limit.
On the user interface, check whether the cooling function in the
diagnosis mode is enabled for a long time. If yes, exit the
diagnosis mode on the user interface and wait for the water
temperature to rise.
1 2 The data reported from
the battery -side supply
water temperature
sensor is abnormal.
1. Power off the ESS by referring to the user manual.
2. Check whether the cable to the temperature sensor is
disconnected or broken. If the cable is disconnected or broken,
reconnect the sensor connector.
3. If the fault persists, replace the LTMS by referring to the
maintenance manual.
4. If the alarm persists, export logs and contact technical
support.

---

## PDF page 155

### 1.7.45 3688 Coolant expiration alarm
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3688 Coolant expiration alarm Major Equipment
alarm
ADAC
### Impact on the System
The system reliability may be affected.
### Possible Cause and Solution
Reason
ID
Cause ID Possible Causes Suggestion
1 1 The coolant usage
duration exceeds the
upper limit.
1. Drain coolant according to the coolant drainage process in
the maintenance manual.
2. Inject coolant according to the coolant injection process in
the maintenance manual.
3. Tap on the user interface to complete the coolant
replacement process.
4. If the fault persists, check for other causes. If all possible
causes have been ruled out, contact technical support.
2 1 The coolant usage
duration exceeds the
upper limit.
1. Drain coolant according to the coolant drainage process in
the maintenance manual.
2. Inject coolant according to the coolant injection process in
the maintenance manual.
3. Tap on the user interface to complete the coolant
replacement process.
4. If the fault persists, check for other causes. If all possible
causes have been ruled out, contact technical support.

---

## PDF page 156

### 1.7.46 3689 Shutdown due to coolant expiration
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3689 Shutdown due to coolant expiration Major Equipment
alarm
ADAC
### Impact on the System
The LTMS shuts down.
### Possible Cause and Solution
Reason
ID
Cause ID Possible Causes Suggestion
1 1 The coolant usage
duration exceeds the
upper limit.
1. Drain coolant according to the coolant drainage process in
the maintenance manual.
2. Inject coolant according to the coolant injection process in
the maintenance manual.
3. Tap on the user interface to complete the coolant
replacement process.
4. If the fault persists, check for other causes. If all possible
causes have been ruled out, contact technical support.

### 1.7.47 3690 Coolant replacement not completed
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3690 Coolant replacement not completed Major Equipment
alarm
ADAC
### Impact on the System
The LTMS cannot start.
### Possible Cause and Solution
Reason
ID
Cause ID Possible Causes Suggestion
1 1 Coolant replacement is
not completed.
1. Check the coolant replacement status on the user
interface.
2. Fill coolant into the LTMS or drain coolant from the LTMS
based on the coolant replacement status by following the
coolant injection/drainage process in the maintenance
manual.
3. If the fault persists, check for other causes. If all possible
causes have been ruled out, contact technical support.

---

## PDF page 157

### 1.7.48 3705 Water pump power supply abnormal
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3705 Water pump power supply
abnormal
Major Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally, but the LTMS may fail to work properly.
Possible Causes and Procedure
Reason
ID
No. Possible Cause Suggestion
1 1 The power supply to the
water pump is abnormal.
1. Use a voltmeter to check whether the power supply to the
water pump is normal.
2. If the power supply is abnormal, locate the cause and
resume the power supply.
2 The cable to the water
pump is loose or
damaged.
1. Power off the ESS by referring to the user manual.
2. Check whether the cable to the water pump is disconnected
or broken. If the cable is disconnected or broken, reconnect the
pump cable connector.
3. If the alarm persists, export logs and contact technical
support.

---

## PDF page 158

### 1.7.49 3706 Water pump function abnormal
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3706 Water pump function abnormal Major Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally, but the LTMS may fail to work properly.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The auxiliary power
module is absent.
1. Power off the ESS by referring to the user manual.
2. Check whether the auxiliary power module is in position. If
not, reconnect the auxiliary power module.
1 2 The cable to the water
pump is loose or
damaged.
1. Power off the ESS by referring to the user manual.
2. Check whether the cable to the water pump is
disconnected or broken. If the cable is disconnected or
broken, reconnect the cable.
1 3 Air is sealed in the
water pump.
1. Manually exhaust air by referring to the maintenance
manual.
1 4 The water pump is
faulty.
1. If the fault persists after the preceding steps, replace the
LTMS by referring to the maintenance manual.
2. If the alarm persists, export logs and contact technical
support.

---

## PDF page 159

### 1.7.50 3707 Water pump fault
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3707 Water pump fault Major Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally, but the LTMS may fail to work properly.
Possible Causes and Procedure
Reason
ID
No. Possible Cause Suggestion
1 1 The water pump is faulty. 1. Replace the LTMS by referring to the maintenance manual.
2. If the alarm persists, export logs and contact technical
support.
2 1 The water pump is faulty. 1. Replace the LTMS by referring to the maintenance manual.
2. If the alarm persists, export logs and contact technical
support.
3 1 The ambient
temperature of the water
pump is too high.
1. Check whether there are abnormal heat sources around the
water pump.
2 The water pump is faulty. 1. Replace the LTMS by referring to the maintenance manual.
2. If the alarm persists, export logs and contact technical
support.

---

## PDF page 160

### 1.7.51 3715 Multi-way valve communication abnormal
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3715 Multi-way valve communication
abnormal
Major Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally, but the LTMS may fail to run properly.
Possible Causes and Procedure
Reason
ID
No. Possible Cause Suggestion
1 1 The cable to the multi -
way valve is loose or
damaged.
1. Power off the ESS by referring to the user manual.
2. Check whether the cable to the multi -way valve is
disconnected or broken. If the cable is disconnected or broken,
reconnect the multi-way valve connector.
1 3 The multi-way valve is
faulty.
1. Replace the LTMS by referring to the maintenance manual.
2. If the alarm persists, export logs and contact technical support.

---

## PDF page 161

### 1.7.52 3716 Multi-way valve power supply abnormal
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3716 Multi-way valve power supply
abnormal
Major Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally, but the LTMS may fail to run properly.
Possible Causes and Procedure
Reason
ID
No. Possible Cause Suggestion
1 1 The power supply to
the multi -way valve is
abnormal.
1. Use a voltmeter to check whether the power supply to the
multi-way valve is normal.
2. If the power supply is abnormal, locate the cause and resume
the power supply.
1 2 The cable to the multi -
way valve is loose or
damaged.
1. Power off the ESS by referring to the user manual.
2. Check whether the cable to the multi -way valve is
disconnected or broken. If the cable is disconnected or broken,
reconnect the multi-way valve connector.
3. If the alarm persists, export logs and contact technical support.

---

## PDF page 162

### 1.7.53 3717 The multi-way valve is faulty
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3717 The multi-way valve is faulty Major Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally, but the LTMS may fail to run properly.
Possible Causes and Procedure
Reason
ID
No. Possible Cause Suggestion
1 2 The multi -way valve is
faulty.
1. Replace the LTMS by referring to the maintenance manual.
2. If the alarm persists, export logs and contact technical
support.
2 1 The cable to the multi -
way valve is loose or
damaged.
1. Power off the ESS by referring to the user manual.
2. Check whether the cable to the multi -way valve is
disconnected or broken. If the cable is disconnected or broken,
reconnect the multi-way valve connector.
2 The multi -way valve is
faulty.
1. Replace the LTMS by referring to the maintenance manual.
2. If the alarm persists, export logs and contact technical
support.
3 1 The multi -way valve is
faulty.
1. Replace the LTMS by referring to the maintenance manual.
2. If the alarm persists, export logs and contact technical
support.
4 1 The multi -way valve is
faulty.
1. Replace the LTMS by referring to the maintenance manual.
2. If the alarm persists, export logs and contact technical
support.

---

## PDF page 163

### 1.7.54 3725 Water tank low liquid level alarm
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3725 Water tank low liquid level alarm Major Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally, but the coolant may be insufficient.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 2 The liquid level sensor
is faulty.
1. Power off the ESS by referring to the user manual.
2. Check whether the cable to the liquid level sensor is
disconnected or broken. If the cable is disconnected or
broken, reconnect the sensor connector.
3. If the alarm persists, replace the LTMS by referring to the
maintenance manual.
1 4 Liquid leakage occurs
in the system.
1. Check whether a leakage occurs in the LTMS or a pipe.
2. If a leakage occurs, replace the LTMS by referring to the
maintenance manual.
1 5 The coolant is
insufficient.
1. Fill coolant in the coolant tank until it is higher than the
MIN line. For details, see the coolant refilling guide in the
maintenance manual.
2. If the alarm persists, export logs and contact technical
support.

---

## PDF page 164

## 1.8 ESU
### 1.8.1 3380 RPCB Software Versions Inconsistent
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3380 RPCB Software Versions
Inconsistent
Minor Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally, but some value-added features may be unavailable.
Possible Causes and Procedure
Reason
ID
No. Possible Cause Suggestion
1 1 The software version of
the RPCB is inconsistent
with the system software
package.
1. If the component version is inconsistent with the system
software package version due to a manual update failure, the
system running is not affected. You are advised to perform the
update at a proper time.
2. If the version is inconsistent with the system software
package version due to component replacement, perform a
manual update.
3. If the update fails for several times, contact technical
support.

---

## PDF page 165

### 1.8.2 3381 Inconsistent DCDC Software Versions
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3381 Inconsistent DCDC Software
Versions
Minor Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally, but some value-added features may be unavailable.
Possible Causes and Procedure
Reason
ID
No. Possible Cause Suggestion
1 1 The software version of
the DCDC is
inconsistent with the
system software
package.
1. If the component version is inconsistent with the system
software package version due to a manual update failure, the
system running is not affected. You are advised to perform the
update at a proper time.
2. If the version is inconsistent with the system software
package version due to component replacement, perform a
manual update.
3. If the update fails for several times, contact technical support.

### 1.8.3 3382 Inconsistent PCS Software Versions
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3382 Inconsistent PCS Software
Versions
Minor Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally, but some value-added features may be unavailable.
Possible Causes and Procedure
Reason
ID
No. Possible Cause Suggestion
1 1 The software version of
the PCS is inconsistent
with the system
software package.
1. If the component version is inconsistent with the system
software package version due to a manual update failure, the
system running is not affected. You are advised to perform the
update at a proper time.
2. If the version is inconsistent with the system software
package version due to component replacement, perform a
manual update.
3. If the update fails for several times, contact technical support.

---

## PDF page 166

### 1.8.4 3384 AC Startup Conditions Not Met
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3384 AC Startup Conditions Not Met Major Environmental
alarm
ADAC
### Impact on the System
The battery rack shuts down.
Possible Causes and Procedure
Reason
ID
No. Possible Cause Suggestion
1 1 The power grid fails or
the AC power cable is
disconnected.
1. Use a multimeter to check whether the AC voltage meets the
power grid standard.
2. Use a multimeter to check whether the AC circuit is
disconnected or the AC circuit breaker is off.
2 The communications
cable is disconnected.
1. Check whether the cables to the PCS communications port,
J9 communications port on the RPCB, and CON3 and CON4
ports on the RCM are loose, disconnected, or incorrectly
connected. If yes, reconnect the cables.
2. If the cable connections are normal, check whether the PCS
power indicator is on. If the indicator is off, check the cable
connections on the DC and AC sides of the PCS.
3 Alarms are generated to
prohibit ESS discharge
or the SOC is low.
1. Clear the alarms based on the alarm handling suggestions.
2. After the alarms are cleared, if the ESS SOC is low, perform
a black start operation on the EMS or DataLogger to charge
the ESS through an external power supply, such as the PV
system or genset.
3. If the alarm persists, export logs and contact technical
support.

---

## PDF page 167

### 1.8.5 3880 AC SPD Faulty
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3880 AC SPD Faulty Minor Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally, but devices in the cabinet may not be protected against
lightning strikes.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The detection
cable is
disconnected or
the SPD of the
RCM is faulty.
1. Check whether the AC SPD signal cable of the RCM is loose
and whether the cable connector is exposed.
2. Check whether the AC SPD indicator of the RCM changes its
color or is burnt.
3. If the color has changed, replace the AC SPD.
4. If the alarm persists, export logs and contact technical support.

### 1.8.6 3881 Door Status Alarm
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3881 Door Status Alarm Minor Equipment
alarm
ADAC
### Impact on the System
Only the door status sensor generates an alarm, but the system can be charged and discharge normally.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The ESS doors
are open, or the
door status sensor
is disconnected,
faulty, incorrectly
installed, or
displaced.
1. Check whether the ESS doors are completely closed. If not,
close the doors.
2. Check whether the cable to the door status sensor or travel
switch is disconnected. If yes, connect the cable properly.
3. Check whether the door status sensor or travel switch is
displaced. If yes, move it back to the original position.
4. If not, replace the door status sensor or travel switch.
5. If the alarm persists, export logs and contact technical support.

---

## PDF page 168

### 1.8.7 3882 ESS Door Open
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3882 ESS Door Open Major Equipment
alarm
ADAC
### Impact on the System
The system is shut down.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The ESS door is open. 1. Check whether the door is completely closed. If not, close
the door completely.
2. Check whether the cable to the door limit switch is
disconnected. If yes, connect the cable properly.
3. Check whether the door status sensor is displaced or the
door panel is deformed. If yes, restore it to the original status.
4. If not, replace the sensor.
5. If the alarm persists, export logs and contact technical
support.

### 1.8.8 3883 Water Alarm
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3883 Water Alarm Major Equipment
alarm
ADMC
### Impact on the System
The system is shut down.
Possible Causes and Procedure
Reason
ID
No. Possible Cause Suggestion
1 1 Water accumulates in
the ESS or the sensor is
faulty.
1. Check whether there is water inside the ESS cabinet. If yes,
drain the water.
2. If not, replace the water sensor.
3. After the replacement, manually clear the alarm.
4. If the alarm persists, export logs and contact technical
support.

---

## PDF page 169

### 1.8.9 3884 Smoke Detector Alarm
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3884 Smoke Detector Alarm Minor Equipment
alarm
ADMC
### Impact on the System
Only the smoke detector generates an alarm, but the system can be charged and discharge normally.
Possible Causes and Procedure
Reason
ID
No. Possible Cause Suggestion
1 1 The humidity inside the
cabin is too high, the
sensor is dusty, or the
cabin is on fire.
1. Observe the system remotely for 30 minutes to check
whether other exceptions (such as abnormal battery voltage,
battery temperature, and combustible gas concentration) occur.
During the remote observation, do not approach the ESS or
open the ESS doors.
2. If no exception is found during the 30 -minute remote
observation, send trained personnel to the site and observe the
system for 30 minutes from a safe distance. If there is smoke
or fire, evacuate onsite personnel as soon as possible, call the
fire emergency service, and provide firefighters with related
product information, including the battery pack type, ESS
capacity, and battery pack location.
3. If no exception is found during remote observation and
onsite observation, open the ESS doors and check and replace
the smoke detector.

---

## PDF page 170

### 1.8.10 3885 High Concentration of Combustible Gas
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3885 High Concentration of Combustible
Gas
Major Equipment
alarm
ADMC
### Impact on the System
Gas exhaust is started. The system shuts down when the fault is serious.
Possible Causes and Procedure
Reason
ID
No. Possible Cause Suggestion
1 1 The gas concentration is
high.
1. Observe the system remotely for 30 minutes to check
whether other exceptions (such as abnormal battery voltage,
battery temperature, and combustible gas concentration) occur.
During the remote observation, do not approach the ESS or
open the ESS doors.
2. If no exception is found during the 30 -minute remote
observation, send trained personnel to the site and observe the
system for 30 minutes from a safe distance. If there is smoke
or fire, evacuate onsite personnel as soon as possible, call the
fire emergency service, and provide firefighters with related
product information, including the battery pack type, ESS
capacity, and battery pack location.
3. Do not enter the affected building or equipment area under
any circumstances, and do not open the ESS doors. Isolate
and monitor the site. Keep irrelevant personnel away from the
site.
4. After calling the fire emergency service, remotely power off
the peripheral devices (such as the Smart Transformer Station,
Smart PCS, auxiliary power supply devices, and combiner box
power supply) while ensuring your own safety.
5. After the fire is extinguished, the site must be handled by
professionals in accordance with local laws and regulations. Do
not open the ESS doors without permission.
2 The detector is faulty. If no exception is found during remote observation and onsite
observation, open the ESS doors and check and replace the
combustible gas detector.
2 1 The gas concentration is
too high.
1. Observe the system remotely for 30 minutes to check
whether other exceptions (such as abnormal battery voltage,
battery temperature, and combustible gas concentration) occur.
During the remote observation, do not approach the ESS or
open the ESS doors.
2. If no exception is found during the 30 -minute remote
observation, send trained personnel to the site and observe the
system for 30 minutes from a safe distance. If there is smoke
or fire, evacuate onsite personnel as soon as possible, call the
fire emergency service, and provide firefighters with related
product information, including the battery pack type, ESS

---

## PDF page 171

capacity, and battery pack location.
3. Do not enter the affected building or equipment area under
any circumstances, and do not open the ESS doors. Isolate
and monitor the site. Keep irrelevant personnel away from the
site.
4. After calling the fire emergency service, remotely power off
the peripheral devices (such as the Smart Transformer Station,
Smart PCS, auxiliary power supply devices, and combiner box
power supply) while ensuring your own safety.
5. After the fire is extinguished, the site must be handled by
professionals in accordance with local laws and regulations. Do
not open the ESS doors without permission.
2 The detector is faulty. If no exception is found during remote observation and onsite
observation, open the ESS doors and check and replace the
combustible gas detector.

---

## PDF page 172

### 1.8.11 3886 Combustible Gas Detector Communication Failed
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3886 Combustible Gas Detector
Communication Failed
Minor Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally, but the CO or H2 gas concentration cannot be detected.
When CO or H2 gas accumulates in the cabinet and cannot be exhausted in a timely manner, the system may
explode.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The communications
cable is disconnected
or the power supply is
abnormal.
1. Check whether the harness connector of the combustible
gas detector module and the harness connectors of the
COM1/12V port on the ESS controller are properly
connected. If not, remove and then insert the connectors.
2. Use a multimeter to check whether the communications
cable of the device is broken or exposed.
1 3 The sensor is faulty. 1. Replace the sensor.
2. If the alarm persists, export logs and contact technical
support.

### 1.8.12 3887 Combustible Gas Detector Faulty
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3887 Combustible Gas Detector Faulty Minor Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally, but the combustible gas concentration cannot be
detected. When combustible gas accumulates in the cabinet and cannot be exhausted in a timely manner, the
system may explode.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The sensor is faulty. 1. Replace the CO or H2 detector and check whether the
fault is rectified.
2. If not, contact technical support.

---

## PDF page 173

### 1.8.13 3888 Temperature and Humidity Sensor Communication
Failed
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3888 Temperature and Humidity Sensor
Communication Failed
Minor Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally, but the system temperature and humidity cannot be
detected or controlled because the communication with the temperature and humidity sensor fails.
Possible Causes and Procedure
Reason
ID
No. Possible Cause Suggestion
1 1 The communications
cable is disconnected,
the power supply is
abnormal, or the sensor
is faulty.
1. Check whether the harness connector of the sensor is
properly connected. If not, remove and then insert the
connector.
2. Use a multimeter to check whether the power supply voltage
of the sensor is normal and whether the power cable is broken.
3. If the alarm persists, replace the sensor.
4. If the alarm persists, export logs and contact technical
support.

### 1.8.14 3889 Temperature and Humidity Sensor Faulty
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3889 Temperature and Humidity Sensor
Faulty
Minor Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally, but the system temperature and humidity cannot be
detected or controlled because the temperature and humidity sensor is faulty.
Possible Causes and Procedure
Reason
ID
No. Possible Cause Suggestion
1 1 The sensor is
faulty.
1. Replace the temperature and humidity sensor and check whether
the alarm is cleared.
2. If the alarm persists, export logs and contact technical support.

---

## PDF page 174

### 1.8.15 3890 Heat Detector Alarm
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3890 Heat Detector Alarm Minor Equipment
alarm
ADMC
### Impact on the System
Only the heat detector generates an alarm, but the system can be charged and discharge normally.
Possible Causes and Procedure
Reason
ID
No. Possible Cause Suggestion
1 1 The cabinet is on
fire or the sensor
is faulty.
1. Observe the system remotely for 30 minutes to check whether other
exceptions (such as abnormal battery voltage, battery temperature,
and combustible gas concentration) occur. During the remote
observation, do not approach the ESS or open the ESS doors.
2. If no exception is found during the 30 -minute remote observation,
send trained personnel to the site and observe the system for 30
minutes from a safe distance. If there is smoke or fire, evacuate onsite
personnel as soon as possible, call the fire emergency service, and
provide firefighters with related product information, including the
battery pack type, ESS capacity, and battery pack location.
3. If no exception is found during remote observation and onsite
observation, open the ESS doors and check and replace the heat
detector.

---

## PDF page 175

### 1.8.16 3891 High Ambient Temperature Inside ESS Cabin
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3891 High Ambient Temperature Inside
ESS Cabin
Minor Equipment
alarm
ADAC
### Impact on the System
The system automatically derates. If the temperature is too high for a long time, the system may be shut
down.
Possible Causes and Procedure
Reason
ID
No. Possible Cause Suggestion
1 1 The LTMS does not work
properly or the weather
is hot.
1. Check whether an alarm is generated for the LTMS. If yes,
handle the alarm first.
2. Check whether the ESS doors are completely closed. If not,
close the doors.
3. If the alarm persists, export logs and contact technical
support.
2 1 The air conditioner does
not work properly or the
weather is hot.
1. Check whether an alarm is generated for the air conditioner
in the control unit cabin. If yes, handle the alarm first.
2. Check whether the door of the control unit cabin is
completely closed. If not, close the door.
3. If the alarm persists, export logs and contact technical
support.

---

## PDF page 176

### 1.8.17 3892 EPO Alarm
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3892 EPO Alarm Major Equipment
alarm
ADMC
### Impact on the System
The ESS, including the LTMS, shuts down.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The EPO button is
pressed.
1. Rectify the system fault first.
2. After the fault is rectified, rotate the EPO button out.
3. Start the ESS on the user interface.
2 The feedback cable to
the EPO button is
disconnected.
1. Check whether the cable to the EPO button is
disconnected or whether the cable connector is exposed.
2. If not, use a multimeter to check whether the cable to the
EPO button is broken.
3. If the alarm persists, replace the EPO button.

---

## PDF page 177

### 1.8.18 3893 Fire Alarm
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3893 Fire Alarm Major Equipment
alarm
ADMC
### Impact on the System
The ESS cabinet and LTMS shut down, and the system cannot run properly.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The electrical circuit or
battery is on fire.
1. If there is smoke or fire, evacuate onsite personnel as
soon as possible, and call the fire emergency service. Notify
professional firefighters and provide them with relevant
product information, including the battery pack type, ESS
capacity, and battery pack location.
2. Do not enter the affected building or equipment area under
any circumstances, and do not open the ESS doors. Isolate
and monitor the site. Keep irrelevant personnel away from
the site.
3. After calling the fire emergency service, remotely power
off the peripheral devices (such as the Smart Transformer
Station, Smart PCS, auxiliary power supply devices, and
combiner box power supply) while ensuring your own safety.
4. After the fire is extinguished, the site must be handled by
professionals in accordance with local laws and regulations.
Do not open the ESS doors without permission.

---

## PDF page 178

### 1.8.19 3894 Exhaust Fan Faulty
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3894 Exhaust Fan Faulty Minor Equipment
alarm
ADAC
### Impact on the System
When CO or H2 gas accumulates in the cabinet, the gas cannot be exhausted in a timely manner. As a result,
the system may explode.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The fan power input or
feedback cable is
abnormal.
1. Check whether the power input cable and control cable of
the exhaust fan are disconnected or whether the cable
connectors are exposed.
2. If yes, reconnect the cables.
3. If not, use a multimeter to check whether the cables are
broken.
2 The fan is faulty. 1. Check whether the fan is damaged or burnt. If yes, replace
the fan.
2. If the alarm persists, export logs and contact technical
support.

---

## PDF page 179

### 1.8.20 3895 Devices Connected and System Configuration
Inconsistent
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3895 Devices Connected and System
Configuration Inconsistent
Major Equipment
alarm
ADAC
### Impact on the System
If the number of some components is inconsistent with the system configuration, the system can be started. If
the number of key components is inconsistent with the system configuration, the system cannot be started.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The number of battery
packs is incorrectly set.
1. Check whether the number of battery packs configured on
the user interface is consistent with the number of battery
packs installed onsite.
2 The BMU
communication is
abnormal or the BMU
is faulty.
1. Check whether the communications cable between the
COM-IN/COM-OUT port on the pack and the
CON_IN/CON_OUT port on the RCM is loose, disconnected,
or incorrectly connected. If yes, rectify the cable connection
fault.
2. If the alarm persists, export logs and contact technical
support.
2 1 The CAN
communication of the
balancing module is
abnormal or the
balancing module is
faulty.
1. Check whether the communications cable between the
COM-IN/COM-OUT port on the pack and the
CON_IN/CON_OUT port on the RCM is loose, disconnected,
or incorrectly connected. If yes, rectify the cable connection
fault.
2. Check whether the number of battery packs configured on
the user interface is consistent with the number of battery
packs installed onsite.
3. If the alarm persists, export logs and contact technical
support.
3 1 The CAN
communication of the
RPCB is abnormal or
the RPCB is faulty.
1. Check whether the communications cable is loose,
disconnected, or incorrectly connected. If yes, reconnect the
cable.
2. If not, replace the RCM.
3. If the alarm persists, export logs and contact technical
support.
4 1 The CAN
communication of the
DCDC is abnormal or
the DCDC is faulty.
1. Check whether the cable between the COM port on the
DCDC and the CON4 port on the RCM is loose,
disconnected, or incorrectly connected. If yes, reconnect the
cable.
2. Check whether the number of configured DCDCs is
consistent with the actual number by referring to the

---

## PDF page 180

component description in the user manual. If not, configure
the DCDCs correctly.
3. If the alarm persists, export logs and contact technical
support.
5 1 The CAN
communication of the
PCS is abnormal or the
PCS is faulty.
1. Check whether the cable between the communications
port on the PCS and the CON3 port on the RCM is loose,
disconnected, or incorrectly connected. If yes, reconnect the
cable.
2. Check whether the number of configured PCSs is
consistent with the actual number by referring to the
component description in the user manual. If not, configure
the PCSs correctly.
3. If the alarm persists, export logs and contact technical
support.
6 2 The Ethernet
communication of the
LCC is abnormal, or
the LCC is faulty or
missing.
1. Check whether the cable between the FE_1 or FE_2 port
on the LCC and the LAN3 port on the BCU is loose,
disconnected, or incorrectly connected. If yes, reconnect the
cable.
2. Check whether the LCC is powered on. If not, rectify the
power supply fault.
3. Check whether the number of configured LCCs is
consistent with the actual number by referring to the
component description in the user manual. If not, configure
the LCCs correctly.
4. If the alarm persists, export logs and contact technical
support.
7 1 The Ethernet
communication of the
LCC is abnormal, or
the LCC is faulty or
missing.
1. Check whether the cable between the FE_1 or FE_2 port
on the LCC and the LAN3 port on the BCU is loose,
disconnected, or incorrectly connected. If yes, reconnect the
cable.
2. Check whether the LCC is powered on. If not, rectify the
power supply fault.
3. Check whether the number of configured LCCs is
consistent with the actual number by referring to the
component description in the user manual. If not, configure
the LCCs correctly.
4. If the alarm persists, export logs and contact technical
support.
8 1 The RS485
communication of the
display module is
abnormal or the
display module is
faulty.
1. Check whether the communications cable between the
RS485 port on the display module and the COM3 port on the
RCM is loose, disconnected, or incorrectly connected. If yes,
reconnect the cable.
2. Check whether the display module is powered on. If not,
rectify the power supply fault.
3. Check whether the number of configured display modules
is consistent with the actual number by referring to the
component description in the user manual. If not, configure
the display modules correctly.
4. If the alarm persists, export logs and contact technical
support.
9 1 The communication of 1. Check whether the communications cable between the

---

## PDF page 181

the fire suppression
system is abnormal or
the fire suppression
system is faulty.
485A/485B port on the fire suppression system and the
CON5 port on the CMU is loose, disconnected, or incorrectly
connected. If yes, reconnect the cable.
2. Check whether the fire suppression system is powered on.
If not, rectify the power supply fault.
3. Check whether the number of configured fire suppression
systems is consistent with the actual number by referring to
the component description in the user manual. If not,
configure the fire suppression systems correctly.
4. If the alarm persists, export logs and contact technical
support.
10 1 The RS485
communication of the
temperature and
humidity sensor is
abnormal or the
temperature and
humidity sensor is
faulty.
1. Check whether the communications cable is loose,
disconnected, or incorrectly connected. If yes, reconnect the
cable.
2. Check whether the temperature and humidity sensor is
powered on. If not, rectify the power supply fault.
3. Check whether the number of configured temperature and
humidity sensors is consistent with the actual number by
referring to the component description in the user manual. If
not, configure the temperature and humidity sensors
correctly.
4. If the alarm persists, export logs and contact technical
support.
11 1 The combustible gas
detector is faulty or the
communication is
abnormal.
1. Check whether the cable to the COM1/12V or COM2/12V
port of the ESS controller is loose, disconnected, or
incorrectly connected. If yes, reconnect the cable.
2. Check whether the combustible gas detector is powered
on. If not, rectify the power supply fault.
3. Check whether the number of configured combustible gas
detectors is consistent with the actual number by referring to
the component description in the user manual. If not,
configure the combustible gas detectors correctly.
4. If the alarm persists, export logs and contact technical
support.

---

## PDF page 182

### 1.8.21 3900 High Relative Humidity Inside ESS Cabin
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3900 High Relative Humidity Inside ESS
Cabin
Minor Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally, but there is a risk of condensation.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 Dehumidification fails. 1. Ensure that the temperature control mode is set to
automatic.
2. Check whether the LTMS is normal and whether the ESS
doors are completely closed.
3. If the alarm persists, export logs and contact technical
support.

### 1.8.22 3901 Offering Software Update Package Not Backed Up
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3901 Offering Software Update Package
Not Backed Up
Warning Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The software update
package is not backed
up or the backup
package is lost.
Download the latest software update package and perform
an update.

---

## PDF page 183

### 1.8.23 3902 Inconsistent Display Module Software Versions
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3902 Inconsistent Display Module
Software Versions
Minor Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally, but some value-added features may be unavailable.
Possible Causes and Procedure
Reason
ID
No. Possible Cause Suggestion
5 1 The software version of
the Display Module is
inconsistent with the
system software
package.
1. If the component version is inconsistent with the system
software package version due to a manual update failure, the
system running is not affected. You are advised to perform the
update at a proper time.
2. If the version is inconsistent with the system software
package version due to component replacement, perform a
manual update.
3. If the update fails for several times, contact technical
support.

---

## PDF page 184

### 1.8.24 3903 E-label Board Data Abnormal
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3903 E-label Board Data Abnormal Major Equipment
alarm
ADAC
### Impact on the System
The system is shut down.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The differentiated data
backed up on the ESS
controller is
inconsistent with that
on the e -label board of
the system, or some
data is damaged.
1. If the ESS controller has been replaced, replace it on the
"Device Replacement" page of the DataLogger WebUI.
2. If only the e -label is replaced or no spare part is replaced,
check the ESS SN on the label and connect to the
FusionSolar app beside the ESS.
3. On the alarm screen of the app, tap "Proceed" to go to the
SN confirming screen and select the SN displayed on the
device label. If the SN is not the one displayed on the device
label, data errors may occur and safety risks may occur
during system running.
4. After the SN is confirmed, the device automatically
synchronizes data and restarts.
5. If the alarm persists, contact technical support.
2 1 The differentiated data
backed up on the ESS
controller and that on
the e-label board of the
system is damaged.
1. If both the ESS controller and e -label board are replaced,
replace them on the "Device Replacement" page of the
DataLogger WebUI.
2. If the alarm persists, contact technical support.
3 1 The cable connection
to the e -label board is
abnormal, or the e -
label board is faulty.
1. Power off the ESS by referring to the user manual.
2. Remove the RCM and reconnect the cable to the e -label
board.
3. After the check is complete, reinstall the RCM, and power
on the ESS by referring to the user manual.
4. If the alarm persists, export logs and contact technical
support.

---

## PDF page 185

### 1.8.25 3904 Certificate About to Expire
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3904 Certificate About to Expire Minor Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The northbound
communication
certificate is about to
expire or the system
time is incorrect.
1. Check whether the time of the ESS is consistent with the
local time on the user interface. If not, set the time on the
user interface to the local time. If yes, go to the next step.
2. Apply for a new certificate from the CA and update the
certificate on the local app. If the alarm persists, contact
technical support.
2 1 The certificate used for
app communication is
about to expire or the
system time is
incorrect.
1. Check whether the time of the ESS is consistent with the
local time on the user interface. If not, set the time on the
user interface to the local time. If yes, go to the next step.
2. Apply for a new certificate from the CA and update the
certificate on the local app. If the alarm persists, contact
technical support.
3 1 The southbound
communication
certificate is about to
expire or the system
time is incorrect.
1. Check whether the time of the ESS is consistent with the
local time on the user interface. If not, set the time on the
user interface to the local time. If yes, go to the next step.
2. Apply for a new certificate from the CA and update the
certificate on the local app. If the alarm persists, contact
technical support.

---

## PDF page 186

### 1.8.26 3905 Certificate Expired
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3905 Certificate Expired Minor Equipment
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The northbound
communication
certificate has expired
or the system time is
incorrect.
1. Check whether the time of the ESS is consistent with the
local time on the user interface. If not, set the time on the
user interface to the local time. If yes, go to the next step.
2. Apply for a new certificate from the CA and update the
certificate on the local app. If the alarm persists, contact
technical support.
2 1 The certificate used for
app communication
has expired or the
system time is
incorrect.
1. Check whether the time of the ESS is consistent with the
local time on the user interface. If not, set the time on the
user interface to the local time. If yes, go to the next step.
2. Apply for a new certificate from the CA and update the
certificate on the local app. If the alarm persists, contact
technical support.
3 1 The southbound
communication
certificate has expired
or the system time is
incorrect.
1. Check whether the time of the ESS is consistent with the
local time on the user interface. If not, set the time on the
user interface to the local time. If yes, go to the next step.
2. Apply for a new certificate from the CA and update the
certificate on the local app. If the alarm persists, contact
technical support.

---

## PDF page 187

### 1.8.27 3906 Communication with Upper-layer Controller Abnormal
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3906 Communication with Upper -layer
Controller Abnormal
Major Equipment
alarm
ADAC
### Impact on the System
The ESS shuts down because it does not receive scheduling instructions from the upper-layer controller.
Possible Causes and Procedure
Reason
ID
No. Possible Cause Suggestion
1 1 The communications
cable is incorrectly
connected, the network
is disconnected, or the
upper-layer controller is
abnormal.
1. Check whether you can log in to the user interface of the
upper-layer controller to determine whether the upper -layer
controller is running properly. Troubleshoot the upper -layer
controller if it is abnormal.
2. Check whether the communications cable between the ESS
and the upper -layer controller is loose, disconnected, or
incorrectly connected. If yes, reconnect the cable.
3. Check whether other GE or LAN ports of the ESS are
incorrectly connected. If yes, reconnect the cables.
4. Check whether the IP addresses of the ESS and the upper -
layer controller are in the same network segment. If not,
configure them in the same network segment.
5. If the alarm persists, export logs and contact technical
support.

---

## PDF page 188

### 1.8.28 3908 Component End of Life
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3908 Component End of Life Warning Equipment
alarm
ADAC
### Impact on the System
The system is charged and discharges normally.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 The 10 -year service
life of a component
expires.
1. Replace the sensor (such as the heat detector, smoke
detector, combustible gas sensor, or fire alarm horn/strobe)
by referring to the maintenance manual.
2. Set "Replace component at end of 10 -year life" to
"Complete" on the user interface.
3. If the alarm persists, export logs and contact technical
support.
1 2 The 10 -year service
life of a component
expires.
1. Replace the component by referring to the list of
components to be replaced after the 10 -year service life
expires in the maintenance manual.
2. Set "Replace component at end of 10 -year life" to
"Complete" on the user interface.
3. If the alarm persists, export logs and contact technical
support.
2 1 The 5 -year service life
of a component
expires.
1. Replace the component by referring to the list of
components to be replaced after the 5 -year service life
expires in the maintenance manual.
2. Set "Replace component at end of 5 -year life" to
"Complete" on the user interface.
3. If the alarm persists, export logs and contact technical
support.

---

## PDF page 189

### 1.8.29 3910 Auxiliary Power Meter Communication Abnormal
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3910 Auxiliary Power Meter
Communication Abnormal
Minor Communications
alarm
ADAC
### Impact on the System
The ESS works properly, but the auxiliary power meter data cannot be obtained.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 2 The communications
cable is improperly
connected or the
meter is faulty.
1. Remove the RCM. Check whether the communications cable
between the RS485 port of the meter and the J10 port of the BCU
is loose, disconnected, or incorrectly connected. If yes, reconnect
the cable.
2. Check whether the meter is powered on. If not, rectify the
power supply fault.
3. If the alarm persists, export logs and contact technical support.

### 1.8.30 3911 Display Module Communication Failure
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3911 Display Module Communication
Failure
Minor Communications
alarm
ADAC
### Impact on the System
The system can be charged and discharge normally, but the SOC indicator and status indicator on the cabinet
door cannot correctly indicate the corresponding status.
Possible Causes and Procedure
Reason
ID
No. Possible Cause Suggestion
1 1 The communications
cable is disconnected
or the display module
is faulty.
1. Check whether the communications cable between the RS485
port on the display module and the COM3 port on the RCM is
loose, disconnected, or incorrectly connected. If yes, reconnect
the cable.
2. Check whether the display module is powered on. If not, rectify
the power supply fault.
3. If the alarm persists, export logs and contact technical support.

---

## PDF page 190

### 1.8.31 3912 Startup Authorization Not Obtained
### Attribute
Alarm ID Alarm Name Alarm Severity Alarm Type Clearance
Category
3912 Startup Authorization Not Obtained Major Equipment
alarm
ADAC
### Impact on the System
The ESS is not started.
### Possible Cause and Solution
Reason
ID
No. Possible Cause Suggestion
1 1 Startup authorization is
not obtained for the
ESS.
Contact technical support to perform startup authorization.

---

## PDF page 191

## Acronyms and abbreviations
A
APP Application

B
BCU Battery Control Unit
BMU Battery Monitoring Unit

D
DCDC DC-DC Converter

E
EPO Emergency Power-off
ESR Energy Storage Rack
ESS Energy Storage System

F
FE fast Ethernet
FPC Flexible Printed Circuit

I
IO Input&Output

L
LAN local area network
LCC liquid cooling controller
LED light-emitting diode
LTMS liquid thermal management system

M

---

## PDF page 192

MBUS Monitoring Bus

N
NTC Negative Temperature Coefficient

P
PACK Battery Pack
PCS Power Converter System
PTC Positive Temperature Coefficient

R
RCCB Residual Current Circuit Breaker
RCM Rack Control Module
RST reset

S
SFP small form-factor pluggable
SIM subscriber identity module
SN serial number
SOC State of Charge

U
UPS Uninterruptible Power System

W
WAN wide area network

---

## PDF page 193

For more information
please contact
your local FIMER
representative or visit:

fimer.com
We reserve the right to make technical changes or
modify the contents of this document without prior notice.
Regarding purchase orders, the agreed particulars shall
prevail. MA Solar Italy does not accept any responsibility
whatsoever for potential errors or possible lack of
information in this document.
We reserve all rights in this document and in the subject
matter and illustrations contained therein. Any
reproduction, disclosure to third parties or utilization of its
contents – in whole or in parts – is forbidden without
prior written consent of MA Solar Italy. Copyright© 2025
MA Solar Italy. All rights reserved.
PVX-(107-241) Series Alarm Manual REV_A 14.05.2026
