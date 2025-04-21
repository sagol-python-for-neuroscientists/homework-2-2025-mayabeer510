from enum import Enum
from collections import namedtuple
from itertools import zip_longest


Condition = Enum("Condition", ("CURE", "HEALTHY", "SICK", "DYING", "DEAD"))
Agent = namedtuple("Agent", ("name", "category"))

def is_active(agent):
    return agent.category != Condition.HEALTHY and agent.category != Condition.DEAD

def improve(condition):
    if condition == Condition.DYING:
        return Condition.SICK
    if condition == Condition.SICK:
        return Condition.HEALTHY
    return condition 

def worsen(condition):
    if condition == Condition.SICK:
        return Condition.DYING
    if condition == Condition.DYING:
        return Condition.DEAD
    
def meeting_cases(a1, a2):
    # Both cure
    if a1.category == Condition.CURE and a2.category == Condition.CURE:
        return a1, a2
    
    # One is cure
    if a1.category == Condition.CURE:
        return a1, Agent(a2.name, improve(a2.category))
    if a2.category == Condition.CURE:
        return Agent(a1.name, improve(a1.category)), a2
    
    # Both dying
    if a1.category == Condition.DYING and a2.category == Condition.DYING:
        return Agent(a1.name, Condition.DEAD), Agent(a2.name, Condition.DEAD)
    
    # Sick + dying
    if a1.category == Condition.SICK and a2.category == Condition.DYING:
        return Agent(a1.name, Condition.DYING), Agent(a2.name, Condition.DEAD)
    if a1.category == Condition.DYING and a2.category == Condition.SICK:
        return Agent(a1.name, Condition.DEAD), Agent(a2.name, Condition.DYING)
    
    # Both sick
    if a1.category == Condition.SICK and a2.category == Condition.SICK:
        return Agent(a1.name, Condition.DYING), Agent(a2.name, Condition.DYING)
    
def meetup(agent_listing: tuple) -> list:
    updated_agents = []

    active_agents = [agent for agent in agent_listing if is_active(agent)]

    for a1, a2 in zip_longest(active_agents[::2], active_agents[1::2]):
        if not a2:
            updated_agents.append(a1)
            continue
        result1, result2 = meeting_cases(a1, a2)
        updated_agents.extend([result1, result2])

    for agent in agent_listing:
        if agent.category in (Condition.HEALTHY, Condition.DEAD):
            updated_agents.append(agent)

    return updated_agents
    