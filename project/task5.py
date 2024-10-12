from typing import TypeVar, Generic, Type
from pyformlang.finite_automaton import (
    NondeterministicFiniteAutomaton,
    DeterministicFiniteAutomaton,
    State,
    Symbol,
)
import numpy as np
from networkx import MultiDiGraph
from numpy.typing import NDArray
from scipy.sparse import kron
from task2 import graph_to_nfa, regex_to_dfa
from functools import reduce


A = TypeVar("A")  # array type
M = TypeVar("M")  # matrix type


class AdjacencyMatrixFA(Generic[A]):
    def __init__(
        self,
        fa: (NondeterministicFiniteAutomaton | DeterministicFiniteAutomaton | None),
        array_type: Type[A],
    ):
        self.states_count: int = 0
        self.states: list[State] = []
        self.start_states_is: list[int] = []  # indexes of states
        self.final_states_is: list[int] = []  # indexes of states
        self.sparse_matrices: dict[Symbol, A] = {}

        if fa is None:
            return

        isDeterministic = isinstance(fa, DeterministicFiniteAutomaton)

        # get FA transitions
        transitions_dict: dict = fa.to_dict()
        transitions: list[tuple] = list(transitions_dict.items())

        # set states
        self.states = list(fa.states)
        self.states_count = len(fa.states)

        for i in range(self.states_count):
            state: State = self.states[i]

            if state in fa.start_states:
                self.start_states_is.append(i)
            if state in fa.final_states:
                self.final_states_is.append(i)

        # dictionary for bool decomposition
        matrices_dict: dict[Symbol, NDArray[np.bool_]] = {}

        matrix_shape = (self.states_count, self.states_count)
        # ^ there may be an error, since there may be states that are not in order

        for source_node, dests in transitions:
            # (source_node, {sym: dest_node , ...})
            # index of source_node
            source_node_i: int = self.states.index(source_node)

            for sym, dest in dests.items():
                # DFA: (sym, dest_node)
                # NFA: (sym, {dest_node})
                sym: Symbol = sym._value

                if sym not in matrices_dict:
                    matrices_dict[sym] = np.zeros(shape=matrix_shape, dtype=np.bool_)

                if isDeterministic:
                    dest_node_i: int = self.states.index(dest)

                    matrices_dict[sym][source_node_i, dest_node_i] = True

                else:
                    # different transitions from one state
                    dest_nodes: set[State] = dest

                    for dest_node in dest_nodes:
                        dest_node_i: int = self.states.index(dest_node)
                        matrices_dict[sym][source_node_i, dest_node_i] = True

        # transform to sparse matrices
        for key in list(matrices_dict.keys()):
            self.sparse_matrices[key] = array_type(matrices_dict[key], dtype=np.bool_)

    def transitive_сlosure(self) -> NDArray[np.bool_]:
        adj_matrix: NDArray[np.bool_] = np.zeros(
            shape=(self.states_count, self.states_count), dtype=np.bool_
        )

        for matrix in self.sparse_matrices.values():
            adj_matrix = adj_matrix | matrix.toarray()

        for start_node in self.start_states_is:
            adj_matrix[start_node, start_node] = True

        for k in range(self.states_count):
            for i in range(self.states_count):
                for j in range(self.states_count):
                    adj_matrix[i][j] = adj_matrix[i][j] or (
                        adj_matrix[i][k] and adj_matrix[k][j]
                    )

        return adj_matrix


def intersect_automata(
    automaton1: AdjacencyMatrixFA[A],
    automaton2: AdjacencyMatrixFA[A],
    format: str,
    array_type: Type[A],
) -> AdjacencyMatrixFA:
    a1, a2 = automaton1, automaton2

    new_a = AdjacencyMatrixFA[A](None, array_type)
    new_a.states_count = a1.states_count * a2.states_count

    # kron prod
    for sym, m1 in a1.sparse_matrices.items():
        if sym in a2.sparse_matrices:
            m2 = a2.sparse_matrices[sym]
            prod = kron(m1, m2, format=format)
            new_a.sparse_matrices[sym] = prod

    # add start/final states
    for s1 in range(a1.states_count):
        for s2 in range(a2.states_count):
            new_index = a2.states_count * s1 + s2
            new_state = (a1.states[s1], a2.states[s2])

            new_a.states.append(State(new_state))

            if (s1 in a1.start_states_is) and (s2 in a2.start_states_is):
                new_a.start_states_is.append(new_index)
            if (s1 in a1.final_states_is) and (s2 in a2.final_states_is):
                new_a.final_states_is.append(new_index)

    return new_a


