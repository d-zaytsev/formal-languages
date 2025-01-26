from pyformlang.regular_expression import Regex
from pyformlang.finite_automaton import EpsilonNFA
from typing import Optional


class RunnableRegex:
    def __init__(self):
        self.__regex = ""
        self.__is_created = False

    __UNIQUE_VAR_PREFIX = "VAR_"

    @property
    def str(self) -> str:
        assert self.__is_created, "Create RunnableRegex first."
        return self.__regex

    @property
    def nfa(self) -> EpsilonNFA:
        assert self.__is_created, "Create RunnableRegex first."
        return Regex(self.__regex).to_epsilon_nfa()

    def init_with_char(self, char: str):
        assert not self.__is_created, "RunnableRegex already has been created."
        self.__is_created = True

        self.__regex = char

        return self

    def init_with_variable(self, var_name: str):
        assert not self.__is_created, "RunnableRegex already has been created."
        self.__is_created = True

        new_name = self.__transform_var_name(var_name)

        self.__regex = new_name

        return self

    def init_with_regex(self, regex: Regex):
        assert not self.__is_created, "RunnableRegex already has been created."
        self.__is_created = True

        self.__regex = str(regex)

        return self

    def __transform_var_name(self, var_name: str):
        """Return variable name for internal usage."""

        return self.__UNIQUE_VAR_PREFIX + var_name

    def __get_common_var_name(self, internal_var_name: str):
        return internal_var_name.replace(self.__UNIQUE_VAR_PREFIX, "")


def intersect(regexA: RunnableRegex, regexB: RunnableRegex) -> RunnableRegex:
    """regexA & regexB"""
    nfaA = regexA.nfa
    nfaB = regexB.nfa

    intersected_nfa: EpsilonNFA = nfaA.get_intersection(nfaB).minimize()
    intersected_regex: Regex = intersected_nfa.to_regex()

    return RunnableRegex().init_with_regex(f"{intersected_regex}")


def concatenate(regexA: RunnableRegex, regexB: RunnableRegex) -> RunnableRegex:
    """regexA . regexB"""
    nfaA = regexA.nfa
    nfaB = regexB.nfa

    concatenated_nfa: EpsilonNFA = nfaA.concatenate(nfaB).minimize()
    concatenated_regex: Regex = concatenated_nfa.to_regex()

    return RunnableRegex().init_with_regex(f"{concatenated_regex}")


def union(regexA: RunnableRegex, regexB: RunnableRegex) -> RunnableRegex:
    """regexA | regexB"""
    nfaA = regexA.nfa
    nfaB = regexB.nfa

    union_nfa: EpsilonNFA = nfaA.union(nfaB).minimize()
    union_regex: Regex = union_nfa.to_regex()

    return RunnableRegex().init_with_regex(f"{union_regex}")


def repeat(regex: RunnableRegex, times: int) -> RunnableRegex:
    """regex ^ [times]"""
    if times == 0:
        return RunnableRegex().init_with_regex("")

    result = regex

    for _ in range(times - 1):
        result = concatenate(result, regex)

    return result

def klini(regex: RunnableRegex):
    return RunnableRegex().init_with_regex(f"{regex.str}*")

def sequence(regex: RunnableRegex, left_border: int, right_border: Optional[int]) -> RunnableRegex:
    """regex ^ [left_border...right_border]"""
    regex_str = regex.str

    if left_border == 0 and right_border is None: # ^ [0..]
        return RunnableRegex().init_with_regex(f"({regex_str}*)")

    if right_border is None: # ^ [left_border..]
        # "a" ^ [2..] => "a"."a".("a"*)
        repeated_regex = repeat(regex, left_border)
        concat_regex = concatenate(repeated_regex, klini(regex))

        return concat_regex

    result_regex = RunnableRegex().init_with_regex('')

    for times in range(left_border, right_border + 1):
        result_regex = union(result_regex, repeat(regex, times))

    return result_regex


def group(regex: RunnableRegex):
    """( regex )"""
    return RunnableRegex().init_with_regex(f"({regex.str})")


# let q = (("a" | "b") . ("b" | "c")) ^ [0..]

a = RunnableRegex().init_with_char("a")
b = RunnableRegex().init_with_char("b")
c = RunnableRegex().init_with_char("c")

a_or_b = union(a, b)
b_or_c = union(b, c)

full_reg = concatenate(a_or_b, b_or_c)

print(sequence(a_or_b, 0, 3).nfa.accepts(''))
