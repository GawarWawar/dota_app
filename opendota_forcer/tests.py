from django.test import TestCase

import random


from .src.match import DotaMatch
from .src.profile import DotaProfile
# Create your tests here.


class DotaMatchTest(TestCase):
    def test_parsed_status(self):
        MATCH_ID = 7904861993
        d_match = DotaMatch(MATCH_ID)
        d_match.check_parsed_status()  
        assert d_match._is_parsed == True
        
    def test_parce_match(self):
        MATCH_ID = 7904861993
        d_match = DotaMatch(MATCH_ID)
        status = d_match.parse_match()  
        assert status == "Parsed status is not defined." 

class DotaProfileTest(TestCase):
    def test_get_last_match(self):
        profile = DotaProfile(167230743)
        last_match = profile.get_last_match()
        assert isinstance(last_match, DotaMatch)
        
    def test_get_recent_matches(self):
        profile = DotaProfile(167230743)
        recent_matches = profile.get_recent_matches()
        assert isinstance(recent_matches[0], DotaMatch)
        
    def test_get_matches(self):
        n_of_matches = random.randint(10, 50)
        profile = DotaProfile(167230743)
        mathces = profile.get_matches(n_of_matches)
        assert isinstance(mathces[0], DotaMatch) and len(mathces) == n_of_matches
