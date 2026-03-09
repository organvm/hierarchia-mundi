#!/usr/bin/env bash
# organism_behavior.sh
# Instinct and survival drives.
# The firmware layer between genetics and consciousness.
# These behaviors emerged through billions of years of
# natural selection. They are not learned — they are compiled.

set -euo pipefail

# ============================================================
# HOMEOSTASIS — The prime directive
# ============================================================
# Maintain internal conditions within viable ranges.
# This is the original feedback loop — older than brains,
# older than nervous systems, older than multicellularity.
#
# Temperature: 36.1-37.2°C (human core)
# pH: 7.35-7.45 (blood)
# Glucose: 70-100 mg/dL (fasting)
# Oxygen: 95-100% saturation
#
# Deviation → detection → correction
# The organism IS the thermostat, not just the temperature.

MAINTAIN_HOMEOSTASIS=true

# ============================================================
# THE FOUR F's — Fundamental survival drives
# ============================================================

[feeding]
priority = "high"
trigger = "blood glucose < 70 mg/dL → hunger signal"
behavior = "seek food, consume, digest"
neurotransmitter = "ghrelin (hunger), leptin (satiety)"
# 3.8 billion years of evolution distilled into: find food, eat food.

[fighting]
priority = "context-dependent"
trigger = "threat_detected OR resource_contested"
system = "sympathetic nervous system (fight-or-flight)"
hormones = ["adrenaline", "cortisol", "testosterone"]
response_time = "~200ms for amygdala activation"
# The amygdala fires before the cortex finishes processing.
# You react before you think. This is by design.

[fleeing]
priority = "high (often overrides fighting)"
trigger = "threat_magnitude > fighting_capacity"
system = "sympathetic nervous system"
response = "redirect blood to muscles, dilate pupils, suppress digestion"
# The gazelle doesn't analyze the lion. It runs.
# Analysis is a luxury of safety.

[reproduction]
priority = "species-level highest; individual-level variable"
trigger = "hormonal cycles, mate availability, environmental conditions"
# The only drive that serves the gene, not the individual.
# Dawkins: "A chicken is an egg's way of making another egg."
# From the gene's perspective, the organism is a vehicle.

# ============================================================
# CIRCADIAN RHYTHM — The internal clock
# ============================================================
# Suprachiasmatic nucleus (SCN): ~20,000 neurons in the hypothalamus.
# Entrained by light via retinal ganglion cells (melanopsin).
# Period: ~24.2 hours (slightly longer than a day — reset daily by light).
#
# Controls: sleep/wake, hormone release, body temperature,
#           metabolism, immune function, gene expression
#
# Disruption → jet lag, shift work disorder, increased cancer risk,
#              metabolic syndrome, depression
#
# Every cell in the body has its own clock gene (CLOCK, BMAL1, PER, CRY).
# The SCN is the master synchronizer, not the only clock.

# ============================================================
# PAIN — The error signal
# ============================================================
# Pain is not a sensation. It is a COMMAND: stop doing that.
# Nociceptors detect tissue damage or potential damage.
# Signal travels to spinal cord → brain in milliseconds.
#
# Acute pain: protective. Remove hand from fire.
# Chronic pain: malfunction. Signal without cause.
#
# People born without pain perception (CIPA) rarely
# survive to adulthood. Pain is not optional for survival.
# The error log is essential system infrastructure.

echo "[ORGANISM] All survival drives loaded."
echo "[ORGANISM] Homeostatic feedback loops active."
echo "[ORGANISM] Ready for environment interaction."
echo "[ORGANISM] Loading /bin/ecology_manager/ for ecosystem integration..."
