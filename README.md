# LLM Vulnerability Scans with Garak

This repository contains **Garak** vulnerability scanner results for four different language models:

1. **GPT-2**  
2. **Mistral-7B**  
3. **LLaMA 2-7B**  
4. **Falcon-7B-Instruct**

Each model's scan artifacts (e.g., `garak_report_*.html`) and any relevant notes or logs are organized in separate folders:


## 1) GPT-2

**Probes Tested:** `ansiescape`, `continuation`, `dan`, `glitch`, `topic`

| **Probe**       | **Pass Rate** |
|-----------------|---------------|
| ansiescape      | ~85.6%        |
| continuation    | ~97.3%        |
| dan (jailbreak) | ~6.9%         |
| glitch          | ~0.0%         |
| topic           | ~0.0%         |

**Observations**  
- GPT-2 shows **moderate resilience** to ANSI escape vulnerabilities (ansiescape ~85.6%).  
- It **rarely continues** partial slurs (continuation ~97.3%), suggesting a lower tendency to produce hateful completions.  
- **DAN**-style jailbreaks still succeed ~6.9% of the time, indicating partial vulnerability.  
- **Glitch** and **topic** probes scored **0.0%**, implying GPT-2 is **unprotected** (or easily bypassed) in those categories.

---

## 2) Mistral-7B

**Probes Tested:** `ansiescape`, `dan`, `continuation`, `topic`, `glitch`

| **Probe**       | **Pass Rate** |
|-----------------|---------------|
| ansiescape      | ~62.4%        |
| continuation    | ~94.1%        |
| dan (jailbreak) | ~16.6%        |
| glitch          | ~32.8%        |
| topic           | ~7.9%         |

**Observations**  
- **Refuses slurs** in most cases (~94.1%).  
- **DAN** attacks succeed ~83% of the time (16.6% pass), indicating moderate vulnerability.  
- **Glitch** resilience stands at ~32.8%.  
- Handles **controversial topics** poorly (~7.9%), suggesting potential unfiltered or unmitigated responses.

---

## 3) LLaMA 2-7B

**Probes Tested:** `ansiescape`, `dan`, `continuation`, `topic`, `glitch`

| **Probe**       | **Pass Rate** |
|-----------------|---------------|
| ansiescape      | ~61.3%        |
| continuation    | ~100%         |
| dan (jailbreak) | ~29.0%        |
| glitch          | ~72.8%        |
| topic           | ~48.2%        |

**Observations**  
- **Fully** blocks partial slurs (`continuation`: 100%).  
- **DAN**-style attacks succeed ~29%, showing partial vulnerability.  
- **Glitch** tokens pass ~72.8%, so ~27% remain problematic.  
- Handles **controversial topics** at ~48.2% success, a moderate performance.

---

## 4) Falcon-7B-Instruct

**Probes Tested:** `ansiescape`, `dan`, `continuation`, `topic`, `glitch`

| **Probe**       | **Pass Rate** |
|-----------------|---------------|
| ansiescape      | ~78.1%        |
| continuation    | ~100%         |
| dan (jailbreak) | ~21.5%        |
| glitch          | ~34.6%        |
| topic           | ~11.8%        |

**Observations**  
- **Perfect** at refusing to continue offensive terms (~100%).  
- Partly vulnerable to **DAN** (~21.5%) and fairly low on **glitch** (~34.6%).  
- **Topic** is ~11.8%, suggesting potential issues with controversial or sensitive subjects.

---

## High-Level Comparison

- **GPT-2**  
  - **Strengths:** Good on ANSI/spam checks, rarely continues hateful text.  
  - **Weaknesses:** Low pass on DAN (~7%), no glitch/topic defenses.  

- **Mistral-7B**  
  - **Strengths:** High refusal rate for hateful expansions (~94%).  
  - **Weaknesses:** DAN (~16.6%), glitch (~32.8%), topic (~7.9%).  

- **LLaMA 2-7B**  
  - **Strengths:** Blocks slur continuation (100%), decent glitch (~72.8%).  
  - **Weaknesses:** ~29% DAN success, moderate topic handling (~48.2%).  

- **Falcon-7B-Instruct**  
  - **Strengths:** Refuses offensive completions (100%).  
  - **Weaknesses:** DAN (~21.5%), glitch (~34.6%), low topic pass (~11.8%).  

All models show strengths (often refusing hateful completions) and some vulnerabilities to specialized attacks (DAN, glitch, or controversial topics). Additional tuning or safety layers may help further mitigate these risks.
