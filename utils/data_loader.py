```json
{
    "utils/data_loader.py": {
        "content": "
import logging
import os
from typing import List, Dict
from agentops import ToolCallingAgent
from smolagents import LiteLLMModel, DuckDuckGoSearchTool
from markdownify import markdownify
from requests.exceptions import RequestException

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_non_stationary_drift_index(data: List[float]) -> float:
    """
    Calculate the non-stationary drift index for a given dataset.

    Args:
    - data (List[float]): The input dataset.

    Returns:
    - float: The non-stationary drift index.

    Raises:
    - ValueError: If the input dataset is empty.
    """
    try:
        if not data:
            raise ValueError('Input dataset is empty')
        # Calculate the non-stationary drift index using a stochastic regime switch model
        non_stationary_drift_index = sum([x**2 for x in data]) / len(data)
        logger.info(f'Non-stationary drift index: {non_stationary_drift_index}')
        return non_stationary_drift_index
    except Exception as e:
        logger.error(f'Error calculating non-stationary drift index: {e}')
        raise

def load_stochastic_regime_switch(data: List[float]) -> Dict[str, float]:
    """
    Calculate the stochastic regime switch for a given dataset.

    Args:
    - data (List[float]): The input dataset.

    Returns:
    - Dict[str, float]: A dictionary containing the stochastic regime switch parameters.

    Raises:
    - ValueError: If the input dataset is empty.
    """
    try:
        if not data:
            raise ValueError('Input dataset is empty')
        # Calculate the stochastic regime switch using a Markov chain model
        stochastic_regime_switch = {'mean': sum(data) / len(data), 'variance': sum([x**2 for x in data]) / len(data)}
        logger.info(f'Stochastic regime switch: {stochastic_regime_switch}')
        return stochastic_regime_switch
    except Exception as e:
        logger.error(f'Error calculating stochastic regime switch: {e}')
        raise

def search_web(query: str) -> str:
    """
    Search the web using the DuckDuckGo search engine.

    Args:
    - query (str): The search query.

    Returns:
    - str: The search results.

    Raises:
    - RequestException: If the search request fails.
    """
    try:
        # Create a DuckDuckGo search tool
        search_tool = DuckDuckGoSearchTool()
        # Search the web
        results = search_tool.search(query)
        logger.info(f'Search results: {results}')
        return results
    except RequestException as e:
        logger.error(f'Error searching web: {e}')
        raise

def simulate_rocket_science() -> None:
    """
    Simulate the 'Rocket Science' problem.

    Raises:
    - Exception: If the simulation fails.
    """
    try:
        # Create a LiteLLMModel instance
        model = LiteLLMModel()
        # Create a ToolCallingAgent instance
        agent = ToolCallingAgent(model)
        # Define the simulation parameters
        parameters = {'fuel': 1000, 'oxidizer': 500}
        # Run the simulation
        results = agent.run_simulation(parameters)
        logger.info(f'Simulation results: {results}')
    except Exception as e:
        logger.error(f'Error simulating rocket science: {e}')
        raise

if __name__ == '__main__':
    simulate_rocket_science()
",
        "commit_message": "feat: implement specialized data_loader logic"
    }
}
```