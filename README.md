# LLM-Based Lean 4 Proof Generator

A prototype that converts natural-language logic problems into
formally verified Lean 4 proofs using an LLM, theorem retrieval,
and the Lean compiler.

## Architecture

Natural Language Problem
        ↓
Theorem Retrieval
        ↓
LLM Proof Generation
        ↓
Lean Verification
        ↓
PASS / FAIL
        ↓
LLM Retry if Proof Fails

## Features

- Natural-language to Lean proof generation
- Retrieval of relevant theorem information
- Mathlib-based Lean environment
- Automatic Lean proof verification
- Automatic retry when Lean reports an error
- Python-based orchestration

## Technologies

- Python
- Lean 4
- Mathlib
- OpenAI API

## Example

### Input

Given:

h : P ∧ Q

Prove:

P

### Retrieved theorem

And.left

### Generated Lean proof

```lean
theorem extract_left (P Q : Prop) (h : P ∧ Q) : P := by
  exact h.left