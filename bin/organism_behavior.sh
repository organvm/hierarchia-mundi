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

# ============================================================
# LOOP TAXONOMY — The operating system of behavior
# ============================================================
# Every organism runs on loops. Not just homeostatic feedback,
# but nested, interlocking cycles at every timescale.
# The organism IS its loops. Remove them and it dies.

[core_loop]
# The innermost loop. Rhythm. Habit. Second-to-second existence.
# Heartbeat: 60-100 bpm. Breathing: 12-20 breaths/minute.
# Nerve impulse: fire → refractory → ready → fire.
# The core loop defines the organism's temporal grain —
# the clock speed of biological computation.
#
# In game design: the moment-to-moment gameplay loop.
# Move → perceive → decide → act → move.
# In organisms: sense → process → respond → sense.
# The core loop is survival at the tick level.
cadence = "seconds to minutes"
function = "maintain_rhythm"

[meta_loop]
# The loop above the loop. Commitment. Identity. Growth.
# Circadian rhythm (documented above): daily cycle.
# Menstrual cycle: ~28 days. Seasonal behavior: annual.
# Life stages: infant → child → adolescent → adult → elder.
#
# The meta loop defines what the organism IS over time.
# A caterpillar's core loop is "eat." Its meta loop is
# "eat → grow → pupate → emerge → reproduce → die."
# The meta loop is the narrative arc of biological existence.
cadence = "days to lifetime"
function = "maintain_identity"

[feedback_loop]
# Consequence. Cause and effect across loops.
# Positive feedback: labor contractions → oxytocin → stronger contractions.
# Negative feedback: blood sugar rises → insulin → blood sugar falls.
#
# The feedback loop is what makes loops ADAPTIVE rather than
# merely repetitive. Without feedback, the organism is a clock.
# With feedback, it is a thermostat — and eventually, a mind.
#
# Learning IS feedback: action → outcome → memory → adjusted action.
# Pain is feedback. Pleasure is feedback.
# Emotion is the user interface of the feedback loop.
cadence = "variable — milliseconds to generations"
function = "adapt_behavior"

[loop_modulation]
# Loops are not fixed. They are modulated by context.
# Stress → cortisol → sleep loop disrupted → immune loop degraded.
# Social bonding → oxytocin → feeding loop modulated (shared meals).
# Seasonal light changes → melatonin → reproductive loop activated.
#
# The organism is a modular synthesizer of loops.
# Each loop is an oscillator. Context is the modulation matrix.
# Health is when the loops are in phase.
# Disease is when they decouple.

echo "[ORGANISM] All survival drives loaded."
echo "[ORGANISM] Core/meta/feedback loops active."
echo "[ORGANISM] Ready for environment interaction."
echo "[ORGANISM] Loading /bin/ecology_manager/ for ecosystem integration..."
