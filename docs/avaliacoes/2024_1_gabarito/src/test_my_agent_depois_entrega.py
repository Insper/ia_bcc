import pytest
import my_agent as agent


def config_0():
    map = [
        "0000",
        "0110",
        "0000",
    ]
    position = (0,0)
    goal = (0,1)
    return map, position, goal

def config_1():
    map = [
        "0000",
        "0110",
        "0000",
    ]
    position = (0,0)
    goal = (2,3)
    return map, position, goal

def config_2():
    map = [
        "0000",
        "0110",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
    ]
    position = (3,3)
    goal = (4,3)
    return map, position, goal

def config_3():
    # sem solucao
    map = [
        "010000",
        "011111",
        "000000",
        "000000",
    ]
    position = (3,3)
    goal = (0,4)
    return map, position, goal

def config_4():
    # mapao
    map = [
        "010000000000000000000000",
        "011111000000000000000000",
        "000000000000000000000000",
        "000000000000000000000000",
        "010101010101010101010101",
        "010101010101010101010101",
        "010101010101010101010101",
        "010101010101010101010101",
        "010101010101010101010101",
        "010101010101010101010101",
        "010101010101010101010101",
    ]
    position = (9,4)
    goal = (0,4)
    return map, position, goal


def config_5():
    # mapao
    map = [
        "010000000000000000000000",
        "011111000000000000000000",
        "000000000000000000000000",
        "000000000000000000000000",
        "010101010101010101010101",
        "010101010101010101010101",
        "010101010101010101010101",
        "010101010101010101010101",
        "010101010101010101010101",
        "010101010101010101010101",
        "010101010101010101010101",
    ]
    position = (0,10)
    goal = (10,12)
    return map, position, goal


def config_6():
    # mapao
    map = [
        "010000000000000000000000",
        "011111000000000000000000",
        "000000000000000000000000",
        "000000000000000000000000",
        "010101010101010101010101",
        "010101010101010101010101",
        "010101010101010101010101",
        "010101010101010101010101",
        "010101010101010101010101",
        "010101010101010101010101",
        "010101010101010101010101",
    ]
    position = (10,0)
    goal = (10,12)
    return map, position, goal


def test_path_0():
    map, position, goal = config_0()
    actions = agent.parser_actions(agent.get_actions(map, position, goal))
    assert actions == [3]

def test_cost_0():
    map, position, goal = config_0()
    actions = agent.parser_actions(agent.get_actions(map, position, goal))
    assert len(actions) == 1

def test_path_1():
    map, position, goal = config_1()
    actions = agent.parser_actions(agent.get_actions(map, position, goal))
    assert actions == [1, 1, 3, 3, 3] or actions == [3, 3, 3, 1, 1]

def test_cost_1():
    map, position, goal = config_1()
    actions = agent.parser_actions(agent.get_actions(map, position, goal))
    assert len(actions) == 5

def test_path_2():
    map, position, goal = config_2()
    actions = agent.parser_actions(agent.get_actions(map, position, goal))
    assert actions == [1] 

def test_cost_2():
    map, position, goal = config_2()
    actions = agent.parser_actions(agent.get_actions(map, position, goal))
    assert len(actions) == 1

def test_path_3():
    # testando o comportamento para uma situação onde não existe caminho
    map, position, goal = config_3()
    actions = agent.parser_actions(agent.get_actions(map, position, goal))
    assert actions == None 

def test_cost_4():
    map, position, goal = config_4()
    actions = agent.parser_actions(agent.get_actions(map, position, goal))
    assert len(actions) == 13

def test_cost_5():
    map, position, goal = config_5()
    actions = agent.parser_actions(agent.get_actions(map, position, goal))
    assert len(actions) == 12

def test_cost_6():
    map, position, goal = config_6()
    actions = agent.parser_actions(agent.get_actions(map, position, goal))
    assert len(actions) == 26

