```json
{
    "utils/visualization_tool.py": {
        "content": "
import logging
from typing import List, Dict
from smolagents import LiteLLMModel, tool
import agentops
from agentops import ManagedAgent
import matplotlib.pyplot as plt
import numpy as np

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class VisualizationTool:
    """
    A tool for visualizing complex data in the Furnace Filter Optimization Engine.
    """
    
    def __init__(self, non_stationary_drift_index: List[float], stochastic_regime_switch: Dict[str, float]):
        """
        Initialize the VisualizationTool with non-stationary drift index and stochastic regime switch data.
        
        Args:
        non_stationary_drift_index (List[float]): A list of non-stationary drift indices.
        stochastic_regime_switch (Dict[str, float]): A dictionary of stochastic regime switch data.
        """
        self.non_stationary_drift_index = non_stationary_drift_index
        self.stochastic_regime_switch = stochastic_regime_switch

    def visualize_non_stationary_drift(self) -> None:
        """
        Visualize the non-stationary drift index data.
        """
        try:
            plt.plot(self.non_stationary_drift_index)
            plt.xlabel('Time')
            plt.ylabel('Non-Stationary Drift Index')
            plt.title('Non-Stationary Drift Index Over Time')
            plt.show()
            logger.info('Non-stationary drift index visualization complete.')
        except Exception as e:
            logger.error(f'Error visualizing non-stationary drift index: {e}')

    def visualize_stochastic_regime_switch(self) -> None:
        """
        Visualize the stochastic regime switch data.
        """
        try:
            plt.bar(self.stochastic_regime_switch.keys(), self.stochastic_regime_switch.values())
            plt.xlabel('Regime')
            plt.ylabel('Switch Probability')
            plt.title('Stochastic Regime Switch Probabilities')
            plt.show()
            logger.info('Stochastic regime switch visualization complete.')
        except Exception as e:
            logger.error(f'Error visualizing stochastic regime switch: {e}')

    def simulate_rocket_science(self) -> None:
        """
        Simulate the 'Rocket Science' problem using the Furnace Filter Optimization Engine.
        """
        try:
            # Create a ManagedAgent to manage the web search agent
            managed_agent = ManagedAgent(
                tool=DuckDuckGoSearchTool(),
                code_interpreter=LiteLLMModel()
            )
            
            # Use the managed agent to search for information on rocket science
            search_results = managed_agent.search('rocket science')
            
            # Visualize the search results
            plt.plot([result.score for result in search_results])
            plt.xlabel('Result Index')
            plt.ylabel('Score')
            plt.title('Rocket Science Search Results')
            plt.show()
            logger.info('Rocket science simulation complete.')
        except Exception as e:
            logger.error(f'Error simulating rocket science: {e}')

if __name__ == '__main__':
    # Create a VisualizationTool instance
    visualization_tool = VisualizationTool(
        non_stationary_drift_index=[0.1, 0.2, 0.3, 0.4, 0.5],
        stochastic_regime_switch={'regime1': 0.6, 'regime2': 0.7}
    )
    
    # Visualize the non-stationary drift index data
    visualization_tool.visualize_non_stationary_drift()
    
    # Visualize the stochastic regime switch data
    visualization_tool.visualize_stochastic_regime_switch()
    
    # Simulate the 'Rocket Science' problem
    visualization_tool.simulate_rocket_science()
",
        "commit_message": "feat: implement specialized visualization_tool logic"
    }
}
```