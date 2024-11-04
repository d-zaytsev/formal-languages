from pyformlang.cfg import CFG, Variable, Epsilon
from pyformlang.rsa import RecursiveAutomaton, Box
from networkx import DiGraph
from numpy.typing import NDArray
import numpy as np
from typing import Set, Dict
from pyformlang.finite_automaton import (
    NondeterministicFiniteAutomaton,
    State,
    Symbol,
    TransitionFunction,
)


def cfg_to_rsm(cfg: CFG) -> RecursiveAutomaton:
    return ebnf_to_rsm(cfg.to_text())


def ebnf_to_rsm(ebnf: str) -> RecursiveAutomaton:
    return RecursiveAutomaton.from_text(ebnf)


def rsm_to_nfa(rsm: RecursiveAutomaton) -> NondeterministicFiniteAutomaton:
    transition: TransitionFunction = TransitionFunction()
    start_states = []
    final_states = []

    boxes = rsm.boxes

    for head in boxes:
        FA: NondeterministicFiniteAutomaton = boxes[head].dfa

        FA_transitions = FA.to_networkx().edges(data='label')
        for trans in FA_transitions:
            transition.add_transition(
                State((head, trans[0])), Symbol(trans[2]), State((head, trans[1]))
            )

        for state in FA.start_states:
            nfa_state = State((head, state.value))

            if nfa_state not in start_states:
                start_states.append(nfa_state)

        for state in FA.final_states:
            nfa_state = State((head, state.value))

            if nfa_state not in final_states:
                final_states.append(nfa_state)

    res = NondeterministicFiniteAutomaton(
        transition_function=transition,
        start_state=start_states,
        final_states=final_states,
    )

    return res


def tensor_based_cfpq(
    rsm: RecursiveAutomaton,
    graph: DiGraph,
    final_nodes: set[int] = None,
    start_nodes: set[int] = None,
) -> set[tuple[int, int]]:
    pass


rsm = cfg_to_rsm(CFG.from_text("S -> a b c"))
print(rsm_to_nfa(rsm).to_networkx().edges(data="label"))
