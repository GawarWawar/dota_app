from django.test import TestCase

import random


from .src.match import DotaMatch
from .src.profile import DotaProfile
# Create your tests here.

#TODO: do tests for Celery tasks

class DotaMatchTest(TestCase):
    match_id = 7904861993
    
    def test_parsed_status(self):
        d_match = DotaMatch(self.match_id)
        d_match.check_parsed_status()  
        assert d_match.is_parsed == True
        
    def test_parce_match(self):
        d_match = DotaMatch(self.match_id)
        status = d_match.parse_match()
        assert status == "Match was already parsed"
        
    def test_is_parsed_error(self):
        d_match = DotaMatch(self.match_id)
        with self.assertRaises(AttributeError):
            d_match.is_parsed = True

class DotaProfileTest(TestCase):
    profile_id = 167230743
    def test_get_last_match(self):
        profile = DotaProfile(self.profile_id)
        last_match = profile.get_last_match()
        assert isinstance(last_match, DotaMatch)
        
    def test_get_recent_matches(self):
        profile = DotaProfile(self.profile_id)
        recent_matches = profile.get_recent_matches()
        assert isinstance(recent_matches[0], DotaMatch)
        
    def test_get_matches(self):
        n_of_matches = random.randint(10, 50)
        profile = DotaProfile(self.profile_id)
        mathces = profile.get_matches(n_of_matches)
        assert isinstance(mathces[0], DotaMatch) and len(mathces) == n_of_matches
