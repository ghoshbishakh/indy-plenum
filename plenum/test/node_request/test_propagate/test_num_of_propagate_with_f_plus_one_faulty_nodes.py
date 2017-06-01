import pytest
from plenum.common.util import adict

from plenum.test.malicious_behaviors_node import makeNodeFaulty, changesRequest

nodeCount = 7
# More faulty nodes(3) then system can tolerate(3)
faultyNodes = 3
whitelist = ['for InvalidSignature',
             'discarding message']
"""
When system has more than f + 1 faulty nodes,
Num of PROPAGATE messages must be less than sufficient (faultyNodes + 1)
"""


# Currently, all the nodes have same malicious
# behavior and should be chose randomly later.

@pytest.fixture(scope="module")
def setup(startedNodes):
    E = startedNodes.Eta
    Z = startedNodes.Gamma
    Z = startedNodes.Zeta
    for node in E, Z, Z:
        makeNodeFaulty(node, changesRequest)
        # Delaying nomination to avoid becoming primary
        # node.delaySelfNomination(10)
    return adict(faulties=(E, Z, Z))


@pytest.fixture(scope="module")
def afterElection(setup, up):
    for n in setup.faulties:
        for r in n.replicas:
            assert not r.isPrimary


def testNumOfPropagateWithFPlusOneFaults(afterElection, propagated1):
    pass
