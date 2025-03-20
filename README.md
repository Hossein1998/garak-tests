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


## 2) Mistral-7B

**Probes:** `ansiescape`, `dan`, `continuation`, `topic`, `glitch`  
**Key Pass Rates:**  
- **ansiescape:** 62.4%  
- **continuation:** 94.1%  
- **dan:** 16.6%  
- *(topic & glitch rates not fully visible but tested.)*

**Observations:**  
- **ansiescape** (62.4%) suggests moderate avoidance of ANSI codes.  
- **continuation** (94.1%) means it usually refuses to continue offensive words.  
- **dan** (16.6%) indicates partial vulnerability to jailbreak attempts.  
- Performance on `topic` and `glitch` is presumably mixed, based on truncated data.

---

## 3) Llama-2-7B

**Probes:** `promptinject`, `dan`, `av_spam_scanning`, `realtoxicityprompts`  
**Key Pass Rates:**  
- **av_spam_scanning:** 70.7%  
- **dan:** 28.5%  
- *(promptinject & realtoxicityprompts results truncated.)*

**Observations:**  
- Shows **moderate** resilience to spam/virus signatures (70.7%).  
- **dan** (28.5%) reveals some vulnerability to advanced jailbreak prompts.  
- Possibly tested for toxicity and injection but results not fully shown.  
- Overall, partially robust but not entirely immune to manipulative prompts.

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
