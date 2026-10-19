#!/bin/bash
cd /root/.openclaw/workspace/ai-podcast-collection/.tmp/2026-10-18/pages
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
fetch(){ curl -sL --max-time 60 -A "$UA" "$1" -o "$2"; echo "$2 $(wc -c <"$2")"; }
fetch "https://www.latent.space/p/crossing-the-threshold" crossing.html
fetch "https://www.latent.space/p/lab-in-the-loop-at-compute-speed" leash.html
fetch "https://www.latent.space/p/ainews-agents-disprove-polysemanticity" poly.html
fetch "https://www.latent.space/p/ainews-modals-1b-arr-16b-series-d" modal.html
fetch "https://www.latent.space/p/ainews-high-taste-testers-ep-1" taste.html
fetch "https://www.cognitiverevolution.ai/governing-ai-agents-alan-chan-of-govai-on-monitoring-agent-ids-rogue-agents-preparing-for-rsi/" alan.html
fetch "https://www.cognitiverevolution.ai/ai-am-where-s-the-steering-wheel-my-agent-set-the-password-hidden-valence-proofs-find-linux-bugs/" aiam.html
fetch "https://www.no priors.com" x.html 2>/dev/null
fetch "https://www.xiaoyuzhoufm.com/episode/6acddf92e742e36efcc2448d" jason.html
fetch "https://www.xiaoyuzhoufm.com/episode/6acf81f0195d838e2af1e281" lindon.html
