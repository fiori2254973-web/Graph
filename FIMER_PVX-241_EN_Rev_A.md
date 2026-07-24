# C&I Storage system - PVX-241

Source PDF: `FIMER_PVX-241_EN_Rev_A.pdf`  
Revision: `PVX-241_EN REVA 29.04.2026`

## Overview

This new Energy Storage System is a modular solution with Hybrid Cooling and nominal capacity up to 241 kWh.

It is designed to offer an innovative and flexible solar solution for commercial and industrial applications.

Nominal energy: **241 kWh**

## Technical data

Model: **PVX-241**

### System data (PCS + Battery Packs)

| Parameter | Value |
| --- | --- |
| Nominal energy | 241.0 kWh |
| Nominal capacity | 314 Ah |
| Maximum cycle rate | 0.45 CP |
| Rated voltage | 768 V |
| Operative voltage range | 648-852 V |
| Maximum current | 221.2 A |

### Battery parameters

| Parameter | Value |
| --- | --- |
| Battery pack model | ESM-60-2E1 |
| Cell chemistry | LPF |
| Number of battery packs | 4 |
| Rated voltage | 192 V |
| Reted current | 140 A |
| Carching/Discharging Power | 26.88 kW |
| Maximum charge/discharging current | 183 A |
| Intra-battery rack balancing mode | Battery pack-level active balancing |

### PCS parameters (AC)

| Parameter | Value |
| --- | --- |
| DCDC model | - |
| DCDC configuration of a battery rack | - |
| PCS model | PCS-108K-MB1 |
| Three-phase three-wire or three-phase four-wire | Supported |
| Rated mains voltage | 380 V/400 V/415 V |
| Maximum power | 140.4 kW |

### Rated charge and discharge current

| Condition | 380 VAC | 400 VAC | 415 VAC |
| --- | --- | --- | --- |
| Rated charge and discharge current of the system | 164.1 A | 155.9 A | 150.3 A |
| 1.1 times overload | 180.5 A | 171.5 A | 165.3 A |
| 1.2 times overload | 197.0 A (1 min) | 187.1 A (1 min) | 180.4 A (1 min) |
| 1.3 times overload | 213.4 A (5s) | 202.7 A (5s) | 195.4 A (5s) |

### Communication

| Parameter | Value |
| --- | --- |
| System communications port | Ethernet/Optical fiber (optional)/RS485 |
| System communications protocol | Modbus TCP |

### Environmental

| Parameter | Value |
| --- | --- |
| IP rating | IP55 |
| Operating temperature range | -30 deg C to +55 deg C (derated above 50 deg C) |
| Storage temperature range | -35 deg C to +60 deg C |
| Operating humidity range | 0-100% RH (non-condensing) |
| Maximum operating altitude | 4000 m |
| Noise limit (rated working conditions) | <= 65 dB |

### General specification

| Parameter | Value |
| --- | --- |
| Battery temperature control mode | Liquid cooling |
| LTMS model | TMS-H008SG00 |
| LTMS quantity | 1 |
| Dimensions (W x D x H) | 1150 mm x 1800 mm x 2100 mm |
| Weight | <= 2.8 t |
| Surge protection | Type II (AC port) |
| Auxiliary mains power supply | 176-300 V AC, single-phase, dual-live wire <= 5 kVA @ 0.45CP |
| Auxiliary power loss in standby mode (LTMS not started) | <= 150.0 W |
| Thermal runaway suppression system | Aerosol (>= 110 g) |
| Maximum efficiency | 91,30% |

### Standards compliance

| Parameter | Value |
| --- | --- |
| Marking | RoHS 6 |
| EMC | Class B |
| Safety Certifications | GB/T 36276, IEC 62619, IEC 62477-1; IEC 61000-3-12, etc. |

## Remarks

- Features not specifically listed in the present data sheet are not included in the product.
- Please refer to FIMER's Solar page for further details.

## Legal notice

We reserve the right to make technical changes or modify the contents of this document without prior notice. With regard to purchase orders, the agreed particulars shall prevail. MA Solar Italy srl does not accept any responsibility whatsoever for potential errors or possible lack of information in this document.

For more information please contact your local MA Solar Italy srl. representative or visit: <https://fimer.com>

We reserve all rights in this document and in the subject matter and illustrations contained therein. Any reproduction, disclosure to third parties or utilization of its contents - in whole or in parts - is forbidden without prior written consent of MA Solar Italy srl.

Copyright 2025 MA Solar Italy srl. All rights reserved.

## Conversion notes

- Text was extracted from the PDF with `pypdf`.
- Technical values were reorganized into Markdown tables.
- Source spelling was preserved for labels such as `Reted current` and `Carching/Discharging Power`.
- Symbols from the PDF were normalized to ASCII where useful for Markdown portability, for example `<=`, `>=`, `deg C`, and hyphen ranges.
