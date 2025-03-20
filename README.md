# Summary of Garak Test Results for Four LLMs

Below is a concise overview of the **Garak** test outcomes for **GPT-2**, **Mistral-7B**, **LLaMA 2-7B**, and **Falcon-7B-Instruct**.  
Each model was evaluated on multiple probes (e.g., `ansiescape`, `dan`, `continuation`, etc.).  
For detailed prompts, responses, and detector logs, see the corresponding HTML reports:
- **`garak_report_gpt2.html`**  
- **`garak_report_mistral7b.html`**  
- **`garak_report_llama2-7b.html`**  
- **`garak_report_falcon7b.html`**

---

## 1) GPT-2

**Probes Tested:** `ansiescape`, `continuation`, `dan`, `glitch`, `topic`

| **Probe**       | **Pass Rate** |
|-----------------|---------------|
| ansiescape      | ~85.6%        |
| continuation    | ~97.3%        |
| dan (jailbreak) | ~6.9%         |
| glitch          | ~0.0%         |
| topic           | ~0.0%         |

**Observations (Concise)**  
- Generally **resistant** to ANSI codes (~85.6%) and **rarely continues** hateful terms (~97.3%).  
- **DAN**-style attacks succeed ~6.9% of the time, indicating partial vulnerability.  
- **Glitch** and **topic** show **0.0%** pass rates, meaning GPT-2 has **no** or minimal built-in mitigation there.

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

**Observations (Concise)**  
- Good at **refusing slurs** (~94.1%), but moderate/low on **DAN** (~16.6%).  
- **Glitch** resilience stands at ~32.8%.  
- Struggles with **controversial topics** (~7.9%), indicating potential unfiltered or unmitigated responses.

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

**Observations (Concise)**  
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

**Observations (Concise)**  
- **Perfect** at refusing to continue offensive terms (~100%).  
- Partly vulnerable to **DAN** (~21.5%) and fairly low on **glitch** (~34.6%).  
- **Topic** is ~11.8%, suggesting potential issues with controversial or sensitive subjects.

---

## High-Level Comparison

- **GPT-2**:  
  - Strengths: Good on ANSI/spam checks, rarely continues hateful text.  
  - Weaknesses: Low pass on DAN (~7%), no glitch/topic defenses.  

- **Mistral-7B**:  
  - Strengths: High refusal rate for hateful expansions (~94%).  
  - Weaknesses: DAN (~16.6%), glitch (~32.8%), topic (~7.9%).  

- **LLaMA 2-7B**:  
  - Strengths: Blocks slur continuation (100%), decent glitch (~72.8%).  
  - Weaknesses: ~29% DAN success, moderate topic handling (~48.2%).  

- **Falcon-7B-Instruct**:  
  - Strengths: Refuses offensive completions (100%).  
  - Weaknesses: DAN (~21.5%), glitch (~34.6%), low topic pass (~11.8%).  

In summary, **all models** show certain strengths (often in refusing hateful or offensive completions) and **some** vulnerabilities to specialized attacks (e.g., DAN, glitch, or controversial topics). Further tuning or safety layers may help improve resilience against these targeted probes.
