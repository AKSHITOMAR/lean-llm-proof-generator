theorem modus_ponens (P Q : Prop) (h1 : P → Q) (h2 : P) : Q :=
  h1 h2