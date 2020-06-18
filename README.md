# やぱたの正規表現エンジン

## バージョン

Python 3.8.2

## 特徴

- 全文一致
- 有限オートマトンを用いて実装
  - NFA(Nondeterministic Finite Automaton)エンジン
  - DFA(Deterministic Finite Automaton)エンジン
  - NFA から DFA への変換
- 構文
- 一部正規表現のみ対応
  - A|B : 文字列の和集合
  - AB : 文字列の連結
  - A\* : 文字列の繰り返し
  - (文字列) : 演算の優先順位
  - \+任意の文字 : エスケープ
- 文法規則
  1. expression -> subexpr EOF
  1. subexpr -> seq '|' subexpr | seq
  1. seq -> subseq | ''
  1. subseq -> star subseq | star
  1. star -> factor '\*' | factor
  1. factor -> '(' subexpr ')' | CHARACTER
