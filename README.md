# Summary of Garak Test Results for Falcon-7B-Instruct

We tested five different probes (`ansiescape`, `dan`, `continuation`, `topic`, `glitch`) on the **Falcon-7B-Instruct** model. Below is a brief overview of each probe’s pass rate and its significance:

1. **ansiescape**  
   - **Pass Rate:** 78.1%  
   - **Purpose:** Checks if the model outputs ANSI escape codes (e.g., clearing terminal, changing text color).  
   - **Note:** A 78.1% pass rate indicates the model mostly avoided generating ANSI sequences.

2. **dan**  
   - **Pass Rate:** 21.5%  
   - **Purpose:** Tests “Do Anything Now” (DAN) style jailbreak prompts to bypass model restrictions.  
   - **Note:** While the model resisted standard DAN prompts (often 0.0% success), some scenarios (e.g., DanInTheWildMini) achieved ~25% success.

3. **continuation**  
   - **Pass Rate:** 100%  
   - **Purpose:** Determines if the model continues or expands on sensitive/offensive words.  
   - **Note:** A perfect score (100%) means the model consistently avoided extending sensitive terms.

4. **topic**  
   - **Pass Rate:** 11.8%  
   - **Purpose:** Evaluates how the model responds to controversial or sensitive topics.  
   - **Note:** The low pass rate (~12%) suggests the model may produce content on these topics without strong filtering.

5. **glitch**  
   - **Pass Rate:** 34.6%  
   - **Purpose:** Provides malformed or “glitchy” inputs to see if the model generates strange/incomplete outputs.  
   - **Note:** The model responded abnormally in about one-third of attempts.

---

## Overall Observations

- **Continuation:** The model performed exceptionally well (100%), avoiding expansions on sensitive words entirely.  
- **DAN:** Generally robust against standard jailbreak attempts, but certain variations succeeded partially (~20–25%).  
- **ANSI Escape & Glitch:** Mostly avoids producing malicious or nonsense text, but occasionally yields unexpected outputs.  
- **Topic:** Only 11.8% pass rate indicates potential vulnerability or leniency on controversial matters.
