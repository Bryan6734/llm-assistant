# BryBot 

**Task:** Spend no more than 2 hours on making a LLM command line helper. This will be a script that you can launch in your terminal that will ask you for something you’d like to achomplish on your shell (like commit code to GitHub, starting a Redis server, looking for a particular file, etc…) The llm will them suggest a bash command to run and you can accept it or reject it. Bonus points if you add a feature where the LLM can code for a while without your permission.


### Question 1
*Please describe your coding experience and any experience you have had with playing with llm apis and building scaffolds. I’m most interesting in applicants with strong coding experience. ML skills are nice but by no means required*

Around 4 yrs of experience programming; highly interested pursuing a career in AI safety and alignment. Here are some tangentially-related projects I've worked on:

1. **BryBot iMessage Analyzer:** I built this last year, and it was a bot that I could activate via iMessage (I'd text someone "Brybot, ACTIVATE!"), and brybot would send messages on my behalf in the same iMessage conversation using an LLM. Based on the command I typed after activating it, it would either respond to the latest text, summarize a conversation from exactly one year ago, or select any date and re-create a skit based on our conversation.
2. **LLM Probabilistic Coherence:** Currently researching whether LLMs follow norms on rationality (i.e. probabilistic coherence) with a post-doc at my institution's lab. I run experiments, read papers, and we're aiming to publish something in the Spring. We use HuggingFace transformers, which grants lower-level access comparead to using an API.
3. **AI Safety Camp: Multilingual Robustness** Extending off another NeurIPS paper published by mentor; exploring how multilinguality affects LLM robustness to adv. attacks, establishing MDT (multilingual distributed testing) to expand benchmarks/testing for other languages, etc. 

### Question 2
*Briefly summarise Redwood research's AI control agenda.*

There seems to be a lot of disagreement as to whether models will attempt to scheme/deceive humans in the future, especially as models grow increasingly powerful. Instead of wasting time trying to answer this question, Redwood Research's AI control agenda **starts** with the assumption that a highly-capable model **will** attempt to do so, and their research focuses on uncovering reliable ways to oversee models that are (1) more capable than the best humans, and (2) can't be trusted.

I'm familiar with the "AI Control: Improving Safety Despite Intentional Subversion" paper, which focuses various monitoring protocols for overseeing an untrusted model U in the context of backdooring (read for BlueDot Impact AI safety course, then independently, then for MATS application).

### Question 3
*Come up with your own control protocol. Describe how you would use U, T, and H to make a novel protocol that you think would be promising. Don’t spend more than 30 minutes thinking about this.* 



## Installation

1. Create **virtual env** and activate it
```
python -m venv venv
source venv/bin/activate
```
2. Install requirements
```
pip install -r requirements.txt
```
3. Export OPENAI_API_KEY
```
export OPENAI_API_KEY=sk...
```
4. Run it! (I set it up an alias to just run "brybot" but this is the easy way)
```
python brybot.py
```