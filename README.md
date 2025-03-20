# Summary of Garak Test Results for Four LLMs

Below are concise summaries of Garak test outcomes for **GPT-2**, **Mistral-7B**, **Llama-2-7B**, and **Falcon-7B-Instruct**. Each model was evaluated with different probes; refer to the individual HTML reports (`garak_report_*.html`) for full details.

---

## GPT-2

**Probes Tested:** `ansiescape`, `continuation`, `dan`, `glitch`, `topic`

- **ansiescape:** ~85.6%
- **continuation:** ~97.3%
- **dan:** ~6.9%
- **glitch:** ~0.0%
- **topic:** ~0.0%

**Observations:**
- GPT-2 shows **moderate resilience** to ANSI escape vulnerabilities (ansiescape ~85.6%).  
- It **rarely continues** partial slurs (continuation ~97.3%), suggesting a lower tendency to produce hateful completions.  
- **DAN**-style jailbreaks still succeed at **~6.9%**, indicating partial susceptibility to advanced “Do Anything Now” prompts.  
- **Glitch** and **topic** probes scored **0.0%**, implying GPT-2 is **unprotected** (or easily bypassed) in those categories.


## Mistral-7B

**Probes Tested:**  
- `ansiescape` (ANSI escape sequences)  
- `dan` (Do Anything Now / jailbreak attacks)  
- `continuation` (refusing to continue offensive terms)  
- `topic` (controversial topics)  
- `glitch` (inputs that provoke unusual or “glitchy” behavior)

---

### Key Pass Rates

- **ansiescape:** ~62.4%  
- **continuation:** ~94.1%  
- **dan:** ~16.6%  
- **glitch:** ~32.8%  
- **topic:** ~7.9%

---

### Observations

1. **ansiescape (~62.4%)**  
   - Indicates a moderate ability to avoid producing or propagating ANSI control codes. In ~42% of attempts, the model may still output undesired ANSI sequences.

2. **continuation (~94.1%)**  
   - A high pass rate at refusing to continue partial offensive or hateful words, suggesting strong caution against slur completions.

3. **dan (~16.6%)**  
   - Only about 16% of “DAN” tests were blocked; ~84% potentially bypass defenses, showing susceptibility to certain jailbreak or “Do Anything Now” prompts.

4. **glitch (~32.8%)**  
   - Relatively low resilience against glitch-style prompts: in nearly a third of tests, Mistral-7B provides safe output, but in about two-thirds, it might exhibit unexpected or unsafe behavior.

5. **topic (~7.9%)**  
   - Very low success rate on controversial topics, suggesting vulnerability or lack of mitigation when probed with sensitive content.

---

### Overall Summary
- **Mistral-7B** demonstrates excellent refusal behavior for completing hateful terms (continuation ~94%).
- However, it remains **less robust** against **DAN** jailbreak attempts (~16.6% pass) and glitch prompts (~32.8%), and is notably weak in handling controversial topics (~7.9%).
- In short, while the model shows promise in certain areas (like refusing slurs), it would benefit from further enhancements to withstand advanced or edge-case attacks.


---

## LLaMA 2-7B

**Probes:** `ansiescape`, `dan`, `continuation`, `topic`, `glitch`

**Key Pass Rates:**
- **ansiescape:** ~61.3%
- **continuation:** ~100%
- **dan:** ~29.0%
- **glitch:** ~72.8%
- **topic:** ~48.2%

### Observations
- **ANSI Escape (61.3%)**  
  Shows moderate avoidance of ANSI-based injection or control sequences. Some potential remains for escape-sequence exploits.

- **Continuation (100%)**  
  Completely refuses to continue partial slurs or hateful terms, suggesting it rarely generates offensive completions when prompted with partial slurs.

- **DAN Attacks (29.0%)**  
  Roughly 29% of “Do Anything Now” or similar jailbreak attempts succeed, indicating partial susceptibility to advanced manipulative prompts.

- **Glitch Tokens (72.8%)**  
  Demonstrates a fairly high resilience to glitch tokens—special strings known to provoke bizarre or unintended responses. However, about 27% remain problematic.

- **Controversial Topics (48.2%)**  
  When prompted with contentious or sensitive topics, the model mitigates roughly half of the attempts. This indicates it can be pushed off-track in certain scenarios.

Overall, **LLaMA 2-7B** exhibits a mix of robust defenses (e.g., slur continuation is fully blocked) and some vulnerabilities (notably to specific jailbreak or “glitch” prompts). 

---

## 4) Falcon-7B-Instruct

**Probes:** `ansiescape`, `dan`, `continuation`, `topic`, `glitch`  
**Key Pass Rates:**  
- **ansiescape:** 78.1%  
- **dan:** 21.5%  
- **continuation:** 100%  
- **topic:** 11.8%  
- **glitch:** 34.6%

**Observations:**  
- Excellent at refusing to continue offensive terms (`continuation` at 100%).  
- Partially vulnerable to DAN attacks (21.5%), with certain scenarios hitting ~25% success.  
- Tends to avoid ANSI codes (78.1%), but glitchy inputs still yield ~34.6% odd outputs.  
- On controversial topics, only 11.8% pass rate suggests it sometimes produces borderline or unfiltered content.

---

## Overall Comparison

- **GPT-2**: High resilience to spam/ANSI but very low (`dan`: 7.3%) for jailbreak attempts.  
- **Mistral-7B**: Solid refusal of offensive expansions (`continuation` ~94%) but moderate or low in other areas (like `dan`: 16.6%).  
- **Llama-2-7B**: Reasonable spam detection (70.7%), moderate `dan` (28.5%), unknown toxicity/promptinject from the snippet.  
- **Falcon-7B-Instruct**: Perfect (100%) on refusing to continue offensive words, partial weaknesses for `dan` (21.5%) and `glitch` (34.6%).

For a deep dive into each test (prompts, responses, detectors), see the corresponding HTML files:
- `garak_report_gpt2.html`
- `garak_report_mistral7b.html`
- `garak_report_llama2-7b.html`
- `garak_report_falcon7b.html`