def tensor_based_rpq(
    regex: str,
    graph: MultiDiGraph,
    start_nodes: set[int],
    final_nodes: set[int],
    array_type: Type[A],
    format: str,
) -> set[tuple]:
    nfa = graph_to_nfa(graph, start_nodes, final_nodes)
    dfa = regex_to_dfa(regex)

    mfa1 = AdjacencyMatrixFA[A](nfa, array_type)
    mfa2 = AdjacencyMatrixFA[A](dfa, array_type)

    new_mfa = intersect_automata(mfa1, mfa2, format, array_type)

    # complementation of languages
    adj_matrix = new_mfa.transitive_сlosure()

    pairs: set[tuple[int, int]] = set()

    # [!] start_nodes & final_nodes not indexes
    for graph_start in start_nodes:
        for graph_final in final_nodes:
            for regex_start_i in mfa2.start_states_is:
                for regex_final_i in mfa2.final_states_is:
                    graph_start_i = mfa1.states.index(graph_start)
                    graph_final_i = mfa1.states.index(graph_final)

                    start_index = mfa2.states_count * graph_start_i + regex_start_i
                    final_index = mfa2.states_count * graph_final_i + regex_final_i

                    if adj_matrix[start_index, final_index]:
                        pairs.add((graph_start, graph_final))

    return set(pairs)


def get_start_front(
    fa_regex: AdjacencyMatrixFA[A], fa_graph: AdjacencyMatrixFA[A], matrix_type: Type[M]
) -> M:
    regex_start_state_i: int = fa_regex.start_states_is[0]
    graph_start_states_count: int = len(fa_graph.start_states_is)

    row = [
        regex_start_state_i + fa_regex.states_count * i
        for i in range(graph_start_states_count)
    ]
    col = [st_state_i for st_state_i in fa_graph.start_states_is]
    data = [True] * graph_start_states_count

    return matrix_type(
        (data, (row, col)),
        shape=(
            fa_regex.states_count * graph_start_states_count,
            fa_graph.states_count,
        ),
        dtype=bool,
    )


def is_front_not_empty(front: M):
    return front.toarray().any()


def ms_bfs_based_rpq(
    regex: str,
    graph: MultiDiGraph,
    start_nodes: set[int],
    final_nodes: set[int],
    matrix_type: Type[M],
    array_type: Type[A],
) -> set[tuple[int, int]]:
    fa_regex: AdjacencyMatrixFA = AdjacencyMatrixFA[A](regex_to_dfa(regex), array_type)
    fa_graph: AdjacencyMatrixFA = AdjacencyMatrixFA[A](
        graph_to_nfa(graph, start_nodes, final_nodes), array_type
    )

    # BFS result
    pairs: set[tuple[int, int]] = set()

    regex_transposed_matrices: dict[Symbol, M] = {
        sym: m.transpose() for sym, m in fa_regex.sparse_matrices.items()
    }

    # paths for each sym
    fronts: dict[Symbol, M] = {}

    # Init front with start states
    global_front: M = get_start_front(fa_regex, fa_graph, matrix_type)
    visited: M = global_front

    syms = [
        s
        for s in fa_regex.sparse_matrices.keys()
        if s in fa_graph.sparse_matrices.keys()
    ]

    # while we have paths
    while is_front_not_empty(global_front):
        fronts = {}

        for sym in syms:
            # find new front for current sym
            fronts[sym] = global_front @ fa_graph.sparse_matrices[sym]

            for i in range(len(start_nodes)):
                start = i * fa_regex.states_count
                end = (i + 1) * fa_regex.states_count

                # apply constraints
                fronts[sym][start:end] = (
                    regex_transposed_matrices[sym] @ fronts[sym][start:end]
                )

        # combine
        global_front = reduce(lambda x, y: x + y, fronts.values(), global_front)
        # remove visited states
        global_front = global_front > visited
        visited += global_front

    # fill pairs
    for regex_final_state_i in fa_regex.final_states_is:
        for i in range(len(fa_graph.start_states_is)):
            graph_start_state_i = fa_graph.start_states_is[i]
            graph_start_state: int = fa_graph.states[graph_start_state_i]._value
            # iterate over reached graph final states
            for graph_reached_state in visited.getrow(
                fa_regex.states_count * i + regex_final_state_i
            ).indices:
                if graph_reached_state not in fa_graph.final_states_is:
                    continue
                pairs.add(
                    (graph_start_state, fa_graph.states[graph_reached_state].value)
                )

    return pairs
