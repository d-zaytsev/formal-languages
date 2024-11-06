from pyformlang.cfg import CFG
from pyformlang.rsa import RecursiveAutomaton
from networkx import DiGraph
from pyformlang.finite_automaton import (
    NondeterministicFiniteAutomaton,
    State,
    Symbol,
)
from project.task3 import AdjacencyMatrixFA, graph_to_nfa, intersect_automata
from scipy.sparse import csr_array, csr_matrix


def cfg_to_rsm(cfg: CFG) -> RecursiveAutomaton:
    return ebnf_to_rsm(cfg.to_text())


def ebnf_to_rsm(ebnf: str) -> RecursiveAutomaton:
    return RecursiveAutomaton.from_text(ebnf)


def rsm_to_nfa(rsm: RecursiveAutomaton) -> NondeterministicFiniteAutomaton:
    transitions = []
    start_states = []
    final_states = []

    boxes = rsm.boxes

    for head in boxes:
        FA: NondeterministicFiniteAutomaton = boxes[head].dfa

        FA_transitions = FA.to_networkx().edges(data="label")

        for trans in FA_transitions:
            label = trans[2]
            if label:
                transitions.append(
                    (State((head, trans[0])), Symbol(label), State((head, trans[1])))
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
        start_state=start_states,
        final_states=final_states,
    )

    res.add_transitions(transitions)

    return res


def update_matrices(
    old: AdjacencyMatrixFA, matrices: dict[Symbol, csr_array]
) -> AdjacencyMatrixFA:
    new_adj = AdjacencyMatrixFA(None)

    new_adj.states_count = old.states_count
    new_adj.states = old.states
    new_adj.start_states_is = old.start_states_is
    new_adj.final_states_is = old.final_states_is
    new_adj.sparse_matrices = old.sparse_matrices.copy()

    for sym, matrix in matrices.items():
        if sym in new_adj.sparse_matrices.keys():
            new_adj.sparse_matrices[sym] += matrix
            continue

        new_adj.sparse_matrices[sym] = matrix

    return new_adj


def tensor_based_cfpq(
    rsm: RecursiveAutomaton,
    graph: DiGraph,
    start_nodes: set[int] = None,
    final_nodes: set[int] = None,
) -> set[tuple[int, int]]:
    rsm_fa = rsm_to_nfa(rsm)
    graph_fa = graph_to_nfa(graph, start_nodes, final_nodes)

    rsm_adj = AdjacencyMatrixFA(rsm_fa)
    graph_adj = AdjacencyMatrixFA(graph_fa)

    # iterate while we can find new paths
    while True:
        intersection_adj: AdjacencyMatrixFA = intersect_automata(graph_adj, rsm_adj)
        closure: csr_matrix = intersection_adj.transitive_сlosure()

        new_matrix: dict[Symbol, csr_matrix] = {}

        row_i, col_i = closure.nonzero()

        # iterate over existing paths
        for x_i, y_i in zip(row_i, col_i):
            common_from_state: State = intersection_adj.states[x_i]
            common_to_state: State = intersection_adj.states[y_i]

            graph_from_state: State = common_from_state.value[0]
            graph_to_state: State = common_to_state.value[0]

            graph_from_state_i: int = graph_adj.states.index(graph_from_state)
            graph_to_state_i: int = graph_adj.states.index(graph_to_state)

            rsm_from_state: State = common_from_state.value[1]
            rsm_to_state: State = common_to_state.value[1]

            rsm_from_state_i: State = rsm_adj.states.index(rsm_from_state)
            rsm_to_state_i: State = rsm_adj.states.index(rsm_to_state)

            if (
                (rsm_from_state.value[0] != rsm_to_state.value[0])
                or (rsm_from_state_i not in rsm_adj.start_states_is)
                or (rsm_to_state_i not in rsm_adj.final_states_is)
            ):
                continue

            label = rsm_from_state.value[0]

            if (label not in graph_adj.sparse_matrices.keys()) or (
                not graph_adj.sparse_matrices[label][
                    graph_from_state_i, graph_to_state_i
                ]
            ):
                if label not in new_matrix.keys():
                    new_matrix[label] = csr_array(
                        (graph_adj.states_count, graph_adj.states_count), dtype=bool
                    )

                new_matrix[label][graph_from_state_i, graph_to_state_i] = True
        # nothing has changed
        if not new_matrix:
            break

        graph_adj = update_matrices(graph_adj, new_matrix)

    if rsm.initial_label not in graph_adj.sparse_matrices.keys():
        return set()

    res = graph_adj.sparse_matrices[rsm.initial_label]
    pairs: set[tuple[int, int]] = set()

    if not start_nodes:
        start_nodes = graph_fa.states
    if not final_nodes:
        final_nodes = graph_fa.states

    for start_state in start_nodes:
        for final_state in final_nodes:
            start_state_i = graph_adj.states.index(start_state)
            final_state_i = graph_adj.states.index(final_state)

            if res[start_state_i, final_state_i]:
                pairs.add((start_state, final_state))

    return pairs
