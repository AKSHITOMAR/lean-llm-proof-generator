

import Mathlib

theorem identity (P : Prop) : P → P := by
  intro h
  exact h

theorem modus_ponens
  (P Q : Prop)
  (h1 : P -> Q)
  (h2 : P) :
    Q := by
    exact h1 h2

theorem and_example
    (P Q : Prop)
    (h1 : P)
    (h2 : Q) :
    P ∧ Q := by
  constructor
  exact h1
  exact h2

theorem get_right
    (P Q : Prop)
    (h : P ∧ Q) :
    Q := by
  exact h.right

theorem or_left
    (P Q : Prop)
    (h : P) :
    P ∨ Q := by
  left
  exact h

theorem forall_example :
    ∀ P : Prop, P → P := by
  intro P
  intro h
  exact h

theorem exists_example :
  ∃ P : Prop, P := by
  use True
  exact True.intro

theorem chain_reasoning
    (P Q R : Prop)
    (h1 : P → Q)
    (h2 : Q → R)
    (h3 : P) :
    R := by
  have h4 : Q := h1 h3
  exact h2 h4

theorem iff_example
    (P Q : Prop)
    (h1 : P → Q)
    (h2 : Q → P) :
    P ↔ Q := by
  constructor
  exact h1
  exact h2

theorem not_example
    (P : Prop)
    (h : P) :
    ¬¬P := by
  intro hnot
  exact hnot h

theorem contradiction_example
    (P : Prop)
    (h1 : P)
    (h2 : ¬P) :
    False := by
  exact h2 h1

theorem and_reasoning
    (P Q R : Prop)
    (h1 : P ∧ Q)
    (h2 : P → Q → R) :
    R := by
  exact h2 h1.left h1.right

theorem logical_deduction
    (P Q R : Prop)
    (h1 : P → Q)
    (h2 : Q → R)
    (h3 : P) :
    P ∧ R := by
  constructor
  · exact h3
  · exact h2 (h1 h3)

theorem llm_reasoning_example
    (Human Mortal : Prop)
    (socrates : Human)
    (all_humans_mortal : Human → Mortal) :
    Mortal := by
  exact all_humans_mortal socrates


