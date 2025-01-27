from pyformlang.regular_expression import Regex
from pyformlang.finite_automaton import EpsilonNFA, Symbol
from typing import Optional
from pyformlang.rsa import RecursiveAutomaton, Box


def nfa_from_char(char: str) -> EpsilonNFA:
    assert len(char) == 1, f"Incorrect char: '{char}'."
    return Regex(char).to_epsilon_nfa()


def nfa_from_var(var_name: str) -> EpsilonNFA:
    return Regex(var_name.upper()).to_epsilon_nfa()


def create_empty_nfa() -> EpsilonNFA:
    return Regex("$").to_epsilon_nfa()


def intersect(nfa1: EpsilonNFA, nfa2: EpsilonNFA) -> EpsilonNFA:
    """regex & regex"""
    intersected_nfa: EpsilonNFA = nfa1.get_intersection(nfa2)

    return intersected_nfa.minimize()


def concatenate(nfa1: EpsilonNFA, nfa2: EpsilonNFA) -> EpsilonNFA:
    """regex . regex"""
    concatenated_nfa: EpsilonNFA = nfa1.concatenate(nfa2)

    return concatenated_nfa.minimize()


def union(nfa1: EpsilonNFA, nfa2: EpsilonNFA) -> EpsilonNFA:
    """regex | regex"""
    union_nfa: EpsilonNFA = nfa1.union(nfa2)

    return union_nfa.minimize()


def repeat(nfa: EpsilonNFA, times: int) -> EpsilonNFA:
    """regex ^ [times]"""
    if times == 0:
        return create_empty_nfa()

    repeat_nfa = nfa

    for _ in range(times - 1):
        repeat_nfa = concatenate(repeat_nfa, nfa)

    return repeat_nfa.minimize()


def kleene(nfa: EpsilonNFA) -> EpsilonNFA:
    """regex *"""
    return nfa.kleene_star().minimize()


def repeat_range(
    nfa: EpsilonNFA, left_border: int, right_border: Optional[int]
) -> EpsilonNFA:
    """regex ^ [left_border..right_border]"""
    if left_border == 0 and right_border is None:  # ^ [0..]
        return kleene(nfa)

    if right_border is None:  # ^ [left_border..]
        # "a" ^ [2..] => "a"."a".("a"*)
        repeated_regex = repeat(nfa, left_border)
        concat_regex = concatenate(repeated_regex, kleene(nfa))

        return concat_regex

    if left_border == right_border:  # ^ [x..x]
        return repeat(nfa, left_border)

    result_nfa = repeat(nfa, left_border)

    for times in range(left_border + 1, right_border + 1):
        repeat_res = repeat(nfa, times)
        result_nfa = union(result_nfa, repeat_res)

    return result_nfa.minimize()


def group(nfa: EpsilonNFA) -> EpsilonNFA:
    """( regex )"""
    return Regex(f"({nfa.minimize().to_regex()})").to_epsilon_nfa()


START_TERMINAL_NAME = "START"


def build_rsm(nfa: EpsilonNFA, subs_dict: dict[str, EpsilonNFA]) -> RecursiveAutomaton:
    boxes = []
    
    for var_name, var_nfa in subs_dict.items():
        boxes.append(Box(var_nfa, Symbol(var_name.upper())))

    boxes.append(Box(nfa, Symbol(START_TERMINAL_NAME)))

    result_rsm = RecursiveAutomaton(
        initial_label=Symbol(START_TERMINAL_NAME), boxes=boxes
    )

    return result_rsm
