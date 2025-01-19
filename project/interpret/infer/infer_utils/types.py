class GraphLangType:
    EDGE = "edge"
    NUM = "num"
    CHAR = "char"
    GRAPH = "graph"
    FA = "FA"
    RSM = "RSM"
    SET = "SET"
    UNKNOWN = "ERROR"


class VariableStore:
    """A wrapper class for managing variables."""

    def __init__(self):
        self.__variable_types: dict[str, GraphLangType] = {}

    def add_variable(self, name: str, type: GraphLangType):
        assert (
            type != GraphLangType.UNKNOWN
        ), "Attempt to assign unknown type to variable"
        self.__variable_types[name] = type

    def get_variable(self, name: str) -> GraphLangType:
        return self.__variable_types[name]

    def contains_variable(self, name: str) -> bool:
        return name in self.__variable_types.keys()

    def get_all_variables(self) -> dict[str, GraphLangType]:
        return self.__variable_types.copy()

    def __len__(self) -> int:
        return len(self.__variable_types)

    def __contains__(self, name: str) -> bool:
        return self.contains_variable(name)

    def __nonzero__(self) -> bool:
        return len(self.__variable_types) > 0


class VariablesPrinter:
    def __init__(self, variables: VariableStore):
        self.__variables = variables

    def print(self):
        if not self.__variables:
            print("* No infered variables *")
            return

        for var_name, var_type in self.__variables.get_all_variables().items():
            print(f"    {var_name} => {var_type}")
