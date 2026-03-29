```json
{
    "state_management/state_manager.py": {
        "content": "
import logging
from typing import Dict, List
from agentops import LiteLLMModel, tool, CodeAgent, ToolCallingAgent, DuckDuckGoSearchTool
from smolagents import ManagedAgent
import os
import re
import requests
from markdownify import markdownify
from requests.exceptions import RequestException

logger = logging.getLogger(__name__)

class StateManager:
    """
    Manages the state of the Furnace Filter Optimization Engine.
    
    Attributes:
    non_stationary_drift_index (float): The index of non-stationary drift in the system.
    stochastic_regime_switch (bool): Whether the system is in a stochastic regime switch.
    """

    def __init__(self, non_stationary_drift_index: float, stochastic_regime_switch: bool):
        """
        Initializes the StateManager.
        
        Args:
        non_stationary_drift_index (float): The index of non-stationary drift in the system.
        stochastic_regime_switch (bool): Whether the system is in a stochastic regime switch.
        """
        self.non_stationary_drift_index = non_stationary_drift_index
        self.stochastic_regime_switch = stochastic_regime_switch
        self.managed_agent = ManagedAgent()

    def manage_state(self, state: Dict) -> Dict:
        """
        Manages the state of the system.
        
        Args:
        state (Dict): The current state of the system.
        
        Returns:
        Dict: The updated state of the system.
        """
        try:
            # Call the DuckDuckGoSearchTool to get the latest information
            search_tool = DuckDuckGoSearchTool()
            result = search_tool.search('furnace filter optimization')
            # Update the state with the latest information
            state['latest_info'] = markdownify(result)
            logger.info('State updated with latest information')
            return state
        except RequestException as e:
            logger.error(f'Error updating state: {e}')
            return state

    def switch_regime(self) -> None:
        """
        Switches the stochastic regime of the system.
        """
        try:
            # Call the CodeAgent to switch the regime
            code_agent = CodeAgent()
            code_agent.execute('switch_regime')
            self.stochastic_regime_switch = not self.stochastic_regime_switch
            logger.info('Regime switched')
        except Exception as e:
            logger.error(f'Error switching regime: {e}')

    def update_drift_index(self, new_index: float) -> None:
        """
        Updates the non-stationary drift index of the system.
        
        Args:
        new_index (float): The new non-stationary drift index.
        """
        try:
            # Call the ToolCallingAgent to update the drift index
            tool_agent = ToolCallingAgent()
            tool_agent.call_tool('update_drift_index', new_index)
            self.non_stationary_drift_index = new_index
            logger.info('Drift index updated')
        except Exception as e:
            logger.error(f'Error updating drift index: {e}')

if __name__ == '__main__':
    # Simulation of the 'Rocket Science' problem
    state_manager = StateManager(0.5, False)
    state = {'latest_info': ''}
    updated_state = state_manager.manage_state(state)
    print(updated_state)
    state_manager.switch_regime()
    state_manager.update_drift_index(0.7)
",
        "commit_message": "feat: implement specialized state_manager logic"
    }
}
```