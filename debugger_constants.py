

```
# debugger_constants.py

from enum import Enum

Debugger_Active = False
DebuggerCNT = 0
Debugger_StopParaRead = False
Debugger_InterpreterStop = False
debugger_BreakpointFlag = False
debugger_InterpreterFinished = False
debugger_LogModeFlag = False

class debugger_GetLokalVars(Enum):
    LOCAL_VAR_1 = "local_var_1"
    LOCAL_VAR_2 = "local_var_2"

class debugger_GetLokalVarValue(Enum):
    LOCAL_VAR_VALUE_1 = "local_var_value_1"
    LOCAL_VAR_VALUE_2 = "local_var_value_2"

class debugger_GetCommand(Enum):
    COMMAND_1 = "command_1"
    COMMAND_2 = "command_2"

class debugger_GetBreakPointType(Enum):
    BREAKPOINT_TYPE_1 = "breakpoint_type_1"
    BREAKPOINT_TYPE_2 = "breakpoint_type_2"
```