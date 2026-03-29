```json
{
    "tests/test_furnace_monitoring_agent.py": {
        "content": "
import logging
from typing import Dict, List
import agentops
from smolagents import LiteLLMModel, tool, CodeAgent, ToolCallingAgent, DuckDuckGoSearchTool
from agentops import ManagedAgent
import os
import re
import requests
from markdownify import markdownify
from requests.exceptions import RequestException

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class FurnaceMonitoringAgent:
    """
    A class to monitor furnace filters and optimize their performance.
    
    Attributes:
    non_stationary_drift_index (float): The index of non-stationary drift in the furnace filter data.
    stochastic_regime_switch (bool): Whether the furnace filter is in a stochastic regime switch.
    """

    def __init__(self, non_stationary_drift_index: float, stochastic_regime_switch: bool):
        """
        Initialize the FurnaceMonitoringAgent.
        
        Args:
        non_stationary_drift_index (float): The index of non-stationary drift in the furnace filter data.
        stochastic_regime_switch (bool): Whether the furnace filter is in a stochastic regime switch.
        """
        self.non_stationary_drift_index = non_stationary_drift_index
        self.stochastic_regime_switch = stochastic_regime_switch

    def monitor_furnace_filters(self) -> Dict[str, str]:
        """
        Monitor the furnace filters and return a dictionary of filter statuses.
        
        Returns:
        Dict[str, str]: A dictionary of filter statuses.
        """
        try:
            # Use the DuckDuckGoSearchTool to search for furnace filter data
            search_tool = DuckDuckGoSearchTool()
            search_results = search_tool.search('furnace filter data')
            # Parse the search results using markdownify
            parsed_results = markdownify(search_results)
            # Extract the filter statuses from the parsed results
            filter_statuses = self.extract_filter_statuses(parsed_results)
            return filter_statuses
        except RequestException as e:
            logger.error(f'Error monitoring furnace filters: {e}')
            return {}

    def extract_filter_statuses(self, parsed_results: str) -> Dict[str, str]:
        """
        Extract the filter statuses from the parsed search results.
        
        Args:
        parsed_results (str): The parsed search results.
        
        Returns:
        Dict[str, str]: A dictionary of filter statuses.
        """
        try:
            # Use regular expressions to extract the filter statuses
            filter_statuses = {}
            for line in parsed_results.splitlines():
                match = re.search(r'Filter (.*) status: (.*)', line)
                if match:
                    filter_name = match.group(1)
                    filter_status = match.group(2)
                    filter_statuses[filter_name] = filter_status
            return filter_statuses
        except Exception as e:
            logger.error(f'Error extracting filter statuses: {e}')
            return {}

    def optimize_furnace_filters(self, filter_statuses: Dict[str, str]) -> List[str]:
        """
        Optimize the furnace filters based on their statuses.
        
        Args:
        filter_statuses (Dict[str, str]): A dictionary of filter statuses.
        
        Returns:
        List[str]: A list of optimized filter recommendations.
        """
        try:
            # Use the LiteLLMModel to optimize the furnace filters
            model = LiteLLMModel()
            optimized_filters = model.optimize_filters(filter_statuses)
            return optimized_filters
        except Exception as e:
            logger.error(f'Error optimizing furnace filters: {e}')
            return []

def main():
    # Create a FurnaceMonitoringAgent
    agent = FurnaceMonitoringAgent(non_stationary_drift_index=0.5, stochastic_regime_switch=True)
    # Monitor the furnace filters
    filter_statuses = agent.monitor_furnace_filters()
    # Optimize the furnace filters
    optimized_filters = agent.optimize_furnace_filters(filter_statuses)
    # Print the optimized filter recommendations
    print(optimized_filters)

if __name__ == '__main__':
    main()
",
        "commit_message": "feat: implement specialized test_furnace_monitoring_agent logic"
    }
}
```